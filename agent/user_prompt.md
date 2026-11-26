# User prompt de l’agent SWIM SENEGAL

```text
Réponds à la question suivante : {{question}}
Date de référence : {{date_reference}}
Applique les étapes, les règles et le format de sortie du System prompt.
```

## Mode d’emploi dans UiPath

1. Supprimer `{{question}}` et `{{date_reference}}` du champ User prompt.
2. Réinsérer les deux variables avec la touche `@` pour qu’elles soient reconnues comme arguments.
3. Vérifier que la variable `{{date_reference}}` est fournie au format `AAAA-MM-JJ`.
4. Ne pas ajouter d’instruction qui contredirait le System prompt.

## Remarque

La date de référence utilisée pour l’évaluation est fixée dans `evaluation/README.md`. Elle doit être identique à celle utilisée pour le prétraitement.
