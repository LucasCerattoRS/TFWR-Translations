[<- Amélioration de Vitesse](docs/unlocks/speed.md) <right>[Expansion 2 ->](docs/unlocks/expand_2.md)
<right>[Exploitation minière ->](docs/unlocks/mining.md)
---
# Expansion 1
Ta ferme s’est agrandie ! Cet espace n’est pas très utile si tu ne peux pas déplacer le drone. Une nouvelle fonction, `move()`, permet donc de le faire. `move()` exige que tu indiques la direction souhaitée. Quatre nouvelles constantes sont disponibles : `North, East, South, West`

Par exemple, `move(North)` déplacera le drone d'une case vers le nord.

Si tu dépasses le bord de la ferme, le drone réapparaît de l’autre côté.

{{codeexample 
{
    "camera_position": {"x": 0, "y": 1.8, "z": 5},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": false,
    "collapsing": true,
    "autoplay": false,
    "items": [],
    "world_size": {"x": 1, "y": 3},
    "execution_speed": 2,
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
while True:
	move(North)
}}

---

[Boucle while](docs/scripting/while.md)      [Opérateurs](docs/scripting/operators.md)      [Expansion 2](docs/unlocks/expand_2.md)

[move()](functions/move)
