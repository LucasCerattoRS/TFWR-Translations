[<- Primi Passi](docs/getting_started.md) <right>[Ciclo While ->](docs/scripting/while.md)
---
# Primo Programma
## Editor di testo
Tutta la programmazione si fa nelle finestre di codice. Ogni finestra di codice corrisponde a un file di testo contenente codice.
Puoi rinominare il file cliccando sul suo nome in cima alla finestra.

Il codice può essere modificato come in qualsiasi editor di testo finché non è in esecuzione.
Puoi eseguire il programma direttamente premendo il pulsante verde di riproduzione nella finestra del codice.
![|x50](PlayButton)

Puoi creare più file di codice usando il pulsante "+" nell'angolo in alto a destra dello schermo.
Puoi agganciare una finestra a un'altra trascinandola su di essa.

Noterai che una volta che inizi a digitare, apparirà una semplice finestra di completamento del codice.
Premi Tab per inserire il completamento selezionato.
Usa i tasti freccia per navigare tra le opzioni di completamento.

Non preoccuparti se è la tua prima volta che programmi. Il linguaggio si sblocca passo dopo passo, quindi non sarai sopraffatto da tutte le cose che puoi fare.
La sintassi è anche simile a Python, uno dei linguaggi di programmazione più usati al mondo, quindi ciò che impari qui ti sarà utile anche altrove.

Se conosci già Python, va benissimo: potrai superare rapidamente le prime fasi del gioco e arrivare alle cose più interessanti.

Attualmente, ci sono due comandi per il drone disponibili.

`harvest()`

e

`do_a_flip()`

Queste sono chiamate a funzione. Puoi pensare a una funzione come a un comando che può essere eseguito. Le parentesi `()` lo eseguono.

Prova a digitare queste istruzioni nella finestra del codice e a premere il pulsante di esecuzione.

Puoi pensare al tuo codice come a una sequenza di istruzioni. Puoi eseguire più istruzioni di seguito disponendole su più righe.
Prova a premere il pulsante di riproduzione in questa finestra di codice incorporata per vedere come viene eseguito il codice:

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
    "operation_ticks": 200,
    "seed": 1,
    "exclude_unlocks": ["watering", "fertilizer"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
#CODE
do_a_flip()
harvest()
harvest()
}}

## Sblocchi
Raccogliere erba ti darà fieno. Il fieno può essere usato per sbloccare i cicli nell'albero tecnologico. Apri l'albero tecnologico con il pulsante nell'angolo in alto a destra dello schermo.

---

[Editor Esterno](docs/external_editor.md)      [Commenti](docs/scripting/comments.md)      [Ciclo While](docs/scripting/while.md)

[harvest()](functions/harvest)      [do_a_flip()](functions/do_a_flip)
