[<- Exploitation minière](docs/unlocks/mining.md) <right>[Bambou ->](docs/unlocks/bamboo.md)
<right>[Citrouilles pétrifiées ->](docs/unlocks/petrified_pumpkins.md)
<right>[Perlite et terreau ->](docs/unlocks/special_soils.md)
---
# Riz

Sous la surface, tu as remarqué une fine couche d’argile. Il s’avère que ce sol fertile est idéal pour planter des pousses de riz.

Le riz assèche l’argile sur laquelle il est planté. Chaque bloc d’argile ne peut être utilisé qu’une seule fois. Heureusement, la couche fait plusieurs blocs d’épaisseur. Et bien sûr, tu peux toujours utiliser `clear()` pour recréer la couche d’argile.

Le code suivant peut t’aider à creuser jusqu’à trouver de l’argile.

{{codeexample 
{
    "camera_position": {"x": -1, "y": 0, "z": 8},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": false,
    "collapsing": false,
    "autoplay": true,
    "items": [{"item": "hay", "n": 100}, {"item": "wood", "n": 100}],
    "exclude_unlocks": ["watering", "fertilizer"],
    "world_size": {"x": 4, "y": 4},
    "execution_speed": 8,
    "digging_speed": 4,
    "action_ticks": 200,
    "operation_ticks": 200,
    "seed": 1
}
#SETUP
move(East)
#CODE
while get_ground_type() != Grounds.Clay:
    dig()
plant(Entities.Rice)
move(North)
do_a_flip()
}}

---

[Statistiques](docs/stats.md)      [Exploitation minière](docs/unlocks/mining.md)      [Sens souterrains](docs/unlocks/underground_senses.md)      [If](docs/scripting/if.md)      [Boucle for](docs/scripting/for.md)

[harvest()](functions/harvest)      [plant()](functions/plant)      [move()](functions/move)      [dig()](functions/dig)      [get_ground_type()](functions/get_ground_type)
