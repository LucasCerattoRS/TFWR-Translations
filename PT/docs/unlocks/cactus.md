[<- Abóboras](docs/unlocks/pumpkins.md) <right>[Dinossauros ->](docs/unlocks/dinosaurs.md)

---

# Cacto

Como outras plantas, [cactos](objects/cactus) podem ser cultivados em solo e colhidos como de costume.

No entanto, eles vêm em vários tamanhos e têm um estranho senso de ordem.

Se você colher um cacto totalmente crescido e todos os cactos vizinhos estiverem em ordem, ele também colherá todos os cactos vizinhos recursivamente.

Um cacto é considerado ordenado se todos os cactos vizinhos ao `North` e ao `East` estiverem totalmente crescidos e forem de tamanho maior ou igual ao dele, enquanto todos os cactos vizinhos ao `South` e ao `West` estiverem totalmente crescidos e forem de tamanho menor ou igual ao dele.

A colheita só se espalhará se todos os cactos adjacentes estiverem totalmente crescidos e em ordem.
Isso significa que, se um quadrado de cactos crescidos estiver ordenado por tamanho e você colher um cacto, ele colherá o quadrado inteiro.

Um cacto totalmente crescido aparecerá marrom se não estiver ordenado. Uma vez ordenado, ele ficará verde novamente.

Você receberá uma quantidade de cactos igual ao quadrado do número de cactos colhidos. Se colher `n` cactos ao mesmo tempo, receberá `n**2` `Items.Cactus`.

O tamanho de um cacto pode ser medido com `measure()`.
É sempre um destes números: `0,1,2,3,4,5,6,7,8,9`.

Você também pode passar uma direção para `measure(direction)` para medir a casa vizinha naquela direção do drone.

Você pode trocar um cacto com seu vizinho em qualquer direção usando o comando `swap()`.
`swap(direction)` troca o objeto sob o drone com o objeto a uma casa de distância na `direction` do drone.

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
    "items": [{"item": "pumpkin", "n": 32}],
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
for _ in range(4):
    for _ in range(4):
        till()
        plant(Entities.Cactus)
        move(East)
    move(North)
for _ in range(4):
    for _ in range(4):
        for _ in range(4):
            x,y = get_pos_x(), get_pos_y()
            if x > 0 and measure(West) > measure():
                swap(West)
            if y > 0 and measure(South) > measure():
                swap(South)
            if x < 3 and measure(East) < measure():
                swap(East)
            if y < 3 and measure(North) < measure():
                swap(North)
            move(East)
        move(North)
move(East)
move(North)
move(North)
swap(West)
swap(South)
swap(East)
swap(North)
#CODE
swap(North)
swap(East)
swap(South)
swap(West)
harvest()
}}

## Exemplos Numéricos

Em cada uma dessas grades, todos os cactos estão em ordem e a colheita se espalhará por todo o campo:

`3 4 5    3 3 3    1 2 3    1 5 9
2 3 4    2 2 2    1 2 3    1 3 8
1 2 3    1 1 1    1 2 3    1 3 4`

Nesta grade, apenas o cacto inferior esquerdo está em ordem, o que não é suficiente para que a colheita se espalhe:

`1 5 3
4 9 7
3 3 2`

<spoiler=mostrar dica 1>
Se cada linha já estiver ordenada de forma independente, ordenar cada coluna de forma independente não desordenará as linhas.
</spoiler>
<spoiler=mostrar dica 2>
Existem muitos algoritmos de ordenação conhecidos e engenhosos. Se você não os conhece, vale a pena pesquisá-los e pensar em quais podem ser adaptados a este problema. Lembre-se de que nem todos funcionam aqui, pois você só pode trocar cactos vizinhos.
</spoiler>
<spoiler=mostrar dica 3>
O "bubble sort" talvez seja o algoritmo de ordenação mais simples. A ideia é percorrer repetidamente os elementos, trocando elementos adjacentes que estejam na ordem errada, até não restar nenhum.

Veja como isso fica com cactos:

{{codeexample 
{
    "camera_position": {"x": -4, "y": 1, "z": 6},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": false,
    "show_inventory": true,
    "show_output": false,
    "collapsing": false,
    "autoplay": true,
    "items": [{"item": "pumpkin", "n": 18}],
    "world_size": {"x": 9, "y": 1},
    "execution_speed": 2,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 1,
    "seed": 1,
    "exclude_unlocks": ["fertilizer", "watering"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
#CODE
for _ in range(9):
    till()
    plant(Entities.Cactus)
    move(East)
sorted = False
while not sorted:
    sorted = True
    for _ in range(9):
        move(East)
        if get_pos_x() > 0 and measure(West) > measure():
            swap(West)
            sorted = False
harvest()
}}

É claro que há muitas maneiras de melhorar essa estratégia!
Depois de conseguir ordenar uma única linha, use a Dica 1 para ordenar o campo inteiro.
</spoiler>

---

[Estatísticas](docs/stats.md)

[harvest()](functions/harvest)      [plant()](functions/plant)      [move()](functions/move)      [till()](functions/till)      [swap()](functions/swap)      [measure()](functions/measure)
