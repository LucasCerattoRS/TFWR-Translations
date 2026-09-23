[<- Irrigação](docs/unlocks/watering.md)

---

# Girassóis

[Girassóis](objects/sunflower) coletam a energia do sol. Você pode colher essa energia. 

Plantá-los funciona exatamente como plantar cenouras ou abóboras. 

Colher um girassol crescido rende energia.
Se houver pelo menos 10 girassóis na fazenda e você colher um dos que têm o maior número de pétalas, receberá `8` vezes mais energia!
Se você colher um girassol enquanto houver outro com mais pétalas, o próximo girassol colhido também renderá apenas a quantidade normal de energia (sem o bônus de 8x).

`measure()` retorna o número de pétalas do girassol sob o drone.
Os girassóis têm no mínimo `7` e no máximo `15` pétalas.
Mesmo antes de crescerem por completo, os girassóis já podem ser medidos e contam para o limite de 10 girassóis.

Vários girassóis podem ter o mesmo número de pétalas, então pode haver mais de um com a maior quantidade. Nesse caso, não importa qual deles você colher.

{{codeexample 
{
    "camera_position": {"x": -1.5, "y": 2, "z": 4},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "inventory_scale": 5,
    "show_output": false,
    "collapsing": true,
    "autoplay": false,
    "items": [{"item": "carrot", "n": 10}],
    "world_size": {"x": 5, "y": 2},
    "execution_speed": 2,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 1,
    "seed": 4,
    "exclude_unlocks": ["fertilizer", "watering"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
move(North)
for _ in range(5):
    till()
    plant(Entities.Sunflower)
    move(East)
move(North)
do_a_flip()
do_a_flip()
do_a_flip()
do_a_flip()
do_a_flip()
#CODE
for _ in range(5):
    till()
    plant(Entities.Sunflower)
    print(measure())
    move(East)
for _ in range(5):
    while not can_harvest():
        pass
    harvest()
    move(East)
}}

Enquanto você tiver energia, o drone a usará para funcionar duas vezes mais rápido.
Ele consome 1 de energia a cada 30 ações, como movimentos, colheitas ou plantios.
Executar outras instruções de código também pode consumir energia, mas muito menos do que as ações do drone.

Em geral, tudo que é acelerado por melhorias de velocidade também é acelerado por energia.
Qualquer coisa acelerada por energia também usa energia proporcional ao tempo que leva para executá-la, ignorando as melhorias de velocidade.

---

[Estatísticas](docs/stats.md)      [Listas](docs/scripting/lists.md)      [Dicionários](docs/scripting/dicts.md)      [Variáveis](docs/scripting/variables.md)      [Loop For](docs/scripting/for.md)      [If](docs/scripting/if.md)      [Operadores](docs/scripting/operators.md)

[harvest()](functions/harvest)      [plant()](functions/plant)      [move()](functions/move)      [till()](functions/till)      [measure()](functions/measure)
