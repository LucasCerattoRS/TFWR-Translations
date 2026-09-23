[<- Citrouilles](docs/unlocks/pumpkins.md)
---
# Polyculture
Tu as peut-être déjà remarqué que parfois les plantes rapportent plus lorsqu'elles sont plantées ensemble.
L'herbe, les buissons, les arbres et les carottes rapportent plus lorsqu'ils ont la bonne plante compagne. La préférence de compagnon est différente pour chaque plante individuelle et ne peut pas être prédite. Heureusement, la préférence de compagnon de la plante sous le drone peut être mesurée en utilisant `get_companion()`. Elle renvoie un tuple où le premier élément est le type de plante qu'elle veut comme compagnon et le deuxième élément est la position où elle veut son compagnon.

{{codeexample 
{
    "camera_position": {"x": -1, "y": 1.8, "z": 5},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": true,
    "collapsing": true,
    "autoplay": false,
    "items": [],
    "world_size": {"x": 3, "y": 3},
    "execution_speed": 1,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 20,
    "seed": 1,
    "exclude_unlocks": ["watering", "fertilizer"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
#CODE
plant(Entities.Bush)
plant_type, (x, y) = get_companion()
print(plant_type, (x, y))
move(East)
move(South)
plant(plant_type)
move(West)
move(North)
do_a_flip()
harvest()
}}

La préférence de compagnon d'une plante peut être soit `Entities.Grass`, `Entities.Bush`, `Entities.Tree` ou `Entities.Carrot`. Chaque plante choisit cela au hasard, mais elle choisira toujours une plante différente d'elle-même. La position peut également être n'importe quelle position à moins de 3 déplacements de la plante, sauf la position de la plante elle-même.

S'il n'y a pas de plante sous le drone qui a une préférence de compagnon, `get_companion()` renverra `None`.

Avant que la polyculture soit débloquée pour la première fois, le multiplicateur de rendement vaut `5`. Il double à chaque amélioration.

---

[Statistiques](docs/stats.md)      [Tuples](docs/scripting/tuples.md)      [Dictionnaires](docs/scripting/dicts.md)      [Sens](docs/unlocks/senses.md)      [Planter](docs/unlocks/plant.md)

[harvest()](functions/harvest)      [plant()](functions/plant)      [move()](functions/move)      [till()](functions/till)      [get_companion()](functions/get_companion)
