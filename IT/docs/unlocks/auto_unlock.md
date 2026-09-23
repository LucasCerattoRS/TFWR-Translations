[<- Costi](docs/unlocks/costs.md)
---
# Sblocchi Automatici
Per automatizzare completamente il gioco, puoi usare la funzione `unlock()` per sbloccare automaticamente le funzionalità.
Ad esempio, puoi usare `unlock(Unlocks.Speed)` e `unlock(Unlocks.Expand)` per sbloccare le funzionalità di velocità ed espansione.

{{codeexample 
{
    "camera_position": {"x": 0, "y": 1, "z": 4},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": false,
    "collapsing": true,
    "autoplay": false,
    "items": [{"item": "hay", "n": 300}, {"item": "wood", "n": 100000}],
    "world_size": {"x": 1, "y": 1},
    "execution_speed": 1,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 1,
    "seed": 1,
    "exclude_unlocks": ["watering", "fertilizer"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
#CODE
for _ in range(6):
    harvest()
    unlock(Unlocks.Grass)
}}

Per determinare il costo di uno sblocco, usa semplicemente la funzione `get_cost()` come faresti per una pianta o un oggetto.
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
    "operation_ticks": 200,
    "seed": 1,
    "exclude_unlocks": ["watering", "fertilizer", "loops"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
#CODE
print(get_cost(Unlocks.Loops))
}}

---

[Costi](docs/unlocks/costs.md)      [Dizionari](docs/scripting/dicts.md)      [If](docs/scripting/if.md)      [Classifica](docs/unlocks/leaderboard.md)

[get_cost()](functions/get_cost)      [unlock()](functions/unlock)
