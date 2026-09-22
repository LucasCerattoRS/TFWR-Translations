[<- Para empezar](docs/getting_started.md) <right>[Bucle while ->](docs/scripting/while.md)
---
# Primer Programa
## Editor de texto
Toda la programación se realiza en ventanas de código. Cada ventana de código corresponde a un archivo de texto que contiene código. 
Puedes renombrar el archivo haciendo clic en su nombre en la parte superior de la ventana.

El código se puede editar como en cualquier editor de texto siempre que no se esté ejecutando.
Puedes ejecutar el programa directamente presionando el botón de reproducción verde en la ventana de código.
![|x50](PlayButton)

Puedes crear más archivos de código usando el botón "+" en la esquina superior derecha de la pantalla.
Puedes acoplar una ventana a otra arrastrándola sobre ella.

Notarás que una vez que empieces a escribir, aparecerá una simple ventana de autocompletado de código.
Presiona Tab para insertar la opción seleccionada.
Usa las teclas de flecha para navegar por las opciones de autocompletado.

No te preocupes si es tu primera vez programando. El lenguaje se desbloquea paso a paso, por lo que no te sentirás abrumado por todas las cosas que puedes hacer. 
La sintaxis también es similar a Python, uno de los lenguajes de programación más utilizados del mundo, así que lo que aprendas aquí te será útil en otros sitios.

Si ya sabes Python, tampoco es un problema: podrás avanzar rápidamente por la primera parte del juego y llegar a las cosas más interesantes.

Actualmente, hay dos comandos de dron disponibles.

`harvest()`

y 

`do_a_flip()`

Estas son llamadas a funciones. Puedes pensar en una función como un comando que se puede ejecutar. Los paréntesis `()` la ejecutan.

Intenta escribir estas instrucciones en la ventana de código y presiona el botón de ejecutar.

Puedes pensar en tu código como una secuencia de instrucciones. Puedes ejecutar varias instrucciones seguidas colocándolas en líneas distintas.
Prueba a pulsar el botón de reproducción de esta ventana de código integrada para ver cómo se ejecuta el código:

{{codeexample 
{
    "camera_position": {"x": 0, "y": 1.5, "z": 4},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": false,
    "collapsing": true,
    "autoplay": false,
    "items": [],
    "world_size": {"x": 1, "y": 1},
    "execution_speed": 1,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 200,
    "seed": 1,
    "exclude_unlocks": ["watering", "fertilizer"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
#CODE
do_a_flip()
harvest()
harvest()
}}

## Desbloqueos
Recolectar hierba te dará heno. El heno se puede usar para desbloquear bucles en el árbol tecnológico. Abre el árbol tecnológico con el botón de la esquina superior derecha de la pantalla.

---

[Editor externo](docs/external_editor.md)      [Comentarios](docs/scripting/comments.md)      [Bucle while](docs/scripting/while.md)

[harvest()](functions/harvest)      [do_a_flip()](functions/do_a_flip)
