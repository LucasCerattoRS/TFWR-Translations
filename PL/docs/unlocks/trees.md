[<- Marchewki](docs/unlocks/carrots.md) <right>[Dynie ->](docs/unlocks/pumpkins.md)
---
# Drzewa
[Drzewa](objects/tree) to lepszy sposób na zdobycie drewna niż krzaki. Dają po 5 drewna. Podobnie jak krzaki, można je sadzić na trawie lub glebie.

Drzewa lubią mieć trochę przestrzeni, a sadzenie ich tuż obok siebie spowolni ich wzrost. Czas wzrostu jest podwajany za każde drzewo znajdujące się na polu bezpośrednio na północ, wschód, zachód lub południe od niego. Więc jeśli posadzisz drzewa na każdym polu, będą rosły `2*2*2*2 = 16` razy dłużej.
{{codeexample 
{
    "camera_position": {"x": -1, "y": 1.8, "z": 5},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": false,
    "show_inventory": true,
    "show_output": false,
    "collapsing": false,
    "autoplay": true,
    "items": [],
    "world_size": {"x": 3, "y": 3},
    "execution_speed": 10,
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
for i in range(get_world_size()):
	for j in range(get_world_size()):
		plant(Entities.Tree)
		move(North)
	move(East)
}}

<spoiler=pokaż> 
Operator `%` może być tutaj przydatny. Operator `%` zwraca resztę z dzielenia. Liczby parzyste podzielone przez `2` dają resztę `0`, a nieparzyste podzielone przez `2` — resztę `1`.
Możesz więc sprawdzić, czy liczba jest parzysta, w ten sposób:

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
def is_even(n):
	return n % 2 == 0

print("is_even(0): ", is_even(0))
print("is_even(1): ", is_even(1))
print("is_even(2): ", is_even(2))
print("is_even(5): ", is_even(5))
print("is_even(-1): ", is_even(-1))
print("is_even(x): ", is_even(get_pos_x()))
}}
</spoiler>

---

[Statystyki](docs/stats.md)      [Operatory](docs/scripting/operators.md)      [If](docs/scripting/if.md)      [Pętla For](docs/scripting/for.md)      [Uprawa współrzędna](docs/unlocks/polyculture.md)

[harvest()](functions/harvest)      [plant()](functions/plant)      [move()](functions/move)
