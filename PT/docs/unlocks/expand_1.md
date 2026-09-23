[<- Melhoria de Velocidade](docs/unlocks/speed.md) <right>[Expansão 2 ->](docs/unlocks/expand_2.md)

<right>[Mineração ->](docs/unlocks/mining.md)

---

# Expansão 1

Sua fazenda cresceu! Esse espaço não serve para muita coisa se você não puder mover o drone, então há uma nova função `move()` que o movimenta. `move()` exige que você especifique a direção para a qual quer mover o drone. Há quatro novas constantes para isso: `North, East, South, West`

Por exemplo, `move(North)` moverá o drone um quadrado para o norte.

Se você atravessar a borda da fazenda, o drone reaparecerá do outro lado.

{{codeexample 
{
    "camera_position": {"x": 0, "y": 1.8, "z": 5},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": false,
    "collapsing": true,
    "autoplay": false,
    "items": [],
    "world_size": {"x": 1, "y": 3},
    "execution_speed": 2,
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
while True:
	move(North)
}}

---

[Loop While](docs/scripting/while.md)      [Operadores](docs/scripting/operators.md)      [Expansão 2](docs/unlocks/expand_2.md)

[move()](functions/move)
