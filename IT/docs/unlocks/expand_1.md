[<- Potenziamento Velocità](docs/unlocks/speed.md) <right>[Espansione 2 ->](docs/unlocks/expand_2.md)
<right>[Estrazione ->](docs/unlocks/mining.md)
---
# Espansione 1
La tua fattoria è cresciuta! Lo spazio serve a poco se non puoi muovere il drone, quindi ora c'è una nuova funzione, `move()`, che sposta il drone. `move()` richiede di specificare la direzione in cui vuoi spostarlo. Ci sono quattro nuove costanti: `North, East, South, West`

Ad esempio, `move(North)` muoverà il drone di una casella a nord.

Se superi il bordo della fattoria, il drone riapparirà dal lato opposto.

{{codeexample 
{
    "camera_position": {"x": 0, "y": 1.8, "z": 5},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": false,
    "collapsing": true,
    "autoplay": false,
    "items": [],
    "world_size": {"x": 1, "y": 3},
    "execution_speed": 2,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 1,
    "seed": 1,
    "exclude_unlocks": ["watering", "fertilizer"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
#CODE
while True:
	move(North)
}}

---

[Ciclo While](docs/scripting/while.md)      [Operatori](docs/scripting/operators.md)      [Espansione 2](docs/unlocks/expand_2.md)

[move()](functions/move)
