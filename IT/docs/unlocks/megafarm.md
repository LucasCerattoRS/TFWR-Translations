[<- Labirinti](docs/unlocks/mazes.md)
---
# Mega Fattoria
Questo sblocco incredibilmente potente ti dà accesso a più droni. 
{{codeexample 
{
    "camera_position": {"x": -3, "y": 2.1, "z": 7},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": false,
    "show_inventory": true,
    "show_output": true,
    "collapsing": false,
    "autoplay": true,
    "items": [],
    "world_size": {"x": 7, "y": 7},
    "execution_speed": 21,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 1,
    "seed": 1,
    "exclude_unlocks": ["fertilizer", "watering"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
move(North)
move(North)
move(North)
move(East)
move(East)
move(East)
change_hat(Hats.Wizard_Hat)
#CODE
def harvest_spiral(radius):
    for i in range(1, radius, 2):
        harvest()
        move(West)
        for j in range(i):
            harvest()
            move(South)
        for j in range(i+1):
            harvest()
            move(East)
        for j in range(i+1):
            harvest()
            move(North)
        for j in range(i+1):
            harvest()
            move(West)

while True:
    spawn_drone(harvest_spiral, 7)
    do_a_flip()
}}

Come prima, inizi ancora con un solo drone. I droni aggiuntivi devono prima essere creati e scompariranno dopo la terminazione del programma.
Ogni drone esegue il proprio programma separato. Nuovi droni possono essere creati usando la funzione `spawn_drone(function)`.

{{codeexample 
{
    "camera_position": {"x": -0.5, "y": 1.5, "z": 4},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": false,
    "collapsing": true,
    "autoplay": false,
    "items": [],
    "world_size": {"x": 2, "y": 1},
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
def drone_function():
    move(East)
    do_a_flip()

spawn_drone(drone_function)
do_a_flip()
}}

Questo crea un nuovo drone nella stessa posizione di quello che ha eseguito il comando `spawn_drone(function)`. Il nuovo drone inizia quindi a eseguire la funzione specificata. Al termine scompare automaticamente, a meno che non sia l'ultimo drone rimasto.

I droni non si scontrano tra loro. 

Usa `max_drones()` per ottenere il numero massimo di droni che possono esistere contemporaneamente.
Usa `num_drones()` per ottenere il numero di droni che sono già sulla fattoria.


## Esempio
{{codeexample 
{
    "camera_position": {"x": -1.5, "y": 2.4, "z": 5},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": true,
    "collapsing": true,
    "autoplay": false,
    "items": [],
    "world_size": {"x": 4, "y": 4},
    "execution_speed": 1,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 100,
    "seed": 1,
    "exclude_unlocks": ["fertilizer", "watering"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
#CODE
def harvest_column():
    for _ in range(get_world_size()):
        harvest()
        move(North)

while True:
    if spawn_drone(harvest_column):
        move(East)
}}

Questo farà sì che il tuo primo drone si muova orizzontalmente e crei altri droni. I droni creati si muoveranno quindi verticalmente e raccoglieranno tutto ciò che trovano sul loro cammino.

Se tutti i droni disponibili sono già stati creati, `spawn_drone()` non farà nulla e restituirà `None`.

Ecco un altro esempio che passa una direzione diversa a ogni drone.
{{codeexample 
{
    "camera_position": {"x": -1, "y": 2, "z": 5},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": true,
    "collapsing": true,
    "autoplay": false,
    "items": [],
    "world_size": {"x": 3, "y": 3},
    "execution_speed": 1,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 100,
    "seed": 1,
    "exclude_unlocks": ["fertilizer", "watering"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
move(North)
move(East)
#CODE
for dir in [North, East, South, West]:
    def task():
        move(dir)
        do_a_flip()
    spawn_drone(task)
}}

## Tutti i Droni Sono Uguali
Non esiste un drone "principale" speciale. Tutti i droni possono crearne altri e tutti contano ai fini del limite. Ogni drone scompare quando termina. Se il primo drone finisce in anticipo, l'esecuzione di un altro drone viene mostrata tramite l'evidenziazione del codice. Tutti i droni possono attivare i breakpoint; quando succede, l'evidenziazione passa a quel drone.

<spoiler=mostra suggerimento> 
Guarda questa utilissima funzione parallela `for_all`, che accetta una funzione qualsiasi e la esegue su ogni casella della fattoria usando tutti i droni disponibili.

{{codeexample 
{
    "camera_position": {"x": -1.5, "y": 2.4, "z": 5},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": true,
    "collapsing": true,
    "autoplay": false,
    "items": [],
    "world_size": {"x": 4, "y": 4},
    "execution_speed": 1,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 100,
    "seed": 1,
    "exclude_unlocks": ["fertilizer", "watering"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
#CODE
def for_all(f):
	def row():
		for _ in range(get_world_size()-1):
			f()
			move(East)
		f()
	for _ in range(get_world_size()):
		if not spawn_drone(row):
			row()
		move(North)

for_all(harvest)
}}

Un modello particolarmente utile è quello di creare un drone se ne è disponibile uno e altrimenti farlo da soli.

`if not spawn_drone(task):
	task()`
</spoiler>

## Attendere un Altro Drone
Usa la funzione `wait_for(drone)` per attendere che un altro drone finisca. Ricevi l'handle del `drone` quando crei il drone.
`wait_for(drone)` restituisce il valore di ritorno della funzione che l'altro drone stava eseguendo.

{{codeexample 
{
    "camera_position": {"x": -0.5, "y": 1.5, "z": 4},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": false,
    "collapsing": true,
    "autoplay": false,
    "items": [],
    "world_size": {"x": 2, "y": 1},
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
move(East)
plant(Entities.Tree)
move(West)
#CODE
def get_entity_type_in_direction(dir):
    move(dir)
    return get_entity_type()

drone = spawn_drone(get_entity_type_in_direction, East)
print(wait_for(drone))
}}

Nota che creare droni richiede tempo, quindi non è una buona idea creare un nuovo drone per ogni piccola cosa.

Puoi usare `has_finished(drone)` per controllare se il drone ha finito senza dover aspettare.

## Nessuna Memoria Condivisa
Ogni drone ha la sua memoria e non può leggere o scrivere direttamente le variabili globali di un altro drone.

{{codeexample 
{
    "camera_position": {"x": -0.5, "y": 1.5, "z": 4},
    "show_image": false,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": false,
    "show_output": true,
    "collapsing": true,
    "autoplay": false,
    "items": [],
    "world_size": {"x": 2, "y": 1},
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
x = 0

def increment():
    global x
    x += 1

wait_for(spawn_drone(increment))
print(x)
}}

Questo stampa `0` perché il nuovo drone ha incrementato la propria copia della variabile globale `x`, senza modificare la `x` del primo drone.

## Passare Argomenti

`spawn_drone()` accetta argomenti facoltativi aggiuntivi che verranno passati alla funzione chiamata:

Ricorda che vale comunque la regola della memoria non condivisa. La funzione chiamata opera quindi su una copia degli argomenti:

{{codeexample 
{
    "camera_position": {"x": -0.5, "y": 1.5, "z": 4},
    "show_image": false,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": false,
    "show_output": true,
    "collapsing": true,
    "autoplay": false,
    "items": [],
    "world_size": {"x": 2, "y": 1},
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
def modify(list):
	list.append('verde')
	print(list)

l = ['rosso']
wait_for(spawn_drone(modify, l))
print(l)
}}

## Condizione di Gara
Più droni possono interagire con la stessa casella della fattoria contemporaneamente. Se due droni interagiscono con la stessa casella durante lo stesso tick, entrambe le interazioni avverranno, ma i risultati potrebbero differire in base all'ordine delle interazioni.

Ad esempio, immagina che i droni `0` e `1` si trovino entrambi sullo stesso albero quasi completamente cresciuto.
Il drone `0` chiama
`use_item(Items.Fertilizer)`
Il drone `1` chiama
`harvest()`

Se queste azioni avvengono contemporaneamente, l'albero verrà prima fertilizzato e poi raccolto. In tal caso, ne riceverai del legno. Tuttavia, se il Drone `1` è leggermente più veloce, l'albero verrà raccolto prima di essere fertilizzato e non riceverai il legno.
Questa è chiamata "race condition". È un problema comune nella programmazione parallela, dove il risultato dipende dall'ordine in cui vengono eseguite le operazioni.

Ecco un'altra situazione problematica che può verificarsi quando più droni eseguono lo stesso codice contemporaneamente nella stessa posizione.
`if get_water() < 0.5:
    use_item(Items.Water)`

Se più droni eseguono questo contemporaneamente, eseguiranno tutti la prima riga, che li inserisce nel blocco `if`. Poi, useranno tutti l'acqua, sprecandone molta.
Quando un drone raggiunge la seconda riga, `get_water()` potrebbe non essere più minore di `0.5`, perché nel frattempo un altro drone ha annaffiato la casella.

---

[Funzioni](docs/scripting/functions.md)      [Scope dei Nomi](docs/scripting/scopes.md)      [Simulazione](docs/unlocks/simulation.md)

[spawn_drone()](functions/spawn_drone)      [num_drones()](functions/num_drones)      [max_drones()](functions/max_drones)      [wait_for()](functions/wait_for)      [has_finished()](functions/has_finished)
