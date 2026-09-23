[<- Espansione 2](docs/unlocks/expand_2.md)
---
# Ciclo For
Il ciclo `for` funziona come in Python. In alcuni linguaggi è chiamato ciclo foreach e non va confuso con il ciclo for in stile C, che funziona in modo diverso.

`for i in sequence:
	#fai qualcosa con i`

Simile al ciclo `while`, anche il ciclo `for` chiama ripetutamente un blocco di codice. Invece di ciclare in base a una condizione, esegue il corpo del ciclo una volta per ogni elemento in una sequenza.

## Sintassi
Un ciclo for si presenta così:

`for nome_variabile in sequenza:
	#blocco di codice`

`nome_variabile` può essere un nome qualsiasi a tua scelta. È una variabile che memorizza l'elemento corrente della sequenza. `sequenza` deve essere un valore iterabile, come un intervallo di numeri. Il blocco di codice viene eseguito una volta per ogni elemento e la variabile del ciclo assume il valore di quell'elemento.

## Sequenze
[Range](functions/range)      <unlock=lists>[Liste](docs/scripting/lists.md)      </unlock><unlock=functions>[Tuple](docs/scripting/tuples.md)      </unlock><unlock=dicts>[Dizionari](docs/scripting/dicts.md)      </unlock><unlock=sets>[Set](docs/scripting/sets.md)</unlock>

## Esempio
{{codeexample 
{
    "camera_position": {"x": 0, "y": 1.5, "z": 4},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": true,
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
for i in range(5):
    harvest()
}}

Questo ciclo esegue il corpo un numero fisso di volte. È essenzialmente lo stesso che scrivere

{{codeexample 
{
    "camera_position": {"x": 0, "y": 1.5, "z": 4},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": true,
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
i = 0
harvest()
i = 1
harvest()
i = 2
harvest()
i = 3
harvest()
i = 4
harvest()
}}


---

[Ciclo While](docs/scripting/while.md)      [Break](docs/scripting/break.md)      [Continue](docs/scripting/continue.md)

[range()](functions/range)
