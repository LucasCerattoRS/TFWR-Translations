[<- Annaffiare](docs/unlocks/watering.md) <right>[Labirinti ->](docs/unlocks/mazes.md)
---
# Fertilizzante
A un certo punto, aspettare che le piante crescano non è più abbastanza efficiente.
Come per l'acqua, riceverai automaticamente 1 fertilizzante ogni 10 secondi. La quantità raddoppia a ogni potenziamento.

Il fertilizzante può far crescere le piante istantaneamente. `use_item(Items.Fertilizer)` riduce il tempo di crescita rimanente della pianta sotto il drone di 2 secondi.

{{codeexample 
{
    "camera_position": {"x": 0, "y": 1, "z": 5},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": false,
    "collapsing": true,
    "autoplay": false,
    "items": [{"item": "fertilizer", "n": 10}],
    "world_size": {"x": 1, "y": 1},
    "execution_speed": 2,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 1,
    "seed": 1,
    "exclude_unlocks": ["watering"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
#CODE
plant(Entities.Tree)
use_item(Items.Fertilizer)
use_item(Items.Fertilizer)
use_item(Items.Fertilizer)
harvest()
}}

Questo ha alcuni effetti collaterali.
Le piante coltivate con fertilizzante saranno infette.

Quando una pianta è infetta, metà del suo raccolto viene trasformata in `Items.Weird_Substance` quando viene raccolta.
La Sostanza Strana può anche essere usata sulle piante, il che ha l'effetto di alternare lo stato di infezione della pianta e di tutte le piante adiacenti.

Se chiami `use_item(Items.Weird_Substance)` su una pianta infetta, la curerà; se lo usi su una pianta sana, la infetterà.

Se lo usi su una pianta infetta con vicini sani, curerà la pianta ma infetterà i vicini, e viceversa.

{{codeexample 
{
    "camera_position": {"x": -1, "y": 1.8, "z": 5},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": false,
    "collapsing": true,
    "autoplay": false,
    "items": [{"item": "weird_substance", "n": 10}],
    "world_size": {"x": 3, "y": 3},
    "execution_speed": 1,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 1,
    "seed": 1,
    "exclude_unlocks": ["watering"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
for _ in range(3):
    for _ in range(3):
        plant(Entities.Tree)
        move(East)
    move(North)

move(North)
move(East)

for _ in range(60):
    do_a_flip()
#CODE
for _ in range(6):
    use_item(Items.Weird_Substance)
    move(East)
}}

---

[Statistiche](docs/stats.md)      [Annaffiare](docs/unlocks/watering.md)      [Labirinti](docs/unlocks/mazes.md)

[use_item()](functions/use_item)
