[<- Começando](docs/getting_started.md) <right>[Loop While ->](docs/scripting/while.md)

---

# Primeiro Programa

## Editor de texto

Toda a programação é feita em janelas de código. Cada janela de código corresponde a um arquivo de texto contendo código. 
Você pode renomear o arquivo clicando em seu nome no topo da janela.

O código pode ser editado como em qualquer editor de texto, desde que não esteja em execução.
Você pode executar o programa diretamente pressionando o botão de play verde na janela de código.
![|x50](PlayButton)

Você pode criar mais arquivos de código usando o botão "+" no canto superior direito da tela.
Você pode acoplar uma janela a outra arrastando-a sobre ela.

Você notará que, assim que começar a digitar, uma janela simples de autocompletar aparecerá.
Pressione Tab para inserir o autocompletar selecionado.
Use as setas para navegar pelas opções de autocompletar.

Não se preocupe se esta é sua primeira vez programando. A linguagem é desbloqueada passo a passo, então você não ficará sobrecarregado com todas as coisas que pode fazer. 
A sintaxe também é semelhante à do Python, uma das linguagens de programação mais usadas no mundo, então o que você aprender aqui será útil em outros lugares.

Se você já conhece Python, também não há problema, você poderá passar rapidamente pelo início do jogo para chegar às coisas mais interessantes.

Atualmente, existem dois comandos de drone disponíveis.

`harvest()`

e 

`do_a_flip()`

Estas são chamadas de função. Você pode pensar em uma função como um comando que pode ser executado. Você o executa usando os parênteses `()`.

Tente digitar essas instruções na janela de código e pressionar o botão de execução.

Você pode pensar no seu código como uma sequência de instruções. Você pode executar várias instruções seguidas colocando-as em várias linhas. 
Experimente pressionar o botão de reprodução nesta janela de código incorporada para ver como o código é executado:

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
    "operation_ticks": 200,
    "seed": 1,
    "exclude_unlocks": ["watering", "fertilizer"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
#CODE
do_a_flip()
harvest()
harvest()
}}

## Desbloqueios

Coletar grama dá feno. O feno pode ser usado para desbloquear loops na árvore de tecnologias. Abra a árvore de tecnologias com o botão no canto superior direito da tela.

---

[Editor Externo](docs/external_editor.md)      [Comentários](docs/scripting/comments.md)      [Loop While](docs/scripting/while.md)

[harvest()](functions/harvest)      [do_a_flip()](functions/do_a_flip)
