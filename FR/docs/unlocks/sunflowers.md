[<- Arrosage](docs/unlocks/watering.md)
---
# Tournesols
Les [tournesols](objects/sunflower) collectent la puissance du soleil. Tu peux récolter cette puissance.

Les planter fonctionne exactement de la même manière que pour les carottes ou les citrouilles.

Récolter un tournesol adulte rapporte de la puissance.
S'il y a au moins 10 tournesols dans la ferme et que tu récoltes celui avec le plus grand nombre de pétales, tu obtiens `8` fois plus de puissance !
Si tu récoltes un tournesol alors qu'un autre a plus de pétales, le prochain tournesol que tu récolteras ne te donnera que la quantité normale de puissance (pas le bonus de 8x).

`measure()` renvoie le nombre de pétales du tournesol sous le drone.
Les tournesols ont au moins `7` et au plus `15` pétales.
Même avant leur maturité, les tournesols peuvent déjà être mesurés et comptent dans le seuil des 10 tournesols.

Plusieurs tournesols peuvent avoir le même nombre de pétales, il peut donc y avoir plusieurs tournesols avec le plus grand nombre de pétales. Dans ce cas, peu importe lequel tu récoltes.

{{codeexample 
{
    "camera_position": {"x": -1.5, "y": 2, "z": 4},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "inventory_scale": 5,
    "show_output": false,
    "collapsing": true,
    "autoplay": false,
    "items": [{"item": "carrot", "n": 10}],
    "world_size": {"x": 5, "y": 2},
    "execution_speed": 2,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 1,
    "seed": 4,
    "exclude_unlocks": ["fertilizer", "watering"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
move(North)
for _ in range(5):
    till()
    plant(Entities.Sunflower)
    move(East)
move(North)
do_a_flip()
do_a_flip()
do_a_flip()
do_a_flip()
do_a_flip()
#CODE
for _ in range(5):
    till()
    plant(Entities.Sunflower)
    print(measure())
    move(East)
for _ in range(5):
    while not can_harvest():
        pass
    harvest()
    move(East)
}}

Tant que tu as de la puissance, le drone l'utilisera pour fonctionner deux fois plus vite.
Il consomme 1 de puissance toutes les 30 actions (comme les déplacements, les récoltes, les plantations...)
Exécuter d'autres instructions de code peut aussi utiliser de la puissance, mais beaucoup moins que les actions du drone.

En général, tout ce qui est accéléré par les améliorations de vitesse est aussi accéléré par la puissance.
Tout ce qui est accéléré par la puissance utilise aussi de la puissance proportionnellement au temps que cela prend pour s'exécuter, sans tenir compte des améliorations de vitesse.
---

[Statistiques](docs/stats.md)      [Listes](docs/scripting/lists.md)      [Dictionnaires](docs/scripting/dicts.md)      [Variables](docs/scripting/variables.md)      [Boucle for](docs/scripting/for.md)      [If](docs/scripting/if.md)      [Opérateurs](docs/scripting/operators.md)

[harvest()](functions/harvest)      [plant()](functions/plant)      [move()](functions/move)      [till()](functions/till)      [measure()](functions/measure)
