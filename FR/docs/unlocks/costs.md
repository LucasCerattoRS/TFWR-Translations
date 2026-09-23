[<- Dictionnaires](docs/scripting/dicts.md) <right>[Déblocages Auto ->](docs/unlocks/auto_unlock.md)
---
# Coûts
Tout coût peut être représenté par un dictionnaire qui mappe des objets à des nombres.

La fonction `get_cost()` renvoie un tel dictionnaire. Elle renvoie le coût d'une plante ou d'un déblocage.

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

Pour les déblocages, un deuxième argument optionnel peut être passé pour le niveau de déblocage dont tu veux obtenir le coût. Par défaut, c'est le niveau de déblocage actuel.

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

Pour les déblocages déjà au niveau maximal, `get_cost()` renvoie un dictionnaire vide.

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
		print("il manque", cost[item] - num_items(item), item)
}}

---

[Dictionnaires](docs/scripting/dicts.md)      [Déblocages Auto](docs/unlocks/auto_unlock.md)      [Classement](docs/unlocks/leaderboard.md)

[get_cost()](functions/get_cost)
