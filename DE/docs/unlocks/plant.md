[<- Geschwindigkeits-Upgrade](docs/unlocks/speed.md) <right>[Karotten ->](docs/unlocks/carrots.md)
<right>[Debug ->](docs/scripting/debug.md)
<right>[Operatoren ->](docs/scripting/operators.md)
---
# Pflanzen
Gras ist schön, weil es automatisch wächst. Alle anderen Pflanzen müssen mit der Funktion `plant()` gepflanzt werden. Die einzige Pflanze, die du im Moment pflanzen kannst, ist ein Busch.
Du kannst die Art der Pflanze, die du pflanzen möchtest, so an die Funktion übergeben:

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
plant(Entities.Bush)
}}

Dies wird einen Busch unter der Drohne pflanzen.

Rufe `clear()` auf, um die Farm auf nur Gras zurückzusetzen und die Drohnenposition zurückzusetzen.

Wenn du mehrere Pflanzenarten gleichzeitig auf der Farm anbaust, kannst du anscheinend manchmal einen höheren Ertrag erzielen. Erforsche Polykultur, um mehr darüber zu erfahren.

---

[Statistiken](docs/stats.md)      [If](docs/scripting/if.md)      [Sinne](docs/unlocks/senses.md)      [Polykultur](docs/unlocks/polyculture.md)

[harvest()](functions/harvest)      [plant()](functions/plant)
