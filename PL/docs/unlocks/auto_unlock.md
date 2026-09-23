[<- Koszty](docs/unlocks/costs.md)
---
# Automatyczne odblokowania
Aby w pełni zautomatyzować grę, możesz użyć funkcji `unlock()`, aby automatycznie odblokowywać funkcje.
Na przykład, możesz użyć `unlock(Unlocks.Speed)` i `unlock(Unlocks.Expand)`, aby odblokować funkcje prędkości i ekspansji.

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

Aby określić koszt odblokowania, użyj funkcji `get_cost()` tak samo jak w przypadku rośliny lub przedmiotu.
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

[Koszty](docs/unlocks/costs.md)      [Słowniki](docs/scripting/dicts.md)      [If](docs/scripting/if.md)      [Tabela wyników](docs/unlocks/leaderboard.md)

[get_cost()](functions/get_cost)      [unlock()](functions/unlock)
