[<- Лабиринты](docs/unlocks/mazes.md)
---
# Мегаферма
Эта невероятно мощная технология дает доступ к нескольким дронам. 
{{codeexample 
{
    "camera_position": {"x": -3, "y": 2.1, "z": 7},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": false,
    "show_inventory": true,
    "show_output": true,
    "collapsing": false,
    "autoplay": true,
    "items": [],
    "world_size": {"x": 7, "y": 7},
    "execution_speed": 21,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 1,
    "seed": 1,
    "exclude_unlocks": ["fertilizer", "watering"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
move(North)
move(North)
move(North)
move(East)
move(East)
move(East)
change_hat(Hats.Wizard_Hat)
#CODE
def harvest_spiral(radius):
    for i in range(1, radius, 2):
        harvest()
        move(West)
        for j in range(i):
            harvest()
            move(South)
        for j in range(i+1):
            harvest()
            move(East)
        for j in range(i+1):
            harvest()
            move(North)
        for j in range(i+1):
            harvest()
            move(West)

while True:
    spawn_drone(harvest_spiral, 7)
    do_a_flip()
}}

Как и раньше, ты начинаешь с одним дроном. Дополнительные дроны нужно создать, и они пропадут после завершения программы.
Каждый дрон выполняет собственную отдельную программу. Новые дроны можно создать с помощью функции `spawn_drone(function)`.

{{codeexample 
{
    "camera_position": {"x": -0.5, "y": 1.5, "z": 4},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": false,
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
def drone_function():
    move(East)
    do_a_flip()

spawn_drone(drone_function)
do_a_flip()
}}

Новый дрон создается на той же позиции, где выполнена команда `spawn_drone(function)`. Он начинает выполнять указанную функцию и по завершении автоматически пропадает, если только не остается последним существующим дроном.

Дроны не сталкиваются друг с другом. 

Используй `max_drones()`, чтобы получить максимально возможное количество дронов.
Используй `num_drones()`, чтобы получить количество дронов, которые уже находятся на ферме.


## Пример:
{{codeexample 
{
    "camera_position": {"x": -1.5, "y": 2.4, "z": 5},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": true,
    "collapsing": true,
    "autoplay": false,
    "items": [],
    "world_size": {"x": 4, "y": 4},
    "execution_speed": 1,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 100,
    "seed": 1,
    "exclude_unlocks": ["fertilizer", "watering"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
#CODE
def harvest_column():
    for _ in range(get_world_size()):
        harvest()
        move(North)

while True:
    if spawn_drone(harvest_column):
        move(East)
}}

Первый дрон будет перемещаться горизонтально и создавать новые дроны. Созданные дроны будут перемещаться вертикально и собирать все на пути.

Если все доступные дроны уже созданы, `spawn_drone()` ничего не сделает и вернет `None`.

Вот еще один пример, где каждому дрону передается свое направление.
{{codeexample 
{
    "camera_position": {"x": -1, "y": 2, "z": 5},
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
    "exclude_unlocks": ["fertilizer", "watering"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
move(North)
move(East)
#CODE
for dir in [North, East, South, West]:
    def task():
        move(dir)
        do_a_flip()
    spawn_drone(task)
}}

## Все дроны равны
Здесь нет особого «главного» дрона. Все дроны могут создавать других дронов, и все они учитываются в общем лимите. Все дроны исчезают по завершении работы. Если первый дрон заканчивает свою программу раньше, другой дрон станет тем, чье выполнение будет отображаться с подсветкой кода. Все дроны могут активировать точки останова, и когда дрон активирует точку останова, подсветка кода переключается на этого дрона.

<spoiler=показать подсказку> 
Обрати внимание на очень полезную параллельную функцию `for_all`: она принимает любую функцию и запускает ее на каждой клетке фермы, используя для этого всех доступных дронов.

{{codeexample 
{
    "camera_position": {"x": -1.5, "y": 2.4, "z": 5},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": true,
    "collapsing": true,
    "autoplay": false,
    "items": [],
    "world_size": {"x": 4, "y": 4},
    "execution_speed": 1,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 100,
    "seed": 1,
    "exclude_unlocks": ["fertilizer", "watering"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
#CODE
def for_all(f):
	def row():
		for _ in range(get_world_size()-1):
			f()
			move(East)
		f()
	for _ in range(get_world_size()):
		if not spawn_drone(row):
			row()
		move(North)

for_all(harvest)
}}

Здесь удобно использовать такую схему: сначала создается дрон, если это возможно, а если нет — ты выполняешь задание самостоятельно.

`if not spawn_drone(task):
	task()`
</spoiler>

## Ожидание другого дрона
Используй функцию `wait_for(drone)`, чтобы дождаться завершения работы другого дрона. Ты получаешь идентификатор `drone`, когда создаешь дрон.
`wait_for(drone)` возвращает значение, которое вернула бы функция, выполнявшаяся другим дроном.

{{codeexample 
{
    "camera_position": {"x": -0.5, "y": 1.5, "z": 4},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": false,
    "collapsing": true,
    "autoplay": false,
    "items": [],
    "world_size": {"x": 2, "y": 1},
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
plant(Entities.Tree)
move(West)
#CODE
def get_entity_type_in_direction(dir):
    move(dir)
    return get_entity_type()

drone = spawn_drone(get_entity_type_in_direction, East)
print(wait_for(drone))
}}

Обрати внимание, что создание дронов занимает время, поэтому не стоит добавлять их для каждой мелочи.

Можно использовать `has_finished(drone)`, чтобы узнать, закончил ли дрон, и не ждать лишнего.

## Отсутствие общей памяти
У каждого дрона собственная память, и он не может напрямую читать или записывать глобальные переменные другого дрона.

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
x = 0

def increment():
    global x
    x += 1

wait_for(spawn_drone(increment))
print(x)
}}

Такой код выведет `0`, потому что новый дрон увеличил собственную копию глобальной переменной `x`, что не влияет на `x` первого дрона.

## Передача аргументов

`spawn_drone()` принимает дополнительные необязательные аргументы, которые будут переданы вызываемой функции:

Обрати внимание, что правило «Отсутствие общей памяти» продолжает действовать. Это значит, что вызываемая функция работает с копией аргументов:

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
def modify(list):
	list.append('зелёный')
	print(list)

l = ['красный']
wait_for(spawn_drone(modify, l))
print(l)
}}

## Состояние гонки
Несколько дронов могут взаимодействовать с одной и той же клеткой фермы одновременно. Если два дрона попытаются взаимодействовать с одной и той же клеткой в течение одного тика, оба действия будут выполнены, но их результаты могут отличаться в зависимости от порядка.

Например, представь, что дроны `0` и `1` находятся над одним и тем же почти полностью выросшим деревом.
Дрон `0` вызывает
`use_item(Items.Fertilizer)`
Дрон `1` вызывает
`harvest()`

Если действия происходят одновременно, дерево сначала будет удобрено, а затем собрано. В этом случае ты получишь с него древесину. Однако, если дрон `1` окажется немного быстрее, дерево будет собрано до того, как его удобрили, и ты не получишь древесину.
Это называется «состояние гонки». Такая проблема часто встречается в параллельном программировании, где результат зависит от порядка выполнения операций.

Вот еще одна проблема, которая может возникнуть, если несколько дронов одновременно выполняют одинаковый код на одной и той же позиции.
`if get_water() < 0.5:
    use_item(Items.Water)`

Если несколько дронов выполняют код одновременно, они все выполнят первую строку и перейдут в блок `if`. Затем все они используют воду и потратят ее впустую.
К тому времени, как дрон достигнет второй строки, `get_water()` может быть уже не меньше `0.5`, потому что другой дрон тем временем полил эту клетку.

---

[Функции](docs/scripting/functions.md)      [Области видимости имен](docs/scripting/scopes.md)      [Симуляция](docs/unlocks/simulation.md)

[spawn_drone()](functions/spawn_drone)      [num_drones()](functions/num_drones)      [max_drones()](functions/max_drones)      [wait_for()](functions/wait_for)      [has_finished()](functions/has_finished)
