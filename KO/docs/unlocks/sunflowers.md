[<- 물주기](docs/unlocks/watering.md)
---
# 해바라기
[해바라기](objects/sunflower)는 태양의 파워를 모아요. 그 파워를 수확할 수 있어요. 

해바라기를 심는 것은 당근이나 호박을 심는 것과 똑같이 작동해요. 

다 자란 해바라기를 수확하면 파워를 얻어요.
농장에 해바라기가 10개 이상 있고 꽃잎이 가장 많은 해바라기를 수확하면 `8`배 더 많은 파워를 얻어요!
꽃잎이 더 많은 다른 해바라기가 있을 때 해바라기를 수확하면, 다음에 수확하는 해바라기도 일반적인 양의 파워만 줘요 (8배 보너스는 없어요).

`measure()`는 드론 아래에 있는 해바라기의 꽃잎 수를 반환해요.
해바라기는 최소 `7`개, 최대 `15`개의 꽃잎을 가져요.
다 자라기 전에도 해바라기를 측정할 수 있고 10개 제한에 포함돼요.

여러 해바라기가 같은 수의 꽃잎을 가질 수 있으므로, 꽃잎이 가장 많은 해바라기도 여러 개일 수 있어요. 이 경우에는 어느 것을 수확하든 상관없어요.

{{codeexample 
{
    "camera_position": {"x": -1.5, "y": 2, "z": 4},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "inventory_scale": 5,
    "show_output": false,
    "collapsing": true,
    "autoplay": false,
    "items": [{"item": "carrot", "n": 10}],
    "world_size": {"x": 5, "y": 2},
    "execution_speed": 2,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 1,
    "seed": 4,
    "exclude_unlocks": ["fertilizer", "watering"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
move(North)
for _ in range(5):
    till()
    plant(Entities.Sunflower)
    move(East)
move(North)
do_a_flip()
do_a_flip()
do_a_flip()
do_a_flip()
do_a_flip()
#CODE
for _ in range(5):
    till()
    plant(Entities.Sunflower)
    print(measure())
    move(East)
for _ in range(5):
    while not can_harvest():
        pass
    harvest()
    move(East)
}}

파워가 있는 동안 드론은 파워를 사용해서 두 배 더 빠르게 움직여요. 
30번의 행동(이동, 수확, 심기 등)마다 1 파워를 소모해요.
다른 코드 문장을 실행할 때도 파워를 사용할 수 있지만, 드론 행동보다는 훨씬 적게 사용해요.

일반적으로, 속도 업그레이드로 빨라지는 모든 것은 파워로도 빨라져요.
파워로 빨라지는 모든 것은 속도 업그레이드를 무시하고 실행에 걸리는 시간에 비례하여 파워를 사용해요.

---

[통계](docs/stats.md)      [리스트](docs/scripting/lists.md)      [딕셔너리](docs/scripting/dicts.md)      [변수](docs/scripting/variables.md)      [for 루프](docs/scripting/for.md)      [If문](docs/scripting/if.md)      [연산자](docs/scripting/operators.md)

[harvest()](functions/harvest)      [plant()](functions/plant)      [move()](functions/move)      [till()](functions/till)      [measure()](functions/measure)
