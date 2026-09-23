[<- Abóboras](docs/unlocks/pumpkins.md)

---

# Policultura

Talvez você já tenha percebido que, às vezes, as plantas rendem mais quando são plantadas juntas.
Grama, arbustos, árvores e cenouras rendem mais quando têm a planta companheira correta. A preferência de companhia é diferente para cada planta e não pode ser prevista. Felizmente, a preferência da planta sob o drone pode ser medida usando `get_companion()`. Ela retorna uma tupla em que o primeiro elemento é o tipo de planta desejado como companheira e o segundo é a posição onde a companheira deve ficar. A planta companheira não precisa estar totalmente crescida para conceder o bônus de rendimento.

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
    "operation_ticks": 20,
    "seed": 1,
    "exclude_unlocks": ["watering", "fertilizer"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
#CODE
plant(Entities.Bush)
plant_type, (x, y) = get_companion()
print(plant_type, (x, y))
move(East)
move(South)
plant(plant_type)
move(West)
move(North)
do_a_flip()
harvest()
}}

A preferência de companhia de uma planta pode ser `Entities.Grass`, `Entities.Bush`, `Entities.Tree` ou `Entities.Carrot`. Cada planta escolhe aleatoriamente, mas sempre escolherá um tipo diferente do próprio. A posição pode estar em qualquer lugar a até 3 movimentos da planta, exceto na posição da própria planta.

Se não houver uma planta com preferência de companhia sob o drone, `get_companion()` retornará `None`.

Antes de a policultura ser desbloqueada pela primeira vez, o multiplicador de rendimento é `5`. Ele dobra a cada melhoria.

---

[Estatísticas](docs/stats.md)      [Tuplas](docs/scripting/tuples.md)      [Dicionários](docs/scripting/dicts.md)      [Sentidos](docs/unlocks/senses.md)      [Plantar](docs/unlocks/plant.md)

[harvest()](functions/harvest)      [plant()](functions/plant)      [move()](functions/move)      [till()](functions/till)      [get_companion()](functions/get_companion)
