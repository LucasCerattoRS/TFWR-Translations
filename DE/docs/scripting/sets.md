[<- Dictionaries](docs/scripting/dicts.md)
---
# Sets
Sets sind wie [Dictionaries](docs/scripting/dicts.md), aber ohne Werte. Sie sind nur eine ungeordnete Menge von Schlüsseln.

Sie werden wie Dictionaries erstellt, aber ohne Werte.
`set = {North, East, West}`

Verwende `set()`, um ein leeres Set zu erstellen. Beachte, dass `{}` ein leeres Dictionary erstellt.

Verwende `set.add(elem)`, um ein neues Element zum Set hinzuzufügen.

Verwende `set.remove(elem)`, um ein Element aus einem Set zu entfernen.

Verwende `if elem in set:`, um zu prüfen, ob das Set ein Element enthält.

Verwende `for elem in set:`, um über alle Elemente der Menge zu iterieren.
Bei größeren Mengen ist der Operator `in` wesentlich schneller als bei einer Liste.

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
    print("North ist im Set")
else:
    print("North ist nicht im Set")
for element in my_set:
    print(element)
}}

Genau wie Dictionaries sind Sets ungeordnet, daher gibt es keine Garantien bezüglich der Reihenfolge, in der die Elemente durchlaufen werden.

Außerdem ist jedes Element in einem Set einzigartig. Wenn du ein Element hinzufügst, das bereits im Set enthalten ist, ändert sich das Set nicht.

---

[Dictionaries](docs/scripting/dicts.md)      [Listen](docs/scripting/lists.md)      [For-Schleife](docs/scripting/for.md)

[len()](functions/len)
