[<- Potenziamento Velocità](docs/unlocks/speed.md) <right>[Carote ->](docs/unlocks/carrots.md)
<right>[Debug ->](docs/scripting/debug.md)
<right>[Operatori ->](docs/scripting/operators.md)
---
# Pianta
L'erba è bella perché cresce automaticamente. Tutte le altre piante devono essere piantate con la funzione `plant()`. L'unica pianta che puoi piantare in questo momento è un cespuglio.
Puoi passare il tipo di pianta che vuoi piantare alla funzione in questo modo:

{{codeexample 
{
    "camera_position": {"x": 0, "y": 1.5, "z": 4},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": false,
    "collapsing": true,
    "autoplay": false,
    "items": [],
    "world_size": {"x": 1, "y": 1},
    "execution_speed": 1,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 100,
    "seed": 1,
    "exclude_unlocks": ["watering", "fertilizer"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
#CODE
plant(Entities.Bush)
}}

Questo pianterà un cespuglio sotto il drone.

Chiama `clear()` per ripristinare la fattoria a tutta erba e reimpostare la posizione del drone.

Sembra che coltivare contemporaneamente più tipi di piante nella fattoria possa talvolta aumentare la resa. Dovrai studiare la policoltura per saperne di più.

---

[Statistiche](docs/stats.md)      [If](docs/scripting/if.md)      [Sensori](docs/unlocks/senses.md)      [Policoltura](docs/unlocks/polyculture.md)

[harvest()](functions/harvest)      [plant()](functions/plant)
