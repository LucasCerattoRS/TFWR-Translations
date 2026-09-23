[<- Plantar](docs/unlocks/plant.md) <right>[Depuração 2 ->](docs/unlocks/debug2.md)

<right>[Medição de Tempo ->](docs/unlocks/timing.md)

---

# Depuração

Às vezes, seu código simplesmente não funciona e você precisa descobrir o porquê. Existem algumas ferramentas para ajudá-lo com isso.

A primeira é executar o programa passo a passo. 
Você pode entrar no modo passo a passo com o botão ao lado do botão Executar ou definindo um ponto de interrupção.

Pontos de interrupção podem ser adicionados clicando no painel à esquerda do código.
![|x227](Breakpoints)
Quando a execução chegar à linha do ponto de interrupção, ela mudará automaticamente para o modo passo a passo.

Quando você move o mouse sobre uma variável, seu valor atual é exibido.

A função `print()` também pode ser muito útil. Ela escreverá qualquer valor passado para ela diretamente no ar.

Exemplos:

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
print(0.24)
}}

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
print(can_harvest())
}}

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
print(get_pos_x(), get_pos_y())
}}

A função `print()` imprime o valor diretamente no ar e na página [Saída](docs/output.md).

Escrever no ar pode ser um pouco lento quando você quer imprimir muitos valores.
Nesse caso, use a função `quick_print()`, que imprime apenas na janela de saída.

A janela de saída também registra avisos e erros, por isso vale a pena consultá-la quando algo não funcionar como esperado.

Quando a execução para, a saída também é gravada no arquivo [output.txt](persistent_data_path/output.txt) da pasta do jogo.

---

[Saída](docs/output.md)      [Comentários](docs/scripting/comments.md)      [Depuração 2](docs/unlocks/debug2.md)      [Blocos Coloridos](docs/unlocks/debug_place.md)      [Simulação](docs/unlocks/simulation.md)

[print()](functions/print)      [quick_print()](functions/quick_print)
