[<- Liste](docs/scripting/lists.md) <right>[Costi ->](docs/unlocks/costs.md)
---
# Dizionari
I dizionari sono una struttura dati che associa chiavi a valori, proprio come un vero dizionario associa le parole alle loro definizioni. Ti permettono di cercare questi valori molto rapidamente.

Un dizionario può essere creato così:

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
right_of = {North:East, East:South, South:West, West:North}
}}

L'espressione prima dei due punti è la chiave e l'espressione dopo i due punti è il valore a cui la chiave mappa.
Il dizionario sopra mappa ogni direzione alla direzione alla sua destra.

Ecco un altro dizionario che associa la posizione del drone all'entità sottostante.
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
x, y = get_pos_x(), get_pos_y()
entity_dict = {(x,y):get_entity_type()}
}}

Accedere al valore mappato a una chiave è simile ad accedere a un elemento in una lista:
`value = dict[key]`

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
right_of = {North:East, East:South, South:West, West:North}
print(right_of[South])
}}

Puoi aggiungere una nuova coppia chiave-valore a un dizionario in questo modo:
`dict[key] = value`

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
    "world_size": {"x": 3, "y": 1},
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
plant(Entities.Bush)
move(East)
plant(Entities.Tree)
move(East)
#CODE
entity_dict = {}
for _ in range(3):
	entity_dict[(get_pos_x(), get_pos_y())] = get_entity_type()
	move(East)
print(entity_dict)
}}

Le chiavi sono uniche, quindi aggiungere una chiave che esiste già nel dizionario sovrascriverà il valore precedente.

Usa `dict.pop(key)` per rimuovere una coppia chiave-valore da `dict`.

`key in dict` restituisce `True` se `key` è una chiave nel `dict` e `False` altrimenti.
Quindi puoi usare `if key in dict:` per verificare se `dict` contiene la chiave.

Inserire un dizionario in un ciclo `for` permette di iterare su tutte le sue chiavi:
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
right_of = {North:East, East:South, South:West, West:North}
print(North in right_of)
for key in right_of:
	value = right_of[key]
	print(key, ":", value)
}}

Non ci sono garanzie sull'ordine in cui le chiavi vengono iterate.

Vedi anche [Set](docs/scripting/sets.md)

---

[Liste](docs/scripting/lists.md)      [Set](docs/scripting/sets.md)      [Tuple](docs/scripting/tuples.md)      [Costi](docs/unlocks/costs.md)

[len()](functions/len)
