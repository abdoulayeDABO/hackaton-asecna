# ATM_API_Recherche

## Rôle

Effectuer une recherche textuelle dans les tables consolidées (aérodromes, pistes, aides radio, espaces aériens, changements) et retourner les lignes correspondantes avec leur identifiant source. L’outil aide l’agent à localiser une donnée quand la question ne donne pas directement un identifiant.

## Entrées

| Entrée | Description |
|---|---|
| `q` | Chaîne recherchée, par exemple `Vallon`, `DVL` ou `ZZDV`. Nom technique du paramètre : À COMPLÉTER. |
| `limite` | Nombre maximal de résultats. Nom technique et valeur par défaut : À COMPLÉTER. |
| `table` | Filtre optionnel sur une table. Nom technique du paramètre : À COMPLÉTER. |

## Sorties

Exemple de forme (valeurs du jeu de démonstration) :

```json
{
  "resultats": [
    {
      "table": "espaces_aeriens",
      "id": "ASP-002",
      "champ": "nom",
      "valeur": "CTR VALLON SIMULEE",
      "changement_associe": "CHG-002"
    },
    {
      "table": "aerodromes",
      "id": "AD-001",
      "champ": "nom",
      "valeur": "AERODROME FICTIF DAKAR-VALLON",
      "changement_associe": "Aucun"
    }
  ],
  "total": 2,
  "requete": "Vallon"
}
```

Schéma de sortie complet : À COMPLÉTER.

## Lecture seule

Oui. L’outil ne fait que lire et retourner des correspondances.

## Entité Data Fabric lue

À COMPLÉTER. L’outil interroge les tables `aerodromes`, `pistes`, `aides_radio`, `espaces_aeriens` et `historique_modifications`.
