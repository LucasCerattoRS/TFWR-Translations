[<- Górnictwo](docs/unlocks/mining.md) <right>[Żelazo ->](docs/unlocks/iron.md)
<right>[Skok ->](docs/unlocks/jump.md)
---
# Węgiel

Okazuje się, że podłoże tuż pod powierzchnią jest dobrym miejscem do szukania złóż węgla.

Węgiel pojawia się losowo w poziomych pokładach o grubości 1 bloku. Rozmiar pokładu rośnie proporcjonalnie do rozmiaru świata, więc warto go zwiększyć, aby znaleźć więcej węgla!

Poniższy program to dobry punkt wyjścia do poszukiwania węgla. Kopie w dół w poszukiwaniu pokładu, a następnie na wschód i zachód, licząc na znalezienie większej ilości węgla.

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
    "world_size": {"x": 4, "y": 4},
    "execution_speed": 4,
    "digging_speed": 2,
    "action_ticks": 200,
    "operation_ticks": 200,
    "seed": 2
}
#SETUP
move(North)
move(East)
move(East)
#CODE
while get_ground_type() != Grounds.Coal:
    dig()
dig()
move(East)
dig()
move(West)
move(West)
dig()
}}

---

[Statystyki](docs/stats.md)      [Górnictwo](docs/unlocks/mining.md)      [Podziemne zmysły](docs/unlocks/underground_senses.md)

[move()](functions/move)      [get_ground_type()](functions/get_ground_type)      [dig()](functions/dig)
