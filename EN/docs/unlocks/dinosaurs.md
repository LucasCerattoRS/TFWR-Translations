[<- Cactus](docs/unlocks/cactus.md)
---
# Dinosaurs
Dinosaurs are ancient, majestic creatures that can be farmed for ancient bones.

Unfortunately, dinosaurs went extinct a long time ago, so the best we can do now is dress up as one.
For this purpose, you have received the new dinosaur hat.

The hat can be equipped with
`change_hat(Hats.Dinosaur_Hat)`

Unfortunately, it doesn't look quite like it did in the advertisement...

If you equip the dinosaur hat and have enough cactus, an [apple](objects/apple) will automatically be purchased and placed under the drone.
When the drone is over an apple and moves again, it will eat the apple and grow its tail by one. If you can afford it, a new apple will be purchased and placed in a random location.
The apple cannot spawn if something else is planted where it wants to be.

The dinosaur's tail is dragged behind the drone, filling the tiles the drone previously moved over. If the drone tries to move onto its tail, `move()` will fail and return `False`.
The last segment of the tail will move out of the way during a move, so you can move onto it. However, if the snake fills the entire farm, you will no longer be able to move. You can therefore check whether the snake is fully grown by checking whether you can still move.
While wearing the dinosaur hat, the drone can't move over the farm border to get to the other side.

Using `measure()` on an apple will return the position of the next apple as a tuple.

`next_x, next_y = measure()`

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
    "items": [{"item": "cactus", "n": 10000}],
    "world_size": {"x": 4, "y": 4},
    "execution_speed": 2,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 1,
    "seed": 5,
    "exclude_unlocks": ["watering"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
#CODE
change_hat(Hats.Dinosaur_Hat)
while True:
    next_x, next_y = measure()
    while get_pos_x() != next_x:
        move(East)
    while get_pos_y() != next_y:
        move(North)
}}

When the hat is unequipped again by equipping a different hat, the tail will be harvested.
You will receive an amount of bones equal to the tail length squared. For a tail of length `n`, you will receive `n**2` `Items.Bone`.
For example:
length 1 => 1 bone
length 2 => 4 bones
length 3 => 9 bones
length 4 => 16 bones
length 16 => 256 bones
length 100 => 10000 bones

The Dinosaur Hat is very heavy, so if you equip it, it will make `move()` take 400 ticks instead of 200. However, each time you pick up an apple, the number of ticks used by `move()` is reduced by 3% (rounded down), because a longer tail can help you move.

The following loop prints the number of ticks used by `move()` after any number of apples:

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
    "operation_ticks": 1,
    "seed": 1,
    "exclude_unlocks": ["watering", "fertilizer"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
#CODE
ticks = 400
for i in range(100):
    quick_print("ticks after ", i, " apples: ", ticks)
    ticks -= ticks * 0.03 // 1
}}

You only have one dinosaur hat, so only one drone can wear it.

<spoiler=show hint 1>
If you keep moving along the same path that covers the whole field, you can easily get a snake that covers the whole field every time. It's not very efficient, but it works.
Fully traversing a very large farm can take a long time and you might not actually need that many bones. Feel free to use `set_world_size()` to change the size of the farm to something more convenient.</spoiler>

---

[Stats](docs/stats.md)      [Tuples](docs/scripting/tuples.md)      [Lists](docs/scripting/lists.md)

[change_hat()](functions/change_hat)      [move()](functions/move)      [measure()](functions/measure)
