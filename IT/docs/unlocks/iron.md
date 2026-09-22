[<- Carbone](docs/unlocks/coal.md) <right>[Quarzo ->](docs/unlocks/quartz.md)
<right>[Prospezione del Ferro ->](docs/unlocks/prospecting.md)
<right>[Mappa del Tesoro ->](docs/unlocks/treasure_map.md)
---
# Ferro

Hai scoperto vene di ferro nello strato di roccia sotto l'argilla.

All'inizio le vene di ferro sono piccole e avrai bisogno di un po' di fortuna per trovarle. Aumentando il livello di questo sblocco, cresce la dimensione massima delle vene di minerale. Per trovare il ferro in modo più affidabile, potresti anche dare un'occhiata allo sblocco della prospezione mineraria.

Una vena di ferro è sempre continua, senza salti diagonali. Se trovi un blocco di ferro, cercane altri sotto o accanto per assicurarti di raccogliere l'intera vena.

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

[Statistiche](docs/stats.md)      [Estrazione](docs/unlocks/mining.md)      [Prospezione del Ferro](docs/unlocks/prospecting.md)      [Sensi Sotterranei](docs/unlocks/underground_senses.md)

[move()](functions/move)      [dig()](functions/dig)
