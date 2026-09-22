[<- Cactus](docs/unlocks/cactus.md)
---
# Dinosaurios
Los dinosaurios son criaturas antiguas y majestuosas que pueden ser criadas para obtener huesos antiguos.

Por desgracia, los dinosaurios se extinguieron hace mucho tiempo, así que lo mejor que podemos hacer es disfrazarnos de uno.
Para ello, has recibido el nuevo sombrero de dinosaurio.

El sombrero se puede equipar con
`change_hat(Hats.Dinosaur_Hat)`

Por desgracia, no se parece mucho al del anuncio...

Si equipas el sombrero de dinosaurio y tienes suficientes cactus, se comprará automáticamente una [manzana](objects/apple) y se colocará debajo del dron.
Cuando el dron está sobre una manzana y se mueve de nuevo, se comerá la manzana y su cola crecerá en uno. Si puedes permitírtelo, se comprará una nueva manzana y se colocará en una ubicación aleatoria.
La manzana no puede aparecer si hay algo más plantado donde quiere estar.

La cola del dinosaurio se arrastra detrás del dron y llena las casillas por las que este ha pasado. Si el dron intenta moverse sobre su cola, `move()` fallará y devolverá `False`.
El último segmento de la cola se apartará durante un movimiento, así que puedes moverte sobre él. Sin embargo, si la serpiente llena toda la granja, ya no podrás moverte. Por tanto, puedes comprobar si ha crecido por completo comprobando si todavía puedes moverte.
Mientras llevas el sombrero de dinosaurio, el dron no puede moverse por el borde de la granja para llegar al otro lado.

Usar `measure()` en una manzana devolverá la posición de la siguiente manzana como una tupla.

`next_x, next_y = measure()`

{{codeexample 
{
    "camera_position": {"x": -1, "y": 2.4, "z": 5},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": true,
    "collapsing": true,
    "autoplay": false,
    "items": [{"item": "cactus", "n": 10000}],
    "world_size": {"x": 4, "y": 4},
    "execution_speed": 2,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 1,
    "seed": 5,
    "exclude_unlocks": ["watering"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
#CODE
change_hat(Hats.Dinosaur_Hat)
while True:
    next_x, next_y = measure()
    while get_pos_x() != next_x:
        move(East)
    while get_pos_y() != next_y:
        move(North)
}}

Cuando se vuelve a quitar el sombrero equipando uno diferente, la cola se cosechará.
Recibirás una cantidad de huesos igual al cuadrado de la longitud de la cola. Para una cola de longitud `n`, recibirás `n**2` `Items.Bone`.
Por ejemplo:
longitud 1 => 1 hueso
longitud 2 => 4 huesos
longitud 3 => 9 huesos
longitud 4 => 16 huesos
longitud 16 => 256 huesos
longitud 100 => 10000 huesos

El Sombrero de Dinosaurio es muy pesado, así que si lo equipas, hará que `move()` tarde 400 ticks en lugar de 200. Sin embargo, cada vez que recoges una manzana, el número de ticks utilizados por `move()` se reduce en un 3% (redondeado hacia abajo), porque una cola más larga puede ayudarte a moverte.

El siguiente bucle imprime el número de ticks utilizados por `move()` después de cualquier número de manzanas:

{{codeexample 
{
    "show_image": false,
    "show_code": true,
    "show_inventory": false,
    "show_output": true,
    "collapsing": true,
    "autoplay": false,
    "execution_speed": 1,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 1,
    "seed": 1,
    "exclude_unlocks": ["watering", "fertilizer"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
#CODE
ticks = 400
for i in range(100):
    quick_print("ticks después de ", i, " manzanas: ", ticks)
    ticks -= ticks * 0.03 // 1
}}

Solo tienes un sombrero de dinosaurio, así que solo un dron puede llevarlo.

<spoiler=mostrar pista 1>
Si sigues moviéndote por el mismo camino que cubre todo el campo, podrás conseguir fácilmente una serpiente que cubra el campo entero cada vez. No es muy eficiente, pero funciona.
Recorrer por completo una granja muy grande puede llevar mucho tiempo y quizá no necesites tantos huesos. Puedes usar `set_world_size()` para cambiar el tamaño de la granja por otro más práctico.</spoiler>

---

[Estadísticas](docs/stats.md)      [Tuplas](docs/scripting/tuples.md)      [Listas](docs/scripting/lists.md)

[change_hat()](functions/change_hat)      [move()](functions/move)      [measure()](functions/measure)
