# API et serveur MCP

## Principe

Les API sont des outils de **lecture seule**. Elles lisent les tables consolidées dans UiPath Data Fabric et ne permettent aucune création, modification ou suppression. L’agent UiPath ne les appelle que pour consulter, vérifier et sourcer une réponse.

## Les 6 outils

| Outil | Rôle | Fichier |
|---|---|---|
| `ATM_API_Etat` | État du jeu de données et date de référence. | [`outils/ATM_API_Etat.md`](outils/ATM_API_Etat.md) |
| `ATM_API_Anomalies` | Anomalies issues du rapport de validation. | [`outils/ATM_API_Anomalies.md`](outils/ATM_API_Anomalies.md) |
| `ATM_API_Aerodromes` | Consultation des aérodromes. | [`outils/ATM_API_Aerodromes.md`](outils/ATM_API_Aerodromes.md) |
| `ATM_API_EspacesAeriens` | Consultation des espaces aériens. | [`outils/ATM_API_EspacesAeriens.md`](outils/ATM_API_EspacesAeriens.md) |
| `ATM_API_Recherche` | Recherche textuelle dans les données. | [`outils/ATM_API_Recherche.md`](outils/ATM_API_Recherche.md) |
| `ATM_API_Changements` | Consultation de l’historique des changements. | [`outils/ATM_API_Changements.md`](outils/ATM_API_Changements.md) |

## Serveur MCP `atm-swim-v1`

Le serveur MCP `atm-swim-v1` expose les six outils ci-dessus à l’agent UiPath. Il sert de passerelle entre l’agent et les API de consultation.

| Élément | Valeur |
|---|---|
| Nom du serveur | `atm-swim-v1` |
| Outils exposés | Les 6 outils `ATM_API_*` |
| Mode | Lecture seule |
| Transport | À COMPLÉTER |
| URL ou point d’accès | À COMPLÉTER |
| Authentification | À COMPLÉTER (aucun secret dans ce dépôt) |
| Environnement | À COMPLÉTER |
| Version | À COMPLÉTER |

## Entités Data Fabric

Les outils lisent les tables consolidées suivantes :

| Table logique | Fichier consolidé | Entité Data Fabric |
|---|---|---|
| Aérodromes | `donnees/pretraitees/aerodromes.csv` | À COMPLÉTER |
| Pistes | `donnees/pretraitees/pistes.csv` | À COMPLÉTER |
| Aides radio | `donnees/pretraitees/aides_radio.csv` | À COMPLÉTER |
| Espaces aériens | `donnees/pretraitees/espaces_aeriens.csv` | À COMPLÉTER |
| Historique des modifications | `donnees/pretraitees/historique_modifications.csv` | À COMPLÉTER |

Les noms techniques des entités Data Fabric ne sont pas fournis dans le jeu du comité. Ils sont donc marqués `À COMPLÉTER`.

## Implémentation de référence locale

Le fichier `api_aixm.py` n’est pas fourni dans ce dépôt. Il n’y a donc pas de dossier `api/reference_fastapi/`. Si ce fichier est fourni ultérieurement, il devra être placé dans `api/reference_fastapi/` avec la mention : « implémentation de référence locale, non utilisée par l’agent ».

## Garde-fous

- Aucun outil d’écriture.
- Aucune URL ni aucun identifiant de production.
- Aucune donnée réelle, personnelle ou sensible.
- Les exemples JSON des fiches outils sont des formes illustratives à compléter, pas des résultats mesurés.
- Les données sont fictives et le XML n’est pas conforme AIXM 5.1.
