[<- Словари](docs/scripting/dicts.md) <right>[Авторазблокировка ->](docs/unlocks/auto_unlock.md)
---
# Стоимость
Любую стоимость можно представить в виде словаря, который сопоставляет предметы с числами.

Функция `get_cost()` возвращает такой словарь: она возвращает стоимость растения или технологии.

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
    "seed": 1,
    "exclude_unlocks": ["watering", "fertilizer"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
#CODE
print(get_cost(Entities.Pumpkin))
}}

В случае с технологиями можно передавать второй, необязательный, аргумент для уровня технологии, стоимость которого ты хочешь узнать. По умолчанию это текущий уровень технологии.

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
    "seed": 1,
    "exclude_unlocks": ["watering", "fertilizer"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
#CODE
print(get_cost(Unlocks.Loops, 0))
print(get_cost(Unlocks.Loops, 1))
}}

Для технологий, уже достигших максимального уровня, `get_cost()` возвращает пустой словарь.

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
    "seed": 1,
    "exclude_unlocks": ["watering", "fertilizer"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
#CODE
cost = get_cost(Entities.Carrot)
for item in cost:
	if num_items(item) < cost[item]:
		print("не хватает", cost[item] - num_items(item), item)
}}

---

[Словари](docs/scripting/dicts.md)      [Авторазблокировка](docs/unlocks/auto_unlock.md)      [Рейтинг](docs/unlocks/leaderboard.md)

[get_cost()](functions/get_cost)
