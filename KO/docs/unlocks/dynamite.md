[<- 버섯](docs/unlocks/mushroom.md)
---
# 다이너마이트

이전의 채광 원정대가 남긴 혁명적인 폭발물이에요. 다행이라고 해야 할지 불행이라고 해야 할지, 드론의 드릴은 다이너마이트를 폭발시켜 주변의 모든 블록을 날려 버리기에 안성맞춤이에요.

다이너마이트를 안전하게 채굴하려면 `Grounds.Dynamite`와 `Grounds.Soot`의 이중 지층을 찾아야 해요. 위쪽의 다이너마이트 땅은 조금 낡아서 일부 블록은 안전하게 파낼 수 있어요. 하지만 일부는 아직 활성 상태라 파면 폭발해요.

{{codeexample 
{
    "camera_position": {"x": -3, "y": -3, "z": 12},
    "show_image": true,
    "image_size": {"x": 900, "y": 500},
    "show_code": true,
    "show_inventory": true,
    "show_output": false,
    "collapsing": false,
    "autoplay": true,
    "items": [{"item": "hay", "n": 100}],
    "world_size": {"x": 5, "y": 5},
    "execution_speed": 8,
    "digging_speed": 8,
    "action_ticks": 200,
    "operation_ticks": 200,
    "seed": 4,
    "exclude_unlocks": ["watering", "fertilizer", "mushrooms", "coal", "quartz", "petrified_pumpkins"]
}
#SETUP
jump(Unlocks.Dynamite)
#CODE
while get_ground_type() != Grounds.Soot:
    dig()
dig()
dig()
}}

불발탄 블록을 모두 찾아 파내고 활성 블록만 남길 수 있을까요? 활성 블록이나 그을음 블록으로만 둘러싸인 활성 블록은 다이너마이트 지층이 사라질 때 추가 다이너마이트를 줘요.

다행히 아래의 그을음 블록이 도와줄 거예요. 이 블록은 인접한 다이너마이트 블록 중 활성 다이너마이트가 든 블록의 수를 감지할 수 있어요. 어느 블록이 활성인지는 알려주지 않고 총개수만 알려주므로, 여러 그을음 블록의 측정값을 조합해 스스로 추론해야 해요.

그을음 블록에서 `measure()`를 호출하면 위쪽 다이너마이트 지층의 인접한 여덟 타일에 있는 지뢰 수를 반환해요. 숫자는 `0`(활성 지뢰 없음)부터 `8`(모든 인접 블록에 활성 지뢰가 있음)까지예요.

다이너마이트 지층에서 처음 파는 블록은 항상 불발탄이에요. 다이너마이트 블록을 파면 다이너마이트를 조금 얻어요. 모든 불발탄을 성공적으로 파내거나 활성 다이너마이트를 실수로 파서 지층이 파괴되면, 완전히 드러난 활성 블록 수의 제곱만큼 다이너마이트를 추가로 얻어요.

활성 다이너마이트를 파면 두 지층이 폭발해요. `Grounds.Dynamite`를 판 뒤 `get_ground_type()`을 사용해 이를 확인할 수 있어요. 땅이 `Grounds.Soot`가 아니라면 퍼즐에 실패한 거예요. 반대로 마지막 비활성 다이너마이트 블록을 파내면 모든 다이너마이트 블록이 사라지고 퍼즐에서 얻을 수 있는 최대 수확량을 받아요. 그을음 지층은 남지만 `measure()`가 `None`을 반환해 퍼즐을 성공적으로 풀었음을 알려 줘요.

`# 다이너마이트 블록을 파고 퍼즐 상태 확인
def dig_dynamite():
    dig()
    if get_ground_type() != Grounds.Soot:
        # 활성 다이너마이트를 팠음, 퍼즐 실패
        return False
    elif measure() == None:
        # 마지막 불발탄 블록을 팠음, 퍼즐 성공
        return True
    else:
        # 측정값을 얻었음, 퍼즐 진행 중
        return None
`

다이너마이트 지층의 활성 지뢰 수와 그것을 찾는 난이도는 깊이에 따라 증가해요.

모은 다이너마이트는 `use_item(Items.Dynamite)`로 사용할 수 있으며 드론 바로 아래에서 즉시 폭발해요.

다이너마이트를 업그레이드하면 다이너마이트 블록을 파거나 활성 블록을 완전히 드러내서 얻는 수확량이 늘어나요. 또한 다이너마이트 폭발 에너지가 30% 증가해요.

---

[통계](docs/stats.md)      [지하 감각](docs/unlocks/underground_senses.md)      [딕셔너리](docs/scripting/dicts.md)      [세트](docs/scripting/sets.md)

[move()](functions/move)      [dig()](functions/dig)      [measure()](functions/measure)      [use_item()](functions/use_item)
