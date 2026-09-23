[<- Amélioration de Vitesse](docs/unlocks/speed.md) <right>[Carottes ->](docs/unlocks/carrots.md)
<right>[Débogage ->](docs/scripting/debug.md)
<right>[Opérateurs ->](docs/scripting/operators.md)
---
# Planter
L'herbe est bien car elle pousse automatiquement. Toutes les autres plantes doivent être plantées avec la fonction `plant()`. La seule plante que tu peux planter pour l'instant est un buisson.
Tu peux passer le type de plante que tu veux planter à la fonction comme ceci :

{{codeexample 
{
    "camera_position": {"x": 0, "y": 1.5, "z": 4},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": false,
    "collapsing": true,
    "autoplay": false,
    "items": [],
    "world_size": {"x": 1, "y": 1},
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
plant(Entities.Bush)
}}

Cela plantera un buisson sous le drone.

Appelle `clear()` pour réinitialiser la ferme à de l'herbe partout et réinitialiser la position du drone.

Il semble que si tu fais pousser plus d'un type de plante dans la ferme en même temps, tu peux parfois obtenir un rendement plus élevé. Tu devras faire des recherches sur la polyculture pour en savoir plus.
---

[Statistiques](docs/stats.md)      [If](docs/scripting/if.md)      [Sens](docs/unlocks/senses.md)      [Polyculture](docs/unlocks/polyculture.md)

[harvest()](functions/harvest)      [plant()](functions/plant)
