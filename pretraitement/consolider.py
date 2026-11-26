#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
import datetime as dt
from pathlib import Path

from lxml import etree

RACINE = Path(__file__).resolve().parents[1]
BRUTES = RACINE / "donnees" / "brutes"
PRETRAITEES = RACINE / "donnees" / "pretraitees"
SCHEMA_XSD = Path(__file__).resolve().parent / "schema_demo.xsd"
RAPPORT = Path(__file__).resolve().parent / "rapport_validation.md"

TABLES = {
    "aerodromes": {
        "fichier": "aerodromes.csv",
        "cle": "id",
        "colonnes": [
            "id",
            "code",
            "nom",
            "pays",
            "latitude",
            "longitude",
            "elevation_ft",
            "statut",
        ],
    },
    "pistes": {
        "fichier": "pistes.csv",
        "cle": "id",
        "colonnes": [
            "id",
            "aerodrome",
            "designation",
            "longueur_m",
            "largeur_m",
            "surface",
            "orientation_magnetique_deg",
            "statut",
        ],
    },
    "aides_radio": {
        "fichier": "aides_radio.csv",
        "cle": "id",
        "colonnes": [
            "id",
            "ident",
            "type",
            "frequence",
            "latitude",
            "longitude",
            "aerodrome",
        ],
    },
    "espaces_aeriens": {
        "fichier": "espaces_aeriens.csv",
        "cle": "id",
        "colonnes": [
            "id",
            "nom",
            "type",
            "limite_inferieure",
            "limite_superieure",
            "classe",
            "centre_lat",
            "centre_lon",
            "rayon_nm",
        ],
    },
}

HISTORIQUE = {
    "fichier": "historique_modifications.csv",
    "cle": "change_id",
    "colonnes": [
        "change_id",
        "objet",
        "champ",
        "ancienne_valeur",
        "nouvelle_valeur",
        "date_effet",
        "validation",
    ],
}

VALIDATIONS = {"VALIDEE", "EN_ATTENTE", "REJETEE"}


def lire_csv(chemin: Path) -> tuple[list[str], list[dict[str, str]], bool]:
    if not chemin.exists():
        raise FileNotFoundError(f"Fichier absent : {chemin}")
    with chemin.open("rb") as flux:
        bom = flux.read(3) == b"\xef\xbb\xbf"
    with chemin.open("r", encoding="utf-8-sig", newline="") as flux:
        lecteur = csv.DictReader(flux)
        colonnes = list(lecteur.fieldnames or [])
        lignes = [
            {cle: (valeur.strip() if isinstance(valeur, str) else valeur) for cle, valeur in ligne.items()}
            for ligne in lecteur
        ]
    return colonnes, lignes, bom


def ecrire_csv(chemin: Path, colonnes: list[str], lignes: list[dict[str, str]]) -> None:
    chemin.parent.mkdir(parents=True, exist_ok=True)
    with chemin.open("w", encoding="utf-8", newline="") as flux:
        writer = csv.DictWriter(flux, fieldnames=colonnes, lineterminator="\n")
        writer.writeheader()
        for ligne in lignes:
            writer.writerow({colonne: ligne.get(colonne, "") for colonne in colonnes})


def parser_date(valeur: str) -> dt.date | None:
    try:
        return dt.date.fromisoformat(valeur)
    except ValueError:
        return None


def jour_precedent(valeur: dt.date) -> dt.date:
    return valeur - dt.timedelta(days=1)


def valeur_future(ancienne: str, nouvelle: str, date_effet: dt.date) -> str:
    return (
        f"{ancienne} jusqu'au {jour_precedent(date_effet).isoformat()}, "
        f"puis {nouvelle} à partir du {date_effet.isoformat()}"
    )


