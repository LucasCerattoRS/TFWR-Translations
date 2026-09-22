[<- Opérateurs](docs/scripting/operators.md) <right>[Listes ->](docs/scripting/lists.md)
<right>[Fonctions ->](docs/scripting/functions.md)
---
# Variables
On peut voir les variables comme des conteneurs nommés qui peuvent contenir une valeur.
L'opérateur `=` est utilisé pour déclarer une variable et y stocker une valeur.

`nom_de_variable = valeur`

Le côté gauche de l'opérateur est le nom de la variable. Tu peux lui donner n’importe quel nom valide.
Le côté droit est une expression dont la valeur résultante sera stockée dans la variable.

Déclare une variable nommée `a` et y stocke la valeur `5` :
`a = 5`
Déclare une variable nommée `b` et y stocke la valeur de retour de `can_harvest()` :
`b = can_harvest()`

Ne confonds pas l'opérateur `=` avec l'opérateur `==`.
L'opérateur `==` vérifie si deux valeurs sont égales et renvoie `True` ou `False`.
L'opérateur `=` assigne la valeur de droite au nom de gauche.

Une fois qu'une variable a été assignée, tu peux l'utiliser dans le code pour récupérer la valeur qu'elle contient

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
a = 5
for i in range(a):
	do_a_flip()
}}

La boucle ci-dessus est exécutée 5 fois car `a` est défini sur `5`.
Le `i` dans la boucle `for` est aussi une variable qui se voit automatiquement assigner la valeur actuelle de la séquence à chaque itération de la boucle. (Il n'est pas obligé de s'appeler `i`, tu peux lui donner n'importe quel nom de variable valide.)

Les variables te permettent aussi de faire la même chose avec une boucle while :

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
a = 5
i = 0
while i < a:
	do_a_flip()
	i = i + 1
}}

Cela fait la même chose que la boucle `for` ci-dessus. Nous devons juste incrémenter `i` manuellement.
Note que pour incrémenter `i`, nous le définissons comme sa propre valeur plus `1`. Changer la valeur d'une variable en fonction de sa valeur précédente est quelque chose de très courant.
Cela peut être abrégé en utilisant ces opérateurs : `+=, -=, *=, /=, %=`

`i = i + 1` est la même chose que `i += 1`
`a = a / 3` est la même chose que `a /= 3`

---

[Opérateurs](docs/scripting/operators.md)      [Boucle while](docs/scripting/while.md)      [Boucle for](docs/scripting/for.md)      [Fonctions](docs/scripting/functions.md)      [Portées des noms](docs/scripting/scopes.md)
