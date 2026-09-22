[<- Словари](docs/scripting/dicts.md)
---
# Множества
Множества похожи на [словари](docs/scripting/dicts.md) без значений. Это просто неупорядоченный набор ключей.

Они создаются как словари, но без значений.
`set = {North, East, West}`

Используй `set()` для создания пустого множества. Обрати внимание, что `{}` создает пустой словарь.

Используй `set.add(elem)` для добавления нового элемента в множество.

Используй `set.remove(elem)` для удаления элемента из множества.

Используй `if elem in set:`, чтобы проверить, содержит ли множество элемент.

Используй `for elem in set:`, чтобы перебрать все элементы в множестве.
С большим множеством оператор `in` справляется гораздо быстрее, чем со списком.

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
    print("North входит в множество")
else:
    print("North не входит в множество")
for element in my_set:
    print(element)
}}

Как и словари, множества не упорядочены, поэтому нет гарантий относительно порядка, в котором будут перебираться элементы.

Кроме того, элементы в множествах уникальны, поэтому добавление элемента, который уже есть в множестве, не изменит последнее.

---

[Словари](docs/scripting/dicts.md)      [Списки](docs/scripting/lists.md)      [Цикл for](docs/scripting/for.md)

[len()](functions/len)
