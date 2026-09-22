[<- 딕셔너리](docs/scripting/dicts.md)
---
# 세트
세트는 [딕셔너리](docs/scripting/dicts.md)와 비슷하지만 값이 없어요. 순서가 없는 키의 집합일 뿐이에요.

딕셔너리처럼 만들지만 값은 없어요.
`set = {North, East, West}`

빈 세트를 만들려면 `set()`을 사용하세요. `{}`는 빈 딕셔너리를 만든다는 점에 유의하세요.

세트에 새 요소를 추가하려면 `set.add(elem)`를 사용하세요.

세트에서 요소를 제거하려면 `set.remove(elem)`를 사용하세요.

세트에 요소가 포함되어 있는지 확인하려면 `if elem in set:`를 사용하세요.

세트의 모든 요소를 반복하려면 `for elem in set:`를 사용하세요.
더 큰 세트의 경우 `in` 연산자는 리스트에서보다 훨씬 빠르게 작동해요.

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
    "operation_ticks": 100,
    "seed": 0,
    "exclude_unlocks": ["watering", "fertilizer"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
#CODE
my_set = set()
print(my_set)
my_set.add(1)
my_set.add(North)
print(my_set)
my_set.remove(North)
print(my_set)
if North in my_set:
    print("North가 세트에 있습니다")
else:
    print("North가 세트에 없습니다")
for element in my_set:
    print(element)
}}

딕셔너리와 마찬가지로 세트는 순서가 없으므로, 요소가 반복되는 순서는 보장되지 않아요.

또한, 세트의 요소는 고유하므로, 세트에 이미 있는 요소를 추가해도 세트는 변경되지 않아요.

---

[딕셔너리](docs/scripting/dicts.md)      [리스트](docs/scripting/lists.md)      [for 루프](docs/scripting/for.md)

[len()](functions/len)
