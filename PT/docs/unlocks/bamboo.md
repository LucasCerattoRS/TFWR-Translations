[<- Arroz](docs/unlocks/rice.md) <right>[Blocos Coloridos ->](docs/unlocks/debug_place.md)
<right>[Pirâmides ->](docs/unlocks/pyramid.md)
---
# Bambu

O bambu pode crescer até 6 blocos de altura. Ele não cresce enquanto houver um drone acima, então use `move` após `plant(Entities.Bamboo)`. Plantar bambu custa arroz.

O bambu floresce ao atingir uma altura escolhida aleatoriamente. Use `measure()` para verificar essa altura. `measure()` começa a contar em 0; se o bambu florescer no segundo bloco, `measure()` retorna 1:

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

Você obterá a produção máxima ao usar `harvest()` com o drone diretamente acima da flor. Para cada bloco de diferença, a produção é dividida por oito.
Por exemplo, se a flor estiver na altura 3 e você colher dois blocos acima, a produção será dividida por 64.

Para colher flores mais altas, voe para dentro do bambu quando o drone estiver na altura desejada. O novo comando `place()` ajuda nisso.

Use `place(Grounds.Dirt)` para empilhar blocos ao lado do bambu e subir. Depois, use `move()` para entrar no bambu pela lateral. O drone deve estar diretamente acima da flor ao chamar `harvest()`.

`place(Grounds.Dirt)` custa 1 bloco! Você também pode colocar outros solos, como `Grounds.Rock`, mas não blocos especiais, como `Grounds.Clay`.

O bambu cresce exatamente 1 bloco por segundo.

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
do_a_flip() # espere um pouco
do_a_flip()
move(West)
harvest()
}}

---

[Estatísticas](docs/stats.md)      [Loop For](docs/scripting/for.md)      [Variáveis](docs/scripting/variables.md)      [If](docs/scripting/if.md)      [Funções](docs/scripting/functions.md)      [Arroz](docs/unlocks/rice.md)

[harvest()](functions/harvest)      [plant()](functions/plant)      [move()](functions/move)      [till()](functions/till)      [place()](functions/place)      [measure()](functions/measure)
