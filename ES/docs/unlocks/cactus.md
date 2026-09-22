[<- Calabazas](docs/unlocks/pumpkins.md) <right>[Dinosaurios ->](docs/unlocks/dinosaurs.md)
---
# Cactus
Como otras plantas, los [cactus](objects/cactus) pueden cultivarse en tierra y cosecharse como de costumbre.

Sin embargo, vienen en varios tamaños y tienen un extraño sentido del orden.

Si cosechas un cactus completamente crecido y todos los cactus vecinos están en orden, también cosechará todos los cactus vecinos de forma recursiva.

Se considera que un cactus está ordenado si todos los cactus vecinos al `North` y al `East` han crecido por completo y tienen un tamaño mayor o igual, mientras que todos los cactus vecinos al `South` y al `West` han crecido por completo y tienen un tamaño menor o igual.

La cosecha solo se propagará si todos los cactus adyacentes están completamente crecidos y en orden.
Esto significa que si un cuadrado de cactus crecidos está ordenado por tamaño y cosechas un cactus, se cosechará todo el cuadrado.

Un cactus completamente crecido aparecerá marrón si no está ordenado. Una vez ordenado, se volverá verde de nuevo.

Recibirás una cantidad de cactus igual al cuadrado del número de cactus cosechados. Si cosechas `n` cactus a la vez, recibirás `n**2` `Items.Cactus`.

El tamaño de un cactus se puede medir con `measure()`.
Siempre es uno de estos números: `0,1,2,3,4,5,6,7,8,9`.

También puedes pasar una dirección a `measure(direction)` para medir la casilla vecina en esa dirección del dron.

Puedes intercambiar un cactus con su vecino en cualquier dirección usando el comando `swap()`.
`swap(direction)` intercambia el objeto debajo del dron con el objeto a una casilla de distancia en la `direction` del dron.

{{codeexample 
{
    "camera_position": {"x": -1.5, "y": 2.4, "z": 5},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": true,
    "collapsing": true,
    "autoplay": false,
    "items": [{"item": "pumpkin", "n": 32}],
    "world_size": {"x": 4, "y": 4},
    "execution_speed": 1,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 100,
    "seed": 1,
    "exclude_unlocks": ["fertilizer", "watering"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
for _ in range(4):
    for _ in range(4):
        till()
        plant(Entities.Cactus)
        move(East)
    move(North)
for _ in range(4):
    for _ in range(4):
        for _ in range(4):
            x,y = get_pos_x(), get_pos_y()
            if x > 0 and measure(West) > measure():
                swap(West)
            if y > 0 and measure(South) > measure():
                swap(South)
            if x < 3 and measure(East) < measure():
                swap(East)
            if y < 3 and measure(North) < measure():
                swap(North)
            move(East)
        move(North)
move(East)
move(North)
move(North)
swap(West)
swap(South)
swap(East)
swap(North)
#CODE
swap(North)
swap(East)
swap(South)
swap(West)
harvest()
}}

## Ejemplos numéricos
En cada una de estas cuadrículas, todos los cactus están ordenados y la cosecha se extenderá por todo el campo:
`3 4 5    3 3 3    1 2 3    1 5 9
2 3 4    2 2 2    1 2 3    1 3 8
1 2 3    1 1 1    1 2 3    1 3 4`

En esta cuadrícula, solo el cactus inferior izquierdo está ordenado, lo que no es suficiente para que se propague:
`1 5 3
4 9 7
3 3 2`

<spoiler=mostrar pista 1>
Si cada fila ya está ordenada por separado, ordenar cada columna por separado no desordenará las filas.
</spoiler>
<spoiler=mostrar pista 2>
Existen muchos algoritmos de ordenación conocidos e ingeniosos. Si no los conoces, quizá te interese investigarlos y pensar cuáles se podrían adaptar a este problema. Ten en cuenta que no todos funcionan aquí, porque solo puedes intercambiar cactus vecinos.
</spoiler>
<spoiler=mostrar pista 3>
La «ordenación de burbuja» es posiblemente el algoritmo de ordenación más sencillo. La idea consiste en recorrer repetidamente los elementos e intercambiar los elementos adyacentes que estén en el orden incorrecto hasta que no quede ninguno.

Este es su aspecto aplicado a los cactus:
{{codeexample 
{
    "camera_position": {"x": -4, "y": 1, "z": 6},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": false,
    "show_inventory": true,
    "show_output": false,
    "collapsing": false,
    "autoplay": true,
    "items": [{"item": "pumpkin", "n": 18}],
    "world_size": {"x": 9, "y": 1},
    "execution_speed": 2,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 1,
    "seed": 1,
    "exclude_unlocks": ["fertilizer", "watering"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
#CODE
for _ in range(9):
    till()
    plant(Entities.Cactus)
    move(East)
sorted = False
while not sorted:
    sorted = True
    for _ in range(9):
        move(East)
        if get_pos_x() > 0 and measure(West) > measure():
            swap(West)
            sorted = False
harvest()
}}
¡Por supuesto, hay muchas formas de mejorar esta estrategia!
Cuando consigas ordenar una sola fila, puedes usar la pista 1 para ordenar todo el campo.
</spoiler>

---

[Estadísticas](docs/stats.md)

[harvest()](functions/harvest)      [plant()](functions/plant)      [move()](functions/move)      [till()](functions/till)      [swap()](functions/swap)      [measure()](functions/measure)
