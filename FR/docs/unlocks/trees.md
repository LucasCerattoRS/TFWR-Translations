[<- Carottes](docs/unlocks/carrots.md) <right>[Citrouilles ->](docs/unlocks/pumpkins.md)
---
# Arbres
Les [arbres](objects/tree) sont un meilleur moyen d'obtenir du bois que les buissons. Ils donnent 5 bois chacun. Comme les buissons, ils peuvent être plantés sur de l'herbe ou de la terre.

Les arbres aiment avoir de l'espace et les planter juste à côté les uns des autres ralentira leur croissance. Le temps de croissance est doublé pour chaque arbre qui se trouve sur une case directement au nord, à l'est, à l'ouest ou au sud de celui-ci. Donc si tu plantes des arbres sur chaque case, ils mettront `2*2*2*2 = 16` fois plus de temps à pousser.
{{codeexample 
{
    "camera_position": {"x": -1, "y": 1.8, "z": 5},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": false,
    "show_inventory": true,
    "show_output": false,
    "collapsing": false,
    "autoplay": true,
    "items": [],
    "world_size": {"x": 3, "y": 3},
    "execution_speed": 10,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 1,
    "seed": 1,
    "exclude_unlocks": ["watering", "fertilizer"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
#CODE
for i in range(get_world_size()):
	for j in range(get_world_size()):
		plant(Entities.Tree)
		move(North)
	move(East)
}}

<spoiler=montrer> L'opérateur `%` peut être utile ici. Rappelle-toi que l'opérateur `%` renvoie le reste de la division. Les nombres pairs divisés par `2` ont un reste de `0` et les nombres impairs divisés par `2` ont un reste de `1`.
Tu peux donc vérifier si un nombre est pair comme ceci :

{{codeexample 
{
    "camera_position": {"x": -0.5, "y": 1.5, "z": 4},
    "show_image": false,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": false,
    "show_output": true,
    "collapsing": true,
    "autoplay": false,
    "items": [],
    "world_size": {"x": 2, "y": 1},
    "execution_speed": 1,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 200,
    "seed": 1,
    "exclude_unlocks": ["watering", "fertilizer"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
#CODE
def is_even(n):
	return n % 2 == 0

print("is_even(0): ", is_even(0))
print("is_even(1): ", is_even(1))
print("is_even(2): ", is_even(2))
print("is_even(5): ", is_even(5))
print("is_even(-1): ", is_even(-1))
print("is_even(x): ", is_even(get_pos_x()))
}}
</spoiler>

---

[Statistiques](docs/stats.md)      [Opérateurs](docs/scripting/operators.md)      [If](docs/scripting/if.md)      [Boucle for](docs/scripting/for.md)      [Polyculture](docs/unlocks/polyculture.md)

[harvest()](functions/harvest)      [plant()](functions/plant)      [move()](functions/move)
