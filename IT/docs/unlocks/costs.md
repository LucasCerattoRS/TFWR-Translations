[<- Dizionari](docs/scripting/dicts.md) <right>[Sblocchi Automatici ->](docs/unlocks/auto_unlock.md)
---
# Costi
Qualsiasi costo può essere rappresentato come un dizionario che mappa oggetti a numeri.

La funzione `get_cost()` restituisce un dizionario di questo tipo. Restituisce il costo di una pianta o di uno sblocco.

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

Per gli sblocchi puoi passare un secondo argomento facoltativo che specifica il livello di cui vuoi conoscere il costo. Per impostazione predefinita viene usato il livello attuale.

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

Per gli sblocchi che hanno già raggiunto il livello massimo, `get_cost()` restituisce un dizionario vuoto.

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
		print("mancano", cost[item] - num_items(item), item)
}}

---

[Dizionari](docs/scripting/dicts.md)      [Sblocchi Automatici](docs/unlocks/auto_unlock.md)      [Classifica](docs/unlocks/leaderboard.md)

[get_cost()](functions/get_cost)
