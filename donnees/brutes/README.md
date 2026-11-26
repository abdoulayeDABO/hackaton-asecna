# Données brutes

Ce dossier contient les fichiers du comité scientifique. Ils sont copiés tels quels et ne doivent jamais être modifiés.

## Fichiers à y copier

| Fichier | Contenu |
|---|---|
| `aerodromes.csv` | Aérodromes fictifs. |
| `pistes.csv` | Pistes fictives. |
| `aides_radio.csv` | Aides radio fictives. |
| `espaces_aeriens.csv` | Espaces aériens fictifs. |
| `historique_modifications.csv` | Changements et statuts de validation. |
| `donnees_aeronautiques_demo.xml` | Représentation XML simplifiée, déclarée `AIXM-inspired-SYNTHETIC-NOT-AIXM-5.1-CONFORMANT`. |
| `catalogue_service_swim_demo.json` | Catalogue de service de démonstration. |
| `questions_test.csv` | 18 questions de test avec la source attendue. |
| `LISEZ_MOI.txt` | Avertissement du comité sur les données fictives. |

## Règles

- Ne pas modifier ces fichiers.
- Ne pas ajouter de données réelles, personnelles ou sensibles.
- Le XML n’est pas conforme AIXM 5.1. Le schéma `pretraitement/schema_demo.xsd` est un schéma maison.
- Les nouvelles valeurs présentes dans les fichiers bruts doivent être recoupées avec `historique_modifications.csv` avant d’être présentées comme valides.
- Aucun secret (mot de passe, jeton, clé) ne doit être placé dans ce dossier.

## Provenance

Fichiers fournis par le comité scientifique de l’AI Agents Challenge — Innovation Days 2026, fiche 004 ATM / SWIM / AIXM 5.1. Données fictives de démonstration.
