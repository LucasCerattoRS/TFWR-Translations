[<- Expansão 2](docs/unlocks/expand_2.md)

---

# Loop For

O loop `for` funciona como no Python. Em algumas linguagens, ele é chamado de loop foreach e não deve ser confundido com o loop for ao estilo de C, que funciona de outra forma.

`for i in sequence:
	#faça algo com i`

Semelhante ao loop `while`, o loop `for` também chama repetidamente um bloco de código. Em vez de fazer um loop com base em uma condição, ele executa o corpo do loop uma vez para cada elemento em uma sequência.

## Sintaxe

Um loop for se parece com isto:

`for variable_name in sequence:
	#bloco de código`

`variable_name` pode ser qualquer nome que você escolher. É uma variável que armazena o elemento atual da sequência. `sequence` deve ser um valor iterável, como um intervalo de números. O bloco de código é executado uma vez para cada elemento, com esse elemento atribuído à variável do loop.

## Sequências

[Ranges](functions/range)      <unlock=lists>[Listas](docs/scripting/lists.md)      </unlock><unlock=functions>[Tuplas](docs/scripting/tuples.md)      </unlock><unlock=dicts>[Dicionários](docs/scripting/dicts.md)      </unlock><unlock=sets>[Conjuntos](docs/scripting/sets.md)</unlock>

## Exemplo

{{codeexample 
{
    "camera_position": {"x": 0, "y": 1.5, "z": 4},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": true,
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
do_a_flip()
#CODE
for i in range(5):
    harvest()
}}

Este loop executa o corpo um número fixo de vezes. É essencialmente o mesmo que escrever

{{codeexample 
{
    "camera_position": {"x": 0, "y": 1.5, "z": 4},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": true,
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
do_a_flip()
#CODE
i = 0
harvest()
i = 1
harvest()
i = 2
harvest()
i = 3
harvest()
i = 4
harvest()
}}

---

[Loop While](docs/scripting/while.md)      [Break](docs/scripting/break.md)      [Continue](docs/scripting/continue.md)

[range()](functions/range)
