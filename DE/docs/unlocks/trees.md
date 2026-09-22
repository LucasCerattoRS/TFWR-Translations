[<- Karotten](docs/unlocks/carrots.md) <right>[Kürbisse ->](docs/unlocks/pumpkins.md)
---
# Bäume
[Bäume](objects/tree) sind eine bessere Möglichkeit, Holz zu bekommen als Büsche. Sie geben jeweils 5 Holz. Wie Büsche können sie auf Gras oder Ackerboden gepflanzt werden.

Bäume mögen etwas Platz, und wenn man sie direkt nebeneinander pflanzt, verlangsamt das ihr Wachstum. Die Wachstumszeit verdoppelt sich für jeden Baum, der sich auf einem Feld direkt nördlich, östlich, westlich oder südlich davon befindet. Wenn du also auf jedes Feld Bäume pflanzt, brauchen sie `2*2*2*2 = 16` mal länger zum Wachsen.
{{codeexample 
{
    "camera_position": {"x": -1, "y": 1.8, "z": 5},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": false,
    "show_inventory": true,
    "show_output": false,
    "collapsing": false,
    "autoplay": true,
    "items": [],
    "world_size": {"x": 3, "y": 3},
    "execution_speed": 10,
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
for i in range(get_world_size()):
	for j in range(get_world_size()):
		plant(Entities.Tree)
		move(North)
	move(East)
}}

<spoiler=Anzeigen> 
Der `%`-Operator kann hier nützlich sein. Denk daran, dass der `%`-Operator den Rest der Division zurückgibt. Gerade Zahlen geteilt durch `2` haben einen Rest von `0` und ungerade Zahlen geteilt durch `2` haben einen Rest von `1`.
Du kannst also so überprüfen, ob eine Zahl gerade ist:

{{codeexample 
{
    "camera_position": {"x": -0.5, "y": 1.5, "z": 4},
    "show_image": false,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": false,
    "show_output": true,
    "collapsing": true,
    "autoplay": false,
    "items": [],
    "world_size": {"x": 2, "y": 1},
    "execution_speed": 1,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 200,
    "seed": 1,
    "exclude_unlocks": ["watering", "fertilizer"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
#CODE
def is_even(n):
	return n % 2 == 0

print("is_even(0): ", is_even(0))
print("is_even(1): ", is_even(1))
print("is_even(2): ", is_even(2))
print("is_even(5): ", is_even(5))
print("is_even(-1): ", is_even(-1))
print("is_even(x): ", is_even(get_pos_x()))
}}
</spoiler>

---

[Statistiken](docs/stats.md)      [Operatoren](docs/scripting/operators.md)      [If](docs/scripting/if.md)      [For-Schleife](docs/scripting/for.md)      [Polykultur](docs/unlocks/polyculture.md)

[harvest()](functions/harvest)      [plant()](functions/plant)      [move()](functions/move)
