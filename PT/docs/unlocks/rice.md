[<- Mineração](docs/unlocks/mining.md) <right>[Bambu ->](docs/unlocks/bamboo.md)
<right>[Abóboras Petrificadas ->](docs/unlocks/petrified_pumpkins.md)
<right>[Perlita e Solo Franco ->](docs/unlocks/special_soils.md)
---
# Arroz

Sob a superfície, você percebeu uma fina camada de argila. Acontece que esse solo fértil é perfeito para plantar mudas de arroz.

O arroz seca a argila em que foi plantado. Cada bloco de argila só pode ser usado uma vez. Felizmente, a camada tem alguns blocos de espessura. E, é claro, você sempre pode usar `clear()` para restaurar a camada de argila.

O código a seguir pode ajudar você a escavar para baixo até encontrar argila.

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

[Estatísticas](docs/stats.md)      [Mineração](docs/unlocks/mining.md)      [Sentidos Subterrâneos](docs/unlocks/underground_senses.md)      [If](docs/scripting/if.md)      [Loop For](docs/scripting/for.md)

[harvest()](functions/harvest)      [plant()](functions/plant)      [move()](functions/move)      [dig()](functions/dig)      [get_ground_type()](functions/get_ground_type)
