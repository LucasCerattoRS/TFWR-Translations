[<- Mineração](docs/unlocks/mining.md) <right>[Ferro ->](docs/unlocks/iron.md)
<right>[Salto ->](docs/unlocks/jump.md)
---
# Carvão

Acontece que o solo logo abaixo da superfície é um bom lugar para encontrar depósitos de carvão.

O carvão surge aleatoriamente em camadas horizontais com 1 bloco de espessura. O tamanho da camada cresce proporcionalmente ao tamanho do mundo, então talvez você queira aumentá-lo para encontrar mais carvão!

O programa a seguir é um bom ponto de partida para encontrar carvão. Ele escava para baixo em busca de uma camada de carvão e depois escava a leste e a oeste na esperança de encontrar mais.

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

[Estatísticas](docs/stats.md)      [Mineração](docs/unlocks/mining.md)      [Sentidos Subterrâneos](docs/unlocks/underground_senses.md)

[move()](functions/move)      [get_ground_type()](functions/get_ground_type)      [dig()](functions/dig)

