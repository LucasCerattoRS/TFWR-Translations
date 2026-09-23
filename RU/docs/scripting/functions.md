[<- Переменные](docs/scripting/variables.md) <right>[Импорт ->](docs/scripting/import.md)
---
# Функции
Используй ключевое слово `def` для определения новой функции:
`def f(arg1, arg2 = False):
	#код функции`

Для вызова функции можно использовать оператор вызова `()`:
`f(42)`

Чтобы узнать о локальных и глобальных переменных в функциях, см. также [Области видимости](docs/scripting/scopes.md).

## Введение
Тебе уже известно про встроенные функции, такие как `harvest()`.
Ты также можешь определять собственные функции, что позволяет структурировать код модульным образом. По сути, ты можешь дать имя блоку кода, чтобы вызывать его откуда угодно.

## Определения функций
Например, можно определить функцию, которая перемещает дрон несколько раз.

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
def move_n_dir(n, dir):
	for i in range(n):
		move(dir)
}}

Ключевое слово `def` указывает, что это определение функции.
`move_n_dir` — имя, к которому привязывается функция. Это может быть любое допустимое имя переменной. Оно будет использоваться для вызова функции.
`n` и `dir` — параметры. Это переменные, которые содержат значения, передаваемые в функцию (они также называются аргументами). В определение функции можно добавить столько параметров, сколько хочется.
После `:` идет блок кода, который будет выполняться при вызове функции.

Следующий код перемещает дрон на `2` клетки в направлении `North`, а затем на `2` клетки в направлении `East`.

{{codeexample 
{
    "camera_position": {"x": -1, "y": 1.8, "z": 5},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": true,
    "collapsing": true,
    "autoplay": false,
    "items": [],
    "world_size": {"x": 3, "y": 3},
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
#CODE
def move_n_dir(n, dir):
	for i in range(n):
		move(dir)

move_n_dir(2, North)
move_n_dir(2, East)
}}

Когда ты видишь `def function():`, то представляй себе это как присваивание переменной, например:
`function = create_new_function_object()`
Как и при любом присваивании, ты не можешь использовать переменную до того, как ей присвоили значение!
Инструкция `def` должна выполниться до любого вызова функции.
Такой код вызовет ошибку:

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
func()
def func():
	pass
}}

## Возвращаемые значения
Используй ключевое слово `return`, чтобы функция возвращала значение.
Например, следующая функция определяет операцию исключающего ИЛИ. Исключающее ИЛИ возвращает `True`, если одно значение `True`, а другое `False`:

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
#CODE
def xor(a, b):
	return a != b

if xor(True, False):
	do_a_flip()
}}

[Кортежи](docs/scripting/tuples.md) позволяют возвращать несколько значений.

## Аргументы по умолчанию
Ты также можешь присвоить значения по умолчанию, которые будут использоваться, если соответствующие аргументы не переданы.

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
#CODE
def f(a = False):
	if a:
		do_a_flip()

f()

f(True)
}}

Аргумент со значением по умолчанию не может следовать за аргументом, у которого нет значения по умолчанию.

## Продвинутое использование функций
Функции — такие же значения, как и любые другие. Инструкция `def`, по сути, действует как инструкция присваивания: она присваивает функцию тому имени, которое ты дашь.
Это позволяет делать следующее:

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
#CODE
def f():
	def d():
		do_a_flip()
	return d

f()()
}}

Здесь `f()` вызывает функцию `f`, которая определяет и возвращает новую функцию `d`. Второй вызов `()` выполняет возвращенную функцию и производит сальто.
(Обычно записывать код подобным образом не стоит, потому что трудно понять, что происходит.)

Функции, принимающие другие функции в качестве аргументов, дают большой простор для фантазии:

{{codeexample 
{
    "camera_position": {"x": -2, "y": 1.5, "z": 4},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": true,
    "collapsing": true,
    "autoplay": false,
    "items": [{"item": "fertilizer", "n": 4}],
    "world_size": {"x": 5, "y": 1},
    "execution_speed": 1,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 100,
    "seed": 1,
    "exclude_unlocks": ["watering"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
#CODE
def f(g, arg):
	for _ in range(4):
		g(arg)

f(move, East)
plant(Entities.Tree)
f(use_item, Items.Fertilizer)
}}

---

[Переменные](docs/scripting/variables.md)      [Области видимости имен](docs/scripting/scopes.md)      [Кортежи](docs/scripting/tuples.md)      [Импорт](docs/scripting/import.md)
