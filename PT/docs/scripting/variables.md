[<- Operadores](docs/scripting/operators.md) <right>[Listas ->](docs/scripting/lists.md)

<right>[Funções ->](docs/scripting/functions.md)

---

# Variáveis

Variáveis podem ser pensadas como recipientes nomeados que podem conter um valor.
O operador `=` é usado para declarar uma variável e armazenar um valor nela.

`nome_da_variavel = valor`

O lado esquerdo do operador é o nome da variável. Você pode dar qualquer nome válido que quiser.
O lado direito é uma expressão cujo valor resultante será armazenado na variável.

Declare uma variável chamada `a` e armazene o valor `5` nela:
`a = 5`
Declare uma variável chamada `b` e armazene o valor de retorno de `can_harvest()` nela:
`b = can_harvest()`

Não confunda o operador `=` com o operador `==`. 
O operador `==` verifica se dois valores são iguais e retorna `True` ou `False`.
O operador `=` atribui o valor à direita ao nome à esquerda.

Depois que uma variável foi atribuída, você pode usá-la no código para recuperar o valor que ela contém

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
a = 5
for i in range(a):
	do_a_flip()
}}

O loop acima é executado 5 vezes porque `a` está definido como `5`.
O `i` no loop `for` também é uma variável que recebe automaticamente o valor atual da sequência a cada iteração do loop. (Não precisa ser chamado de `i`, você pode dar qualquer nome de variável válido.)

Variáveis também permitem que você faça a mesma coisa com um loop while:

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
a = 5
i = 0
while i < a:
	do_a_flip()
	i = i + 1
}}

Isso faz a mesma coisa que o loop `for` acima. Nós apenas temos que incrementar `i` manualmente.
Note que, para incrementar `i`, nós o definimos como seu próprio valor mais `1`. Mudar o valor de uma variável com base em seu valor anterior é algo muito comum. 
Isso pode ser abreviado usando estes operadores: `+=, -=, *=, /=, %=`

`i = i + 1` é o mesmo que `i += 1`
`a = a / 3` é o mesmo que `a /= 3`

---

[Operadores](docs/scripting/operators.md)      [Loop While](docs/scripting/while.md)      [Loop For](docs/scripting/for.md)      [Funções](docs/scripting/functions.md)      [Escopos de Nomes](docs/scripting/scopes.md)
