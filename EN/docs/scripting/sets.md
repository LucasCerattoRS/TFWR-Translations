[<- Dictionaries](docs/scripting/dicts.md)
---
# Sets
Sets are like [dictionaries](docs/scripting/dicts.md), but without values. They're just an unordered set of keys. 

They are created like dictionaries, but without values.
`set = {North, East, West}`

Use `set()` to create an empty set. Note that `{}` creates an empty dictionary.

Use `set.add(elem)` to add a new element to the set.

Use `set.remove(elem)` to remove an element from a set.

Use `if elem in set:` to check if the set contains an element.

Use `for elem in set:` to iterate over all elements in the set.
For larger sets, the `in` operator is much faster than it would be on a list.

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
    print("North is in set")
else:
    print("North is not in set")
for element in my_set:
    print(element)
}}

Just like dictionaries, sets are unordered, so there are no guarantees about the order in which the elements are iterated.

Also, elements in sets are unique, so adding an element that is already in the set will not change the set.

---

[Dictionaries](docs/scripting/dicts.md)      [Lists](docs/scripting/lists.md)      [For Loop](docs/scripting/for.md)

[len()](functions/len)
