[<- Expansion 1](docs/unlocks/expand_1.md)
---
# Expansion 2
Ta ferme s'est encore agrandie ! Maintenant, les cases ne sont plus en une belle rangée, tu dois donc trouver un moyen de parcourir une grille carrée.

Avec la boucle `while`, ce n'est pas possible tant que tu n'as pas débloqué les sens et les opérateurs.
Il est temps d'introduire la boucle `for`.

Tu peux tout lire sur la boucle `for` sur la page [Boucle For](docs/scripting/for.md), mais pour l'instant tu n'en auras besoin que pour répéter du code un nombre fixe de fois.

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
for i in range(5):
	do_a_flip()
}}

`range(n)` crée une séquence de `n` nombres allant de `0` à `n - 1`. La boucle `for` exécute son corps une fois pour chaque élément de la séquence. Dans cet exemple, `do_a_flip()` est appelée `5` fois.

La fonction `get_world_size()` est également disponible maintenant. Elle renvoie la longueur d'un côté de ta ferme. De cette façon, tu peux écrire du code qui ne se cassera pas avec la prochaine amélioration d'expansion.

{{codeexample 
{
    "camera_position": {"x": -1, "y": 1.8, "z": 5},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": false,
    "collapsing": true,
    "autoplay": false,
    "items": [],
    "world_size": {"x": 3, "y": 3},
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
do_a_flip()
#CODE
for i in range(get_world_size()):
	harvest()
	move(North)
}}

Cet exemple récolte une colonne de la ferme pour n'importe quelle taille de ferme.

Si tu ne sais pas comment déplacer le drone dans toute la ferme, consulte l’indice ci-dessous.
<spoiler=afficher l’indice>Il existe bien sûr plusieurs façons de parcourir la ferme.
Nous cherchons une méthode systématique qui continuera de fonctionner lorsque la ferme s’agrandira de nouveau.
Pour atteindre systématiquement chaque case de la ferme, tu pourrais répéter indéfiniment les deux étapes suivantes :

1. Aller vers `North` jusqu’à ce que le drone réapparaisse de l’autre côté.
2. Aller vers `East`.

`for i in range(get_world_size()):` peut t’aider à traduire cette idée en code.
</spoiler>
<spoiler=afficher une solution possible>
{{codeexample 
{
    "camera_position": {"x": -1, "y": 1.8, "z": 5},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": false,
    "collapsing": true,
    "autoplay": false,
    "items": [],
    "world_size": {"x": 3, "y": 3},
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
do_a_flip()
#CODE
for i in range(get_world_size()):
	for j in range(get_world_size()):
		#parcourir chaque case
		do_a_flip()
		move(North)
	move(East)
}}
</spoiler>
---

[Boucle for](docs/scripting/for.md)      [Boucle while](docs/scripting/while.md)      [Variables](docs/scripting/variables.md)

[move()](functions/move)      [get_world_size()](functions/get_world_size)
