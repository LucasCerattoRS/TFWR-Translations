[<- Ciclo While](docs/scripting/while.md) <right>[Espansione 1 ->](docs/unlocks/expand_1.md)
<right>[Pianta ->](docs/unlocks/plant.md)
---
# Potenziamento Velocità
La velocità di esecuzione è raddoppiata. Il problema è che ora il drone raccoglie più velocemente di quanto cresca l'erba, senza ottenere alcuna resa. Per risolvere il problema sono ora sbloccati i rami [if](docs/scripting/if.md) e la funzione [can_harvest()](functions/can_harvest).

## Controllare Prima di Raccogliere
Un'istruzione `if` esegue una volta il proprio blocco di codice se la condizione indicata è `True`.

La nuova funzione `can_harvest()` fornisce una condizione utile. `can_harvest()` restituisce `True` se la pianta sotto il drone può essere raccolta e `False` altrimenti.

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
do_a_flip()
#CODE
if can_harvest():
	do_a_flip()
}}

Puoi immaginare un valore di ritorno come se, durante la valutazione dell'`if`, l'espressione di chiamata `can_harvest()` venisse sostituita dal valore restituito `True`.

Cosa succede quando il codice sopra viene eseguito:
- Viene eseguita l'istruzione `if`.
- Viene chiamata `can_harvest()`.
- `can_harvest()` restituisce `True` perché l'erba è completamente cresciuta.
- L'istruzione ora è `if True:`.
- Il ramo viene eseguito perché il valore è `True`.

Se l'erba non fosse completamente cresciuta, il drone non farebbe un flip.

Ora possiamo usare `if` per impedire al drone di raccogliere troppo presto.

---

[If](docs/scripting/if.md)      [Ciclo While](docs/scripting/while.md)

[harvest()](functions/harvest)      [can_harvest()](functions/can_harvest)
