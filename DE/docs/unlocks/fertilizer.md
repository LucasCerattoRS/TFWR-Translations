[<- Bewässerung](docs/unlocks/watering.md) <right>[Labyrinthe ->](docs/unlocks/mazes.md)
---
# Dünger
Irgendwann ist es einfach nicht mehr effizient genug, auf das Wachsen der Pflanzen zu warten.
Ähnlich wie bei Wasser erhältst du automatisch alle 10 Sekunden 1 Dünger, wobei sich die Menge mit jedem Upgrade verdoppelt.

Dünger kann Pflanzen sofort wachsen lassen. `use_item(Items.Fertilizer)` reduziert die verbleibende Wachstumszeit der Pflanze unter der Drohne um 2 Sekunden.

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

Dies hat einige Nebenwirkungen.
Pflanzen, die mit Dünger angebaut werden, werden infiziert.

Wenn eine Pflanze infiziert ist, wird die Hälfte ihres Ertrags beim Ernten in `Items.Weird_Substance` umgewandelt.
Seltsame Substanz kann auch auf Pflanzen angewendet werden, was den Infektionsstatus der Pflanze und aller benachbarten Pflanzen umschaltet.

Wenn du also `use_item(Items.Weird_Substance)` auf eine infizierte Pflanze anwendest, wird sie geheilt, aber wenn du es auf eine gesunde Pflanze anwendest, wird sie infiziert.

Wenn du es auf eine infizierte Pflanze mit gesunden Nachbarn anwendest, wird die Pflanze geheilt, aber ihre Nachbarn werden infiziert – und umgekehrt.

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

[Statistiken](docs/stats.md)      [Bewässerung](docs/unlocks/watering.md)      [Labyrinthe](docs/unlocks/mazes.md)

[use_item()](functions/use_item)
