# ATM_API_EspacesAeriens

## Rôle

Consulter la liste des espaces aériens ou le détail d’un espace aérien : type, limites, classe, centre et rayon. L’outil renvoie la valeur valide à la date de référence et le changement associé.

## Entrées

| Entrée | Description |
|---|---|
| `id` | Identifiant de l’espace, par exemple `ASP-002`. Nom technique du paramètre : À COMPLÉTER. |
| `type` | Filtre par type, par exemple `TMA` ou `CTR`. Nom technique du paramètre : À COMPLÉTER. |
| `classe` | Filtre par classe, par exemple `C` ou `D`. Nom technique du paramètre : À COMPLÉTER. |
| Aucun filtre | Retourne la liste des espaces aériens. |

## Sorties

Exemple de forme (valeurs du jeu de démonstration) :

```json
{
  "espaces_aeriens": [
    {
      "id": "ASP-002",
      "nom": "CTR VALLON SIMULEE",
      "type": "CTR",
      "limite_inferieure": "SFC",
      "limite_superieure": "3000 FT AMSL",
      "classe": "D",
      "centre_lat": "14.69",
      "centre_lon": "-17.12",
      "rayon_nm": "12",
      "changement_associe": "CHG-002"
    }
  ],
  "total": 1,
  "date_reference": "2026-11-26"
}
```

Champs complémentaires et schéma de sortie complets : À COMPLÉTER.

## Lecture seule

Oui. L’outil ne crée, ne modifie et ne supprime aucun espace aérien.

## Entité Data Fabric lue

À COMPLÉTER. Table logique : `espaces_aeriens` (`donnees/pretraitees/espaces_aeriens.csv`).
