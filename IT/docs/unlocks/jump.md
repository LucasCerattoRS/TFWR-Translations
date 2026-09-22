[<- Carbone](docs/unlocks/coal.md)
---
# Salto

Il tuo drone ha sbloccato il comando `jump()`.

Questo comando permette di scegliere determinati sblocchi come bersaglio e saltare direttamente verso di essi. È particolarmente utile per il debug o per tornare a una vena mineraria che hai appena mancato. Per usarlo, passa uno sblocco come argomento, per esempio `Unlocks.Iron`.

`jump()` funziona solo con gli sblocchi presenti nel sottosuolo, come `jump(Unlocks.Rice)` o `jump(Unlocks.Iron)`.

{{codeexample 
{
    "camera_position": {"x": -1, "y": 0, "z": 8},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": false,
    "collapsing": true,
    "autoplay": false,
    "items": [],
    "world_size": {"x": 4, "y": 4},
    "execution_speed": 1,
    "digging_speed": 3,
    "action_ticks": 200,
    "operation_ticks": 200,
    "seed": 1,
    "exclude_unlocks": ["watering", "fertilizer", "mushrooms"],
    "starting_chunk": 0
}
#CODE
dig()
dig()
dig()
jump(Unlocks.Iron)
do_a_flip()
}}

Non è garantito che il salto ti porti direttamente allo sblocco bersaglio, quindi potresti dover cercare un po' nei dintorni, ma il bersaglio sarà sicuramente nelle vicinanze.

`jump()` può essere usato una sola volta per esecuzione del programma.

---

[jump()](functions/jump)
