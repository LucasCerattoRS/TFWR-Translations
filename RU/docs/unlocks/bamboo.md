[<- Рис](docs/unlocks/rice.md) <right>[Цветные блоки ->](docs/unlocks/debug_place.md)
<right>[Пирамиды ->](docs/unlocks/pyramid.md)
---
# Бамбук

Бамбук — растение, способное вырасти до 6 блоков в высоту. Он не растет, пока над ним находится дрон, поэтому после `plant(Entities.Bamboo)` обязательно отведи дрон командой `move`. Для посадки бамбука нужен рис.

Достигнув случайно выбранной высоты, бамбук зацветает. С помощью `measure()` можно узнать, на какой высоте появится цветок. Отсчет в `measure()` начинается с 0, поэтому, если бамбук зацветет на втором блоке, `measure()` вернет 1:

{{codeexample 
{
    "camera_position": {"x": -1, "y": 0, "z": 8},
    "show_image": true,
    "image_size": {"x": 1000, "y": 500},
    "show_code": true,
    "show_inventory": true,
    "show_output": false,
    "collapsing": true,
    "autoplay": false,
    "items": [{"item": "rice", "n": 100}],
    "world_size": {"x": 4, "y": 4},
    "execution_speed": 2,
    "action_ticks": 200,
    "operation_ticks": 200,
    "seed": 1,
    "exclude_unlocks": ["watering", "fertilizer", "mushrooms", "coal"]
}
#SETUP
move(North)
move(East)
#CODE
till()
plant(Entities.Bamboo)
print(measure())
move(East)
}}

Чтобы получить максимальный урожай бамбука, вызови `harvest()`, когда дрон находится прямо над цветком. За каждый блок отклонения от этой высоты урожай делится на восемь.
Например, если цветок находится на высоте 3, а бамбук собран на два блока выше, урожай будет разделен на 64.

Чтобы собирать цветы на большой высоте, влетай в бамбук сбоку, когда дрон находится на нужном уровне. В этом поможет новая команда `place()`.

Складывай блоки рядом с бамбуком командой `place(Grounds.Dirt)`, чтобы подняться. Затем используй `move()`, чтобы влететь в бамбук сбоку. При вызове `harvest()` дрон должен находиться прямо над цветком.

Команда `place(Grounds.Dirt)` расходует 1 блок! Можно устанавливать и другие виды грунта, например `Grounds.Rock`, но не особые блоки вроде `Grounds.Clay`.

Бамбук вырастает ровно на 1 блок в секунду.

{{codeexample 
{
    "camera_position": {"x": -1, "y": 0, "z": 8},
    "show_image": true,
    "image_size": {"x": 1000, "y": 500},
    "show_code": true,
    "show_inventory": true,
    "show_output": false,
    "collapsing": true,
    "autoplay": false,
    "items": [{"item": "block", "n": 100}, {"item": "rice", "n": 100}],
    "world_size": {"x": 4, "y": 4},
    "execution_speed": 2,
    "action_ticks": 200,
    "operation_ticks": 200,
    "seed": 1,
    "exclude_unlocks": ["watering", "fertilizer", "mushrooms", "coal"]
}
#SETUP
move(North)
move(East)
#CODE
till()
plant(Entities.Bamboo)
print(measure())
move(East)
place(Grounds.Dirt)
do_a_flip() # немного подождать
do_a_flip()
move(West)
harvest()
}}

---

[Статистика](docs/stats.md)      [Цикл for](docs/scripting/for.md)      [Переменные](docs/scripting/variables.md)      [If](docs/scripting/if.md)      [Функции](docs/scripting/functions.md)      [Рис](docs/unlocks/rice.md)

[harvest()](functions/harvest)      [plant()](functions/plant)      [move()](functions/move)      [till()](functions/till)      [place()](functions/place)      [measure()](functions/measure)
