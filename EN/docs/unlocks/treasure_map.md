[<- Iron](docs/unlocks/iron.md)
---
# Treasure Map

Legends tell of an elusive treasure hidden by a long-dead, forgetful pirate—or something like that. What if they wrote the path to the treasure on a map and then lost it? Maybe they dropped the map when cornered by a river of lava, and it was preserved below a layer of basalt. Measuring the basalt might reveal something.

<spoiler=tell me more>
You should look out for a layer of `Grounds.Basalt`. Try measuring the basalt and see what it tells you. The hint might lead you to the treasure map and measuring the map will surely return you the path to the treasure itself – but can you decipher the instructions the map gives you?
</spoiler>

<spoiler=just tell me how>
Okay, here's the deal: find the `Grounds.Basalt` stratum and the `Grounds.Treasure_Map` block directly below it. You can `measure()` the basalt to get the `(x, y)` position of the map block below.

Call `measure()` on the map block to get the treasure path as a string of direction letters. N, E, S, and W stand for `North`, `East`, `South`, and `West`, respectively, while D stands for "Down" or "Dig." These letters describe a path made of `Grounds.Treasure_Path` blocks that leads to the treasure.

```
path = measure()
for letter in path:
    do_something(letter)
```

The drone that digs into the treasure map block is the drone that has to find the treasure. It has to stay on top of `Grounds.Treasure_Path` blocks the whole time. If it moves to other ground, the path will break and the treasure will be lost.

At the end of the path is a `Grounds.Treasure_Goal` block. If the drone hasn't strayed from the path, an `Entities.Underground_Treasure` will appear on top of it. The drone can `harvest()` the chest to collect its gold.

The amount of gold is proportional to the length of the treasure path. Upgrading the Treasure Map unlock increases the path's depth, while upgrading Expand gives it more room to move laterally. Both upgrades increase the treasure path's length and the amount of gold you will find.
</spoiler>

---

[Stats](docs/stats.md)      [For Loop](docs/scripting/for.md)      [Tuples](docs/scripting/tuples.md)      [Underground Senses](docs/unlocks/underground_senses.md)

[harvest()](functions/harvest)      [move()](functions/move)      [dig()](functions/dig)      [measure()](functions/measure)
