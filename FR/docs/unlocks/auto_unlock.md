[<- Coûts](docs/unlocks/costs.md)
---
# Déblocages Auto
Pour automatiser entièrement le jeu, tu peux utiliser la fonction `unlock()` pour débloquer automatiquement des fonctionnalités.
Par exemple, tu peux utiliser `unlock(Unlocks.Speed)` et `unlock(Unlocks.Expand)` pour débloquer les fonctionnalités de vitesse et d'expansion.

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

Pour déterminer le coût d'un déblocage, utilise simplement la fonction `get_cost()` comme tu le ferais pour une plante ou un objet.
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

[Coûts](docs/unlocks/costs.md)      [Dictionnaires](docs/scripting/dicts.md)      [If](docs/scripting/if.md)      [Classement](docs/unlocks/leaderboard.md)

[get_cost()](functions/get_cost)      [unlock()](functions/unlock)
