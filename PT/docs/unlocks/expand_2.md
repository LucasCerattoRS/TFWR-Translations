[<- Expansão 1](docs/unlocks/expand_1.md)

---

# Expansão 2

Sua fazenda expandiu novamente! Agora as casas não estão mais em uma bela fila, então você precisa encontrar uma maneira de percorrer uma grade quadrada.

Com o loop `while` isso não é possível até que você desbloqueie sensores e operadores.
É hora de apresentar o loop `for`.

Você pode ler tudo sobre o loop `for` na página [Loop For](docs/scripting/for.md), mas por enquanto você só precisará dele para repetir código um número fixo de vezes.

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
    "operation_ticks": 100,
    "seed": 1,
    "exclude_unlocks": ["watering", "fertilizer"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
#CODE
for i in range(5):
	do_a_flip()
}}

`range(n)` cria uma sequência de `n` números de `0` a `n - 1`. O loop `for` executa seu corpo uma vez para cada elemento da sequência. Neste exemplo, `do_a_flip()` será chamado `5` vezes.

A função `get_world_size()` também está disponível agora. Ela retorna o comprimento do lado da sua fazenda. Desta forma, você pode escrever código que não quebrará com a próxima melhoria de expansão.

{{codeexample 
{
    "camera_position": {"x": -1, "y": 1.8, "z": 5},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": false,
    "collapsing": true,
    "autoplay": false,
    "items": [],
    "world_size": {"x": 3, "y": 3},
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
do_a_flip()
#CODE
for i in range(get_world_size()):
	harvest()
	move(North)
}}

Este exemplo colhe uma coluna da fazenda para qualquer tamanho de fazenda.

Se você não consegue descobrir como mover o drone pela fazenda, veja a dica abaixo.
<spoiler=mostrar dica>É claro que há várias maneiras de se mover pela fazenda.
Estamos procurando uma forma sistemática de percorrê-la que não pare de funcionar quando a fazenda crescer novamente.
Uma forma sistemática de chegar a todos os lugares da fazenda seria repetir estes dois passos para sempre:

1. Mover para `North` até o drone reaparecer do outro lado.

2. Mover para `East`.

`for i in range(get_world_size()):` pode ajudar a transformar essa ideia em código.
</spoiler>
<spoiler=mostrar possível solução>

{{codeexample 
{
    "camera_position": {"x": -1, "y": 1.8, "z": 5},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": false,
    "collapsing": true,
    "autoplay": false,
    "items": [],
    "world_size": {"x": 3, "y": 3},
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
do_a_flip()
#CODE
for i in range(get_world_size()):
	for j in range(get_world_size()):
		#dê uma cambalhota em cada quadrado
		do_a_flip()
		move(North)
	move(East)
}}

</spoiler>

---

[Loop For](docs/scripting/for.md)      [Loop While](docs/scripting/while.md)      [Variáveis](docs/scripting/variables.md)

[move()](functions/move)      [get_world_size()](functions/get_world_size)
