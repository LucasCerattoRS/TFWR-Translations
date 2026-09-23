[<- Diccionarios](docs/scripting/dicts.md) <right>[Autodesbloqueos ->](docs/unlocks/auto_unlock.md)
---
# Costes
Cualquier coste puede representarse como un diccionario que asigna ítems a números.

La función `get_cost()` devuelve dicho diccionario. Devuelve el coste de una planta o un desbloqueo.

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

Para los desbloqueos, puedes pasar un segundo argumento opcional que especifique el nivel de desbloqueo cuyo coste quieres consultar. De forma predeterminada, se usa el nivel de desbloqueo actual.

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

Para los desbloqueos que ya están en el nivel máximo, `get_cost()` devuelve un diccionario vacío.

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
		print("faltan", cost[item] - num_items(item), item)
}}

---

[Diccionarios](docs/scripting/dicts.md)      [Autodesbloqueos](docs/unlocks/auto_unlock.md)      [Tabla de clasificación](docs/unlocks/leaderboard.md)

[get_cost()](functions/get_cost)
