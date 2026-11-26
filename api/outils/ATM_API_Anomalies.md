# ATM_API_Anomalies

## Rôle

Lister les anomalies détectées lors du prétraitement et de la consolidation : écart entre la valeur source et la valeur valide, référence inconnue, structure inattendue ou incohérence de l’historique. L’agent utilise cet outil pour décider s’il peut répondre directement ou s’il doit escalader.

## Entrées

| Entrée | Description |
|---|---|
| Filtre par table | À COMPLÉTER (nom technique du paramètre). |
| Filtre par objet | À COMPLÉTER (identifiant de l’objet). |
| Filtre par champ | À COMPLÉTER. |
| Filtre par type ou gravité | À COMPLÉTER. |

## Sorties

Exemple de forme (anomalies réellement produites par le prétraitement du jeu de démonstration) :

```json
{
  "anomalies": [
    {
      "table": "pistes",
      "objet": "RWY-001",
      "champ": "longueur_m",
      "type": "ecart_valeur_source",
      "detail": "Valeur source 3100 déjà passée à la nouvelle valeur alors que l’effet est futur (2026-12-03) ; changement CHG-001."
    },
    {
      "table": "aides_radio",
      "objet": "NAV-002",
      "champ": "frequence",
      "type": "ecart_valeur_source",
      "detail": "Valeur source 345 kHz différente de la valeur valide 340 kHz ; changement CHG-003 REJETEE."
    },
    {
      "table": "espaces_aeriens",
      "objet": "ASP-002",
      "champ": "limite_superieure",
      "type": "ecart_valeur_source",
      "detail": "Valeur source 3500 FT AMSL différente de la valeur valide 3000 FT AMSL ; changement CHG-002 EN_ATTENTE."
    }
  ],
  "total": 3,
  "date_reference": "2026-11-26"
}
```

Schéma de sortie complet : À COMPLÉTER.

## Lecture seule

Oui. L’outil ne corrige pas les anomalies et ne modifie aucune donnée.

## Entité Data Fabric lue

À COMPLÉTER. Table logique : anomalies issues de `pretraitement/rapport_validation.md`, importées dans Data Fabric.
