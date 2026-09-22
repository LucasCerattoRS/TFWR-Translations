[<- Kwarc](docs/unlocks/quartz.md) <right>[Dynamit ->](docs/unlocks/dynamite.md)
---
# Grzyby

W podziemnych koloniach rośnie wiele rodzajów grzybów. Podczas kopania szukaj warstwy `Grounds.Mushroom`. Następnie możesz użyć `measure()` na podłożu, aby uzyskać rodzaj grzyba jako liczbę zaczynającą się od `0`.

{{codeexample 
{
    "camera_position": {"x": -1, "y": 0, "z": 6},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": false,
    "collapsing": true,
    "autoplay": false,
    "items": [{"item": "hay", "n": 100}, {"item": "iron", "n": 100}],
    "world_size": {"x": 4, "y": 4},
    "execution_speed": 2,
    "digging_speed": 6,
    "action_ticks": 200,
    "operation_ticks": 200,
    "seed": 9,
    "exclude_unlocks": ["watering", "fertilizer", "dynamite", "iron"]
}

#SETUP
jump(Unlocks.Mushrooms)
#CODE
while get_ground_type() != Grounds.Mushroom:
    dig()
do_a_flip()
print(measure())
}}

Grzyby tego samego rodzaju lubią być razem, ale są zbyt nieśmiałe, by rosnąć jeden na drugim. Wepchnij blok grzyba na inny blok tego samego rodzaju, a oba znikną i otrzymasz w nagrodę grzyby.

Za pomocą `can_push(direction)` możesz sprawdzić, czy blok pod dronem można popchnąć i czy coś nie blokuje go w danym kierunku. `push(direction)` popycha blok i zwraca informację, czy operacja się powiodła.

Bloków nie można popychać w górę, a pchnięcie nie powiedzie się, jeśli na drodze znajduje się inny blok. Bloki wypchnięte w powietrze spadają i lądują na najbliższym bloku poniżej.

Pamiętaj, że możesz wywołać `place(Grounds.Dirt)`, aby umieszczać bloki pod dronem. Przydaje się to do wypełniania dziur, tak aby można było przepychać nad nimi inne bloki.

---

[Statystyki](docs/stats.md)      [Podziemne zmysły](docs/unlocks/underground_senses.md)      [Słowniki](docs/scripting/dicts.md)

[move()](functions/move)      [measure()](functions/measure)      [can_push()](functions/can_push)      [push()](functions/push)      [place()](functions/place)      [get_ground_type()](functions/get_ground_type)
