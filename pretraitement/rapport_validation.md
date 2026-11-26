# Rapport de validation — SWIM SENEGAL

Date de génération : 2026-11-26 00:13
Date de référence utilisée : 2026-11-26

> Données fictives de démonstration. Le schéma XSD utilisé est un schéma maison, et non un schéma AIXM 5.1 officiel. Le fichier XML source se déclare `AIXM-inspired-SYNTHETIC-NOT-AIXM-5.1-CONFORMANT`.

## 1. Fichiers traités

| Fichier | Lignes lues | BOM détecté | Colonnes conformes |
|---|---:|---|---|
| aerodromes.csv | 2 | Oui | Oui |
| pistes.csv | 2 | Oui | Oui |
| aides_radio.csv | 3 | Oui | Oui |
| espaces_aeriens.csv | 3 | Oui | Oui |
| historique_modifications.csv | 3 | Oui | Oui |

## 2. Contrôles de structure

| Contrôle | Résultat | Détail |
|---|---|---|
| Colonnes attendues | OK | Colonnes comparées aux en-têtes du jeu du comité. |
| Unicité des identifiants | OK | Contrôle des clés `id` et `change_id`. |
| Références entre tables | OK | Pistes et aides radio rattachées à un code aérodrome ; changements rattachés à un objet existant. |
| Historique des modifications | OK | Statuts, champs, dates et valeurs contrôlés. |

## 3. Validation du schéma XSD maison

- Fichier de schéma : `pretraitement/schema_demo.xsd`.
- Résultat : **Validé**.
- Aucune erreur de structure XML détectée par le schéma maison.
- Ce contrôle ne vaut pas validation AIXM 5.1.

## 4. Anomalies détectées

| Table | Objet | Champ | Type | Détail |
|---|---|---|---|---|
| pistes | RWY-001 | longueur_m | ecart_valeur_source | Valeur source « 3100 » déjà passée à la nouvelle valeur alors que l’effet est futur (2026-12-03) ; changement CHG-001. |
| aides_radio | NAV-002 | frequence | ecart_valeur_source | Valeur source « 345 kHz » différente de la valeur valide « 340 kHz » ; changement CHG-003 REJETEE. |
| espaces_aeriens | ASP-002 | limite_superieure | ecart_valeur_source | Valeur source « 3500 FT AMSL » différente de la valeur valide « 3000 FT AMSL » ; changement CHG-002 EN_ATTENTE. |

## 5. Valeurs retenues après consolidation

| Table | Objet | Champ | Valeur source | Valeur valide retenue | Changement | Statut |
|---|---|---|---|---|---|---|
| pistes | RWY-001 | longueur_m | 3100 | 3000 applicable au 2026-11-26 ; 3100 à partir du 2026-12-03 | CHG-001 | FUTURE |
| aides_radio | NAV-002 | frequence | 345 kHz | 340 kHz (inchangée) | CHG-003 | REJETEE |
| espaces_aeriens | ASP-002 | limite_superieure | 3500 FT AMSL | 3000 FT AMSL (inchangée) | CHG-002 | EN_ATTENTE |

## 6. Fichiers consolidés écrits

| Fichier | Lignes |
|---|---:|
| `donnees/pretraitees/aerodromes.csv` | 2 |
| `donnees/pretraitees/pistes.csv` | 2 |
| `donnees/pretraitees/aides_radio.csv` | 3 |
| `donnees/pretraitees/espaces_aeriens.csv` | 3 |
| `donnees/pretraitees/historique_modifications.csv` | 3 |

## 7. Règles de consolidation appliquées

- Changement `VALIDEE` avec date d’effet passée ou égale à la date de référence : nouvelle valeur retenue.
- Changement `VALIDEE` avec date d’effet future : valeur avant et valeur après conservées, avec les dates.
- Changement `EN_ATTENTE` ou `REJETEE` : valeur inchangée, changement signalé dans `changement_associe`.
- La colonne `changement_associe` vaut `Aucun` lorsqu’aucun changement ne concerne la ligne.

## 8. Limites

- Le schéma XSD est un schéma maison ; il ne s’agit pas d’une validation XSD AIXM 5.1 officielle.
- Le jeu de données est petit et fictif ; les contrôles ne couvrent pas un jeu de production.
- Les contrôles portent sur la structure et la cohérence interne, pas sur la validité aéronautique réelle.

