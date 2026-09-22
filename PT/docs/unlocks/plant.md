[<- Melhoria de Velocidade](docs/unlocks/speed.md) <right>[Cenouras ->](docs/unlocks/carrots.md)

<right>[Depuração ->](docs/scripting/debug.md)

<right>[Operadores ->](docs/scripting/operators.md)

---

# Plantar

A grama é boa porque cresce automaticamente. Todas as outras plantas precisam ser plantadas com a função `plant()`. A única planta que você pode plantar agora é um arbusto.
Você pode passar o tipo de planta que deseja plantar para a função desta forma:

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
plant(Entities.Bush)
}}

Isso plantará um arbusto sob o drone.

Chame `clear()` para redefinir a fazenda para toda grama e redefinir a posição do drone.

Parece que se você cultivar mais de um tipo de planta na fazenda ao mesmo tempo, às vezes pode obter um rendimento maior. Você precisará pesquisar policultura para aprender mais.

---

[Estatísticas](docs/stats.md)      [If](docs/scripting/if.md)      [Sentidos](docs/unlocks/senses.md)      [Policultura](docs/unlocks/polyculture.md)

[harvest()](functions/harvest)      [plant()](functions/plant)
