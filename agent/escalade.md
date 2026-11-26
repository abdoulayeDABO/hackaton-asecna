# Description de l’escalade

L’agent ne corrige jamais une donnée et ne prend aucune décision opérationnelle. Il crée une tâche dans l’application de revue Action Center et attend la validation de l’expert métier.

## Principe

- **Simple consultation sans anomalie** : réponse directe, aucune tâche Action Center.
- **Cas nécessitant une revue** : création d’une tâche avec un motif, un contenu factuel et un commentaire.
- Une tâche ne vaut pas validation : elle demande une décision à l’expert.
- L’agent ne propose jamais une valeur inventée. Il expose la valeur observée, la valeur attendue et les sources.

## Les 4 cas d’escalade

| Cas | Déclencheur | Motif | Décision attendue |
|---|---|---|---|
| 1. Anomalie sur l’objet demandé | `ATM_API_Anomalies` signale une anomalie sur l’objet ou le champ demandé. | `ANOMALIE_DONNEES` | Confirmer ou corriger la donnée avant de répondre. |
| 2. Demande de création, modification ou suppression | L’utilisateur demande d’ajouter, de modifier ou de supprimer une donnée. | `DEMANDE_MODIFICATION` | Refuser l’écriture automatique et faire traiter la demande par l’expert. |
| 3. Deux sources en désaccord | Deux outils ou deux sources donnent des valeurs différentes pour le même objet et le même champ. | `ECART_VALEUR` | Arbitrer la valeur de référence. |
| 4. Correction envisagée | L’agent constate qu’une valeur paraît incohérente ou qu’une correction serait nécessaire. | `ECART_VALEUR` | Vérifier l’écart et décider d’une correction éventuelle. |

## Motifs autorisés

- `ANOMALIE_DONNEES`
- `ECART_VALEUR`
- `DEMANDE_MODIFICATION`

Aucun autre motif ne doit être utilisé.

## Application de revue Action Center

Application de revue : À COMPLÉTER (nom de l’application dans Action Center).

### Champ `Content`

Le champ `Content` contient un résumé court et factuel :

```text
Question : <question reçue>
Objet : <identifiant et libellé de l’objet>
Champ : <champ concerné>
Motif : <ANOMALIE_DONNEES | ECART_VALEUR | DEMANDE_MODIFICATION>
Valeur observée : <valeur et source>
Valeur attendue ou valeur valide : <valeur et source, ou À COMPLÉTER>
Date de référence : <AAAA-MM-JJ>
Action demandée : <vérifier | arbitrer | traiter la demande de modification>
```

### Champ `Comment`

Le champ `Comment` contient les éléments de preuve et le détail :

```text
Sources : <identifiants des lignes, changements et outils consultés>
Constat : <description factuelle de l’anomalie, de l’écart ou de la demande>
Changement associé : <identifiant du changement, statut, date d’effet, ou Aucun>
Étapes déjà réalisées : <outils appelés et résultats obtenus>
Limite : l’agent est en lecture seule et ne peut pas modifier la donnée.
Mention : Données fictives de démonstration. À valider par le référent métier.
```

## Règles de rédaction

- Ne jamais écrire de secret, de mot de passe, de jeton ou de clé dans `Content` ou `Comment`.
- Ne jamais présenter une valeur `EN_ATTENTE` ou `REJETEE` comme valide.
- Ne jamais affirmer que la donnée est conforme AIXM 5.1.
- Ne jamais créer de tâche pour une simple consultation sans anomalie.
- Ne jamais inclure de données personnelles ou de données réelles dans la démonstration.
- Tracer la date de référence, les identifiants des sources et le motif.

## Sortie de l’agent en cas d’escalade

```text
reponse : Une tâche de revue a été créée pour l’expert métier. Aucune donnée n’a été modifiée. Données fictives de démonstration. À valider par le référent métier.
statut : ESCALADE
sources : <identifiants concernés, ou AUCUNE>
changement_associe : <identifiant du changement, ou Aucun>
```
