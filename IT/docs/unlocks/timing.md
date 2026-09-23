[<- Debug](docs/scripting/debug.md) <right>[Simulazione ->](docs/unlocks/simulation.md)
---
# Tempi
Se vuoi davvero ottimizzare i tuoi metodi, devi capire come viene misurato il tempo in questo gioco. Questo sblocco serve proprio a questo.

## Nuove Funzioni
Ci sono due funzioni utili per misurare quanto tempo impiegano le cose:

`get_time()` restituisce il tempo in secondi dall'inizio del gioco.

`get_tick_count()` restituisce il numero di tick eseguiti dall'inizio dell'esecuzione.

Queste due funzioni, così come `quick_print()`, sono completamente gratuite. Perfino l'operazione di chiamata non costa nulla.

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
    "operation_ticks": 1,
    "seed": 1,
    "exclude_unlocks": ["watering", "fertilizer"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
#CODE
start_time, start_ticks = get_time(), get_tick_count()
harvest()
time, ticks = get_time(), get_tick_count()
quick_print(time - start_time, ticks - start_ticks)
}}

## Dettagli sul Runtime

### Attenzione
Questo non è il modo in cui le prestazioni funzionano nel mondo reale. Queste sono solo regole create per questo gioco per avere un modello di timing coerente e comprensibile.
Probabilmente ti interesserà solo se vuoi iper-ottimizzare il tuo codice.


L'unità di tempo fondamentale per l'esecuzione del codice si chiama "tick". Senza potenziamenti di velocità né energia, l'esecuzione procede a `400` tick al secondo.

In generale, le operazioni che combinano due valori come `+, -, *, /, //, %, and, or, ...` richiedono un tick per essere eseguite.
Gli operatori unari `-` e `not` sono gratuiti.
Un ramo `if` richiede anche un tick per essere eseguito (oltre al tempo necessario per valutare l'espressione della condizione).
Le chiamate di funzione e le letture e scritture di variabili sono gratuite, ma le definizioni di funzione richiedono 1 tick.
Le istruzioni `import` sono gratuite.
L'accesso a un modulo importato con l'operatore `.` è gratuito.
Se una funzione o un modulo è stato passato tramite argomenti o assegnazioni di variabili, il suo utilizzo costerà 1 tick invece di 0.
I cicli `for` e `while` richiedono un tick per iniziare, ma le iterazioni sono gratuite (senza contare il tempo per valutare le espressioni di condizione/sequenza).
`return`, `break` e `continue` sono tutti gratuiti.
`pass` richiede un tick, quindi può essere usato per creare ritardi precisi.
L'indicizzazione di una struttura dati richiede un tick per l'operatore di indice e, nel caso di un dizionario o set, tick aggiuntivi in base alle dimensioni della chiave.

Il numero di tick necessari per eseguire le funzioni predefinite è indicato nella pagina di ciascuna funzione.

---

[Debug](docs/scripting/debug.md)      [Simulazione](docs/unlocks/simulation.md)      [Classifica](docs/unlocks/leaderboard.md)

[get_time()](functions/get_time)      [get_tick_count()](functions/get_tick_count)      [quick_print()](functions/quick_print)
