[<- Hierro](docs/unlocks/iron.md)
---
# Mapa del tesoro

Las leyendas hablan de un escurridizo tesoro escondido por un pirata olvidadizo que murió hace mucho... o algo así. ¿Y si trazó en un mapa el camino hacia el tesoro y luego lo perdió? Quizá dejó caer el mapa al verse acorralado por un río de lava y este quedó conservado bajo una capa de basalto. Medir el basalto podría revelar algo.

<spoiler=cuéntame más>
Deberías buscar una capa de `Grounds.Basalt`. Prueba a medir el basalto y comprueba qué te dice. Puede que la pista te lleve hasta el mapa del tesoro, y medir el mapa sin duda te dará el camino hacia el propio tesoro... pero ¿serás capaz de descifrar sus instrucciones?
</spoiler>

<spoiler=dime cómo hacerlo>
Muy bien, esto es lo que hay: encuentra el estrato de `Grounds.Basalt` y el bloque de `Grounds.Treasure_Map` situado justo debajo. Puedes usar `measure()` sobre el basalto para obtener la posición `(x, y)` del bloque del mapa inferior.

Llama a `measure()` sobre el bloque del mapa para obtener el camino del tesoro como una cadena de letras que representan direcciones. N, E, S y W corresponden a `North`, `East`, `South` y `West`, respectivamente, mientras que D significa «Down» o «Dig». Estas letras describen un camino formado por bloques de `Grounds.Treasure_Path` que conduce al tesoro.

```
path = measure()
for letter in path:
    do_something(letter)
```

El dron que excave el bloque del mapa del tesoro es el que tendrá que encontrar el tesoro. Debe permanecer sobre bloques de `Grounds.Treasure_Path` en todo momento. Si se desplaza a otro terreno, el camino se romperá y el tesoro se perderá.

Al final del camino hay un bloque de `Grounds.Treasure_Goal`. Si el dron no se ha desviado del camino, aparecerá un `Entities.Underground_Treasure` encima. El dron puede usar `harvest()` sobre el cofre para recoger su oro.

La cantidad de oro es proporcional a la longitud del camino del tesoro. Mejorar el desbloqueo Mapa del tesoro aumenta la profundidad del camino, mientras que mejorar Expandir le proporciona más espacio para moverse lateralmente. Ambas mejoras aumentan la longitud del camino del tesoro y la cantidad de oro que encontrarás.
</spoiler>

---

[Estadísticas](docs/stats.md)      [Bucle for](docs/scripting/for.md)      [Tuplas](docs/scripting/tuples.md)      [Sentidos subterráneos](docs/unlocks/underground_senses.md)

[harvest()](functions/harvest)      [move()](functions/move)      [dig()](functions/dig)      [measure()](functions/measure)
