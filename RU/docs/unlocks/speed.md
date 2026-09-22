[<- Цикл while](docs/scripting/while.md) <right>[Расширение 1 ->](docs/unlocks/expand_1.md)
<right>[Посадка ->](docs/unlocks/plant.md)
---
# Повышение скорости
Скорость выполнения удвоилась. Проблема в том, что теперь дрон собирает урожай быстрее, чем успевает вырасти трава, и в итоге не получает ничего. Для решения разблокированы ветвление [if](docs/scripting/if.md) и функция [can_harvest()](functions/can_harvest).

## Проверка перед сбором урожая
Инструкция `if` выполняет свой блок кода один раз, если заданное условие равно `True`.

Новая функция `can_harvest()` лучше подойдет в качестве условия. `can_harvest()` возвращает `True`, если под дроном можно собрать урожай, в противном случае — `False`.

{{codeexample 
{
    "camera_position": {"x": 0, "y": 1.5, "z": 4},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": false,
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
if can_harvest():
	do_a_flip()
}}

Такое возвращаемое значение можно представить следующим образом: при вычислении `if` выражение с вызовом функции `can_harvest()` заменяется возвращенным значением `True`.

Что происходит при выполнении приведенного выше кода:
- Выполняется инструкция `if`.
- Вызывается `can_harvest()`.
- `can_harvest()` возвращает `True`, потому что трава полностью выросла.
- Теперь инструкция имеет вид `if True:`.
- Ветка выполняется, потому что значение равно `True`.

Если бы трава выросла не полностью, дрон не сделал бы сальто.

Теперь можно использовать `if`, чтобы дрон не собирал урожай слишком рано.

---

[If](docs/scripting/if.md)      [Цикл while](docs/scripting/while.md)

[harvest()](functions/harvest)      [can_harvest()](functions/can_harvest)
