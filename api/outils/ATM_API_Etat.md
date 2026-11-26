# ATM_API_Etat

## Rôle

Retourner l’état du jeu de données consulté : date de référence, tables disponibles, nombre de lignes et statut de la consolidation. Cet outil permet à l’agent de vérifier qu’il travaille sur la bonne version des données avant de répondre.

## Entrées

| Entrée | Description |
|---|---|
| Aucune entrée obligatoire | À COMPLÉTER si un filtre ou une date de référence est exposé. |
| Nom technique des paramètres | À COMPLÉTER |

## Sorties

Exemple de forme (valeurs du jeu de démonstration, pas un résultat mesuré) :

```json
{
  "statut": "À COMPLÉTER",
  "date_reference": "2026-11-26",
  "source": "donnees/pretraitees/",
  "tables": {
    "aerodromes": 2,
    "pistes": 2,
    "aides_radio": 3,
    "espaces_aeriens": 3,
    "historique_modifications": 3
  },
  "version": "À COMPLÉTER",
  "derniere_consolidation": "À COMPLÉTER"
}
```

Schéma de sortie complet : À COMPLÉTER.

## Lecture seule

Oui. Aucun paramètre ni aucun appel ne permet d’écrire dans Data Fabric.

## Entité Data Fabric lue

À COMPLÉTER. L’outil agrège l’état des tables `aerodromes`, `pistes`, `aides_radio`, `espaces_aeriens` et `historique_modifications`.
