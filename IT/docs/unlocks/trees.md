[<- Carote](docs/unlocks/carrots.md) <right>[Zucche ->](docs/unlocks/pumpkins.md)
---
# Alberi
Gli [alberi](objects/tree) sono un modo migliore per ottenere legno rispetto ai cespugli. Danno 5 legni ciascuno. Come i cespugli, possono essere piantati su erba o terra.

Agli alberi piace avere un po' di spazio e piantarli uno accanto all'altro rallenterà la loro crescita. Il tempo di crescita è raddoppiato per ogni albero che si trova su una casella direttamente a nord, est, ovest o sud di esso. Quindi, se pianti alberi su ogni casella, impiegheranno `2*2*2*2 = 16` volte più tempo a crescere.
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

<spoiler=mostra> 
Qui può essere utile l'operatore `%`. L'operatore `%` restituisce il resto della divisione. I numeri pari divisi per `2` hanno resto `0`, mentre i numeri dispari divisi per `2` hanno resto `1`.
Quindi puoi controllare se un numero è pari in questo modo:

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

[Statistiche](docs/stats.md)      [Operatori](docs/scripting/operators.md)      [If](docs/scripting/if.md)      [Ciclo For](docs/scripting/for.md)      [Policoltura](docs/unlocks/polyculture.md)

[harvest()](functions/harvest)      [plant()](functions/plant)      [move()](functions/move)
