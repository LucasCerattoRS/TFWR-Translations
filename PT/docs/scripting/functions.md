[<- Variáveis](docs/scripting/variables.md) <right>[Import ->](docs/scripting/import.md)

---

# Funções

Use a palavra-chave `def` para definir uma nova função:

`def f(arg1, arg2 = False):
	#código da função`

Você pode usar o operador de chamada `()` para chamar a função:
`f(42)`

Veja também [Escopos](docs/scripting/scopes.md) para aprender sobre variáveis locais e globais em funções.

## Introdução

Você já viu funções internas como `harvest()`.
Você também pode definir suas próprias funções, o que permite estruturar seu código de forma modular. Uma função dá um nome a um bloco de código para que você possa chamá-lo sempre que precisar.

## Definições de Funções

Por exemplo, você poderia definir uma função que move o drone várias vezes.

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
def move_n_dir(n, dir):
	for i in range(n):
		move(dir)
}}

A palavra-chave `def` indica que esta é uma definição de função. 
`move_n_dir` é o nome ao qual a função será vinculada. Pode ser qualquer nome de variável válido e será usado para chamar a função.
`n` e `dir` são parâmetros. Eles são variáveis que armazenam os valores passados para a função; esses valores também são chamados de argumentos. Você pode adicionar quantos parâmetros quiser a uma definição de função.
Depois de `:` vem o bloco de código que será executado quando a função for chamada.

O código a seguir move o drone `2` quadrados para `North` e `2` quadrados para `East`.

{{codeexample 
{
    "camera_position": {"x": -1, "y": 1.8, "z": 5},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": true,
    "collapsing": true,
    "autoplay": false,
    "items": [],
    "world_size": {"x": 3, "y": 3},
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
def move_n_dir(n, dir):
	for i in range(n):
		move(dir)

move_n_dir(2, North)
move_n_dir(2, East)
}}

Quando você vir `def function():`, pense nisso como uma atribuição de variável deste tipo:
`function = create_new_function_object()`
Como em qualquer atribuição, você não pode usar a variável antes que um valor seja atribuído a ela!
A instrução `def` precisa ser executada antes de qualquer chamada da função.
Este código causará um erro:

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
func()
def func():
	pass
}}

## Valores de Retorno

Use a palavra-chave `return` para fazer uma função retornar um valor. 
Por exemplo, a função a seguir define a operação OU exclusivo. O OU exclusivo retorna `True` quando um valor é `True` e o outro é `False`:

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
#CODE
def xor(a, b):
	return a != b

if xor(True, False):
	do_a_flip()
}}

[Tuplas](docs/scripting/tuples.md) permitem retornar múltiplos valores.

## Argumentos Padrão

Você também pode atribuir valores padrão, que serão usados quando os argumentos correspondentes forem omitidos.

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
#CODE
def f(a = False):
	if a:
		do_a_flip()

f()

f(True)
}}

Um argumento que tem um valor padrão não pode ser seguido por um argumento que não tem um valor padrão.

## Uso Avançado de Funções

Funções são valores como qualquer outro valor, e a declaração `def` age como uma declaração de atribuição, atribuindo a função a qualquer nome que você lhe der.
Isso permite fazer coisas como esta:

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
#CODE
def f():
	def d():
		do_a_flip()
	return d

f()()
}}

Aqui, `f()` chama a função `f`, que define e retorna uma nova função, `d`. O segundo `()` executa a função retornada e dá uma cambalhota.
(Fazer esse tipo de coisa geralmente não é uma boa ideia, porque fica difícil entender o que está acontecendo.)

Funções que recebem outras funções como argumentos permitem que você seja realmente criativo:

{{codeexample 
{
    "camera_position": {"x": -2, "y": 1.5, "z": 4},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": true,
    "collapsing": true,
    "autoplay": false,
    "items": [{"item": "fertilizer", "n": 4}],
    "world_size": {"x": 5, "y": 1},
    "execution_speed": 1,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 100,
    "seed": 1,
    "exclude_unlocks": ["watering"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
#CODE
def f(g, arg):
	for _ in range(4):
		g(arg)

f(move, East)
plant(Entities.Tree)
f(use_item, Items.Fertilizer)
}}

---

[Variáveis](docs/scripting/variables.md)      [Escopos de Nomes](docs/scripting/scopes.md)      [Tuplas](docs/scripting/tuples.md)      [Import](docs/scripting/import.md)
