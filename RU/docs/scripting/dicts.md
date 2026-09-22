[<- Списки](docs/scripting/lists.md) <right>[Стоимость ->](docs/unlocks/costs.md)
---
# Словари
Словарь — структура данных, которая позволяет сопоставлять ключи со значениями так же, как настоящий словарь сопоставляет слова с их определениями, что облегчает поиск.

Словарь можно создать так:

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
right_of = {North:East, East:South, South:West, West:North}
}}

Выражение перед двоеточием — это ключ, а выражение после двоеточия — значение, которому сопоставлен ключ.
Вышеуказанный словарь сопоставляет каждое направление с направлением справа от него.

Вот еще один, который сопоставляет позицию дрона с объектом-сущностью под ним.
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
x, y = get_pos_x(), get_pos_y()
entity_dict = {(x,y):get_entity_type()}
}}

Значение, сопоставленное с ключом, получают аналогично с элементом списка:
`value = dict[key]`

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
right_of = {North:East, East:South, South:West, West:North}
print(right_of[South])
}}

Ты можешь добавить новую пару ключ-значение в словарь так:
`dict[key] = value`

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
    "items": [],
    "world_size": {"x": 3, "y": 1},
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
plant(Entities.Bush)
move(East)
plant(Entities.Tree)
move(East)
#CODE
entity_dict = {}
for _ in range(3):
	entity_dict[(get_pos_x(), get_pos_y())] = get_entity_type()
	move(East)
print(entity_dict)
}}

Ключи уникальны, поэтому добавление ключа, который уже существует в словаре, перезапишет предыдущее значение.

Для удаления пары ключ-значение из `dict` используй `dict.pop(key)`.

`key in dict` равно `True`, если `key` является ключом в `dict`, в противном случае — `False`.
Таким образом, можно использовать `if key in dict:`, чтобы проверить, содержит ли `dict` ключ.

Использование словаря в цикле `for` позволяет перебирать все ключи:
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
right_of = {North:East, East:South, South:West, West:North}
print(North in right_of)
for key in right_of:
	value = right_of[key]
	print(key, ":", value)
}}

Нельзя с точностью сказать, в каком порядке будет выполнен перебор.

См. также [Множества](docs/scripting/sets.md)

---

[Списки](docs/scripting/lists.md)      [Множества](docs/scripting/sets.md)      [Кортежи](docs/scripting/tuples.md)      [Стоимость](docs/unlocks/costs.md)

[len()](functions/len)
