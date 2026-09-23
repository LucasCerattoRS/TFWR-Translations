[<- Riso](docs/unlocks/rice.md) <right>[Blocchi Colorati ->](docs/unlocks/debug_place.md)
<right>[Piramidi ->](docs/unlocks/pyramid.md)
---
# Bambù

Il bambù è una pianta che può raggiungere un'altezza di 6 blocchi. Non cresce finché c'è un drone sopra di esso, quindi assicurati di spostare il drone con `move` dopo aver usato `plant(Entities.Bamboo)`. Piantare bambù costa riso.

Il bambù produce fiori quando raggiunge una certa altezza, scelta casualmente. Usa `measure()` per verificare a quale altezza fiorirà. `measure()` inizia a contare da 0, quindi se il bambù fiorisce sul secondo blocco, `measure()` restituisce 1:

{{codeexample 
{
    "camera_position": {"x": -1, "y": 0, "z": 8},
    "show_image": true,
    "image_size": {"x": 1000, "y": 500},
    "show_code": true,
    "show_inventory": true,
    "show_output": false,
    "collapsing": true,
    "autoplay": false,
    "items": [{"item": "rice", "n": 100}],
    "world_size": {"x": 4, "y": 4},
    "execution_speed": 2,
    "action_ticks": 200,
    "operation_ticks": 200,
    "seed": 1,
    "exclude_unlocks": ["watering", "fertilizer", "mushrooms", "coal"]
}
#SETUP
move(North)
move(East)
#CODE
till()
plant(Entities.Bamboo)
print(measure())
move(East)
}}

Otterrai la resa massima dal bambù usando `harvest()` quando il drone si trova direttamente sopra il fiore. Per ogni blocco di distanza da quell'altezza, la resa viene divisa per otto.
Per esempio, se il fiore si trova all'altezza 3 ma lo raccogli due blocchi più in alto, la resa viene divisa per 64.

Per raccogliere i fiori più in alto, vola dentro il bambù quando il drone si trova all'altezza desiderata. Il comando appena sbloccato `place()` ti aiuta a farlo.

Usa `place(Grounds.Dirt)` per impilare blocchi accanto al bambù e salire. Poi usa `move()` per volare nel bambù di lato. Quando chiami `harvest()`, il drone deve trovarsi direttamente sopra il fiore.

`place(Grounds.Dirt)` costa 1 blocco! Puoi posizionare anche altri terreni come `Grounds.Rock`, ma non blocchi speciali come `Grounds.Clay`.

Il bambù cresce esattamente di 1 blocco al secondo.

{{codeexample 
{
    "camera_position": {"x": -1, "y": 0, "z": 8},
    "show_image": true,
    "image_size": {"x": 1000, "y": 500},
    "show_code": true,
    "show_inventory": true,
    "show_output": false,
    "collapsing": true,
    "autoplay": false,
    "items": [{"item": "block", "n": 100}, {"item": "rice", "n": 100}],
    "world_size": {"x": 4, "y": 4},
    "execution_speed": 2,
    "action_ticks": 200,
    "operation_ticks": 200,
    "seed": 1,
    "exclude_unlocks": ["watering", "fertilizer", "mushrooms", "coal"]
}
#SETUP
move(North)
move(East)
#CODE
till()
plant(Entities.Bamboo)
print(measure())
move(East)
place(Grounds.Dirt)
do_a_flip() # aspetta un po'
do_a_flip()
move(West)
harvest()
}}

---

[Statistiche](docs/stats.md)      [Ciclo For](docs/scripting/for.md)      [Variabili](docs/scripting/variables.md)      [If](docs/scripting/if.md)      [Funzioni](docs/scripting/functions.md)      [Riso](docs/unlocks/rice.md)

[harvest()](functions/harvest)      [plant()](functions/plant)      [move()](functions/move)      [till()](functions/till)      [place()](functions/place)      [measure()](functions/measure)
