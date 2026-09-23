[<- Słowniki](docs/scripting/dicts.md) <right>[Automatyczne odblokowania ->](docs/unlocks/auto_unlock.md)
---
# Koszty
Każdy koszt można przedstawić jako słownik, który mapuje przedmioty na liczby.

Funkcja `get_cost()` zwraca taki słownik. Zwraca koszt rośliny lub odblokowania.

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

W przypadku odblokowań możesz przekazać opcjonalny drugi argument określający poziom odblokowania, którego koszt chcesz poznać. Domyślnie używany jest bieżący poziom.

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

W przypadku odblokowań, które osiągnęły już maksymalny poziom, `get_cost()` zwraca pusty słownik.

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
		print("brakuje", cost[item] - num_items(item), item)
}}

---

[Słowniki](docs/scripting/dicts.md)      [Automatyczne odblokowania](docs/unlocks/auto_unlock.md)      [Tabela wyników](docs/unlocks/leaderboard.md)

[get_cost()](functions/get_cost)
