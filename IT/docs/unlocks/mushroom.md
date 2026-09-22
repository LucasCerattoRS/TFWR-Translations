[<- Quarzo](docs/unlocks/quartz.md) <right>[Dinamite ->](docs/unlocks/dynamite.md)
---
# Funghi

Molti tipi di funghi crescono in colonie sotterranee. Mentre scavi, cerca uno strato di `Grounds.Mushroom`. Puoi quindi usare `measure()` sul terreno per ottenere il tipo di fungo sotto forma di numero, a partire da `0`.

{{codeexample 
{
    "camera_position": {"x": -1, "y": 0, "z": 6},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": false,
    "collapsing": true,
    "autoplay": false,
    "items": [{"item": "hay", "n": 100}, {"item": "iron", "n": 100}],
    "world_size": {"x": 4, "y": 4},
    "execution_speed": 2,
    "digging_speed": 6,
    "action_ticks": 200,
    "operation_ticks": 200,
    "seed": 9,
    "exclude_unlocks": ["watering", "fertilizer", "dynamite", "iron"]
}

#SETUP
jump(Unlocks.Mushrooms)
#CODE
while get_ground_type() != Grounds.Mushroom:
    dig()
do_a_flip()
print(measure())
}}

I funghi dello stesso tipo amano stare insieme, ma sono troppo timidi per crescere uno sopra l'altro. Spingi un blocco di funghi sopra un altro blocco dello stesso tipo: scompariranno e riceverai funghi come ricompensa.

Puoi usare `can_push(direction)` per controllare se il blocco sotto il drone può essere spinto e se qualcosa lo ostacola nella direzione indicata. `push(direction)` spinge il blocco e restituisce se l'operazione è riuscita.

I blocchi non possono essere spinti verso l'alto e l'operazione fallisce se un altro blocco ostacola il percorso. Se vengono spinti nel vuoto, i blocchi cadono e atterrano sul blocco successivo sotto di loro.

Ricorda che puoi chiamare `place(Grounds.Dirt)` per posizionare blocchi sotto il drone. Può essere utile per riempire le buche e spingervi sopra altri blocchi.

---

[Statistiche](docs/stats.md)      [Sensi Sotterranei](docs/unlocks/underground_senses.md)      [Dizionari](docs/scripting/dicts.md)

[move()](functions/move)      [measure()](functions/measure)      [can_push()](functions/can_push)      [push()](functions/push)      [place()](functions/place)      [get_ground_type()](functions/get_ground_type)
