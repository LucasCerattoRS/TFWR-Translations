[<- Quartzo](docs/unlocks/quartz.md) <right>[Dinamite ->](docs/unlocks/dynamite.md)
---
# Cogumelo

Muitos tipos de cogumelo crescem em colônias no subsolo. Procure um estrato de `Grounds.Mushroom` ao escavar. Depois, use `measure()` no solo para obter o tipo de cogumelo como um número a partir de `0`.

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

Cogumelos do mesmo tipo gostam de ficar juntos, mas são tímidos demais para crescer uns sobre os outros. Empurre um bloco de cogumelo sobre outro do mesmo tipo; ambos desaparecerão e renderão cogumelos como recompensa.

Use `can_push(direction)` para verificar se o bloco sob o drone pode ser empurrado e se há algo bloqueando a direção. `push(direction)` empurra o bloco e informa se a ação foi bem-sucedida.

Blocos não podem ser empurrados para cima, e o empurrão falha se houver outro bloco no caminho. Quando empurrados para o ar, eles caem e pousam no próximo bloco abaixo.

Lembre-se de que você pode chamar `place(Grounds.Dirt)` para colocar blocos sob o drone. Isso ajuda a preencher buracos e empurrar blocos por cima deles.

---

[Estatísticas](docs/stats.md)      [Sentidos Subterrâneos](docs/unlocks/underground_senses.md)      [Dicionários](docs/scripting/dicts.md)

[move()](functions/move)      [measure()](functions/measure)      [can_push()](functions/can_push)      [push()](functions/push)      [place()](functions/place)      [get_ground_type()](functions/get_ground_type)

