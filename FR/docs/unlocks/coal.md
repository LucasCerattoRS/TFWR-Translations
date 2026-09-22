[<- Exploitation minière](docs/unlocks/mining.md) <right>[Fer ->](docs/unlocks/iron.md)
<right>[Saut ->](docs/unlocks/jump.md)
---
# Charbon

Il s’avère que le sous-sol juste sous la surface est un bon endroit où trouver des gisements de charbon.

Le charbon apparaît aléatoirement en couches horizontales de 1 bloc d’épaisseur. La taille de la couche augmente proportionnellement à celle de ton monde : tu peux donc l’agrandir pour trouver plus de charbon !

Le programme suivant est un bon point de départ pour chercher du charbon. Il creuse vers le bas à la recherche d’une couche, puis creuse à l’est et à l’ouest dans l’espoir d’en trouver davantage.

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
    "world_size": {"x": 4, "y": 4},
    "execution_speed": 4,
    "digging_speed": 2,
    "action_ticks": 200,
    "operation_ticks": 200,
    "seed": 2
}
#SETUP
move(North)
move(East)
move(East)
#CODE
while get_ground_type() != Grounds.Coal:
    dig()
dig()
move(East)
dig()
move(West)
move(West)
dig()
}}

---

[Statistiques](docs/stats.md)      [Exploitation minière](docs/unlocks/mining.md)      [Sens souterrains](docs/unlocks/underground_senses.md)

[move()](functions/move)      [get_ground_type()](functions/get_ground_type)      [dig()](functions/dig)
