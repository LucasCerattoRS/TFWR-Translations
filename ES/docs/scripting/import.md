[<- Funciones](docs/scripting/functions.md)
---
# Import
Poner todo tu código en un solo archivo se vuelve inmanejable rápidamente. 
Las sentencias `import` te permiten importar funciones y variables globales de otro archivo.
Cómo funciona en una captura de pantalla:
![|x400](ImportsInOnePicture)

Aquí, `import module2` ejecuta el archivo llamado `module2` y te da acceso a todas sus variables globales.
Luego puedes acceder a las variables y funciones dentro del módulo importado usando el operador `.`.
Así que en este ejemplo, `module2.print_x()` llama a `print_x()` en `module2`.

### No es necesario seguir leyendo

También puedes mover las variables globales del módulo importado al ámbito actual donde se ejecuta la sentencia de importación usando la sintaxis `from`.

`from module2 import print_x
print_x()`
Importa solo las variables globales especificadas de `module2`.

o

`from module2 import *
print_x()`
Importa todas las variables globales de `module2`.

Esto también importa el archivo `module2`, pero, en vez de acceder a él mediante una variable llamada `module2`, desempaqueta las variables globales de `module2` y las asigna directamente en el ámbito local.

Esta forma de importar no suele recomendarse porque no funciona bien cuando dos archivos se importan mutuamente, y podrías sobrescribir accidentalmente variables en el archivo que importa debido a colisiones de nombres. Es más seguro evitar la sintaxis `from` si no sabes lo que estás haciendo.

# Cómo funciona realmente

## En resumen
Las importaciones pueden ser poco intuitivas, pero la mayoría de los problemas se pueden evitar usando la sintaxis `import archivo` en lugar de `from archivo import`, y envolviendo todo lo que no sea una definición global en
`if __name__ == "__main__":`

## Efectos Secundarios de la Importación
La primera vez que importas un archivo, el juego ejecuta todo el archivo y después te da acceso a todas las variables definidas durante esa ejecución.
Si vuelves a importar el mismo archivo, devuelve el módulo almacenado en caché durante la primera importación.

Esto significa que las sentencias de importación pueden tener efectos secundarios. Si importas un archivo que llama a `harvest()`, realmente cosechará durante la importación. Pero cuando lo importes de nuevo, no volverá a cosechar porque el archivo solo se ejecuta una vez.

Hay una forma de evitar tales efectos secundarios usando la variable `__name__`. Esta es una variable que se establece automáticamente a `"__main__"` cuando un archivo se ejecuta directamente, y al nombre del archivo cuando se ejecuta a través de `import`.
Se considera una buena práctica colocar el código que no quieres ejecutar al importar el archivo dentro de un bloque `if __name__ == "__main__":`.

Una estructura de archivo común en Python es poner el código que debe ejecutarse cuando se ejecuta el archivo en una función `main()`. De esta manera tienes una distinción clara entre las variables locales (definidas dentro de `main()`) y las variables globales que se pueden importar (definidas fuera de `main()`).

`una_variable_global = "global"

def main():
    una_variable_local = "local"
    # hacer cosas

if __name__ == "__main__":
    main()`

## Ciclos de Importación
¿Qué pasa si el archivo `a` importa el archivo `b` y el archivo `b` importa el archivo `a`?

archivo `a`:
`import b
x = 0`

archivo `b`:
`import a
def f():
    print(a.x)`

Esto funcionará bien. Digamos que ninguno de los dos archivos está cargado todavía, y alguien más ejecuta `import a`.

- `a` se ejecuta hasta la línea `import b`.
- `b` se ejecuta hasta la línea `import a`.
- El módulo `a` ya existe, pero no contiene `x` porque solo ha llegado hasta la línea `import b`.
- `b` almacena una referencia al módulo `a`, cargado a medias, en una variable llamada `a`.
- `b` ejecuta la instrucción `def` y almacena la función `f()`.
- `a` sigue ejecutándose e inicializa `x`.

Cuando alguien llama a `b.f()`, imprimirá `0` correctamente porque el módulo `a` al que `b` tiene una referencia ya está completamente cargado.

Ahora considera el mismo código usando la sintaxis `from`.

archivo `a`:
`from b import *
x = 0`

archivo `b`:
`from a import *
def f():
    print(x)`

- `a` se ejecuta hasta la línea `from b import *`.
- `b` se ejecuta hasta la línea `from a import *`.
- El módulo `a` ya existe, pero aún no se ha ejecutado por completo.
- `b` desempaqueta todo lo que contiene `a` en ese momento en su propio ámbito global. En este punto, `a` no contiene nada porque todavía no ha llegado a la línea `x = 0`, así que no se importa nada.
- `b` ejecuta la instrucción `def` y almacena la función `f()`.
- `a` sigue ejecutándose e inicializa `x`.

Si ahora alguien llama a `b.f()`, recibirá un error que indica que `x` no existe en el ámbito actual. Esto se debe a que esta vez `b` no tiene una referencia al módulo `a`, que aún se está cargando, y no ve las definiciones añadidas después de la importación.

---

[Funciones](docs/scripting/functions.md)      [Ámbitos de nombres](docs/scripting/scopes.md)
