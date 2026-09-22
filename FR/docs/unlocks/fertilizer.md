[<- Arrosage](docs/unlocks/watering.md) <right>[Labyrinthes ->](docs/unlocks/mazes.md)
---
# Engrais
À un certain moment, attendre que les plantes poussent n'est tout simplement plus assez efficace. 
Comme pour l'eau, tu recevras automatiquement 1 engrais toutes les 10 secondes, et cette quantité double à chaque amélioration.

L'engrais peut faire pousser les plantes instantanément. `use_item(Items.Fertilizer)` réduit le temps de croissance restant de la plante sous le drone de 2 secondes.

{{codeexample 
{
    "camera_position": {"x": 0, "y": 1, "z": 5},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": false,
    "collapsing": true,
    "autoplay": false,
    "items": [{"item": "fertilizer", "n": 10}],
    "world_size": {"x": 1, "y": 1},
    "execution_speed": 2,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 1,
    "seed": 1,
    "exclude_unlocks": ["watering"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
#CODE
plant(Entities.Tree)
use_item(Items.Fertilizer)
use_item(Items.Fertilizer)
use_item(Items.Fertilizer)
harvest()
}}

Cela a quelques effets secondaires.
Les plantes cultivées avec de l'engrais seront infectées.

Lorsqu'une plante est infectée, la moitié de son rendement est transformée en `Items.Weird_Substance` lorsqu'elle est récoltée.
La Substance Étrange peut également être utilisée sur les plantes, ce qui a pour effet de basculer le statut infecté de la plante et de toutes les plantes adjacentes.

Donc, si tu appelles `use_item(Items.Weird_Substance)` sur une plante infectée, cela la guérira, mais si tu l'utilises sur une plante saine, cela l'infectera.

Si tu l'utilises sur une plante infectée qui a des voisins sains, cela guérira la plante mais infectera les voisins et vice versa.
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
    "items": [{"item": "weird_substance", "n": 10}],
    "world_size": {"x": 3, "y": 3},
    "execution_speed": 1,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 1,
    "seed": 1,
    "exclude_unlocks": ["watering"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
for _ in range(3):
    for _ in range(3):
        plant(Entities.Tree)
        move(East)
    move(North)

move(North)
move(East)

for _ in range(60):
    do_a_flip()
#CODE
for _ in range(6):
    use_item(Items.Weird_Substance)
    move(East)
}}

---

[Statistiques](docs/stats.md)      [Arrosage](docs/unlocks/watering.md)      [Labyrinthes](docs/unlocks/mazes.md)

[use_item()](functions/use_item)
