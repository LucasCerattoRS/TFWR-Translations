[<- Hierro](docs/unlocks/iron.md)
---
# Prospección de hierro

Puede que hayas notado que a veces cuesta encontrar vetas de hierro. Podrías excavar por todas partes y confiar en encontrarlas por casualidad, pero hay una forma mejor: como el hierro es magnético, podemos detectarlo desde lejos.

El comando `prospect_iron()` sirve precisamente para eso. `prospect_iron()` devuelve la dirección cardinal (`North`, `East`, `South` o `West`) en la que tendría que moverse el dron para dar un paso hacia el mineral de hierro más cercano. Ejecutar el comando cuesta 1 carbón.

`prospect_iron()` devuelve `None` si el dron ya está justo encima del mineral de hierro más cercano, si no tienes suficiente carbón para ejecutar el comando o si no hay hierro dentro del alcance.

Puedes usar el siguiente código para acercarte un paso al siguiente mineral de hierro:

`if prospect_iron() != None:
    move(prospect_iron())
`

Quizá te convenga optimizar este código con una variable, porque ahora llama dos veces a `prospect_iron()` y cuesta 2 de carbón.

La distancia al mineral de hierro más cercano se calcula según el número de pasos que debe dar el dron. Si hay mineral de hierro 2 bloques al este y 3 bloques al norte del dron, se considera que está a una distancia de 5, porque el dron necesitaría cinco pasos para llegar hasta allí.

Excavar también cuenta como un paso. Así que, si además el hierro está enterrado 7 bloques bajo tierra, se considera que está a una distancia de 12, porque el dron necesitaría cinco pasos para colocarse encima del hierro y después siete excavaciones para alcanzarlo.

---

[Hierro](docs/unlocks/iron.md)      [Sentidos subterráneos](docs/unlocks/underground_senses.md)

[move()](functions/move)      [dig()](functions/dig)      [prospect_iron()](functions/prospect_iron)
