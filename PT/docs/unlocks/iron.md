[<- Carvão](docs/unlocks/coal.md) <right>[Quartzo ->](docs/unlocks/quartz.md)
<right>[Prospecção de Ferro ->](docs/unlocks/prospecting.md)
<right>[Mapa do Tesouro ->](docs/unlocks/treasure_map.md)
---
# Ferro

Você descobriu veios de ferro na camada de pedra abaixo da argila.

Os veios de ferro começam pequenos, e você precisará de sorte para encontrá-los. Conforme este desbloqueio sobe de nível, o tamanho máximo dos veios aumenta. Para encontrar ferro de forma mais confiável, confira também o desbloqueio de prospecção de minério.

Um veio de ferro é sempre contínuo, sem saltos diagonais. Se encontrar um pedaço de ferro, procure mais abaixo ou ao lado para garantir que coletou o veio inteiro.

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

[Estatísticas](docs/stats.md)      [Mineração](docs/unlocks/mining.md)      [Prospecção de Ferro](docs/unlocks/prospecting.md)      [Sentidos Subterrâneos](docs/unlocks/underground_senses.md)

[move()](functions/move)      [dig()](functions/dig)

