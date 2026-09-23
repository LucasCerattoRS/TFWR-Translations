[<- Arroz](docs/unlocks/rice.md) <right>[Bloques de colores ->](docs/unlocks/debug_place.md)
<right>[Pirámides ->](docs/unlocks/pyramid.md)
---
# Bambú

El bambú es una planta que puede crecer hasta 6 bloques de altura. No crecerá mientras haya un dron encima, así que asegúrate de usar `move` para apartarlo después de llamar a `plant(Entities.Bamboo)`. Plantar bambú cuesta arroz.

El bambú produce flores cuando alcanza una altura determinada al azar. Usa `measure()` para comprobar a qué altura florecerá. `measure()` empieza a contar desde 0, así que, si el bambú florece en el segundo bloque, `measure()` devuelve 1:

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

Obtendrás el máximo rendimiento del bambú si usas `harvest()` cuando tu dron esté justo encima de la flor. Por cada bloque de diferencia, el rendimiento se dividirá entre ocho.
Por ejemplo, si la flor está a una altura de 3 pero la cosechas dos bloques más arriba, el rendimiento se dividirá entre 64.

Para cosechar flores que estén más arriba, vuela hacia el bambú cuando el dron se encuentre a la altura deseada. El comando `place()` que acabas de desbloquear te ayudará a hacerlo.

Usa `place(Grounds.Dirt)` para apilar bloques junto al bambú y subir. Después, usa `move()` para entrar en el bambú desde un lado. Tu dron debe estar justo encima de la flor cuando llames a `harvest()`.

¡`place(Grounds.Dirt)` cuesta 1 bloque! También puedes colocar otros terrenos, como `Grounds.Rock`, pero no bloques especiales, como `Grounds.Clay`.

El bambú crece exactamente 1 bloque por segundo.

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
do_a_flip() # espera un poco
do_a_flip()
move(West)
harvest()
}}

---

[Estadísticas](docs/stats.md)      [Bucle for](docs/scripting/for.md)      [Variables](docs/scripting/variables.md)      [If](docs/scripting/if.md)      [Funciones](docs/scripting/functions.md)      [Arroz](docs/unlocks/rice.md)

[harvest()](functions/harvest)      [plant()](functions/plant)      [move()](functions/move)      [till()](functions/till)      [place()](functions/place)      [measure()](functions/measure)
