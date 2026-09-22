[<- Расширение 2](docs/unlocks/expand_2.md)
---
# Цикл `for`
Цикл `for` работает в игре, как и в Python. (В некоторых языках называется он foreach. Не путать с циклом for в языке C, это другое).

`for i in sequence:
	#сделать что-то с i`

Подобно циклу `while`, `for` также многократно вызывает блок кода. Но вместо того, чтобы циклически выполнять его на основе условия, он выполняет тело цикла один раз для каждого элемента в последовательности.

## Синтаксис
Цикл for выглядит так:

`for variable_name in sequence:
	#блок кода`

Для `variable_name` можно задать любое имя. Эта переменная хранит текущий элемент последовательности. `sequence` должно быть перебираемым значением, например диапазоном чисел. Блок кода выполняется один раз для каждого элемента, при этом переменной цикла присваивается этот элемент.

## Последовательности
[Диапазоны](functions/range)      <unlock=lists>[Списки](docs/scripting/lists.md)      </unlock><unlock=functions>[Кортежи](docs/scripting/tuples.md)      </unlock><unlock=dicts>[Словари](docs/scripting/dicts.md)      </unlock><unlock=sets>[Множества](docs/scripting/sets.md)</unlock>

## Пример
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
do_a_flip()
#CODE
for i in range(5):
    harvest()
}}

Этот цикл выполняет тело определенное количество раз. По сути, это равносильно следующему:

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
do_a_flip()
#CODE
i = 0
harvest()
i = 1
harvest()
i = 2
harvest()
i = 3
harvest()
i = 4
harvest()
}}


---

[Цикл while](docs/scripting/while.md)      [Break](docs/scripting/break.md)      [Continue](docs/scripting/continue.md)

[range()](functions/range)
