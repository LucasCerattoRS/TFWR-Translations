[<- Espansione 1](docs/unlocks/expand_1.md)
---
# Espansione 2
La tua fattoria si è espansa di nuovo! Ora le caselle non sono più in una bella fila, quindi devi trovare un modo per attraversare una griglia quadrata.

Con il ciclo `while` questo non è possibile finché non sblocchi i sensori e gli operatori.
È ora di introdurre il ciclo `for`.

Puoi leggere tutto sul ciclo `for` nella pagina [Ciclo For](docs/scripting/for.md), ma per ora ti servirà solo per ripetere del codice un numero fisso di volte.

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
for i in range(5):
	do_a_flip()
}}

`range(n)` crea una sequenza di `n` numeri da `0` a `n - 1`. Il ciclo `for` esegue il proprio corpo una volta per ogni elemento della sequenza. In questo esempio, `do_a_flip()` viene chiamata `5` volte.

Ora è disponibile anche la funzione `get_world_size()`. Restituisce la lunghezza del lato della tua fattoria. In questo modo puoi scrivere codice che non si romperà con il prossimo potenziamento di espansione.

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
    "items": [],
    "world_size": {"x": 3, "y": 3},
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
do_a_flip()
#CODE
for i in range(get_world_size()):
	harvest()
	move(North)
}}

Questo esempio raccoglie una colonna della fattoria per qualsiasi dimensione della fattoria.

Se non riesci a capire come spostare il drone nella fattoria, consulta il suggerimento qui sotto.
<spoiler=mostra suggerimento>Ci sono, ovviamente, diversi modi per muoversi nella fattoria.
Quello che cerchiamo è un modo per attraversarla sistematicamente che non si rompa quando la fattoria crescerà di nuovo.
Un modo sistematico per raggiungere ogni punto della fattoria consiste nel ripetere per sempre i due passaggi seguenti:

1. Muoviti verso `North` finché il drone non riappare dal lato opposto.
2. Muoviti verso `East`.

`for i in range(get_world_size()):` potrebbe essere utile per trasformare questa idea in codice.
</spoiler>
<spoiler=mostra soluzione possibile>
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
    "items": [],
    "world_size": {"x": 3, "y": 3},
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
do_a_flip()
#CODE
for i in range(get_world_size()):
	for j in range(get_world_size()):
		#fai una capriola su ogni casella
		do_a_flip()
		move(North)
	move(East)
}}
</spoiler>

---

[Ciclo For](docs/scripting/for.md)      [Ciclo While](docs/scripting/while.md)      [Variabili](docs/scripting/variables.md)

[move()](functions/move)      [get_world_size()](functions/get_world_size)
