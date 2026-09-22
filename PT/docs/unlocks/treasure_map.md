[<- Ferro](docs/unlocks/iron.md)
---
# Mapa do Tesouro

Lendas falam de um tesouro esquivo escondido por um pirata esquecido, morto há muito tempo — ou algo assim. E se ele anotou o caminho em um mapa e depois o perdeu? Talvez tenha deixado o mapa cair ao ser encurralado por um rio de lava, e ele ficou preservado sob uma camada de basalto. Medir o basalto pode revelar algo.

<spoiler=conte mais>
Procure uma camada de `Grounds.Basalt`. Tente medir o basalto e veja o que ele informa. A pista pode levar ao mapa do tesouro, e medir o mapa certamente revelará o caminho até o tesouro — mas você consegue decifrar as instruções?
</spoiler>

<spoiler=só diga como>
Certo: encontre o estrato de `Grounds.Basalt` e o bloco `Grounds.Treasure_Map` diretamente abaixo. Use `measure()` no basalto para obter a posição `(x, y)` do bloco do mapa.

Chame `measure()` no bloco do mapa para obter o caminho como uma sequência de letras de direção. N, E, S e W representam `North`, `East`, `South` e `West`; D significa "Down" ou "Dig". Essas letras descrevem um caminho de blocos `Grounds.Treasure_Path` até o tesouro.

```
path = measure()
for letter in path:
    do_something(letter)
```

O drone que escavar o bloco do mapa é quem deve encontrar o tesouro. Ele precisa permanecer sobre blocos `Grounds.Treasure_Path` o tempo todo. Se passar para outro solo, o caminho se romperá e o tesouro será perdido.

No fim do caminho há um bloco `Grounds.Treasure_Goal`. Se o drone não tiver saído da trilha, um `Entities.Underground_Treasure` aparecerá sobre ele. O drone pode usar `harvest()` no baú para coletar o ouro.

A quantidade de ouro é proporcional ao comprimento do caminho. Melhorar Mapa do Tesouro aumenta sua profundidade, enquanto melhorar Expandir dá mais espaço lateral. Ambas as melhorias aumentam o comprimento do caminho e a quantidade de ouro encontrada.
</spoiler>

---

[Estatísticas](docs/stats.md)      [Loop For](docs/scripting/for.md)      [Tuplas](docs/scripting/tuples.md)      [Sentidos Subterrâneos](docs/unlocks/underground_senses.md)

[harvest()](functions/harvest)      [move()](functions/move)      [dig()](functions/dig)      [measure()](functions/measure)

