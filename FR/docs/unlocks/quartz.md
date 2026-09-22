[<- Fer](docs/unlocks/iron.md) <right>[Champignon ->](docs/unlocks/mushroom.md)
---
# Quartz

Le quartz pousse en filons en forme d’aiguilles près du bas de la couche rocheuse et dans la terre dure située dessous. Ces filons forment des colonnes verticales, ce qui les rend assez difficiles à trouver au hasard.

Heureusement, nous pouvons utiliser notre fer et le tordre pour fabriquer une sorte de baguette de sourcier qui facilite la localisation de ces filons de quartz. La commande correspondante est `prospect_quartz()`.

`prospect_quartz()` fonctionne différemment de `prospect_iron()`. Au lieu de renvoyer la direction du minerai de quartz le plus proche, elle renvoie sa distance euclidienne (distance en 3D). Exécuter `prospect_quartz()` coûte 1 fer : mieux vaut donc utiliser cette commande avec parcimonie.

Si `prospect_quartz()` ne trouve aucun quartz à proximité, ou si tu n’as pas assez de fer pour effectuer la recherche, elle renvoie `None`.

L’extrait de code suivant permet à ton drone de traverser la terre et de s’enfoncer dans la couche rocheuse. Avec un peu de chance, un filon de quartz se trouvera à proximité et ton drone affichera sa distance.

{{codeexample 
{
    "camera_position": {"x": -1, "y": 0, "z": 8},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": false,
    "collapsing": true,
    "autoplay": false,
    "items": [{"item": "hay", "n": 100}, {"item": "iron", "n": 100}],
    "world_size": {"x": 3, "y": 3},
    "execution_speed": 8,
    "digging_speed": 16,
    "action_ticks": 200,
    "operation_ticks": 200,
    "seed": 9,
    "exclude_unlocks": ["watering", "fertilizer", "mushrooms", "dynamite"]
}

#CODE
move(East)
move(North)
while get_ground_type() != Grounds.Rock:
    dig()
for i in range(30):
    dig()
do_a_flip()
do_a_flip()
print(prospect_quartz())
}}

---

[Statistiques](docs/stats.md)      [Exploitation minière](docs/unlocks/mining.md)      [Sens souterrains](docs/unlocks/underground_senses.md)      [Variables](docs/scripting/variables.md)      [Opérateurs](docs/scripting/operators.md)

[move()](functions/move)      [dig()](functions/dig)      [get_ground_type()](functions/get_ground_type)      [prospect_quartz()](functions/prospect_quartz)
