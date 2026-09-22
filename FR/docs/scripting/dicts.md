[<- Listes](docs/scripting/lists.md) <right>[Coûts ->](docs/unlocks/costs.md)
---
# Dictionnaires
Les dictionnaires sont une structure de données qui te permet de mapper des clés à des valeurs de la même manière qu'un vrai dictionnaire mappe des mots à leurs définitions et tu peux les rechercher très rapidement.

Un dictionnaire peut être créé comme ceci :

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
right_of = {North:East, East:South, South:West, West:North}
}}

L'expression avant les deux-points est la clé et l'expression après les deux-points est la valeur à laquelle la clé est mappée.
Le dictionnaire ci-dessus mappe chaque direction à la direction à sa droite.

En voici un autre qui mappe la position du drone à l'entité qui se trouve dessus.
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
x, y = get_pos_x(), get_pos_y()
entity_dict = {(x,y):get_entity_type()}
}}

Accéder à la valeur mappée à une clé est similaire à l'accès à un élément dans une liste :
`value = dict[key]`

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
right_of = {North:East, East:South, South:West, West:North}
print(right_of[South])
}}

Tu peux ajouter une nouvelle paire clé-valeur à un dictionnaire comme ceci :
`dict[key] = value`

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
    "world_size": {"x": 3, "y": 1},
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
plant(Entities.Bush)
move(East)
plant(Entities.Tree)
move(East)
#CODE
entity_dict = {}
for _ in range(3):
	entity_dict[(get_pos_x(), get_pos_y())] = get_entity_type()
	move(East)
print(entity_dict)
}}

Les clés sont uniques, donc l'ajout d'une clé qui existe déjà dans le dictionnaire écrasera la valeur précédente.

Utilise `dict.pop(key)` pour supprimer une paire clé-valeur de `dict`.

`key in dict` s'évalue à `True` si `key` est une clé dans le `dict` et `False` sinon.
Tu peux donc utiliser `if key in dict:` pour vérifier si `dict` contient la clé.

Mettre un dictionnaire dans une boucle `for` te permet d'itérer à travers toutes les clés :
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
right_of = {North:East, East:South, South:West, West:North}
print(North in right_of)
for key in right_of:
	value = right_of[key]
	print(key, ":", value)
}}

Il n'y a aucune garantie sur l'ordre dans lequel les clés sont itérées.

Voir aussi [Sets](docs/scripting/sets.md)

---

[Listes](docs/scripting/lists.md)      [Sets](docs/scripting/sets.md)      [Tuples](docs/scripting/tuples.md)      [Coûts](docs/unlocks/costs.md)

[len()](functions/len)
