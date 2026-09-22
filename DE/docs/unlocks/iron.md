[<- Kohle](docs/unlocks/coal.md) <right>[Quarz ->](docs/unlocks/quartz.md)
<right>[Eisensuche ->](docs/unlocks/prospecting.md)
<right>[Schatzkarte ->](docs/unlocks/treasure_map.md)
---
# Eisen

Du hast Eisenadern in der Gesteinsschicht unter dem Ton entdeckt.

Eisenadern sind anfangs klein, und du brauchst etwas Glück, um sie zu finden. Mit höheren Stufen dieser Freischaltung steigt die maximale Größe einer Erzader. Wenn du Eisen zuverlässiger finden möchtest, solltest du dir auch die Freischaltung zur Erzsuche ansehen.

Eine Eisenader ist immer zusammenhängend und weist keine diagonalen Sprünge auf. Wenn du einen Eisenblock findest, suche darunter und daneben nach weiteren, damit du die gesamte Ader abbaust.

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

[Statistiken](docs/stats.md)      [Bergbau](docs/unlocks/mining.md)      [Eisensuche](docs/unlocks/prospecting.md)      [Unterirdische Sinne](docs/unlocks/underground_senses.md)

[move()](functions/move)      [dig()](functions/dig)
