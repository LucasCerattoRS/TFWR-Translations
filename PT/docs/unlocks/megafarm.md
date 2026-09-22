[<- Labirintos](docs/unlocks/mazes.md)

---

# Megafazenda

Este desbloqueio incrivelmente poderoso lhe dá acesso a vários drones. 

{{codeexample 
{
    "camera_position": {"x": -3, "y": 2.1, "z": 7},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": false,
    "show_inventory": true,
    "show_output": true,
    "collapsing": false,
    "autoplay": true,
    "items": [],
    "world_size": {"x": 7, "y": 7},
    "execution_speed": 21,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 1,
    "seed": 1,
    "exclude_unlocks": ["fertilizer", "watering"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
move(North)
move(North)
move(North)
move(East)
move(East)
move(East)
change_hat(Hats.Wizard_Hat)
#CODE
def harvest_spiral(radius):
    for i in range(1, radius, 2):
        harvest()
        move(West)
        for j in range(i):
            harvest()
            move(South)
        for j in range(i+1):
            harvest()
            move(East)
        for j in range(i+1):
            harvest()
            move(North)
        for j in range(i+1):
            harvest()
            move(West)

while True:
    spawn_drone(harvest_spiral, 7)
    do_a_flip()
}}

Como antes, você ainda começa com apenas um drone. Drones adicionais devem primeiro ser gerados e desaparecerão após o término do programa.
Cada drone executa seu próprio programa separado. Novos drones podem ser gerados usando a função `spawn_drone(function)`.

{{codeexample 
{
    "camera_position": {"x": -0.5, "y": 1.5, "z": 4},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": false,
    "collapsing": true,
    "autoplay": false,
    "items": [],
    "world_size": {"x": 2, "y": 1},
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
def drone_function():
    move(East)
    do_a_flip()

spawn_drone(drone_function)
do_a_flip()
}}

Isso cria um novo drone na mesma posição do drone que executou o comando `spawn_drone(function)`. O novo drone começa então a executar a função especificada. Quando terminar, desaparecerá automaticamente, a menos que seja o último drone existente.

Drones não colidem entre si. 

Use `max_drones()` para obter o número máximo de drones que podem existir simultaneamente.
Use `num_drones()` para obter o número de drones que já estão na fazenda.

## Exemplo

{{codeexample 
{
    "camera_position": {"x": -1.5, "y": 2.4, "z": 5},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": true,
    "collapsing": true,
    "autoplay": false,
    "items": [],
    "world_size": {"x": 4, "y": 4},
    "execution_speed": 1,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 100,
    "seed": 1,
    "exclude_unlocks": ["fertilizer", "watering"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
#CODE
def harvest_column():
    for _ in range(get_world_size()):
        harvest()
        move(North)

while True:
    if spawn_drone(harvest_column):
        move(East)
}}

Isso fará com que seu primeiro drone se mova horizontalmente e gere mais drones. Os drones gerados se moverão verticalmente e colherão tudo em seu caminho.

Se todos os drones disponíveis já tiverem sido gerados, `spawn_drone()` não fará nada e retornará `None`.

Aqui está outro exemplo que passa uma direção diferente para cada drone.

{{codeexample 
{
    "camera_position": {"x": -1, "y": 2, "z": 5},
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
    "exclude_unlocks": ["fertilizer", "watering"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
move(North)
move(East)
#CODE
for dir in [North, East, South, West]:
    def task():
        move(dir)
        do_a_flip()
    spawn_drone(task)
}}

## Todos os Drones São Iguais

Não existe um drone "principal" especial. Todos os drones podem criar outros drones, e todos contam para o limite de drones. Todos desaparecem quando terminam. Se o primeiro drone concluir o programa antes dos demais, outro drone terá sua execução visualizada pelos destaques no código. Todos os drones podem acionar pontos de interrupção. Quando isso acontece, o destaque do código muda para esse drone.

<spoiler=mostrar dica> Confira esta função paralela super útil `for_all`, que pega qualquer função e a executa em cada casa da fazenda. Ela utiliza todos os drones disponíveis para fazer isso.

{{codeexample 
{
    "camera_position": {"x": -1.5, "y": 2.4, "z": 5},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": true,
    "collapsing": true,
    "autoplay": false,
    "items": [],
    "world_size": {"x": 4, "y": 4},
    "execution_speed": 1,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 100,
    "seed": 1,
    "exclude_unlocks": ["fertilizer", "watering"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
#CODE
def for_all(f):
	def row():
		for _ in range(get_world_size()-1):
			f()
			move(East)
		f()
	for _ in range(get_world_size()):
		if not spawn_drone(row):
			row()
		move(North)

for_all(harvest)
}}

Um padrão particularmente útil é gerar um drone se houver um disponível e, caso contrário, fazer você mesmo.

`if not spawn_drone(task):
	task()`

</spoiler>

## Aguardando Outro Drone

Use a função `wait_for(drone)` para esperar que outro drone termine. Você recebe o handle `drone` quando gera o drone.
`wait_for(drone)` retorna o valor de retorno da função que o outro drone estava executando.

{{codeexample 
{
    "camera_position": {"x": -0.5, "y": 1.5, "z": 4},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": false,
    "collapsing": true,
    "autoplay": false,
    "items": [],
    "world_size": {"x": 2, "y": 1},
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
move(East)
plant(Entities.Tree)
move(West)
#CODE
def get_entity_type_in_direction(dir):
    move(dir)
    return get_entity_type()

drone = spawn_drone(get_entity_type_in_direction, East)
print(wait_for(drone))
}}

Note que gerar drones leva tempo, então não é uma boa ideia gerar um novo drone para cada pequena coisa.

Você pode usar `has_finished(drone)` para ver se o drone terminou sem precisar esperar.

## Sem Memória Compartilhada

Cada drone tem sua própria memória e não pode ler ou escrever diretamente as variáveis globais de outro drone.

{{codeexample 
{
    "camera_position": {"x": -0.5, "y": 1.5, "z": 4},
    "show_image": false,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": false,
    "show_output": true,
    "collapsing": true,
    "autoplay": false,
    "items": [],
    "world_size": {"x": 2, "y": 1},
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
x = 0

def increment():
    global x
    x += 1

wait_for(spawn_drone(increment))
print(x)
}}

Isso imprime `0` porque o novo drone incrementou sua própria cópia do `x` global, o que não afeta o `x` do primeiro drone.

## Passando Argumentos

`spawn_drone()` aceita argumentos opcionais adicionais que serão passados para a função chamada:

Observe que a regra de não compartilhar memória ainda se aplica. Isso significa que a função chamada opera sobre uma cópia dos argumentos:

{{codeexample 
{
    "camera_position": {"x": -0.5, "y": 1.5, "z": 4},
    "show_image": false,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": false,
    "show_output": true,
    "collapsing": true,
    "autoplay": false,
    "items": [],
    "world_size": {"x": 2, "y": 1},
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
def modify(list):
	list.append('verde')
	print(list)

l = ['vermelho']
wait_for(spawn_drone(modify, l))
print(l)
}}

## Condições de Corrida

Vários drones podem interagir com a mesma casa da fazenda ao mesmo tempo. Se dois drones interagirem com a mesma casa durante o mesmo tick, ambas as interações ocorrerão, mas os resultados podem diferir com base na ordem das interações.

Por exemplo, imagine que os drones `0` e `1` estão ambos sobre a mesma árvore que está quase totalmente crescida.
O drone `0` chama
`use_item(Items.Fertilizer)`
O drone `1` chama
`harvest()`

Se essas ações ocorrerem ao mesmo tempo, a árvore será primeiro fertilizada e depois colhida. Nesse caso, você receberá madeira dela. No entanto, se o Drone `1` for um pouco mais rápido, a árvore será colhida antes de ser fertilizada, e você não receberá a madeira.
Isso é chamado de "condição de corrida". É um problema comum em programação paralela, onde o resultado depende da ordem em que as operações são realizadas.

Aqui está outra situação problemática que pode acontecer quando vários drones executam o mesmo código simultaneamente na mesma posição.

`if get_water() < 0.5:
    use_item(Items.Water)`

Se vários drones executarem isso simultaneamente, todos eles executarão a primeira linha, o que os coloca no bloco `if`. Então, todos eles usarão água, desperdiçando muita dela.
No momento em que um drone chega à segunda linha, `get_water()` pode não ser mais menor que `0.5` porque outro drone já regou a casa nesse meio tempo.

---

[Funções](docs/scripting/functions.md)      [Escopos de Nomes](docs/scripting/scopes.md)      [Simulação](docs/unlocks/simulation.md)

[spawn_drone()](functions/spawn_drone)      [num_drones()](functions/num_drones)      [max_drones()](functions/max_drones)      [wait_for()](functions/wait_for)      [has_finished()](functions/has_finished)
