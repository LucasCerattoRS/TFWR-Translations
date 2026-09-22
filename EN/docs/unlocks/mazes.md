[<- Fertilizer](docs/unlocks/fertilizer.md) <right>[Mega Farm ->](docs/unlocks/megafarm.md)
---
# Mazes
`Items.Weird_Substance` has a strange effect on bushes. If the drone is over a bush and you call `use_item(Items.Weird_Substance, amount)`, the bush will grow into a maze of hedges.
The size of the maze depends on the amount of `Items.Weird_Substance` used (the second argument of the `use_item()` call).
Without maze upgrades, using `n` `Items.Weird_Substance` will result in an `n`x`n` maze. Each maze upgrade level doubles the treasure, but it also doubles the amount of `Items.Weird_Substance` needed.
So to make a full field maze:

{{codeexample 
{
    "camera_position": {"x": -1, "y": 2.4, "z": 5},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": false,
    "collapsing": true,
    "autoplay": false,
    "items": [{"item": "weird_substance", "n": 10}],
    "world_size": {"x": 4, "y": 4},
    "execution_speed": 1,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 1,
    "seed": -1,
    "exclude_unlocks": ["watering"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
#CODE
plant(Entities.Bush)
size = get_world_size()
substance = size * 2**(num_unlocked(Unlocks.Mazes) - 1)
use_item(Items.Weird_Substance, substance)
}}


For some reason the drone can't fly over the hedges, even though they don't look that high.

There is a treasure hidden somewhere in the maze. Use `harvest()` on the treasure to receive gold equal to the area of the maze. For example, a 5x5 maze will yield 25 gold.

If you use `harvest()` anywhere else, the maze will simply disappear.

`get_entity_type()` is equal to `Entities.Treasure` if the drone is over the treasure and `Entities.Hedge` everywhere else in the maze.

Mazes do not contain any loops unless you reuse them (see below). Therefore, the drone cannot return to the same position without retracing its path.

You can check if there is a wall by trying to move through it. 
`move()` returns `True` if it succeeded and `False` otherwise.

`can_move()` can be used to check if there is a wall without moving.

{{codeexample 
{
    "camera_position": {"x": -1, "y": 2.4, "z": 5},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": true,
    "collapsing": true,
    "autoplay": false,
    "items": [{"item": "weird_substance", "n": 10}],
    "world_size": {"x": 4, "y": 4},
    "execution_speed": 1,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 100,
    "seed": 1,
    "exclude_unlocks": ["watering"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
move(East)
plant(Entities.Bush)
size = get_world_size()
substance = size * 2**(num_unlocked(Unlocks.Mazes) - 1)
use_item(Items.Weird_Substance, substance)
#CODE
quick_print(
    can_move(North), 
    can_move(East), 
    can_move(South), 
    can_move(West)
)
if move(North) and get_entity_type() == Entities.Treasure:
    harvest()
}}

If you have no idea how to get to the treasure, take a look at Hint 1. It shows you how to approach a problem like this.

Using `measure()` anywhere in the maze returns the position of the treasure.
`x, y = measure()`

For an extra challenge, you can reuse the maze by using the same amount of `Items.Weird_Substance` on the treasure again.
This will collect the treasure and spawn a new treasure at a random position in the maze.

Each time the treasure is moved, some of the maze's walls may be randomly removed. So reused mazes can contain loops.

Note that loops in the maze make it much more difficult because it means that you can get to the same location again without moving back.
Reusing a maze doesn't give you more gold than just harvesting and spawning a new maze.
This is 100% an extra challenge that you can just skip.
It's only worth it if the extra information and the shortcuts help you solve the maze faster.

The treasure can be relocated up to 300 times. After that, using Weird Substance on it will no longer increase the gold it contains or move it.

<spoiler=show hint 1>
Here's a general approach to solving the problem:

Create a maze and imagine that you are the drone.

Think about how you would try to find the treasure if you were in the maze.

Write down your strategy step by step so that someone else could follow it without thinking.

Now try translating your steps into code.
</spoiler>
<spoiler=show hint 2>
As long as there are no loops, all the walls form one large connected wall. If you put your left hand on the wall and follow it, it will lead you through the whole maze.
This approach requires very little code and you do not need to keep track of where you have already been. Around 10 lines of code is all you need for this.
{{codeexample 
{
    "camera_position": {"x": -1, "y": 2.4, "z": 5},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": false,
    "show_inventory": true,
    "show_output": true,
    "collapsing": false,
    "autoplay": true,
    "items": [{"item": "weird_substance", "n": 10}],
    "world_size": {"x": 4, "y": 4},
    "execution_speed": 2,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 1,
    "seed": -1,
    "exclude_unlocks": ["watering"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
plant(Entities.Bush)
size = get_world_size()
substance = size * 2**(num_unlocked(Unlocks.Mazes) - 1)
use_item(Items.Weird_Substance, substance)
#CODE
directions = [North, East, South, West]
index = 0
while get_entity_type() != Entities.Treasure:
    index = (index - 1) % 4
    for _ in range(4):
        if move(directions[index]):
            break
        index = (index + 1) % 4
do_a_flip()
harvest()
}}
</spoiler>
<spoiler=show hint 3>
Instead of moving the drone in absolute directions like east or west, it can be useful to move it in relative directions like "turn right" or "turn left." To do this, you need to keep track of the direction in which the drone is currently moving. The drone never actually rotates, but you can still maintain a "virtual" rotation in code.
The following index trick is helpful for this:

{{codeexample 
{
    "camera_position": {"x": -1, "y": 1.8, "z": 5},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": true,
    "collapsing": true,
    "autoplay": false,
    "items": [{"item": "weird_substance", "n": 10}],
    "world_size": {"x": 3, "y": 3},
    "execution_speed": 1,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 200,
    "seed": 1,
    "exclude_unlocks": ["watering"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
#CODE
directions = [North, East, South, West]
index = 0
move(directions[index])

#turn right
index = (index + 1) % 4
move(directions[index])

#turn left
index = (index - 1) % 4
move(directions[index])
}}


`% 4` is used to allow it to rotate "around the circle", so that `3 (West) + 1` is `0 (North)` again because `4 % 4 == 0` and `-1 % 4 == 3`.</spoiler>
<spoiler=show hint 4>
If you can't solve it, you can always simplify the problem by using a less efficient approach.
Solving a `1`x`1` maze is trivial.</spoiler>

---

[Stats](docs/stats.md)      [Lists](docs/scripting/lists.md)      [Dictionaries](docs/scripting/dicts.md)      [Tuples](docs/scripting/tuples.md)

[harvest()](functions/harvest)      [plant()](functions/plant)      [can_move()](functions/can_move)      [move()](functions/move)      [use_item()](functions/use_item)
