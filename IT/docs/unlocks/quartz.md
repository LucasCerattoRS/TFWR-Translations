[<- Ferro](docs/unlocks/iron.md) <right>[Funghi ->](docs/unlocks/mushroom.md)
---
# Quarzo

Il quarzo cresce in vene a forma di ago vicino al fondo dello strato di roccia e nella terra dura sottostante. Le vene formano colonne verticali, perciò sono piuttosto difficili da trovare procedendo per tentativi.

Per fortuna possiamo prendere il ferro e deformarlo fino a ottenere qualcosa di simile a una bacchetta da rabdomante, così da individuare più facilmente le vene di quarzo. Il comando apposito è `prospect_quartz()`.

`prospect_quartz()` funziona diversamente da `prospect_iron()`. Invece di restituire la direzione del minerale di quarzo più vicino, restituisce la distanza euclidea (distanza 3D) dal quarzo più vicino. Eseguire `prospect_quartz()` costa 1 ferro, quindi conviene usare il comando con parsimonia.

Se `prospect_quartz()` non trova quarzo nelle vicinanze oppure non hai abbastanza ferro per eseguire la ricerca, restituisce `None`.

Il codice seguente fa scavare il drone oltre la terra e in profondità nello strato di roccia. Con un po' di fortuna ci sarà una vena di quarzo nelle vicinanze e il drone ne stamperà la distanza.

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

[Statistiche](docs/stats.md)      [Estrazione](docs/unlocks/mining.md)      [Sensi Sotterranei](docs/unlocks/underground_senses.md)      [Variabili](docs/scripting/variables.md)      [Operatori](docs/scripting/operators.md)

[move()](functions/move)      [dig()](functions/dig)      [get_ground_type()](functions/get_ground_type)      [prospect_quartz()](functions/prospect_quartz)
