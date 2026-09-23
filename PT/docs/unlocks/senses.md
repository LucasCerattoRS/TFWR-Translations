[<- Operadores](docs/scripting/operators.md)

---

# Sentidos

O drone pode ver agora! 

As funções `get_pos_x()` e `get_pos_y()` retornam as coordenadas x e y atuais do drone. Na posição inicial, ambas são `0`. A coordenada x aumenta em `1` a cada quadrado na direção `East`, e a coordenada y aumenta em `1` a cada quadrado na direção `North`.
{{codeexample 
{
    "camera_position": {"x": -1, "y": 1.8, "z": 4},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": true,
    "collapsing": true,
    "autoplay": false,
    "items": [],
    "world_size": {"x": 2, "y": 2},
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
#CODE
print("x =", get_pos_x(), "y =", get_pos_y())
if get_pos_x() == 1 and get_pos_y() == 0:
    do_a_flip()
}}

`num_items(item)` retorna a quantidade que você possui de um item.

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
    "items": [{"item": "hay", "n": 10}],
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
print(num_items(Items.Hay))
}}

`get_entity_type()` e `get_ground_type()` retornam o tipo de entidade ou solo que está sob o drone.

{{codeexample 
{
    "camera_position": {"x": 0, "y": 1.5, "z": 6},
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
plant(Entities.Bush)
#CODE
print(get_entity_type())
if get_entity_type() == Entities.Bush:
	do_a_flip()

print(get_ground_type())
if get_ground_type() != Grounds.Soil:
	do_a_flip()
}}

A palavra-chave `None` também está desbloqueada agora! `None` é um valor que representa a ausência de valor.
Por exemplo, uma função que não tem uma declaração `return` na verdade retornará `None`.

`get_entity_type()` retorna `None` se não houver entidade sob o drone.

Se você quiser descobrir quantos de um determinado desbloqueio você tem, use a função `num_unlocked(unlock)`.

Por exemplo, `num_unlocked(Unlocks.Speed)` retornará o número de melhorias de velocidade que você tem.

`num_unlocked(Unlocks.Senses)` retornará `1` se os sentidos estiverem desbloqueados e `0` se não estiverem.

Você também pode usar `num_unlocked()` em itens ou entidades. A função retorna `1` se o item ou a entidade estiver desbloqueado e `0` caso contrário.

Tenha cuidado: `num_unlocked(Unlocks.Carrots)` retorna o número de vezes que o desbloqueio foi liberado ou aprimorado.
`num_unlocked(Items.Carrot)` retorna somente `0` ou `1`. O mesmo vale para outras plantas.

---

[If](docs/scripting/if.md)      [Operadores](docs/scripting/operators.md)      [Variáveis](docs/scripting/variables.md)      [Tuplas](docs/scripting/tuples.md)      [Dicionários](docs/scripting/dicts.md)      [Sentidos Subterrâneos](docs/unlocks/underground_senses.md)

[get_pos_x()](functions/get_pos_x)      [get_pos_y()](functions/get_pos_y)      [get_entity_type()](functions/get_entity_type)      [get_ground_type()](functions/get_ground_type)      [num_items()](functions/num_items)      [num_unlocked()](functions/num_unlocked)
