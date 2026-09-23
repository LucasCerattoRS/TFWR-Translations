[<- Górnictwo](docs/unlocks/mining.md) <right>[Bambus ->](docs/unlocks/bamboo.md)
<right>[Skamieniałe dynie ->](docs/unlocks/petrified_pumpkins.md)
<right>[Perlit i gleba próchnicza ->](docs/unlocks/special_soils.md)
---
# Ryż

Pod powierzchnią zauważasz cienką warstwę gliny. Okazuje się, że to żyzne podłoże idealnie nadaje się do sadzenia ryżu.

Ryż wysusza glinę, na której został posadzony. Każdego bloku gliny możesz użyć tylko raz. Na szczęście warstwa ma grubość kilku bloków. Oczywiście zawsze możesz użyć `clear()`, aby odtworzyć warstwę gliny.

Poniższy kod może pomóc ci kopać w dół, aż znajdziesz glinę.

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
    "exclude_unlocks": ["watering", "fertilizer"],
    "world_size": {"x": 4, "y": 4},
    "execution_speed": 8,
    "digging_speed": 4,
    "action_ticks": 200,
    "operation_ticks": 200,
    "seed": 1
}
#SETUP
move(East)
#CODE
while get_ground_type() != Grounds.Clay:
    dig()
plant(Entities.Rice)
move(North)
do_a_flip()
}}

---

[Statystyki](docs/stats.md)      [Górnictwo](docs/unlocks/mining.md)      [Podziemne zmysły](docs/unlocks/underground_senses.md)      [If](docs/scripting/if.md)      [Pętla for](docs/scripting/for.md)

[harvest()](functions/harvest)      [plant()](functions/plant)      [move()](functions/move)      [dig()](functions/dig)      [get_ground_type()](functions/get_ground_type)
