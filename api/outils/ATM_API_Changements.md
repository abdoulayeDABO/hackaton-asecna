# ATM_API_Changements

## Rôle

Consulter l’historique des changements : objet concerné, champ, ancienne valeur, nouvelle valeur, date d’effet et statut de validation. L’outil permet à l’agent de déterminer la valeur valide à la date de référence et de signaler les changements `EN_ATTENTE` ou `REJETEE`.

## Entrées

| Entrée | Description |
|---|---|
| `change_id` | Identifiant du changement, par exemple `CHG-002`. Nom technique du paramètre : À COMPLÉTER. |
| `objet` | Identifiant de l’objet concerné, par exemple `ASP-002`. Nom technique du paramètre : À COMPLÉTER. |
| `champ` | Champ concerné, par exemple `limite_superieure`. Nom technique du paramètre : À COMPLÉTER. |
| `validation` | Filtre par statut : `VALIDEE`, `EN_ATTENTE` ou `REJETEE`. Nom technique du paramètre : À COMPLÉTER. |

## Sorties

Exemple de forme (valeurs du jeu de démonstration) :

```json
{
  "changements": [
    {
      "change_id": "CHG-002",
      "objet": "ASP-002",
      "champ": "limite_superieure",
      "ancienne_valeur": "3000 FT AMSL",
      "nouvelle_valeur": "3500 FT AMSL",
      "date_effet": "2026-12-31",
      "validation": "EN_ATTENTE",
      "valeur_valide_a_la_date_reference": "3000 FT AMSL",
      "applicable": false
    }
  ],
  "total": 1,
  "date_reference": "2026-11-26"
}
```

Champs complémentaires et schéma de sortie complets : À COMPLÉTER.

## Lecture seule

Oui. L’outil ne valide, ne rejette et ne modifie aucun changement.

## Entité Data Fabric lue

À COMPLÉTER. Table logique : `historique_modifications` (`donnees/pretraitees/historique_modifications.csv`).
