[<- 철](docs/unlocks/iron.md)
---
# 철 탐사

철 광맥을 찾기가 때때로 어렵다는 걸 눈치채셨을 거예요. 운에 맡기고 주변을 파볼 수도 있지만, 더 좋은 방법이 있어요. 철은 자성을 띠므로 멀리서도 찾을 수 있어요.

`prospect_iron()` 명령이 바로 그 일을 해요. `prospect_iron()`은 가장 가까운 철광석으로 한 걸음 다가가기 위해 드론이 이동해야 하는 방위(`North`, `East`, `South`, `West`)를 반환해요. 명령을 실행하면 석탄 1개를 소모해요.

드론이 이미 가장 가까운 철광석 바로 위에 있거나, 명령을 실행할 석탄이 부족하거나, 범위 내에 철이 없으면 `prospect_iron()`은 `None`을 반환해요.

다음 코드를 사용하면 다음 철광석으로 한 걸음 다가갈 수 있어요.

`if prospect_iron() != None:
    move(prospect_iron())
`

이 코드는 현재 `prospect_iron()`을 두 번 호출해 석탄 2개를 소모하므로 변수를 사용해 최적화하는 것이 좋아요.

가장 가까운 철광석은 드론이 이동해야 하는 걸음 수로 계산해요. 드론에서 동쪽으로 2블록, 북쪽으로 3블록 떨어진 곳에 철광석이 있다면, 드론이 그곳까지 다섯 걸음을 이동해야 하므로 거리는 5로 계산돼요.

땅을 파는 것도 한 걸음으로 계산해요. 철이 추가로 지하 7블록 깊이에 묻혀 있다면, 철 위로 이동하는 데 다섯 걸음, 이후 철에 도달하는 데 일곱 번을 파야 하므로 거리는 12로 계산돼요.

---

[철](docs/unlocks/iron.md)      [지하 감각](docs/unlocks/underground_senses.md)

[move()](functions/move)      [dig()](functions/dig)      [prospect_iron()](functions/prospect_iron)
