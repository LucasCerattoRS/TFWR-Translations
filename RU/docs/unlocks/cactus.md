[<- Тыквы](docs/unlocks/pumpkins.md) <right>[Динозавры ->](docs/unlocks/dinosaurs.md)
---
# Кактус
Как и другие растения, [кактусы](objects/cactus) можно выращивать на грядках и собирать как обычно.

Однако они бывают разных размеров и обладают странным чувством порядка.

Если ты собираешь созревший кактус, а все соседние кактусы находятся в отсортированном порядке, дрон рекурсивно соберет и их.

Кактус находится в отсортированном порядке, если все соседние кактусы в направлениях `North` и `East` созрели и имеют больший или равный размер, а все соседние кактусы в направлениях `South` и `West` созрели и имеют меньший или равный размер.

Дрон соберет соседние кактусы только в том случае, если все они созрели и находятся в отсортированном порядке.
То есть, если созревшие кактусы в квадрате отсортированы по размеру, при сборе одного кактуса ты соберешь растения со всего квадрата.

Созревший кактус будет коричневым, если он не отсортирован. После сортировки он снова станет зеленым.

Ты получишь кактусы в количестве, равном квадрату числа собранных кактусов. Так, если ты соберешь `n` кактусов одновременно, то получишь `n**2` `Items.Cactus`.

Размер кактуса можно измерить с помощью `measure()`.
Он всегда выражается одним из этих чисел: `0,1,2,3,4,5,6,7,8,9`.

Также можно передать направление через `measure(direction)`, чтобы измерить соседнюю к дрону клетку в указанном направлении.

Ты можешь поменять кактус местами с его соседом в любом направлении с помощью команды `swap()`.
`swap(direction)` меняет местами объект под дроном с объектом, находящимся на одну клетку в указанном направлении `direction` от дрона.

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
    "items": [{"item": "pumpkin", "n": 32}],
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
for _ in range(4):
    for _ in range(4):
        till()
        plant(Entities.Cactus)
        move(East)
    move(North)
for _ in range(4):
    for _ in range(4):
        for _ in range(4):
            x,y = get_pos_x(), get_pos_y()
            if x > 0 and measure(West) > measure():
                swap(West)
            if y > 0 and measure(South) > measure():
                swap(South)
            if x < 3 and measure(East) < measure():
                swap(East)
            if y < 3 and measure(North) < measure():
                swap(North)
            move(East)
        move(North)
move(East)
move(North)
move(North)
swap(West)
swap(South)
swap(East)
swap(North)
#CODE
swap(North)
swap(East)
swap(South)
swap(West)
harvest()
}}

## Числовые примеры
На каждом из этих полей все кактусы находятся в отсортированном порядке, поэтому сбор распространится на все поле:
`3 4 5    3 3 3    1 2 3    1 5 9
2 3 4    2 2 2    1 2 3    1 3 8
1 2 3    1 1 1    1 2 3    1 3 4`

На этом поле только нижний левый кактус находится в отсортированном порядке, а этого недостаточно для сбора остальных:
`1 5 3
4 9 7
3 3 2`

<spoiler=показать подсказку 1>
Если каждая строка уже отсортирована независимо, независимая сортировка каждого столбца не нарушит сортировку строк.
</spoiler>
<spoiler=показать подсказку 2>
Существует множество известных хитроумных алгоритмов сортировки. Если ты с ними не знаком, можно изучить их и подумать, какие удастся приспособить к этой задаче. Учти, что здесь подходят не все алгоритмы, потому что менять местами можно только соседние кактусы.
</spoiler>
<spoiler=показать подсказку 3>
«Пузырьковая сортировка» — пожалуй, самый простой алгоритм сортировки. Его идея в том, чтобы многократно проходить по элементам, меняя местами соседние элементы в неправильном порядке, пока таких не останется.

Вот как это выглядит с кактусами:
{{codeexample 
{
    "camera_position": {"x": -4, "y": 1, "z": 6},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": false,
    "show_inventory": true,
    "show_output": false,
    "collapsing": false,
    "autoplay": true,
    "items": [{"item": "pumpkin", "n": 18}],
    "world_size": {"x": 9, "y": 1},
    "execution_speed": 2,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 1,
    "seed": 1,
    "exclude_unlocks": ["fertilizer", "watering"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
#CODE
for _ in range(9):
    till()
    plant(Entities.Cactus)
    move(East)
sorted = False
while not sorted:
    sorted = True
    for _ in range(9):
        move(East)
        if get_pos_x() > 0 and measure(West) > measure():
            swap(West)
            sorted = False
harvest()
}}
Конечно, эту стратегию можно улучшить множеством способов!
Когда получится отсортировать одну строку, воспользуйся подсказкой 1, чтобы отсортировать все поле.
</spoiler>

---

[Статистика](docs/stats.md)

[harvest()](functions/harvest)      [plant()](functions/plant)      [move()](functions/move)      [till()](functions/till)      [swap()](functions/swap)      [measure()](functions/measure)
