[<- Podlewanie](docs/unlocks/watering.md)
---
# Słoneczniki
[Słoneczniki](objects/sunflower) zbierają energię słoneczną. Możesz zbierać tę energię. 
Sadzenie ich działa dokładnie tak samo, jak sadzenie marchewek czy dyń. 

Zebranie dojrzałego słonecznika daje energię.
Jeśli na farmie znajduje się co najmniej 10 słoneczników i zbierzesz jeden z największą liczbą płatków, otrzymasz `8` razy więcej energii!
Jeśli zbierzesz słonecznik, podczas gdy inny ma więcej płatków, następny zebrany słonecznik również da tylko zwykłą ilość energii (bez premii 8x).

`measure()` zwraca liczbę płatków słonecznika pod dronem.
Słoneczniki mają co najmniej `7` i co najwyżej `15` płatków.
Można je mierzyć jeszcze przed pełnym wzrostem i już wtedy wliczają się do limitu 10 słoneczników.

Kilka słoneczników może mieć tę samą liczbę płatków, więc kilka może mieć ich najwięcej. W takim przypadku nie ma znaczenia, który zbierzesz.

{{codeexample 
{
    "camera_position": {"x": -1.5, "y": 2, "z": 4},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "inventory_scale": 5,
    "show_output": false,
    "collapsing": true,
    "autoplay": false,
    "items": [{"item": "carrot", "n": 10}],
    "world_size": {"x": 5, "y": 2},
    "execution_speed": 2,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 1,
    "seed": 4,
    "exclude_unlocks": ["fertilizer", "watering"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
move(North)
for _ in range(5):
    till()
    plant(Entities.Sunflower)
    move(East)
move(North)
do_a_flip()
do_a_flip()
do_a_flip()
do_a_flip()
do_a_flip()
#CODE
for _ in range(5):
    till()
    plant(Entities.Sunflower)
    print(measure())
    move(East)
for _ in range(5):
    while not can_harvest():
        pass
    harvest()
    move(East)
}}

Dopóki masz energię, dron będzie jej używał, aby działać dwa razy szybciej.
Zużywa 1 jednostkę energii co 30 akcji, takich jak ruch, zbiór czy sadzenie.
Wykonywanie innych instrukcji kodu również może zużywać energię, ale znacznie mniej niż akcje drona.
Ogólnie rzecz biorąc, wszystko, co jest przyspieszane przez ulepszenia prędkości, jest również przyspieszane przez energię.
Wszystko, co jest przyspieszane przez energię, zużywa ją proporcjonalnie do czasu potrzebnego na wykonanie, ignorując ulepszenia prędkości.

---

[Statystyki](docs/stats.md)      [Listy](docs/scripting/lists.md)      [Słowniki](docs/scripting/dicts.md)      [Zmienne](docs/scripting/variables.md)      [Pętla For](docs/scripting/for.md)      [If](docs/scripting/if.md)      [Operatory](docs/scripting/operators.md)

[harvest()](functions/harvest)      [plant()](functions/plant)      [move()](functions/move)      [till()](functions/till)      [measure()](functions/measure)
