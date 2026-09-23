[<- Operatori](docs/scripting/operators.md)
---
# Sensori
Il drone ora può vedere! 

Le funzioni `get_pos_x()` e `get_pos_y()` restituiscono le coordinate x e y attuali del drone. Nella posizione iniziale sono entrambe `0`. La coordinata x aumenta di `1` per ogni casella verso `East`, mentre la coordinata y aumenta di `1` per ogni casella verso `North`.
{{codeexample 
{
    "camera_position": {"x": -1, "y": 1.8, "z": 4},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": true,
    "collapsing": true,
    "autoplay": false,
    "items": [],
    "world_size": {"x": 2, "y": 2},
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
#CODE
print("x =", get_pos_x(), "y =", get_pos_y())
if get_pos_x() == 1 and get_pos_y() == 0:
    do_a_flip()
}}

`num_items(item)` restituisce quanti esemplari di un oggetto possiedi.
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
    "items": [{"item": "hay", "n": 10}],
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
print(num_items(Items.Hay))
}}

`get_entity_type()` e `get_ground_type()` restituiscono il tipo di entità o terreno che si trova sotto il drone.
{{codeexample 
{
    "camera_position": {"x": 0, "y": 1.5, "z": 6},
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
plant(Entities.Bush)
#CODE
print(get_entity_type())
if get_entity_type() == Entities.Bush:
	do_a_flip()

print(get_ground_type())
if get_ground_type() != Grounds.Soil:
	do_a_flip()
}}

La parola chiave `None` è ora sbloccata! `None` è un valore che rappresenta l'assenza di un valore.
Ad esempio, una funzione che non ha un'istruzione `return` restituirà effettivamente `None`.

`get_entity_type()` restituisce `None` se non c'è alcuna entità sotto il drone.


Se vuoi scoprire quanti esemplari di un particolare sblocco possiedi, usa la funzione `num_unlocked(unlock)`.

Ad esempio, `num_unlocked(Unlocks.Speed)` restituirà il numero di potenziamenti di velocità che hai.

`num_unlocked(Unlocks.Senses)` restituirà `1` se i sensori sono sbloccati e `0` se non lo sono.

Puoi usare `num_unlocked()` anche sugli oggetti o sulle entità. Restituisce `1` se l'oggetto o l'entità è sbloccato e `0` altrimenti.

Attenzione: `num_unlocked(Unlocks.Carrots)` restituisce il numero di volte in cui lo sblocco è stato sbloccato o potenziato.
`num_unlocked(Items.Carrot)` restituisce solo `0` o `1`. Lo stesso vale per le altre piante.

---

[If](docs/scripting/if.md)      [Operatori](docs/scripting/operators.md)      [Variabili](docs/scripting/variables.md)      [Tuple](docs/scripting/tuples.md)      [Dizionari](docs/scripting/dicts.md)      [Sensi Sotterranei](docs/unlocks/underground_senses.md)

[get_pos_x()](functions/get_pos_x)      [get_pos_y()](functions/get_pos_y)      [get_entity_type()](functions/get_entity_type)      [get_ground_type()](functions/get_ground_type)      [num_items()](functions/num_items)      [num_unlocked()](functions/num_unlocked)
