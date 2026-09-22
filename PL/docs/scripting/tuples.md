[<- Funkcje](docs/scripting/functions.md)
---
# Krotki
Krotki to świetny sposób na połączenie wielu wartości w jedną.
Aby utworzyć krotkę, po prostu oddziel wartości przecinkami:

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
tuple = 1, 2
print(tuple)
}}

Można je również rozpakować do kilku zmiennych. W poniższym kodzie krotka `(1, 2)` jest rozpakowywana do dwóch zmiennych: `a` i `b`.

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
a, b = 1, 2
print(a)
a, b = b, a
print(a)
}}

Krotki można indeksować jak listy, ale są one niemutowalne i nie można ich zmieniać po utworzeniu.

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
tuple = 1, 2
print(tuple[1])

tuple[0] = 3
}}

<unlock=dicts>
W przeciwieństwie do list, krotek można używać jako kluczy w słownikach.

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
d = {(1,2):(4,5)}

print(d[(1,2)])
}}</unlock>

Mogą być również przydatne do zwracania wielu wartości w funkcji.

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
def f():
    return 1, 2

a, b = f()
}}

---

[Listy](docs/scripting/lists.md)      [Słowniki](docs/scripting/dicts.md)      [Funkcje](docs/scripting/functions.md)
