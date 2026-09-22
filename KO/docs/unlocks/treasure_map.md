[<- 철](docs/unlocks/iron.md)
---
# 보물지도

전설에 따르면 오래전 죽은 건망증 해적이 숨겨 놓아 좀처럼 찾기 어려운 보물이 있다고 해요. 아니면 대충 그런 얘기예요. 해적이 보물로 가는 길을 지도에 적어 놓고 지도를 잃어버렸다면 어떨까요? 용암의 강에 몰렸을 때 지도를 떨어뜨렸고, 그 위에 현무암층이 쌓여 보존되었을지도 몰라요. 현무암을 측정하면 무언가를 알아낼 수 있을 거예요.

<spoiler=더 알려주세요>
`Grounds.Basalt` 층을 찾아보세요. 현무암을 측정해 무엇을 알려주는지 확인해 보세요. 단서는 보물지도로 이끌 것이고, 지도를 측정하면 틀림없이 보물로 가는 길을 알려줄 거예요. 하지만 지도의 지시를 해독할 수 있을까요?
</spoiler>

<spoiler=방법만 알려주세요>
알겠어요. `Grounds.Basalt` 지층과 그 바로 아래의 `Grounds.Treasure_Map` 블록을 찾으세요. 현무암에서 `measure()`를 사용하면 아래 지도 블록의 `(x, y)` 위치를 얻을 수 있어요.

지도 블록에서 `measure()`를 호출하면 방향 문자열로 보물 길을 얻어요. N, E, S, W는 각각 `North`, `East`, `South`, `West`를, D는 "Down" 또는 "Dig"를 뜻해요. 이 문자들은 보물로 이어지는 `Grounds.Treasure_Path` 블록의 길을 나타내요.

```
path = measure()
for letter in path:
    do_something(letter)
```

보물지도 블록을 파는 드론이 보물을 찾아야 하는 드론이에요. 이 드론은 항상 `Grounds.Treasure_Path` 블록 위에 머물러야 해요. 다른 땅으로 이동하면 길이 끊어지고 보물을 잃게 돼요.

길 끝에는 `Grounds.Treasure_Goal` 블록이 있어요. 드론이 길을 벗어나지 않았다면 그 위에 `Entities.Underground_Treasure`가 나타나요. 드론은 상자를 `harvest()`해 황금을 모을 수 있어요.

황금의 양은 보물 길의 길이에 비례해요. 보물지도 해금을 업그레이드하면 길의 깊이가 늘고, 확장을 업그레이드하면 좌우로 더 넓게 움직일 수 있어요. 두 업그레이드 모두 보물 길의 길이와 발견하는 황금의 양을 늘려줘요.
</spoiler>

---

[통계](docs/stats.md)      [for 루프](docs/scripting/for.md)      [튜플](docs/scripting/tuples.md)      [지하 감각](docs/unlocks/underground_senses.md)

[harvest()](functions/harvest)      [move()](functions/move)      [dig()](functions/dig)      [measure()](functions/measure)
