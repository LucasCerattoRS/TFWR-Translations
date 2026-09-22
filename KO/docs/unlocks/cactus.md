[<- 호박](docs/unlocks/pumpkins.md) <right>[공룡 ->](docs/unlocks/dinosaurs.md)
---
# 선인장
다른 식물들처럼, [선인장](objects/cactus)도 흙에서 키우고 평소처럼 수확할 수 있어요.

하지만, 선인장은 다양한 크기로 자라며 이상한 순서 감각을 가지고 있어요.

다 자란 선인장을 수확할 때 모든 이웃 선인장이 정렬된 순서라면, 모든 이웃 선인장도 재귀적으로 수확해요.

`North`와 `East` 방향의 모든 이웃 선인장이 다 자랐고 크기가 같거나 더 크고, `South`와 `West` 방향의 모든 이웃 선인장이 다 자랐고 크기가 같거나 더 작으면, 그 선인장은 정렬된 것으로 간주돼요.

수확은 모든 인접한 선인장이 다 자랐고 정렬된 순서일 경우에만 퍼져나가요.
즉, 다 자란 선인장 사각형이 크기 순으로 정렬되어 있고 그중 하나를 수확하면, 사각형 전체가 수확된다는 뜻이에요.

다 자란 선인장은 정렬되지 않았으면 갈색으로 보여요. 정렬되면 다시 녹색으로 변해요.

수확한 선인장 개수의 제곱만큼 선인장을 받게 돼요. 따라서 `n`개의 선인장을 동시에 수확하면 `n**2`개의 `Items.Cactus`를 받게 돼요.

선인장의 크기는 `measure()`로 측정할 수 있어요.
크기는 항상 `0,1,2,3,4,5,6,7,8,9` 중 하나예요.

`measure(direction)`에 방향을 전달하여 드론의 해당 방향에 있는 이웃 타일을 측정할 수도 있어요.

`swap()` 명령을 사용하여 어떤 방향으로든 이웃한 선인장과 위치를 바꿀 수 있어요.
`swap(direction)`은 드론 아래의 객체와 드론의 `direction` 방향으로 한 칸 떨어진 객체를 교환해요.

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

## 숫자 예시
다음 각 격자에서 모든 선인장은 정렬된 순서이며 수확은 밭 전체로 퍼져나가요:
`3 4 5    3 3 3    1 2 3    1 5 9
2 3 4    2 2 2    1 2 3    1 3 8
1 2 3    1 1 1    1 2 3    1 3 4`

이 격자에서는 왼쪽 아래 선인장만 정렬된 순서이며, 이는 수확이 퍼져나가기에 충분하지 않아요:
`1 5 3
4 9 7
3 3 2`

<spoiler=힌트 1 보기>
행이 이미 정렬되어 있다면, 열을 정렬해도 행의 정렬이 풀리지 않아요.
</spoiler>
<spoiler=힌트 2 보기>
널리 알려진 영리한 정렬 알고리즘이 많아요. 익숙하지 않다면 찾아보고 이 문제에 적용할 수 있는 알고리즘을 생각해 보세요. 이웃한 선인장끼리만 교환할 수 있으므로 모든 알고리즘이 여기서 작동하는 것은 아니에요.
</spoiler>
<spoiler=힌트 3 보기>
"버블 정렬"은 아마 가장 단순한 정렬 알고리즘일 거예요. 잘못된 순서로 놓인 인접 요소가 없어질 때까지 요소들을 반복해서 훑으며 서로 교환하는 방식이에요.

선인장에서는 다음과 같이 보여요.
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
물론 이 전략을 개선하는 방법은 많아요!
한 행을 정렬하는 데 성공했다면 힌트 1을 이용해 밭 전체를 정렬할 수 있어요.
</spoiler>

---

[통계](docs/stats.md)

[harvest()](functions/harvest)      [plant()](functions/plant)      [move()](functions/move)      [till()](functions/till)      [swap()](functions/swap)      [measure()](functions/measure)
