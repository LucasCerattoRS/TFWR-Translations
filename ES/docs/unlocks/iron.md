[<- Carbón](docs/unlocks/coal.md) <right>[Cuarzo ->](docs/unlocks/quartz.md)
<right>[Prospección de hierro ->](docs/unlocks/prospecting.md)
<right>[Mapa del tesoro ->](docs/unlocks/treasure_map.md)
---
# Hierro

Has descubierto vetas de hierro en la capa de roca que hay debajo de la arcilla.

Las vetas de hierro empiezan siendo pequeñas y necesitarás algo de suerte para encontrarlas. A medida que consigas niveles más altos de este desbloqueo, aumentará el tamaño máximo de las vetas. Si quieres una forma más fiable de encontrar hierro, también puedes echar un vistazo al desbloqueo de prospección de minerales.

Las vetas de hierro siempre son continuas y no dan saltos diagonales. Si encuentras un bloque de hierro, busca más debajo o a su lado para asegurarte de recoger toda la veta.

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
    "world_size": {"x": 5, "y": 5},
    "execution_speed": 1,
    "digging_speed": 4,
    "action_ticks": 200,
    "operation_ticks": 200,
    "seed": 9,
    "exclude_unlocks": ["watering", "fertilizer", "mushrooms", "coal", "quartz"]
}
#SETUP
jump(Unlocks.Iron)
#CODE
for i in range(4):
    dig()
do_a_flip()
}}

---

[Estadísticas](docs/stats.md)      [Minería](docs/unlocks/mining.md)      [Prospección de hierro](docs/unlocks/prospecting.md)      [Sentidos subterráneos](docs/unlocks/underground_senses.md)

[move()](functions/move)      [dig()](functions/dig)
