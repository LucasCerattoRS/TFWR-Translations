[<- Cacto](docs/unlocks/cactus.md)

---

# Dinossauros

Dinossauros são criaturas antigas e majestosas que podem ser cultivadas por seus ossos antigos.

Infelizmente, os dinossauros foram extintos há muito tempo, então o melhor que podemos fazer agora é nos fantasiar de um.
Para isso, você recebeu o novo chapéu de dinossauro.

O chapéu pode ser equipado com
`change_hat(Hats.Dinosaur_Hat)`

Infelizmente, ele não se parece muito com o que aparecia no anúncio...

Se você equipar o chapéu de dinossauro e tiver cactos suficientes, uma [maçã](objects/apple) será comprada e colocada automaticamente sob o drone.
Quando o drone está sobre uma maçã e se move novamente, ele come a maçã e sua cauda cresce em um. Se você puder pagar, uma nova maçã será comprada e colocada em um local aleatório.
A maçã não pode surgir se outra coisa estiver plantada onde ela quer estar.

A cauda do dinossauro é arrastada atrás do drone, preenchendo os quadrados pelos quais ele passou. Se o drone tentar se mover sobre a própria cauda, `move()` falhará e retornará `False`.
O último segmento da cauda sairá do caminho durante um movimento, então você pode se mover até ele. Porém, se a cobra preencher a fazenda inteira, você não conseguirá mais se mover. Assim, é possível verificar se a cobra atingiu o tamanho máximo conferindo se você ainda consegue se mover.
Enquanto usa o chapéu de dinossauro, o drone não pode atravessar a borda da fazenda para chegar ao outro lado.

Usar `measure()` em uma maçã retornará a posição da próxima maçã como uma tupla.

`next_x, next_y = measure()`

{{codeexample 
{
    "camera_position": {"x": -1, "y": 2.4, "z": 5},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": true,
    "collapsing": true,
    "autoplay": false,
    "items": [{"item": "cactus", "n": 10000}],
    "world_size": {"x": 4, "y": 4},
    "execution_speed": 2,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 1,
    "seed": 5,
    "exclude_unlocks": ["watering"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
#CODE
change_hat(Hats.Dinosaur_Hat)
while True:
    next_x, next_y = measure()
    while get_pos_x() != next_x:
        move(East)
    while get_pos_y() != next_y:
        move(North)
}}

Quando o chapéu for desequipado ao equipar outro, a cauda será colhida.
Você receberá uma quantidade de ossos igual ao quadrado do comprimento da cauda. Para uma cauda de comprimento `n`, receberá `n**2` `Items.Bone`.
Por exemplo:
comprimento 1 => 1 osso
comprimento 2 => 4 ossos
comprimento 3 => 9 ossos
comprimento 4 => 16 ossos
comprimento 16 => 256 ossos
comprimento 100 => 10000 ossos

O Chapéu de Dinossauro é muito pesado, então se você o equipar, fará com que `move()` leve 400 ticks em vez de 200. No entanto, cada vez que você pega uma maçã, o número de ticks usados por `move()` é reduzido em 3% (arredondado para baixo), porque uma cauda mais longa pode ajudar você a se mover.

O loop a seguir imprime o número de ticks usados por `move()` após qualquer número de maçãs:

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
    "operation_ticks": 1,
    "seed": 1,
    "exclude_unlocks": ["watering", "fertilizer"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
#CODE
ticks = 400
for i in range(100):
    quick_print("ticks após ", i, " maçãs: ", ticks)
    ticks -= ticks * 0.03 // 1
}}

Você só tem um chapéu de dinossauro, então apenas um drone pode usá-lo.

<spoiler=mostrar dica 1>
Se continuar seguindo o mesmo caminho que percorre o campo inteiro, você conseguirá facilmente uma cobra que cubra todo o campo sempre. Não é muito eficiente, mas funciona.
Percorrer completamente uma fazenda muito grande pode levar bastante tempo, e talvez você nem precise de tantos ossos. Fique à vontade para usar `set_world_size()` e ajustar a fazenda a um tamanho mais conveniente.</spoiler>

---

[Estatísticas](docs/stats.md)      [Tuplas](docs/scripting/tuples.md)      [Listas](docs/scripting/lists.md)

[change_hat()](functions/change_hat)      [move()](functions/move)      [measure()](functions/measure)
