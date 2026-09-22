[<- Variabili](docs/scripting/variables.md) <right>[Import ->](docs/scripting/import.md)
---
# Funzioni
Usa la parola chiave `def` per definire una nuova funzione:
`def f(arg1, arg2 = False):
	#codice della funzione`

Puoi usare l'operatore di chiamata `()` per chiamare la funzione:
`f(42)`

Vedi anche [Scope](docs/scripting/scopes.md) per imparare le variabili locali e globali nelle funzioni.

## Introduzione
Hai già visto funzioni integrate come `harvest()`.
Puoi anche definire le tue funzioni, organizzando così il codice in modo modulare. Una funzione dà un nome a un blocco di codice, permettendoti di richiamarlo ovunque ti serva.

## Definizioni di Funzioni
Ad esempio, potresti definire una funzione che muove il drone più volte.

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
def move_n_dir(n, dir):
	for i in range(n):
		move(dir)
}}

La parola chiave `def` segnala che questa è una definizione di funzione.
`move_n_dir` è il nome a cui la funzione viene associata. Può essere qualsiasi nome di variabile valido e sarà usato per chiamare la funzione.
`n` e `dir` sono parametri. Sono variabili che contengono i valori passati alla funzione; questi valori sono anche detti argomenti. Puoi aggiungere alla definizione di una funzione tutti i parametri che vuoi.
Dopo i `:` viene il blocco di codice che verrà eseguito quando la funzione viene chiamata.

Il codice seguente sposta il drone di `2` caselle verso `North` e di `2` caselle verso `East`.

{{codeexample 
{
    "camera_position": {"x": -1, "y": 1.8, "z": 5},
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
    "exclude_unlocks": ["watering", "fertilizer"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
#CODE
def move_n_dir(n, dir):
	for i in range(n):
		move(dir)

move_n_dir(2, North)
move_n_dir(2, East)
}}

Quando vedi `def function():`, dovresti pensarci come a un'assegnazione di variabile del tipo:
`function = create_new_function_object()`
Come per tutte le assegnazioni, non puoi usare la variabile prima che le sia stato assegnato un valore!
L'istruzione `def` deve essere eseguita prima di qualsiasi chiamata alla funzione.
Questo codice genererà un errore:

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
func()
def func():
	pass
}}

## Valori di Ritorno
Usa la parola chiave `return` per far sì che una funzione restituisca un valore.
Per esempio, la funzione seguente definisce l'operazione OR esclusivo. L'OR esclusivo restituisce `True` se un valore è `True` e l'altro è `False`:

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
#CODE
def xor(a, b):
	return a != b

if xor(True, False):
	do_a_flip()
}}

Le [Tuple](docs/scripting/tuples.md) permettono di restituire più valori.

## Argomenti Predefiniti
Puoi anche assegnare valori predefiniti, che verranno usati quando gli argomenti corrispondenti vengono omessi.

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
#CODE
def f(a = False):
	if a:
		do_a_flip()

f()

f(True)
}}

Un argomento con un valore predefinito non può essere seguito da un argomento che non ha un valore predefinito.

## Uso Avanzato delle Funzioni
Le funzioni sono valori come qualsiasi altro valore, e l'istruzione `def` agisce semplicemente come un'istruzione di assegnazione, assegnando la funzione al nome che le dai.
Questo permette di fare cose come questa:

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
#CODE
def f():
	def d():
		do_a_flip()
	return d

f()()
}}

Qui `f()` chiama la funzione `f`, che definisce e restituisce una nuova funzione, `d`. Il secondo `()` esegue quindi la funzione restituita e fa un flip.
(Fare questo genere di cose di solito non è una buona idea, perché è difficile capire cosa stia succedendo.)

Le funzioni che prendono altre funzioni come argomenti ti permettono di essere molto creativo:

{{codeexample 
{
    "camera_position": {"x": -2, "y": 1.5, "z": 4},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": true,
    "collapsing": true,
    "autoplay": false,
    "items": [{"item": "fertilizer", "n": 4}],
    "world_size": {"x": 5, "y": 1},
    "execution_speed": 1,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 100,
    "seed": 1,
    "exclude_unlocks": ["watering"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
#CODE
def f(g, arg):
	for _ in range(4):
		g(arg)

f(move, East)
plant(Entities.Tree)
f(use_item, Items.Fertilizer)
}}

---

[Variabili](docs/scripting/variables.md)      [Scope dei Nomi](docs/scripting/scopes.md)      [Tuple](docs/scripting/tuples.md)      [Import](docs/scripting/import.md)
