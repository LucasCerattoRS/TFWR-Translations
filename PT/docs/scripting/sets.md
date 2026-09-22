[<- Dicionários](docs/scripting/dicts.md)

---

# Conjuntos

Conjuntos são como [dicionários](docs/scripting/dicts.md), mas sem valores. Eles são apenas um conjunto não ordenado de chaves. 

Eles são criados como dicionários, mas sem valores.
`set = {North, East, West}`

Use `set()` para criar um conjunto vazio. Note que `{}` cria um dicionário vazio.

Use `set.add(elem)` para adicionar um novo elemento ao conjunto.

Use `set.remove(elem)` para remover um elemento de um conjunto.

Use `if elem in set:` para verificar se o conjunto contém um elemento.

Use `for elem in set:` para percorrer todos os elementos do conjunto.
Para conjuntos maiores, o operador `in` é muito mais rápido do que seria em uma lista.

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
    print("North está no conjunto")
else:
    print("North não está no conjunto")
for element in my_set:
    print(element)
}}

Assim como os dicionários, os conjuntos não são ordenados, então não há garantias sobre a ordem em que os elementos são iterados.

Além disso, os elementos nos conjuntos são únicos, então adicionar um elemento que já está no conjunto não alterará o conjunto.

---

[Dicionários](docs/scripting/dicts.md)      [Listas](docs/scripting/lists.md)      [Loop For](docs/scripting/for.md)

[len()](functions/len)
