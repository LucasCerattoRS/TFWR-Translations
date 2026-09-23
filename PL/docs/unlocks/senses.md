[<- Operatory](docs/scripting/operators.md)
---
# Zmysły
Dron teraz widzi! 

Funkcje `get_pos_x()` i `get_pos_y()` zwracają bieżące współrzędne x i y drona. W pozycji początkowej obie wynoszą `0`. Współrzędna x rośnie o `1` z każdym polem w kierunku `East`, a współrzędna y o `1` z każdym polem w kierunku `North`.
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

`num_items(item)` zwraca liczbę posiadanych sztuk danego przedmiotu.
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

`get_entity_type()` i `get_ground_type()` zwracają typ obiektu lub podłoża, które znajduje się pod dronem.
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

Słowo kluczowe `None` jest teraz również odblokowane! `None` to wartość, która reprezentuje brak wartości.
Na przykład, funkcja, która nie ma instrukcji `return`, w rzeczywistości zwróci `None`.

`get_entity_type()` zwraca `None`, jeśli pod dronem nie ma żadnego obiektu.


Jeśli chcesz dowiedzieć się, ile masz danego odblokowania, użyj funkcji `num_unlocked(unlock)`.

Na przykład, `num_unlocked(Unlocks.Speed)` zwróci liczbę posiadanych ulepszeń prędkości.

`num_unlocked(Unlocks.Senses)` zwróci `1`, jeśli zmysły są odblokowane, i `0`, jeśli nie są.

Możesz także używać `num_unlocked()` na przedmiotach lub obiektach. Zwraca `1`, jeśli dany przedmiot lub obiekt jest odblokowany, a w przeciwnym razie `0`.

Uważaj: `num_unlocked(Unlocks.Carrots)` zwraca liczbę odblokowań lub ulepszeń tego odblokowania.
`num_unlocked(Items.Carrot)` zwraca tylko `0` albo `1`. To samo dotyczy innych roślin.

---

[If](docs/scripting/if.md)      [Operatory](docs/scripting/operators.md)      [Zmienne](docs/scripting/variables.md)      [Krotki](docs/scripting/tuples.md)      [Słowniki](docs/scripting/dicts.md)      [Podziemne zmysły](docs/unlocks/underground_senses.md)

[get_pos_x()](functions/get_pos_x)      [get_pos_y()](functions/get_pos_y)      [get_entity_type()](functions/get_entity_type)      [get_ground_type()](functions/get_ground_type)      [num_items()](functions/num_items)      [num_unlocked()](functions/num_unlocked)
