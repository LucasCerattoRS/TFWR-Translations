[<- Expansion 2](docs/unlocks/expand_2.md)
---
# Boucle For
La boucle `for` fonctionne comme en Python. (Appelée boucle foreach dans certains langages, à ne pas confondre avec la boucle for de style C, qui est une chose différente).

`for i in sequence:
	#faire quelque chose avec i`

Similaire à la boucle `while`, la boucle `for` appelle également un bloc de code de manière répétée. Au lieu de boucler sur la base d'une condition, elle exécute le corps de la boucle une fois pour chaque élément d'une séquence.

## Syntaxe
Une boucle for ressemble à ceci :

`for variable_name in sequence:
	#bloc de code`

`variable_name` peut être n'importe quel nom que tu choisis. C'est une variable qui stocke l'élément actuel dans la séquence. `sequence` doit être une valeur qui peut être itérée comme un range de nombres. Le bloc de code est exécuté pour chaque élément avec la variable de boucle assignée à cet élément.

## Séquences
[Ranges](functions/range)      <unlock=lists>[Listes](docs/scripting/lists.md)      </unlock><unlock=functions>[Tuples](docs/scripting/tuples.md)      </unlock><unlock=dicts>[Dictionnaires](docs/scripting/dicts.md)      </unlock><unlock=sets>[Sets](docs/scripting/sets.md)</unlock>

## Exemple
{{codeexample 
{
    "camera_position": {"x": 0, "y": 1.5, "z": 4},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": true,
    "collapsing": true,
    "autoplay": false,
    "items": [],
    "world_size": {"x": 1, "y": 1},
    "execution_speed": 1,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 100,
    "seed": 1,
    "exclude_unlocks": ["watering", "fertilizer"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
do_a_flip()
#CODE
for i in range(5):
    harvest()
}}

Cette boucle exécute le corps un nombre fixe de fois. C'est essentiellement la même chose que d'écrire

{{codeexample 
{
    "camera_position": {"x": 0, "y": 1.5, "z": 4},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": true,
    "collapsing": true,
    "autoplay": false,
    "items": [],
    "world_size": {"x": 1, "y": 1},
    "execution_speed": 1,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 100,
    "seed": 1,
    "exclude_unlocks": ["watering", "fertilizer"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
do_a_flip()
#CODE
i = 0
harvest()
i = 1
harvest()
i = 2
harvest()
i = 3
harvest()
i = 4
harvest()
}}


---

[Boucle while](docs/scripting/while.md)      [Break](docs/scripting/break.md)      [Continue](docs/scripting/continue.md)

[range()](functions/range)
