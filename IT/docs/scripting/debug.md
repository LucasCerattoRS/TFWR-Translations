[<- Pianta](docs/unlocks/plant.md) <right>[Debug 2 ->](docs/unlocks/debug2.md)
<right>[Tempi ->](docs/unlocks/timing.md)
---
# Debug
A volte il tuo codice semplicemente non funziona e devi scoprire perché. Ci sono un paio di strumenti per aiutarti a farlo.

Il primo è eseguire il programma passo dopo passo.
Puoi entrare in modalità passo dopo passo con il pulsante accanto al pulsante Esegui o impostando un breakpoint.

I breakpoint possono essere aggiunti cliccando sul pannello dei breakpoint a sinistra del codice.
![|x227](Breakpoints)
Quando l'esecuzione raggiunge la riga in cui si trova il breakpoint, passerà automaticamente alla modalità passo dopo passo.

Quando sposti il mouse su una variabile, viene visualizzato il suo valore attuale.

Anche la funzione `print()` può essere molto utile. Scriverà qualsiasi valore passato ad essa direttamente in aria.

Esempi:

{{codeexample 
{
    "show_image": false,
    "show_code": true,
    "show_inventory": false,
    "show_output": true,
    "collapsing": true,
    "autoplay": false,
    "execution_speed": 1,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 100,
    "seed": 0,
    "exclude_unlocks": ["watering", "fertilizer"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
#CODE
print(0.24)
}}

{{codeexample 
{
    "show_image": false,
    "show_code": true,
    "show_inventory": false,
    "show_output": true,
    "collapsing": true,
    "autoplay": false,
    "execution_speed": 1,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 100,
    "seed": 0,
    "exclude_unlocks": ["watering", "fertilizer"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
#CODE
print(can_harvest())
}}

{{codeexample 
{
    "show_image": false,
    "show_code": true,
    "show_inventory": false,
    "show_output": true,
    "collapsing": true,
    "autoplay": false,
    "execution_speed": 1,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 100,
    "seed": 0,
    "exclude_unlocks": ["watering", "fertilizer"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
#CODE
print(get_pos_x(), get_pos_y())
}}

La funzione `print()` stampa il valore direttamente in aria e nella pagina [Output](docs/output.md).

Scrivere in aria a volte può essere un po' lento se vuoi stampare molti valori.
In questo caso puoi usare la funzione `quick_print()`, che stampa solo nella finestra di output.

La finestra di output registra anche avvisi ed errori, quindi può essere utile controllarla quando qualcosa non funziona come previsto.

Quando l'esecuzione si ferma, l'output viene scritto anche nel file [output.txt](persistent_data_path/output.txt) nella cartella del gioco.

---

[Output](docs/output.md)      [Commenti](docs/scripting/comments.md)      [Debug 2](docs/unlocks/debug2.md)      [Blocchi Colorati](docs/unlocks/debug_place.md)      [Simulazione](docs/unlocks/simulation.md)

[print()](functions/print)      [quick_print()](functions/quick_print)
