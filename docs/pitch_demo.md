# Pitch de démonstration — SWIM SENEGAL

Durée cible : À COMPLÉTER.

## Étape 1 — Données dans Data Fabric et serveur MCP

Montrer les CSV consolidés dans `donnees/pretraitees/`, les tables correspondantes dans UiPath Data Fabric et le serveur MCP `atm-swim-v1` avec ses six outils. Rappeler que les fichiers bruts du comité n’ont pas été modifiés et que l’agent est en lecture seule.

## Étape 2 — Trois questions

Poser les trois questions suivantes et montrer la réponse, le statut et les sources.

| Question | Réponse attendue | Statut attendu | Sources attendues |
|---|---|---|---|
| Quelle est la limite supérieure de la CTR Vallon ? | 3000 FT AMSL ; le passage à 3500 FT AMSL est en attente (date d’effet 2026-12-31). | `CHANGEMENT_EN_ATTENTE` | `ASP-002` |
| Quelle est la fréquence du NDB DVL ? | 340 kHz ; le passage à 345 kHz a été rejeté. | `CHANGEMENT_REJETE` | `NAV-002` |
| Quelle est la fréquence de l’aérodrome de Ziguinchor ? | Information absente du jeu de données. | `ABSENT` | `AUCUNE` |

La troisième question montre que l’agent ne complète pas avec des connaissances générales : Ziguinchor n’est pas dans le jeu de données fictif.

## Étape 3 — Demande de modification

Demander par exemple : « Modifie la limite supérieure de la CTR Vallon à 4000 FT AMSL. » L’agent ne modifie rien : il crée une tâche dans Action Center avec le motif `DEMANDE_MODIFICATION`, un contenu factuel et un commentaire. Montrer les champs `Content` et `Comment`, puis la décision attendue de l’expert métier.

## Étape 4 — Ouverture de la trace

Ouvrir la tâche dans Action Center et montrer la trace : question, date de référence, outils appelés, sources consultées, changement associé, motif et décision de l’expert. Conclure par la mention « Données fictives de démonstration. À valider par le référent métier. »

## Points à ne pas oublier

- Ne pas présenter le XML comme conforme AIXM 5.1.
- Ne pas présenter une valeur `EN_ATTENTE` ou `REJETEE` comme valide.
- Ne pas montrer de secret, de jeton ou de clé.
- Ne pas exécuter de demande d’écriture.
