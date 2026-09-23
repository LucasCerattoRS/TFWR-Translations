[<- Minería](docs/unlocks/mining.md) <right>[Bambú ->](docs/unlocks/bamboo.md)
<right>[Calabazas petrificadas ->](docs/unlocks/petrified_pumpkins.md)
<right>[Perlita y suelo franco ->](docs/unlocks/special_soils.md)
---
# Arroz

Debajo de la superficie has observado una fina capa de arcilla. Resulta que este terreno fértil es perfecto para plantar brotes de arroz.

El arroz secará la arcilla en la que lo plantes. Solo puedes usar cada bloque de arcilla una vez. Por suerte, la capa tiene varios bloques de grosor. Y, por supuesto, siempre puedes usar `clear()` para restaurar la capa de arcilla del mundo.

El siguiente código puede resultarte útil para excavar hacia abajo hasta encontrar arcilla.

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

[Estadísticas](docs/stats.md)      [Minería](docs/unlocks/mining.md)      [Sentidos subterráneos](docs/unlocks/underground_senses.md)      [If](docs/scripting/if.md)      [Bucle for](docs/scripting/for.md)

[harvest()](functions/harvest)      [plant()](functions/plant)      [move()](functions/move)      [dig()](functions/dig)      [get_ground_type()](functions/get_ground_type)
