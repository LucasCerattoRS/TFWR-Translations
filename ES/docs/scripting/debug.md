[<- Plantar](docs/unlocks/plant.md) <right>[Depuración 2 ->](docs/unlocks/debug2.md)
<right>[Medición de Tiempo ->](docs/unlocks/timing.md)
---
# Depuración
A veces tu código simplemente no funciona y necesitas averiguar por qué. Hay un par de herramientas para ayudarte a hacerlo.

La primera es ejecutar el programa paso a paso. 
Puedes entrar en el modo paso a paso con el botón junto al botón Ejecutar o estableciendo un punto de interrupción.

Los puntos de interrupción se pueden añadir haciendo clic en el panel de puntos de interrupción a la izquierda del código.
![|x227](Breakpoints)
Cuando la ejecución llega a la línea donde está el punto de interrupción, cambiará automáticamente al modo paso a paso.

Cuando mueves el ratón sobre una variable, se muestra su valor actual.

La función `print()` también puede ser muy útil. Escribirá cualquier valor que se le pase directamente en el aire.

Ejemplos:

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
    "operation_ticks": 100,
    "seed": 0,
    "exclude_unlocks": ["watering", "fertilizer"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
#CODE
print(0.24)
}}

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
    "operation_ticks": 100,
    "seed": 0,
    "exclude_unlocks": ["watering", "fertilizer"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
#CODE
print(can_harvest())
}}

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
    "operation_ticks": 100,
    "seed": 0,
    "exclude_unlocks": ["watering", "fertilizer"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
#CODE
print(get_pos_x(), get_pos_y())
}}

La función `print()` imprime el valor directamente en el aire y en la página de [Salida](docs/output.md).

Escribir en el aire a veces puede ser un poco lento si quieres imprimir muchos valores.
En este caso, puedes usar la función `quick_print()`, que imprime solo en la ventana de salida.

La ventana de salida también registra advertencias y errores, por lo que puede ser útil revisarla cuando algo no funciona como esperabas.

Cuando la ejecución se detiene, la salida también se escribe en el archivo [output.txt](persistent_data_path/output.txt) de la carpeta del juego.

---

[Salida](docs/output.md)      [Comentarios](docs/scripting/comments.md)      [Depuración 2](docs/unlocks/debug2.md)      [Bloques de colores](docs/unlocks/debug_place.md)      [Simulación](docs/unlocks/simulation.md)

[print()](functions/print)      [quick_print()](functions/quick_print)
