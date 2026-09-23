[<- Annaffiare](docs/unlocks/watering.md)
---
# Girasoli
I [girasoli](objects/sunflower) raccolgono l'energia del sole. Puoi raccogliere quell'energia. 

Piantarli funziona esattamente come piantare carote o zucche. 

La raccolta di un girasole cresciuto produce energia.
Se nella fattoria ci sono almeno 10 girasoli e ne raccogli uno con il maggior numero di petali, ottieni `8` volte più energia!
Se raccogli un girasole mentre ce n'è un altro con più petali, anche il prossimo girasole che raccoglierai ti darà solo la quantità normale di energia (non il bonus 8x).

`measure()` restituisce il numero di petali del girasole sotto il drone.
I girasoli hanno almeno `7` e al massimo `15` petali.
I girasoli possono essere misurati e contano per il limite di 10 già prima di essere completamente cresciuti.

Più girasoli possono avere lo stesso numero di petali, quindi potrebbero essercene diversi con il numero massimo. In questo caso non importa quale raccogli.

{{codeexample 
{
    "camera_position": {"x": -1.5, "y": 2, "z": 4},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "inventory_scale": 5,
    "show_output": false,
    "collapsing": true,
    "autoplay": false,
    "items": [{"item": "carrot", "n": 10}],
    "world_size": {"x": 5, "y": 2},
    "execution_speed": 2,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 1,
    "seed": 4,
    "exclude_unlocks": ["fertilizer", "watering"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
move(North)
for _ in range(5):
    till()
    plant(Entities.Sunflower)
    move(East)
move(North)
do_a_flip()
do_a_flip()
do_a_flip()
do_a_flip()
do_a_flip()
#CODE
for _ in range(5):
    till()
    plant(Entities.Sunflower)
    print(measure())
    move(East)
for _ in range(5):
    while not can_harvest():
        pass
    harvest()
    move(East)
}}

Finché hai energia, il drone la usa per funzionare al doppio della velocità.
Consuma 1 unità di energia ogni 30 azioni, come movimenti, raccolti o semine.
Anche l'esecuzione di altre istruzioni di codice può consumare energia, ma molto meno delle azioni del drone.

In generale, tutto ciò che è accelerato dai potenziamenti di velocità è anche accelerato dall'energia.
Qualsiasi cosa accelerata dall'energia consuma anche energia in proporzione al tempo necessario per eseguirla, ignorando i potenziamenti di velocità.

---

[Statistiche](docs/stats.md)      [Liste](docs/scripting/lists.md)      [Dizionari](docs/scripting/dicts.md)      [Variabili](docs/scripting/variables.md)      [Ciclo For](docs/scripting/for.md)      [If](docs/scripting/if.md)      [Operatori](docs/scripting/operators.md)

[harvest()](functions/harvest)      [plant()](functions/plant)      [move()](functions/move)      [till()](functions/till)      [measure()](functions/measure)
