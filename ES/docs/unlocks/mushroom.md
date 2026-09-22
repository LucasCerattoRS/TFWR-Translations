[<- Cuarzo](docs/unlocks/quartz.md) <right>[Dinamita ->](docs/unlocks/dynamite.md)
---
# Hongo

Muchos tipos de hongos crecen en colonias bajo tierra. Busca un estrato de `Grounds.Mushroom` mientras excavas. Después puedes usar `measure()` sobre el terreno para obtener el tipo de hongo como un número, empezando por `0`.

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

A los hongos del mismo tipo les gusta estar juntos, pero les da demasiada vergüenza crecer unos encima de otros. Empuja un bloque de hongo sobre otro bloque del mismo tipo y ambos desaparecerán, dándote hongos como recompensa.

Puedes usar `can_push(direction)` para comprobar si se puede empujar el bloque que hay debajo del dron y si hay algo que lo bloquee en la dirección indicada. `push(direction)` empuja el bloque y devuelve si el empujón tuvo éxito.

Los bloques no se pueden empujar hacia arriba, y el empujón fallará si hay otro bloque en medio. Al empujarlos al aire, los bloques caen y aterrizan sobre el siguiente bloque que haya debajo.

Recuerda que puedes llamar a `place(Grounds.Dirt)` para colocar bloques debajo del dron. Esto puede resultar útil para rellenar agujeros y poder empujar bloques por encima de ellos.

---

[Estadísticas](docs/stats.md)      [Sentidos subterráneos](docs/unlocks/underground_senses.md)      [Diccionarios](docs/scripting/dicts.md)

[move()](functions/move)      [measure()](functions/measure)      [can_push()](functions/can_push)      [push()](functions/push)      [place()](functions/place)      [get_ground_type()](functions/get_ground_type)
