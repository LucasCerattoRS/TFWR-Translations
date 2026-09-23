[<- Dictionaries](docs/scripting/dicts.md) <right>[Automatische Freischaltungen ->](docs/unlocks/auto_unlock.md)
---
# Kosten
Jede Kostenaufstellung kann als ein Dictionary dargestellt werden, das Items auf Zahlen abbildet.

Die `get_cost()`-Funktion gibt ein solches Dictionary zurück. Sie gibt die Kosten für eine Pflanze oder eine Freischaltung zurück.

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

Bei Freischaltungen kann optional ein zweites Argument für die Freischalt-Stufe übergeben werden, für die du die Kosten erhalten möchtest. Standardmäßig ist es die aktuelle Freischalt-Stufe.

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

Bei Freischaltungen, die bereits die höchste Stufe erreicht haben, gibt `get_cost()` ein leeres Dictionary zurück.

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
		print("Es fehlen", cost[item] - num_items(item), item)
}}

---

[Dictionaries](docs/scripting/dicts.md)      [Automatische Freischaltungen](docs/unlocks/auto_unlock.md)      [Bestenliste](docs/unlocks/leaderboard.md)

[get_cost()](functions/get_cost)
