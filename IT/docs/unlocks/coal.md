[<- Estrazione](docs/unlocks/mining.md) <right>[Ferro ->](docs/unlocks/iron.md)
<right>[Salto ->](docs/unlocks/jump.md)
---
# Carbone

Si scopre che il terreno subito sotto la superficie è un buon posto in cui trovare giacimenti di carbone.

Il carbone compare casualmente in strati orizzontali spessi 1 blocco. Le dimensioni dello strato aumentano in proporzione alle dimensioni del mondo, quindi potresti voler aumentare le dimensioni del mondo per trovare più carbone!

Il programma seguente è un buon punto di partenza per trovare il carbone. Scava verso il basso alla ricerca di uno strato di carbone, poi scava a est e a ovest nella speranza di trovarne altro.

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

[Statistiche](docs/stats.md)      [Estrazione](docs/unlocks/mining.md)      [Sensi Sotterranei](docs/unlocks/underground_senses.md)

[move()](functions/move)      [get_ground_type()](functions/get_ground_type)      [dig()](functions/dig)
