[<- Посадка](docs/unlocks/plant.md) <right>[Отладка 2 ->](docs/unlocks/debug2.md)
<right>[Время ->](docs/unlocks/timing.md)
---
# Отладка
Иногда код выполняется неправильно, и тебе нужно выяснить причину. Для этого есть несколько инструментов.

Первый — выполнение программы по шагам.
Чтобы перейти в пошаговый режим, нажми на кнопку рядом с кнопкой выполнения или задай точку останова.

Точки останова можно добавить, щелкнув на панели слева от кода.
![|x227](Breakpoints)
Когда выполнение дойдет до строки с точкой останова, игра автоматически перейдет в пошаговый режим.

Если навести мышь на переменную, отобразится ее текущее значение.

Также может пригодиться функция `print()`. Она выводит любое переданное ей значение в воздухе.

Примеры:

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
print(0.24)
}}

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
print(can_harvest())
}}

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
print(get_pos_x(), get_pos_y())
}}

Функция `print()` выводит значение прямо в воздухе, а также на странице [Вывод](docs/output.md).

Если вы хотите вывести много значений, вывод в воздух может происходить медленно.
В этом случае можно использовать функцию `quick_print()`, которая выводит значение только в окно вывода.

Окно вывода также фиксирует предупреждения и ошибки. Если что-то пошло не так, как ожидалось, стоит туда заглянуть.

Когда выполнение кода останавливается, вывод также записывается в файл output.txt в папке игры: [output.txt](persistent_data_path/output.txt).
---

[Вывод](docs/output.md)      [Комментарии](docs/scripting/comments.md)      [Отладка 2](docs/unlocks/debug2.md)      [Цветные блоки](docs/unlocks/debug_place.md)      [Симуляция](docs/unlocks/simulation.md)

[print()](functions/print)      [quick_print()](functions/quick_print)
