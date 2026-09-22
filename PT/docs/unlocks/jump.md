[<- Carvão](docs/unlocks/coal.md)
---
# Salto

Seu drone desbloqueou o comando `jump()`.

Este comando permite escolher certos desbloqueios como alvo e saltar até eles. É especialmente útil para depuração ou para saltar até um veio de minério que você acabou de deixar passar. Use-o passando um desbloqueio como argumento, como `Unlocks.Iron`.

`jump()` funciona apenas com desbloqueios que aparecem no subsolo, como `jump(Unlocks.Rice)` ou `jump(Unlocks.Iron)`.

{{codeexample 
{
    "camera_position": {"x": -1, "y": 0, "z": 8},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": false,
    "collapsing": true,
    "autoplay": false,
    "items": [],
    "world_size": {"x": 4, "y": 4},
    "execution_speed": 1,
    "digging_speed": 3,
    "action_ticks": 200,
    "operation_ticks": 200,
    "seed": 1,
    "exclude_unlocks": ["watering", "fertilizer", "mushrooms"],
    "starting_chunk": 0
}
#CODE
dig()
dig()
dig()
jump(Unlocks.Iron)
do_a_flip()
}}

Não há garantia de que o salto leve você diretamente ao desbloqueio escolhido, então talvez ainda seja preciso procurar um pouco, mas o alvo certamente estará por perto.

`jump()` só pode ser usado uma vez por execução do programa.

---

[jump()](functions/jump)

