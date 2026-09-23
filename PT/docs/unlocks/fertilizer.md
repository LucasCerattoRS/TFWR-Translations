[<- Irrigação](docs/unlocks/watering.md) <right>[Labirintos ->](docs/unlocks/mazes.md)

---

# Fertilizante

Em algum momento, esperar as plantas crescerem deixa de ser eficiente.
Assim como com a água, você receberá automaticamente 1 fertilizante a cada 10 segundos. A quantidade dobra a cada melhoria.

O fertilizante pode fazer as plantas crescerem instantaneamente. `use_item(Items.Fertilizer)` reduz o tempo de crescimento restante da planta sob o drone em 2 segundos.

{{codeexample 
{
    "camera_position": {"x": 0, "y": 1, "z": 5},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": false,
    "collapsing": true,
    "autoplay": false,
    "items": [{"item": "fertilizer", "n": 10}],
    "world_size": {"x": 1, "y": 1},
    "execution_speed": 2,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 1,
    "seed": 1,
    "exclude_unlocks": ["watering"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
#CODE
plant(Entities.Tree)
use_item(Items.Fertilizer)
use_item(Items.Fertilizer)
use_item(Items.Fertilizer)
harvest()
}}

Isso tem alguns efeitos colaterais.
Plantas cultivadas com fertilizante ficarão infectadas.

Quando uma planta está infectada, metade de seu rendimento é transformado em `Items.Weird_Substance` quando é colhida.
A Substância Estranha também pode ser usada em plantas, o que tem o efeito de alternar o status de infecção da planta e de todas as plantas adjacentes.

Se você chamar `use_item(Items.Weird_Substance)` sobre uma planta infectada, ela será curada; se usar em uma planta saudável, ela será infectada.

Se você usar em uma planta infectada que tem vizinhos saudáveis, irá curar a planta, mas infectar os vizinhos e vice-versa.

{{codeexample 
{
    "camera_position": {"x": -1, "y": 1.8, "z": 5},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": false,
    "collapsing": true,
    "autoplay": false,
    "items": [{"item": "weird_substance", "n": 10}],
    "world_size": {"x": 3, "y": 3},
    "execution_speed": 1,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 1,
    "seed": 1,
    "exclude_unlocks": ["watering"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
for _ in range(3):
    for _ in range(3):
        plant(Entities.Tree)
        move(East)
    move(North)

move(North)
move(East)

for _ in range(60):
    do_a_flip()
#CODE
for _ in range(6):
    use_item(Items.Weird_Substance)
    move(East)
}}

---

[Estatísticas](docs/stats.md)      [Irrigação](docs/unlocks/watering.md)      [Labirintos](docs/unlocks/mazes.md)

[use_item()](functions/use_item)
