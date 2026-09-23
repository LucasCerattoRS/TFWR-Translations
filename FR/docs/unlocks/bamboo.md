[<- Riz](docs/unlocks/rice.md) <right>[Blocs colorés ->](docs/unlocks/debug_place.md)
<right>[Pyramides ->](docs/unlocks/pyramid.md)
---
# Bambou

Le bambou est une plante qui peut atteindre 6 blocs de haut. Il ne pousse pas tant qu’un drone se trouve au-dessus : pense donc à `move` le drone après avoir utilisé `plant(Entities.Bamboo)`. Planter du bambou coûte du riz.

Le bambou produit des fleurs lorsqu’il atteint une certaine hauteur, choisie aléatoirement. Utilise `measure()` pour connaître la hauteur à laquelle il fleurira. `measure()` commence à compter à 0 : si le bambou fleurit sur le deuxième bloc, `measure()` renvoie 1 :

{{codeexample 
{
    "camera_position": {"x": -1, "y": 0, "z": 8},
    "show_image": true,
    "image_size": {"x": 1000, "y": 500},
    "show_code": true,
    "show_inventory": true,
    "show_output": false,
    "collapsing": true,
    "autoplay": false,
    "items": [{"item": "rice", "n": 100}],
    "world_size": {"x": 4, "y": 4},
    "execution_speed": 2,
    "action_ticks": 200,
    "operation_ticks": 200,
    "seed": 1,
    "exclude_unlocks": ["watering", "fertilizer", "mushrooms", "coal"]
}
#SETUP
move(North)
move(East)
#CODE
till()
plant(Entities.Bamboo)
print(measure())
move(East)
}}

Tu obtiendras le rendement maximal du bambou si tu utilises `harvest()` lorsque ton drone se trouve directement au-dessus de la fleur. Pour chaque bloc d’écart, le rendement sera divisé par huit.
Par exemple, si la fleur se trouve à la hauteur 3, mais que tu la récoltes deux blocs plus haut, le rendement sera divisé par 64.

Pour récolter les fleurs situées plus haut, vole dans le bambou lorsque le drone est à la hauteur souhaitée. La nouvelle commande `place()` t’y aidera.

Utilise `place(Grounds.Dirt)` pour empiler des blocs à côté du bambou et grimper. Utilise ensuite `move()` pour entrer dans le bambou par le côté. Ton drone doit se trouver directement au-dessus de la fleur lorsque tu appelles `harvest()`.

`place(Grounds.Dirt)` te coûte 1 bloc ! Tu peux aussi placer d’autres sols comme `Grounds.Rock`, mais pas de blocs spéciaux comme `Grounds.Clay`.

Le bambou pousse d’exactement 1 bloc par seconde.

{{codeexample 
{
    "camera_position": {"x": -1, "y": 0, "z": 8},
    "show_image": true,
    "image_size": {"x": 1000, "y": 500},
    "show_code": true,
    "show_inventory": true,
    "show_output": false,
    "collapsing": true,
    "autoplay": false,
    "items": [{"item": "block", "n": 100}, {"item": "rice", "n": 100}],
    "world_size": {"x": 4, "y": 4},
    "execution_speed": 2,
    "action_ticks": 200,
    "operation_ticks": 200,
    "seed": 1,
    "exclude_unlocks": ["watering", "fertilizer", "mushrooms", "coal"]
}
#SETUP
move(North)
move(East)
#CODE
till()
plant(Entities.Bamboo)
print(measure())
move(East)
place(Grounds.Dirt)
do_a_flip() # attendre un peu
do_a_flip()
move(West)
harvest()
}}

---

[Statistiques](docs/stats.md)      [Boucle for](docs/scripting/for.md)      [Variables](docs/scripting/variables.md)      [If](docs/scripting/if.md)      [Fonctions](docs/scripting/functions.md)      [Riz](docs/unlocks/rice.md)

[harvest()](functions/harvest)      [plant()](functions/plant)      [move()](functions/move)      [till()](functions/till)      [place()](functions/place)      [measure()](functions/measure)
