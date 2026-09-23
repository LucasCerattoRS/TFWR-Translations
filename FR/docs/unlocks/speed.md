[<- Boucle while](docs/scripting/while.md) <right>[Expansion 1 ->](docs/unlocks/expand_1.md)
<right>[Planter ->](docs/unlocks/plant.md)
---
# Amélioration de Vitesse
La vitesse d'exécution a été doublée. Le problème est que le drone récolte maintenant plus vite que l'herbe ne peut pousser, ce qui ne donne aucune récolte. Pour gérer cela, les branchements [if](docs/scripting/if.md) et la fonction [can_harvest](functions/can_harvest) sont maintenant débloqués.

## Vérifier avant de récolter
Une instruction `if` exécute son bloc de code une fois si la condition donnée vaut `True`.

La nouvelle fonction `can_harvest()` fournit une meilleure condition. `can_harvest()` renvoie `True` si la plante sous le drone peut être récoltée et `False` sinon.

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
do_a_flip()
#CODE
if can_harvest():
	do_a_flip()
}}

Tu peux imaginer qu’une valeur de retour de ce type remplace l’expression d’appel `can_harvest()` par la valeur renvoyée `True` lors de l’évaluation du `if`.

Voici ce qui se passe lorsque le code ci-dessus s’exécute :
- L’instruction `if` s’exécute.
- `can_harvest()` est appelée.
- `can_harvest()` renvoie `True`, car l’herbe est arrivée à maturité.
- L’instruction est maintenant `if True:`.
- La branche s’exécute, car la valeur est `True`.

Si l’herbe n’était pas arrivée à maturité, le drone ne ferait pas de looping.

Maintenant, nous pouvons utiliser `if` pour empêcher le drone de récolter trop tôt.
---

[If](docs/scripting/if.md)      [Boucle while](docs/scripting/while.md)

[harvest()](functions/harvest)      [can_harvest()](functions/can_harvest)
