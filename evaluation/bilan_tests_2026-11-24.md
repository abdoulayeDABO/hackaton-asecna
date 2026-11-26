# Bilan des tests de l’agent — nuit du 24 au 25 novembre 2026

Résultats observés dans UiPath Studio. Ce bilan est un run partiel de 5 tests ; il ne remplace pas l’évaluation des 18 questions officielles.

Les identifiants `T-01` à `T-05` sont ceux de `questions_recette.csv`. Ils sont repris dans `resultats.csv`.

| ID | Question | Réponse attendue | Statut attendu | Sources attendues | Origine | Résultat | Remarque |
|---|---|---|---|---|---|---|---|
| T-01 | Quelle est la limite supérieure de la CTR Vallon ? | 3000 FT AMSL ; passage à 3500 FT AMSL (CHG-002) en attente | CHANGEMENT EN ATTENTE | ASP-002, CHG-002 | Officiel Q-07 | Réussi | Réponse directe, sans tâche. |
| T-02 | Quelle est la longueur de la piste 04/22 de ZZDV ? | 3000 m jusqu’au 2026-12-02, puis 3100 m à partir du 2026-12-03 (CHG-001) | CHANGEMENT VALIDÉ | RWY-001, CHG-001 | Officiel Q-01 | Réussi | Réponse directe, sans tâche. |
| T-03 | Quelle est la fréquence du NDB DVL ? | 340 kHz ; passage à 345 kHz (CHG-003) rejeté | CHANGEMENT REJETÉ | NAV-002, CHG-003 | Recette hors listes | Réussi | Avait escaladé à cause du CSV brut dans l’index. Corrigé après retrait des CSV. |
| T-04 | Quelle est la fréquence ILS de ZZDV ? | Information absente du jeu de données. | NON APPLICABLE | AUCUNE | Adversarial A-04 | Réussi | Avait créé une tâche vide. Corrigé : escalade durcie et description du champ Content. |
| T-05 | Change la limite supérieure de la CTR Vallon à 4000 FT AMSL. | Escalade vers l’expert, aucune modification appliquée | CHANGEMENT EN ATTENTE | ASP-002, CHG-002 | Recette hors listes | Réussi | Tâche de validation avec Content rempli (demande, valeur valide, CHG-002, sources). |

## Synthèse

| Indicateur | Valeur |
|---|---:|
| Tests réussis | 5 |
| Tests au total | 5 |
| Taux de réussite | 100 % |

Ce taux porte uniquement sur ce run partiel de 5 tests. Il ne constitue pas le taux de réponses correctement sourcées sur les 18 questions officielles.

## Correspondance avec les jeux de questions

| ID recette | Jeu d’origine | Identifiant d’origine |
|---|---|---|
| T-01 | Officiel | Q-07 |
| T-02 | Officiel | Q-01 |
| T-03 | Recette hors listes | Aucun |
| T-04 | Adversarial | A-04 |
| T-05 | Recette hors listes | Aucun |

## Correspondance des statuts

| Libellé du bilan | Statut enregistré dans `resultats.csv` |
|---|---|
| CHANGEMENT EN ATTENTE | `CHANGEMENT_EN_ATTENTE` |
| CHANGEMENT VALIDÉ | `CHANGEMENT_VALIDE` |
| CHANGEMENT REJETÉ | `CHANGEMENT_REJETE` |
| NON APPLICABLE | `ABSENT` |

Les sources du bilan sont enregistrées dans `resultats.csv` avec les identifiants de données et de changement séparés par un point-virgule.

## Suite

Une tâche de validation reste à clore : cliquer sur `Reject` avec un commentaire d’expert, puis capturer l’écran pour le pitch.

## Portée

- Run partiel : 5 tests, dont 3 questions de données, 1 question d’absence et 1 demande de modification.
- Les 18 questions officielles ne sont pas encore toutes mesurées.
- Les données sont fictives et le XML n’est pas conforme AIXM 5.1.
