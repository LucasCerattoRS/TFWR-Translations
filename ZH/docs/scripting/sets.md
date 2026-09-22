[<- 字典](docs/scripting/dicts.md)
---
# 集合
集合就像[字典](docs/scripting/dicts.md)，但是没有值，仅由一组无序的键构成。

它的创建方式类似字典，只是没有值。
`set = {North, East, West}`

调用 `set()` 函数创建一个空集合。注意，`{}` 创建的是一个空字典。

调用 `set.add(elem)` 函数向集合添加 1 个新元素。

调用 `set.remove(elem)` 函数从集合中删除 1 个元素。

调用 `if elem in set:` 函数判断集合是否包含某个元素。

调用 `for elem in set:` 函数迭代集合中的所有元素。
对于较大的集合，`in` 运算符的执行速度比在列表上快得多。

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
    print("North 在集合中")
else:
    print("North 不在集合中")
for element in my_set:
    print(element)
}}

集合与字典一样是无序的，所以无法保证元素迭代的顺序。

此外，集合中的元素是唯一的，所以添加一个已存在于集合中的元素不会改变集合。

---

[字典](docs/scripting/dicts.md)      [列表](docs/scripting/lists.md)      [For 循环](docs/scripting/for.md)

[len()](functions/len)
