[<- Pumpkins](docs/unlocks/pumpkins.md) <right>[Dinosaurs ->](docs/unlocks/dinosaurs.md)
---
# Cactus
Like other plants, [cacti](objects/cactus) can be grown on soil and harvested as usual.

However, they come in various sizes and have a strange sense of order.

If you harvest a fully-grown cactus and all neighboring cacti are in sorted order, it will also harvest all neighboring cacti recursively.

A cactus is considered to be in sorted order if all neighboring cacti to the `North` and `East` are fully grown and greater than or equal to it in size, while all neighboring cacti to the `South` and `West` are fully grown and less than or equal to it in size.

The harvest will only spread if all adjacent cacti are fully grown and in sorted order.
This means that if a square of grown cacti is sorted by size and you harvest one cactus, it will harvest the entire square.

A fully grown cactus will appear brown if it is not sorted. Once sorted, it will turn green again.

You will receive an amount of cactus equal to the number of harvested cacti squared. If you harvest `n` cacti simultaneously, you will receive `n**2` `Items.Cactus`.

The size of a cactus can be measured with `measure()`.
It is always one of these numbers: `0,1,2,3,4,5,6,7,8,9`.

You can also pass a direction into `measure(direction)` to measure the neighboring tile in that direction of the drone.

You can swap a cactus with its neighbor in any direction using the `swap()` command.
`swap(direction)` swaps the object under the drone with the object one tile in the `direction` of the drone.

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

## Number Examples
In each of these grids, all the cacti are in sorted order and the harvest will spread over the entire field:
`3 4 5    3 3 3    1 2 3    1 5 9
2 3 4    2 2 2    1 2 3    1 3 8
1 2 3    1 1 1    1 2 3    1 3 4`

In this grid, only the lower left cactus is in sorted order, which is not enough for it to spread:
`1 5 3
4 9 7
3 3 2`

<spoiler=show hint 1>
If each row is already sorted independently, sorting each column independently will not unsort the rows.
</spoiler>
<spoiler=show hint 2>
There are many clever, well-known sorting algorithms. If you're not familiar with them, you might want to research them and consider which ones could be adapted to this problem. Keep in mind that not all of them work here because you can only swap neighboring cacti.
</spoiler>
<spoiler=show hint 3>
The "bubble sort" is possibly the simplest sorting algorithm. The idea is to repeatedly go over the elements, swapping any adjacent elements that are in the wrong order, until there are none left.

Here's what this looks like with cacti:
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
There are of course many ways to improve this strategy!
After you manage to sort a single row, you can use Hint 1 to sort the entire field.
</spoiler>

---

[Stats](docs/stats.md)

[harvest()](functions/harvest)      [plant()](functions/plant)      [move()](functions/move)      [till()](functions/till)      [swap()](functions/swap)      [measure()](functions/measure)
