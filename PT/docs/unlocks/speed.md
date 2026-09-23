[<- Loop While](docs/scripting/while.md) <right>[Expansão 1 ->](docs/unlocks/expand_1.md)

<right>[Plantar ->](docs/unlocks/plant.md)

---

# Melhoria de Velocidade

A velocidade de execução dobrou. O problema é que agora o drone colhe mais rápido do que a grama consegue crescer, o que não gera rendimento algum. Para lidar com isso, agora estão desbloqueados os desvios [if](docs/scripting/if.md) e a função [can_harvest()](functions/can_harvest).

## Verificando Antes de Colher

Uma instrução `if` executa seu bloco de código uma vez se a condição fornecida for `True`.

A nova função `can_harvest()` fornece uma condição útil. `can_harvest()` retorna `True` se a planta sob o drone puder ser colhida e `False` caso contrário.

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
do_a_flip()
#CODE
if can_harvest():
	do_a_flip()
}}

Você pode entender um valor de retorno como se a expressão de chamada da função `can_harvest()` fosse substituída pelo valor retornado `True` durante a avaliação do `if`.

O que acontece quando o código acima é executado:

- A instrução `if` é executada.

- `can_harvest()` é chamada.

- `can_harvest()` retorna `True` porque a grama está totalmente crescida.

- Agora a instrução é `if True:`.

- O desvio é executado porque o valor é `True`.

Se a grama não estivesse totalmente crescida, o drone não daria uma cambalhota.

Agora podemos usar `if` para impedir que o drone colha cedo demais.

---

[If](docs/scripting/if.md)      [Loop While](docs/scripting/while.md)

[harvest()](functions/harvest)      [can_harvest()](functions/can_harvest)
