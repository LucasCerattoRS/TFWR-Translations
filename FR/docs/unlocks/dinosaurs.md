[<- Cactus](docs/unlocks/cactus.md)
---
# Dinosaures
Les dinosaures sont d'anciennes créatures majestueuses que l'on peut élever pour obtenir des os anciens.

Malheureusement, les dinosaures ont disparu il y a bien longtemps, donc le mieux que nous puissions faire maintenant est de nous déguiser en l'un d'eux.
À cette fin, tu as reçu le nouveau chapeau de dinosaure.

Le chapeau peut être équipé avec
`change_hat(Hats.Dinosaur_Hat)`

Malheureusement, il n'a pas tout à fait l'air de ce qu'on voit sur la publicité...

Si tu équipes le chapeau de dinosaure et que tu as assez de cactus, une [pomme](objects/apple) sera automatiquement achetée et placée sous le drone.
Quand le drone est sur une pomme et se déplace à nouveau, il mangera la pomme et sa queue grandira de un. Si tu peux te le permettre, une nouvelle pomme sera achetée et placée à un endroit aléatoire.
La pomme ne peut pas apparaître si quelque chose d'autre est planté là où elle veut être.

La queue du dinosaure sera traînée derrière le drone, remplissant les cases précédentes sur lesquelles le drone s'est déplacé. Si un drone essaie de se déplacer sur la queue, `move()` échouera et renverra `False`. 
Le dernier segment de la queue s'écartera pendant le déplacement, tu pourras donc te déplacer dessus. Cependant, si le serpent remplit toute la ferme, tu ne pourras plus te déplacer. Tu peux donc vérifier si le serpent est adulte en vérifiant si tu ne peux plus bouger.
En portant le chapeau de dinosaure, le drone ne peut pas traverser la bordure de la ferme pour atteindre l'autre côté.

Utiliser `measure()` sur une pomme renverra la position de la prochaine pomme sous forme de tuple.

`next_x, next_y = measure()`

{{codeexample 
{
    "camera_position": {"x": -1, "y": 2.4, "z": 5},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": true,
    "collapsing": true,
    "autoplay": false,
    "items": [{"item": "cactus", "n": 10000}],
    "world_size": {"x": 4, "y": 4},
    "execution_speed": 2,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 1,
    "seed": 5,
    "exclude_unlocks": ["watering"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
#CODE
change_hat(Hats.Dinosaur_Hat)
while True:
    next_x, next_y = measure()
    while get_pos_x() != next_x:
        move(East)
    while get_pos_y() != next_y:
        move(North)
}}

Lorsque le chapeau est de nouveau retiré en équipant un chapeau différent, la queue sera récoltée.
Tu recevras un nombre d'os égal au carré de la longueur de la queue. Donc pour une queue de longueur `n`, tu recevras `n**2` `Items.Bone`. 
Par Exemple :
longueur 1 => 1 os
longueur 2 => 4 os
longueur 3 => 9 os
longueur 4 => 16 os
longueur 16 => 256 os
longueur 100 => 10000 os

Le Chapeau de Dinosaure est très lourd, donc si tu l'équipes, `move()` prendra 400 ticks au lieu de 200. Cependant, chaque fois que tu ramasses une pomme, le nombre de ticks utilisés par `move()` est réduit de 3% (arrondi à l'inférieur), car une queue plus longue peut t'aider à te déplacer.

La boucle suivante affiche le nombre de ticks utilisés par `move()` après n'importe quel nombre de pommes :

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
    "operation_ticks": 1,
    "seed": 1,
    "exclude_unlocks": ["watering", "fertilizer"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
#CODE
ticks = 400
for i in range(100):
    quick_print("ticks après ", i, " pommes : ", ticks)
    ticks -= ticks * 0.03 // 1
}}

Tu n'as qu'un seul chapeau de dinosaure, donc un seul drone peut le porter.

<spoiler=afficher l’indice 1>
Si tu suis toujours le même trajet couvrant tout le champ, tu peux facilement obtenir à chaque fois un serpent qui remplit toute la ferme. Ce n’est pas très efficace, mais ça fonctionne.
Parcourir entièrement une très grande ferme peut prendre beaucoup de temps, et tu n’as peut-être pas besoin d’autant d’os. N’hésite pas à utiliser `set_world_size()` pour choisir une taille de ferme plus pratique.</spoiler>

---

[Statistiques](docs/stats.md)      [Tuples](docs/scripting/tuples.md)      [Listes](docs/scripting/lists.md)

[change_hat()](functions/change_hat)      [move()](functions/move)      [measure()](functions/measure)
