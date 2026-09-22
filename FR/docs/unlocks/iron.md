[<- Charbon](docs/unlocks/coal.md) <right>[Quartz ->](docs/unlocks/quartz.md)
<right>[Prospection du fer ->](docs/unlocks/prospecting.md)
<right>[Carte au trésor ->](docs/unlocks/treasure_map.md)
---
# Fer

Tu as découvert des filons de fer dans la couche rocheuse située sous l’argile.

Les filons de fer sont petits au début et il te faudra un peu de chance pour les trouver. À mesure que tu augmentes le niveau de ce déblocage, la taille maximale d’un filon de minerai augmente. Pour trouver du fer de façon plus fiable, tu peux aussi consulter le déblocage de la prospection du minerai.

Un filon de fer est toujours continu, sans liaison en diagonale. Si tu trouves un morceau de fer, cherche-en d’autres dessous ou à côté afin de récolter tout le filon.

{{codeexample 
{
    "camera_position": {"x": -1, "y": 0, "z": 8},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": false,
    "collapsing": false,
    "autoplay": true,
    "items": [{"item": "hay", "n": 100}, {"item": "wood", "n": 100}],
    "world_size": {"x": 5, "y": 5},
    "execution_speed": 1,
    "digging_speed": 4,
    "action_ticks": 200,
    "operation_ticks": 200,
    "seed": 9,
    "exclude_unlocks": ["watering", "fertilizer", "mushrooms", "coal", "quartz"]
}
#SETUP
jump(Unlocks.Iron)
#CODE
for i in range(4):
    dig()
do_a_flip()
}}

---

[Statistiques](docs/stats.md)      [Exploitation minière](docs/unlocks/mining.md)      [Prospection du fer](docs/unlocks/prospecting.md)      [Sens souterrains](docs/unlocks/underground_senses.md)

[move()](functions/move)      [dig()](functions/dig)
