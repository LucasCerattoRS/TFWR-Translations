[<- Słowniki](docs/scripting/dicts.md)
---
# Zbiory
Zbiory są jak [słowniki](docs/scripting/dicts.md), ale bez wartości. To po prostu nieuporządkowany zbiór kluczy. 

Tworzy się je jak słowniki, ale bez wartości.
`zbiór = {North, East, West}`

Użyj `set()`, aby utworzyć pusty zbiór. Zauważ, że `{}` tworzy pusty słownik.

Użyj `set.add(elem)`, aby dodać nowy element do zbioru.

Użyj `set.remove(elem)`, aby usunąć element ze zbioru.

Użyj `if elem in set:`, aby sprawdzić, czy zbiór zawiera dany element.

Użyj `for elem in set:`, aby iterować po wszystkich elementach zbioru.
W przypadku większych zbiorów operator `in` działa znacznie szybciej niż na liście.

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
my_set = set()
print(my_set)
my_set.add(1)
my_set.add(North)
print(my_set)
my_set.remove(North)
print(my_set)
if North in my_set:
    print("North znajduje się w zbiorze")
else:
    print("North nie znajduje się w zbiorze")
for element in my_set:
    print(element)
}}

Podobnie jak słowniki, zbiory są nieuporządkowane, więc nie ma gwarancji co do kolejności, w jakiej elementy są iterowane.

Ponadto elementy w zbiorach są unikalne, więc dodanie elementu, który już znajduje się w zbiorze, nie zmieni zbioru.
---

[Słowniki](docs/scripting/dicts.md)      [Listy](docs/scripting/lists.md)      [Pętla For](docs/scripting/for.md)

[len()](functions/len)
