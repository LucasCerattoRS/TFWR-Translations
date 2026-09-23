[<- Funções](docs/scripting/functions.md)

---

# Escopos de Nomes

Escopos determinam quais variáveis podem ser acessadas e de onde. Um escopo é basicamente um mapeamento de nomes para valores.
Eles funcionam basicamente da mesma forma que em Python.

Existe um escopo global, e cada função tem um escopo local.
Quando você define uma variável, ela é adicionada ao escopo atual.
Qualquer coisa fora de uma definição de função é considerada parte do escopo global.

`x = 1`
Atribui o valor `1` ao nome `x` no escopo global.

Esta declaração `def` atribui uma função ao nome `f` no escopo global.

`def f():
    `Atribui o valor `1` ao nome `y` no escopo local de `f`.`
    y = 1

    `Atribui uma função ao nome `g` no escopo local de `f`.`
    def g():
        pass`

`f()`
Recupera a função armazenada em `f` do escopo global e a chama.

`print(y)`
Esta declaração `print` no escopo global lança um erro porque `y` nunca foi declarado no escopo global, então não podemos lê-lo aqui.
Ele só existia no escopo local de `f`.

## A palavra-chave global

Por padrão, todas as variáveis em funções se vinculam ao escopo local, mesmo que uma variável com o mesmo nome exista no escopo global.

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
x = 0

def f():
    x = 1
f()
print(x)
}}

Este código imprime `0` porque o `x` local dentro de `f` não é a mesma variável que o `x` global, então o `x` global permanece inalterado. Isso é importante porque, caso contrário, uma chamada de função poderia acidentalmente sobrescrever uma variável global que por acaso tem o mesmo nome de uma variável local dessa função.

Se você quiser escrever em uma variável global, deve fazê-lo explicitamente usando a palavra-chave `global`.

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
x = 0

def f():
    global x
    x = 1
f()
print(x)
}}

Neste exemplo, `global x` vincula `x` à variável global `x` definida acima. Isso agora imprimirá `1`.
Note que alterar variáveis globais geralmente é o primeiro passo para o "código espaguete", onde cada parte do programa afeta todas as outras partes do programa, então não abuse.

## Loops e desvios

Loops e desvios não criam seus próprios escopos, então qualquer coisa declarada dentro deles ainda pode ser usada fora.

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
for i in range(3):
    pass
print(i)
}}

Isso imprimirá `2` porque a última iteração do loop `for` atribuiu `2` a `i`.

---

[Variáveis](docs/scripting/variables.md)      [Funções](docs/scripting/functions.md)      [Import](docs/scripting/import.md)      [Megafazenda](docs/unlocks/megafarm.md)
