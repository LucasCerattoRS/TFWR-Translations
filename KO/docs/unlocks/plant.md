[<- 속도 업그레이드](docs/unlocks/speed.md) <right>[당근 ->](docs/unlocks/carrots.md)
<right>[디버그 ->](docs/scripting/debug.md)
<right>[연산자 ->](docs/scripting/operators.md)
---
# 심기
풀은 자동으로 자라기 때문에 좋아요. 다른 모든 식물은 `plant()` 함수로 심어야 해요. 지금 심을 수 있는 유일한 식물은 덤불이에요.
심고 싶은 식물의 종류를 다음과 같이 함수에 전달할 수 있어요:

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

이것은 드론 아래에 덤불을 심을 거예요.

농장을 모두 풀로 초기화하고 드론 위치를 재설정하려면 `clear()`를 호출하세요.

농장에서 한 번에 한 종류 이상의 식물을 키우면 때때로 더 높은 수확량을 얻을 수 있는 것 같아요. 더 배우려면 혼합 재배를 연구해야 할 거예요.

---

[통계](docs/stats.md)      [If문](docs/scripting/if.md)      [감각](docs/unlocks/senses.md)      [혼합 재배](docs/unlocks/polyculture.md)

[harvest()](functions/harvest)      [plant()](functions/plant)
