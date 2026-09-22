[<- Pour commencer](docs/getting_started.md) <right>[Boucle while ->](docs/scripting/while.md)
---
# Premier Programme
## Éditeur de texte
Toute la programmation se fait dans des fenêtres de code. Chaque fenêtre de code correspond à un fichier texte contenant du code.
Tu peux renommer le fichier en cliquant sur son nom en haut de la fenêtre.

Le code peut être modifié comme dans n'importe quel éditeur de texte tant qu'il n'est pas en cours d'exécution.
Tu peux exécuter le programme directement en appuyant sur le bouton de lecture vert dans la fenêtre de code.
![](PlayButton)

Tu peux créer plus de fichiers de code en utilisant le bouton "+" dans le coin supérieur droit de l'écran.
Tu peux ancrer une fenêtre à une autre en la faisant glisser dessus.

Tu remarqueras qu'une fois que tu commences à taper, une simple fenêtre de complétion de code apparaîtra.
Appuie sur Tab pour insérer la complétion de code.
Utilise les touches fléchées pour naviguer dans les options de complétion.

Ne t'inquiète pas si c'est ta première fois en programmation. Le langage est débloqué étape par étape, donc tu ne seras pas submergé par toutes les choses que tu peux faire.
La syntaxe est également similaire à celle de Python, qui est l'un des langages de programmation les plus utilisés au monde, donc l'apprendre n'est pas complètement inutile.

Si tu connais déjà Python, ce n'est pas un problème non plus, tu pourras simplement passer rapidement le début du jeu pour arriver aux choses plus intéressantes.

Actuellement, deux commandes de drone sont disponibles.

`harvest()`

et 

`do_a_flip()`

Ce sont des appels de fonction. Tu peux penser à une fonction comme une commande qui peut être exécutée. Tu l'exécutes en utilisant les parenthèses `()`.

Essaie de taper ces instructions dans la fenêtre de code et d'appuyer sur le bouton d'exécution.

Tu peux considérer ton code comme une séquence d’instructions. Tu peux exécuter plusieurs instructions à la suite en les plaçant sur plusieurs lignes.
Appuie sur le bouton de lecture de cette fenêtre de code intégrée pour voir comment le code s’exécute :

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
    "operation_ticks": 200,
    "seed": 1,
    "exclude_unlocks": ["watering", "fertilizer"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
#CODE
do_a_flip()
harvest()
harvest()
}}

## Déblocages
La collecte d'herbe te donnera du foin. Le foin peut être utilisé pour débloquer des boucles dans le menu de déblocage. Ouvre le menu de déblocage avec le bouton dans le coin supérieur droit.

---

[Éditeur externe](docs/external_editor.md)      [Commentaires](docs/scripting/comments.md)      [Boucle while](docs/scripting/while.md)

[harvest()](functions/harvest)      [do_a_flip()](functions/do_a_flip)
