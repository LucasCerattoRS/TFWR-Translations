[<- Minería](docs/unlocks/mining.md) <right>[Hierro ->](docs/unlocks/iron.md)
<right>[Saltar ->](docs/unlocks/jump.md)
---
# Carbón

Resulta que el terreno situado justo debajo de la superficie es un buen lugar para encontrar depósitos de carbón.

El carbón aparece al azar en capas horizontales de 1 bloque de grosor. El tamaño de la capa crecerá en proporción al tamaño de tu mundo, así que puede que te convenga aumentarlo para encontrar más carbón.

El siguiente programa es un buen punto de partida para encontrar carbón. Excava hacia abajo en busca de una capa de carbón y luego excava hacia el este y el oeste con la esperanza de hallar más.

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

[Estadísticas](docs/stats.md)      [Minería](docs/unlocks/mining.md)      [Sentidos subterráneos](docs/unlocks/underground_senses.md)

[move()](functions/move)      [get_ground_type()](functions/get_ground_type)      [dig()](functions/dig)
