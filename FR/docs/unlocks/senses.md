[<- Opérateurs](docs/scripting/operators.md)
---
# Sens
Le drone peut voir maintenant !

Les fonctions `get_pos_x()` et `get_pos_y()` renvoient les positions x et y actuelles du drone. À la position de départ, elles sont toutes les deux à `0`. La position x augmente de `1` à chaque case vers l'`East` et la position y augmente de `1` à chaque case vers le `North`.
{{codeexample 
{
    "camera_position": {"x": -1, "y": 1.8, "z": 4},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": true,
    "collapsing": true,
    "autoplay": false,
    "items": [],
    "world_size": {"x": 2, "y": 2},
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
move(East)
#CODE
print("x =", get_pos_x(), "y =", get_pos_y())
if get_pos_x() == 1 and get_pos_y() == 0:
    do_a_flip()
}}

`num_items(item)` renvoie la quantité d’un objet que tu possèdes.
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
    "items": [{"item": "hay", "n": 10}],
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
#CODE
print(num_items(Items.Hay))
}}

`get_entity_type()` et `get_ground_type()` renvoient le type d'entité ou de sol qui se trouve sous le drone.
{{codeexample 
{
    "camera_position": {"x": 0, "y": 1.5, "z": 6},
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
plant(Entities.Bush)
#CODE
print(get_entity_type())
if get_entity_type() == Entities.Bush:
	do_a_flip()

print(get_ground_type())
if get_ground_type() != Grounds.Soil:
	do_a_flip()
}}

Le mot-clé `None` est également débloqué maintenant ! `None` est une valeur qui représente l'absence de valeur.
Par exemple, une fonction qui n'a pas d'instruction `return` renverra en fait `None`.

`get_entity_type()` renvoie `None` s'il n'y a pas d'entité sous le drone.


Si tu veux savoir combien de déblocages d'un certain type tu as, utilise la fonction `num_unlocked(unlock)`.

Par exemple, `num_unlocked(Unlocks.Speed)` renverra le nombre d'améliorations de vitesse que tu as.

`num_unlocked(Unlocks.Senses)` renverra `1` si les sens sont débloqués et `0` sinon.

Tu peux aussi utiliser `num_unlocked()` sur des objets ou des entités. Elle renvoie `1` si l’objet ou l’entité est débloqué, et `0` sinon.

Attention, `num_unlocked(Unlocks.Carrots)` renverra le nombre de fois où il a été débloqué/amélioré.
`num_unlocked(Items.Carrot)` ne renverra que `0` ou `1`. (Pareil pour les autres plantes)
---

[If](docs/scripting/if.md)      [Opérateurs](docs/scripting/operators.md)      [Variables](docs/scripting/variables.md)      [Tuples](docs/scripting/tuples.md)      [Dictionnaires](docs/scripting/dicts.md)      [Sens souterrains](docs/unlocks/underground_senses.md)

[get_pos_x()](functions/get_pos_x)      [get_pos_y()](functions/get_pos_y)      [get_entity_type()](functions/get_entity_type)      [get_ground_type()](functions/get_ground_type)      [num_items()](functions/num_items)      [num_unlocked()](functions/num_unlocked)
