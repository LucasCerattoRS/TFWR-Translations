[<- Mushroom](docs/unlocks/mushroom.md)
---
# Dynamite

The revolutionary explosive, left behind by previous mining expeditions. (Un-)fortunately, your drill is perfect to make dynamite explode, blasting away all the blocks around you.

To safely mine dynamite, you'll have to find the double-stratum of `Grounds.Dynamite` and `Grounds.Soot`. The dynamite ground above has gotten a bit old, and some of its blocks are safe to dig into. However, some of the dynamite is still live and will explode when dug.

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

Can you find and dig all the dud blocks, leaving only live blocks behind? Every live block that's surrounded only by other live blocks or soot blocks will yield you extra dynamite once the dynamite stratum disappears.

Luckily, the soot blocks below will help you: they can detect the number of neighboring dynamite blocks that contain live dynamite. They won't tell you exactly which blocks are live, only the total number, so you need to combine the readings from multiple soot blocks and work it out yourself.

Calling `measure()` on a soot block returns the number of mines in the eight neighboring tiles on the dynamite stratum above. The number can range from `0` (no live mines) to `8` (every neighbor contains a live mine).

The first dig into the dynamite stratum is always a dud. Every mined block of dynamite yields a bit of dynamite. When the dynamite stratum is destroyed, either through successfully digging up all the duds or by inadvertently digging into live dynamite, you also gain dynamite equal to the number of fully uncovered live blocks, squared.

If dig into live dynamite, the two strata explode. You can check for this using `get_ground_type()` after digging into `Grounds.Dynamite`. If the ground is not `Grounds.Soot`, you failed solving the puzzle. On the other hand, if the last non-live dynamite block is dug up, all dynamite blocks disappear and you earn the max amount of yield for the puzzle. The soot stratum remains but `measure()` returns `None`, indicating the puzzle was solved successfully.

`# Dig into a dynamite block and check the puzzle state
def dig_dynamite():
    dig()
    if get_ground_type() != Grounds.Soot:
        # Dug into live dynamite, puzzle failed
        return False
    elif measure() == None:
        # Dug up final dud block, puzzle solved
        return True
    else:
        # Got a count from measuring, puzzle still ongoing
        return None
`

The number of live mines in the dynamite stratum and therefore the difficulty of finding them increases with depth.

Collected dynamite can be used with `use_item(Items.Dynamite)` and explodes immediately below the drone.

Upgrade dynamite to increase the yield of digging into dynamite blocks and fully uncovering live blocks. The upgrade also increases the energy of dynamite explosions by 30%.

---

[Stats](docs/stats.md)      [Underground Senses](docs/unlocks/underground_senses.md)      [Dictionaries](docs/scripting/dicts.md)      [Sets](docs/scripting/sets.md)

[move()](functions/move)      [dig()](functions/dig)      [measure()](functions/measure)      [use_item()](functions/use_item)