def valider_xml() -> tuple[bool, list[str], str]:
    xml_path = BRUTES / "donnees_aeronautiques_demo.xml"
    if not xml_path.exists():
        return False, ["Fichier XML absent."], "Fichier absent"
    if not SCHEMA_XSD.exists():
        return False, ["Schéma XSD absent."], "Schéma absent"
    try:
        schema = etree.XMLSchema(etree.parse(str(SCHEMA_XSD)))
        document = etree.parse(str(xml_path))
        valide = schema.validate(document)
        erreurs = [str(erreur) for erreur in schema.error_log]
        return valide, erreurs, "Validé" if valide else "Non validé"
    except (etree.XMLSchemaParseError, etree.XMLSyntaxError) as erreur:
        return False, [str(erreur)], "Erreur de lecture"


def echapper_markdown(valeur: object) -> str:
    return str(valeur).replace("|", "\\|")


def construire_rapport(
    date_reference: dt.date,
    structures: list[dict[str, object]],
    anomalies: list[dict[str, str]],
    applications: list[dict[str, str]],
    xml_valide: bool,
    xml_erreurs: list[str],
    xml_statut: str,
    lignes_ecrites: list[tuple[str, int]],
) -> str:
    maintenant = dt.datetime.now().strftime("%Y-%m-%d %H:%M")
    lignes: list[str] = []
    lignes.append("# Rapport de validation — SWIM SENEGAL")
    lignes.append("")
    lignes.append(f"Date de génération : {maintenant}")
    lignes.append(f"Date de référence utilisée : {date_reference.isoformat()}")
    lignes.append("")
    lignes.append("> Données fictives de démonstration. Le schéma XSD utilisé est un schéma maison, "
                  "et non un schéma AIXM 5.1 officiel. Le fichier XML source se déclare "
                  "`AIXM-inspired-SYNTHETIC-NOT-AIXM-5.1-CONFORMANT`.")
    lignes.append("")
    lignes.append("## 1. Fichiers traités")
    lignes.append("")
    lignes.append("| Fichier | Lignes lues | BOM détecté | Colonnes conformes |")
    lignes.append("|---|---:|---|---|")
    for structure in structures:
        lignes.append(
            "| {fichier} | {lignes} | {bom} | {colonnes} |".format(
                fichier=echapper_markdown(structure["fichier"]),
                lignes=structure["lignes"],
                bom="Oui" if structure["bom"] else "Non",
                colonnes="Oui" if structure["colonnes_ok"] else "Non",
            )
        )
    lignes.append("")
    lignes.append("## 2. Contrôles de structure")
    lignes.append("")
    lignes.append("| Contrôle | Résultat | Détail |")
    lignes.append("|---|---|---|")
    controles_ok = all(bool(structure["colonnes_ok"]) for structure in structures)
    lignes.append(
        f"| Colonnes attendues | {'OK' if controles_ok else 'ÉCART'} | "
        "Colonnes comparées aux en-têtes du jeu du comité. |"
    )
    ids_ok = not any(anomalie["type"] == "identifiant_duplique" for anomalie in anomalies)
    lignes.append(
        f"| Unicité des identifiants | {'OK' if ids_ok else 'ÉCART'} | "
        "Contrôle des clés `id` et `change_id`. |"
    )
    refs_ok = not any(anomalie["type"] == "reference_inconnue" for anomalie in anomalies)
    lignes.append(
        f"| Références entre tables | {'OK' if refs_ok else 'ÉCART'} | "
        "Pistes et aides radio rattachées à un code aérodrome ; changements rattachés à un objet existant. |"
    )
    histo_ok = not any(anomalie["type"].startswith("historique_") for anomalie in anomalies)
    lignes.append(
        f"| Historique des modifications | {'OK' if histo_ok else 'ÉCART'} | "
        "Statuts, champs, dates et valeurs contrôlés. |"
    )
    lignes.append("")
    lignes.append("## 3. Validation du schéma XSD maison")
    lignes.append("")
    lignes.append(f"- Fichier de schéma : `pretraitement/schema_demo.xsd`.")
    lignes.append(f"- Résultat : **{xml_statut}**.")
    if xml_erreurs:
        lignes.append("- Erreurs :")
        for erreur in xml_erreurs:
            lignes.append(f"  - {echapper_markdown(erreur)}")
    else:
        lignes.append("- Aucune erreur de structure XML détectée par le schéma maison.")
    lignes.append("- Ce contrôle ne vaut pas validation AIXM 5.1.")
    lignes.append("")
    lignes.append("## 4. Anomalies détectées")
    lignes.append("")
    if anomalies:
        lignes.append("| Table | Objet | Champ | Type | Détail |")
        lignes.append("|---|---|---|---|---|")
        for anomalie in anomalies:
            lignes.append(
                "| {table} | {objet} | {champ} | {type} | {detail} |".format(
                    table=echapper_markdown(anomalie["table"]),
                    objet=echapper_markdown(anomalie["objet"]),
                    champ=echapper_markdown(anomalie["champ"]),
                    type=echapper_markdown(anomalie["type"]),
                    detail=echapper_markdown(anomalie["detail"]),
                )
            )
    else:
        lignes.append("Aucune anomalie détectée.")
    lignes.append("")
    lignes.append("## 5. Valeurs retenues après consolidation")
    lignes.append("")
    if applications:
        lignes.append("| Table | Objet | Champ | Valeur source | Valeur valide retenue | Changement | Statut |")
        lignes.append("|---|---|---|---|---|---|---|")
        for application in applications:
            lignes.append(
                "| {table} | {objet} | {champ} | {source} | {valide} | {changement} | {statut} |".format(
                    table=echapper_markdown(application["table"]),
                    objet=echapper_markdown(application["objet"]),
                    champ=echapper_markdown(application["champ"]),
                    source=echapper_markdown(application["source"]),
                    valide=echapper_markdown(application["valide"]),
                    changement=echapper_markdown(application["changement"]),
                    statut=echapper_markdown(application["statut"]),
                )
            )
    else:
        lignes.append("Aucun changement appliqué.")
    lignes.append("")
    lignes.append("## 6. Fichiers consolidés écrits")
    lignes.append("")
    lignes.append("| Fichier | Lignes |")
    lignes.append("|---|---:|")
    for nom, nombre in lignes_ecrites:
        lignes.append(f"| `donnees/pretraitees/{nom}` | {nombre} |")
    lignes.append("")
    lignes.append("## 7. Règles de consolidation appliquées")
    lignes.append("")
    lignes.append("- Changement `VALIDEE` avec date d’effet passée ou égale à la date de référence : nouvelle valeur retenue.")
    lignes.append("- Changement `VALIDEE` avec date d’effet future : valeur avant et valeur après conservées, avec les dates.")
    lignes.append("- Changement `EN_ATTENTE` ou `REJETEE` : valeur inchangée, changement signalé dans `changement_associe`.")
    lignes.append("- La colonne `changement_associe` vaut `Aucun` lorsqu’aucun changement ne concerne la ligne.")
    lignes.append("")
    lignes.append("## 8. Limites")
    lignes.append("")
    lignes.append("- Le schéma XSD est un schéma maison ; il ne s’agit pas d’une validation XSD AIXM 5.1 officielle.")
    lignes.append("- Le jeu de données est petit et fictif ; les contrôles ne couvrent pas un jeu de production.")
    lignes.append("- Les contrôles portent sur la structure et la cohérence interne, pas sur la validité aéronautique réelle.")
    lignes.append("")
    return "\n".join(lignes)


