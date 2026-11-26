# ATM_API_Aerodromes

## Rôle

Consulter la liste des aérodromes ou le détail d’un aérodrome à partir de son identifiant ou de son code. L’outil renvoie les champs de la table consolidée et le changement associé.

## Entrées

| Entrée | Description |
|---|---|
| `code` | Code de l’aérodrome, par exemple `ZZDV` ou `ZZSL`. Nom technique du paramètre : À COMPLÉTER. |
| `id` | Identifiant de l’aérodrome, par exemple `AD-001`. Nom technique du paramètre : À COMPLÉTER. |
| Aucun filtre | Retourne la liste des aérodromes. |

## Sorties

Exemple de forme (valeurs du jeu de démonstration) :

```json
{
  "aerodromes": [
    {
      "id": "AD-001",
      "code": "ZZDV",
      "nom": "AERODROME FICTIF DAKAR-VALLON",
      "pays": "SENEGAL",
      "latitude": "14.69",
      "longitude": "-17.12",
      "elevation_ft": "92",
      "statut": "FICTIF",
      "changement_associe": "Aucun"
    }
  ],
  "total": 1,
  "date_reference": "2026-11-26"
}
```

Champs complémentaires et schéma de sortie complets : À COMPLÉTER.

## Lecture seule

Oui. L’outil ne crée, ne modifie et ne supprime aucun aérodrome.

## Entité Data Fabric lue

À COMPLÉTER. Table logique : `aerodromes` (`donnees/pretraitees/aerodromes.csv`).
