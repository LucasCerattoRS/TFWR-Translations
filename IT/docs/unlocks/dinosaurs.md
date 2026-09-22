[<- Cactus](docs/unlocks/cactus.md)
---
# Dinosauri
I dinosauri sono creature antiche e maestose che possono essere allevate per ottenere ossa antiche.

Purtroppo i dinosauri si sono estinti molto tempo fa, quindi il massimo che possiamo fare è travestirci da uno di loro.
Per questo hai ricevuto il nuovo cappello da dinosauro.

Il cappello può essere equipaggiato con
`change_hat(Hats.Dinosaur_Hat)`

Purtroppo non ha proprio l'aspetto che aveva nella pubblicità...

Se equipaggi il cappello da dinosauro e hai abbastanza cactus, una [mela](objects/apple) verrà automaticamente acquistata e posizionata sotto il drone.
Quando il drone si trova su una mela e si muove di nuovo, mangerà la mela e la sua coda si allungherà di uno. Se te lo puoi permettere, una nuova mela verrà acquistata e posizionata in un luogo casuale.
La mela non può comparire se c'è qualcos'altro piantato dove vorrebbe essere.

La coda del dinosauro viene trascinata dietro il drone e riempie le caselle su cui è passato. Se il drone prova a muoversi sulla propria coda, `move()` fallisce e restituisce `False`.
L'ultimo segmento della coda si sposta durante il movimento, quindi puoi muoverti sopra di esso. Se però il serpente riempie l'intera fattoria, non potrai più muoverti. Puoi quindi verificare se il serpente ha raggiunto la lunghezza massima controllando se riesci ancora a muoverti.
Mentre indossi il cappello da dinosauro, il drone non può superare il bordo della fattoria per passare dall'altro lato.

Usando `measure()` su una mela si ottiene la posizione della mela successiva come una tupla.

`next_x, next_y = measure()`

{{codeexample 
{
    "camera_position": {"x": -1, "y": 2.4, "z": 5},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": true,
    "collapsing": true,
    "autoplay": false,
    "items": [{"item": "cactus", "n": 10000}],
    "world_size": {"x": 4, "y": 4},
    "execution_speed": 2,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 1,
    "seed": 5,
    "exclude_unlocks": ["watering"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
#CODE
change_hat(Hats.Dinosaur_Hat)
while True:
    next_x, next_y = measure()
    while get_pos_x() != next_x:
        move(East)
    while get_pos_y() != next_y:
        move(North)
}}

Quando il cappello viene rimosso equipaggiandone un altro, la coda verrà raccolta.
Riceverai una quantità di ossa pari al quadrato della lunghezza della coda. Per una coda lunga `n`, riceverai `n**2` `Items.Bone`.
Per esempio:
lunghezza 1 => 1 osso
lunghezza 2 => 4 ossa
lunghezza 3 => 9 ossa
lunghezza 4 => 16 ossa
lunghezza 16 => 256 ossa
lunghezza 100 => 10000 ossa

Il Cappello da Dinosauro è molto pesante, quindi se lo equipaggi, `move()` impiegherà 400 tick invece di 200. Tuttavia, ogni volta che raccogli una mela, il numero di tick usati da `move()` si riduce del 3% (arrotondato per difetto), perché una coda più lunga può aiutarti a muoverti.

Il seguente ciclo stampa il numero di tick usati da `move()` dopo un qualsiasi numero di mele:

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
ticks = 400
for i in range(100):
    quick_print("tick dopo ", i, " mele: ", ticks)
    ticks -= ticks * 0.03 // 1
}}

Hai solo un cappello da dinosauro, quindi solo un drone può indossarlo.

<spoiler=mostra suggerimento 1>
Se continui a seguire lo stesso percorso che copre tutto il campo, puoi ottenere facilmente ogni volta un serpente che occupa l'intero campo. Non è molto efficiente, ma funziona.
Attraversare interamente una fattoria molto grande può richiedere molto tempo e forse non ti servono davvero così tante ossa. Puoi usare `set_world_size()` per impostare una dimensione più comoda.</spoiler>

---

[Statistiche](docs/stats.md)      [Tuple](docs/scripting/tuples.md)      [Liste](docs/scripting/lists.md)

[change_hat()](functions/change_hat)      [move()](functions/move)      [measure()](functions/measure)