def main() -> int:
    parser = argparse.ArgumentParser(description="Consolide les données aéronautiques fictives.")
    parser.add_argument(
        "--date-reference",
        default=dt.date.today().isoformat(),
        help="Date de référence au format AAAA-MM-JJ (défaut : date du jour).",
    )
    arguments = parser.parse_args()
    date_reference = parser_date(arguments.date_reference)
    if date_reference is None:
        parser.error("La date de référence doit être au format AAAA-MM-JJ.")

    structures: list[dict[str, object]] = []
    anomalies: list[dict[str, str]] = []
    applications: list[dict[str, str]] = []
    tables: dict[str, tuple[list[str], list[dict[str, str]]]] = {}

    for nom, configuration in TABLES.items():
        chemin = BRUTES / configuration["fichier"]
        colonnes, lignes, bom = lire_csv(chemin)
        colonnes_ok = colonnes == configuration["colonnes"]
        structures.append(
            {
                "fichier": configuration["fichier"],
                "lignes": len(lignes),
                "bom": bom,
                "colonnes_ok": colonnes_ok,
            }
        )
        if not colonnes_ok:
            anomalies.append(
                {
                    "table": nom,
                    "objet": "-",
                    "champ": "-",
                    "type": "structure_colonnes",
                    "detail": f"Colonnes lues : {', '.join(colonnes)}",
                }
            )
        vus: set[str] = set()
        for ligne in lignes:
            identifiant = ligne.get(configuration["cle"], "")
            if not identifiant:
                anomalies.append(
                    {
                        "table": nom,
                        "objet": "-",
                        "champ": configuration["cle"],
                        "type": "identifiant_absent",
                        "detail": "Identifiant vide.",
                    }
                )
            elif identifiant in vus:
                anomalies.append(
                    {
                        "table": nom,
                        "objet": identifiant,
                        "champ": configuration["cle"],
                        "type": "identifiant_duplique",
                        "detail": "Identifiant présent plusieurs fois.",
                    }
                )
            vus.add(identifiant)
        tables[nom] = (colonnes, lignes)

    colonnes_histo, lignes_histo, bom_histo = lire_csv(BRUTES / HISTORIQUE["fichier"])
    colonnes_histo_ok = colonnes_histo == HISTORIQUE["colonnes"]
    structures.append(
        {
            "fichier": HISTORIQUE["fichier"],
            "lignes": len(lignes_histo),
            "bom": bom_histo,
            "colonnes_ok": colonnes_histo_ok,
        }
    )
    if not colonnes_histo_ok:
        anomalies.append(
            {
                "table": "historique_modifications",
                "objet": "-",
                "champ": "-",
                "type": "structure_colonnes",
                "detail": f"Colonnes lues : {', '.join(colonnes_histo)}",
            }
        )

    objets_connus: dict[str, str] = {}
    for nom, (_, lignes) in tables.items():
        for ligne in lignes:
            objets_connus[ligne.get("id", "")] = nom

    changements_par_objet: dict[str, list[dict[str, str]]] = {}
    for changement in lignes_histo:
        change_id = changement.get("change_id", "")
        objet = changement.get("objet", "")
        champ = changement.get("champ", "")
        validation = changement.get("validation", "")
        date_effet = parser_date(changement.get("date_effet", ""))
        if not change_id:
            anomalies.append(
                {
                    "table": "historique_modifications",
                    "objet": "-",
                    "champ": "change_id",
                    "type": "historique_identifiant_absent",
                    "detail": "Identifiant de changement vide.",
                }
            )
        if validation not in VALIDATIONS:
            anomalies.append(
                {
                    "table": "historique_modifications",
                    "objet": change_id,
                    "champ": "validation",
                    "type": "historique_validation_inconnue",
                    "detail": f"Statut lu : {validation}",
                }
            )
        if date_effet is None:
            anomalies.append(
                {
                    "table": "historique_modifications",
                    "objet": change_id,
                    "champ": "date_effet",
                    "type": "historique_date_invalide",
                    "detail": f"Date lue : {changement.get('date_effet', '')}",
                }
            )
        if objet not in objets_connus:
            anomalies.append(
                {
                    "table": "historique_modifications",
                    "objet": objet,
                    "champ": "objet",
                    "type": "reference_inconnue",
                    "detail": "Objet absent des tables de données.",
                }
            )
        else:
            table_cible = objets_connus[objet]
            if champ not in TABLES[table_cible]["colonnes"]:
                anomalies.append(
                    {
                        "table": "historique_modifications",
                        "objet": objet,
                        "champ": champ,
                        "type": "historique_champ_inconnu",
                        "detail": f"Champ absent de la table {table_cible}.",
                    }
                )
        changements_par_objet.setdefault(objet, []).append(changement)

    for nom, (colonnes, lignes) in tables.items():
        for ligne in lignes:
            identifiant = ligne.get("id", "")
            changements = changements_par_objet.get(identifiant, [])
            ligne["changement_associe"] = "Aucun"
            if not changements:
                continue
            references: list[str] = []
            for changement in changements:
                champ = changement.get("champ", "")
                if champ not in colonnes:
                    continue
                validation = changement.get("validation", "")
                date_effet = parser_date(changement.get("date_effet", ""))
                ancienne = changement.get("ancienne_valeur", "")
                nouvelle = changement.get("nouvelle_valeur", "")
                source = ligne.get(champ, "")
                references.append(changement.get("change_id", ""))

                if validation == "VALIDEE" and date_effet is not None and date_effet <= date_reference:
                    ligne[champ] = nouvelle
                    valide = nouvelle
                    statut = "APPLIQUEE"
                elif validation == "VALIDEE" and date_effet is not None:
                    ligne[champ] = valeur_future(ancienne, nouvelle, date_effet)
                    valide = (
                        f"{ancienne} applicable au {date_reference.isoformat()} ; "
                        f"{nouvelle} à partir du {date_effet.isoformat()}"
                    )
                    statut = "FUTURE"
                elif validation in {"EN_ATTENTE", "REJETEE"}:
                    ligne[champ] = ancienne
                    valide = f"{ancienne} (inchangée)"
                    statut = validation
                else:
                    valide = source
                    statut = "NON_DETERMINE"

                if source != ancienne and validation in {"EN_ATTENTE", "REJETEE"}:
                    anomalies.append(
                        {
                            "table": nom,
                            "objet": identifiant,
                            "champ": champ,
                            "type": "ecart_valeur_source",
                            "detail": (
                                f"Valeur source « {source} » différente de la valeur valide « {ancienne} » ; "
                                f"changement {changement.get('change_id', '')} {validation}."
                            ),
                        }
                    )
                elif validation == "VALIDEE" and date_effet is not None and date_effet > date_reference and source != ancienne:
                    anomalies.append(
                        {
                            "table": nom,
                            "objet": identifiant,
                            "champ": champ,
                            "type": "ecart_valeur_source",
                            "detail": (
                                f"Valeur source « {source} » déjà passée à la nouvelle valeur alors que l’effet "
                                f"est futur ({date_effet.isoformat()}) ; changement {changement.get('change_id', '')}."
                            ),
                        }
                    )

                applications.append(
                    {
                        "table": nom,
                        "objet": identifiant,
                        "champ": champ,
                        "source": source,
                        "valide": valide,
                        "changement": changement.get("change_id", ""),
                        "statut": statut,
                    }
                )
            ligne["changement_associe"] = ";".join(references) if references else "Aucun"

    codes_aerodromes = {ligne.get("code", "") for ligne in tables["aerodromes"][1]}
    for nom in ("pistes", "aides_radio"):
        for ligne in tables[nom][1]:
            code = ligne.get("aerodrome", "")
            if code not in codes_aerodromes:
                anomalies.append(
                    {
                        "table": nom,
                        "objet": ligne.get("id", ""),
                        "champ": "aerodrome",
                        "type": "reference_inconnue",
                        "detail": f"Code aérodrome absent : {code}",
                    }
                )

    xml_valide, xml_erreurs, xml_statut = valider_xml()

    PRETRAITEES.mkdir(parents=True, exist_ok=True)
    lignes_ecrites: list[tuple[str, int]] = []
    for nom, (colonnes, lignes) in tables.items():
        colonnes_sortie = colonnes + ["changement_associe"]
        ecrire_csv(PRETRAITEES / f"{nom}.csv", colonnes_sortie, lignes)
        lignes_ecrites.append((f"{nom}.csv", len(lignes)))
    ecrire_csv(PRETRAITEES / HISTORIQUE["fichier"], colonnes_histo, lignes_histo)
    lignes_ecrites.append((HISTORIQUE["fichier"], len(lignes_histo)))

    rapport = construire_rapport(
        date_reference,
        structures,
        anomalies,
        applications,
        xml_valide,
        xml_erreurs,
        xml_statut,
        lignes_ecrites,
    )
    RAPPORT.write_text(rapport + "\n", encoding="utf-8")

    print(f"Date de référence : {date_reference.isoformat()}")
    print(f"Fichiers consolidés : {PRETRAITEES}")
    print(f"Rapport : {RAPPORT}")
    print(f"Anomalies : {len(anomalies)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
