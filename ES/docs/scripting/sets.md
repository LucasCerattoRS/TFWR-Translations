[<- Diccionarios](docs/scripting/dicts.md)
---
# Conjuntos
Los conjuntos son como los [diccionarios](docs/scripting/dicts.md), pero sin valores. Son solo un conjunto desordenado de claves. 

Se crean como los diccionarios, pero sin valores.
`set = {North, East, West}`

Usa `set()` para crear un conjunto vacío. Ten en cuenta que `{}` crea un diccionario vacío.

Usa `set.add(elem)` para añadir un nuevo elemento al conjunto.

Usa `set.remove(elem)` para eliminar un elemento de un conjunto.

Usa `if elem in set:` para comprobar si el conjunto contiene un elemento.

Usa `for elem in set:` para iterar sobre todos los elementos del conjunto.
Para conjuntos más grandes, el operador `in` funciona mucho más rápido que en una lista.

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
    print("North está en el conjunto")
else:
    print("North no está en el conjunto")
for element in my_set:
    print(element)
}}

Al igual que los diccionarios, los conjuntos son desordenados, por lo que no hay garantías sobre el orden en que se iteran los elementos.

Además, los elementos en los conjuntos son únicos, por lo que añadir un elemento que ya está en el conjunto no cambiará el conjunto.

---

[Diccionarios](docs/scripting/dicts.md)      [Listas](docs/scripting/lists.md)      [Bucle for](docs/scripting/for.md)

[len()](functions/len)
