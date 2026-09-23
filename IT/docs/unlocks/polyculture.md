[<- Zucche](docs/unlocks/pumpkins.md)
---
# Policoltura
Potresti aver già notato che a volte le piante rendono di più se piantate insieme.
Erba, cespugli, alberi e carote rendono di più quando hanno la giusta pianta compagna. La preferenza varia per ogni singola pianta e non può essere prevista. Per fortuna puoi misurare la preferenza della pianta sotto il drone usando `get_companion()`. La funzione restituisce una tupla: il primo elemento è il tipo di pianta desiderato come compagna, il secondo è la posizione in cui deve trovarsi. La pianta compagna non deve essere completamente cresciuta per ottenere il bonus alla resa.

{{codeexample 
{
    "camera_position": {"x": -1, "y": 1.8, "z": 5},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": true,
    "collapsing": true,
    "autoplay": false,
    "items": [],
    "world_size": {"x": 3, "y": 3},
    "execution_speed": 1,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 20,
    "seed": 1,
    "exclude_unlocks": ["watering", "fertilizer"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
#CODE
plant(Entities.Bush)
plant_type, (x, y) = get_companion()
print(plant_type, (x, y))
move(East)
move(South)
plant(plant_type)
move(West)
move(North)
do_a_flip()
harvest()
}}

La compagna preferita può essere `Entities.Grass`, `Entities.Bush`, `Entities.Tree` o `Entities.Carrot`. Ogni pianta sceglie casualmente, ma sempre un tipo diverso dal proprio. La posizione può trovarsi ovunque entro 3 mosse dalla pianta, tranne nella posizione della pianta stessa.

Se sotto il drone non c'è una pianta con una preferenza, `get_companion()` restituisce `None`.

Prima di sbloccare la policoltura per la prima volta, il moltiplicatore della resa è `5`. Raddoppia a ogni potenziamento.

---

[Statistiche](docs/stats.md)      [Tuple](docs/scripting/tuples.md)      [Dizionari](docs/scripting/dicts.md)      [Sensori](docs/unlocks/senses.md)      [Pianta](docs/unlocks/plant.md)

[harvest()](functions/harvest)      [plant()](functions/plant)      [move()](functions/move)      [till()](functions/till)      [get_companion()](functions/get_companion)
