[<- Premier programme](docs/first_program.md)
---
# Commentaires
Les commentaires sont des parties du code qui sont ignorées lors de l'exécution.
Les commentaires peuvent être ajoutés en utilisant `#`. Tout ce qui se trouve sur la même ligne après le `#` est un commentaire et sera ignoré.

{{codeexample 
{
    "show_image": false,
    "show_code": true,
    "show_inventory": false,
    "show_output": true,
    "collapsing": true,
    "autoplay": false,
    "execution_speed": 1,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 100,
    "seed": 0,
    "exclude_unlocks": ["watering", "fertilizer"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
#CODE
#ceci est un commentaire
#harvest()
}}

Cela peut être utile pour ajouter des notes au code, et aussi pour désactiver temporairement des parties du code sans les supprimer.

Tout commentaire sur la ligne précédant une définition de fonction fera partie des informations contextuelles qui apparaissent lorsque tu survoles le nom de la fonction avec la souris.

---

[Premier programme](docs/first_program.md)      [Débogage](docs/scripting/debug.md)      [Fonctions](docs/scripting/functions.md)
