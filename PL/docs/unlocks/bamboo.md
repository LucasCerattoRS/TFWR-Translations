[<- Ryż](docs/unlocks/rice.md) <right>[Kolorowe bloki ->](docs/unlocks/debug_place.md)
<right>[Piramidy ->](docs/unlocks/pyramid.md)
---
# Bambus

Bambus to roślina, która może urosnąć na wysokość 6 bloków. Nie rośnie, gdy znajduje się nad nim dron, więc po użyciu `plant(Entities.Bamboo)` pamiętaj, aby wykonać `move`. Sadzenie bambusa kosztuje ryż.

Bambus zakwita po osiągnięciu pewnej losowo wybranej wysokości. Użyj `measure()`, aby sprawdzić, na jakiej wysokości zakwitnie. `measure()` liczy od 0, więc jeśli bambus zakwitnie na drugim bloku, `measure()` zwróci 1:

{{codeexample 
{
    "camera_position": {"x": -1, "y": 0, "z": 8},
    "show_image": true,
    "image_size": {"x": 1000, "y": 500},
    "show_code": true,
    "show_inventory": true,
    "show_output": false,
    "collapsing": true,
    "autoplay": false,
    "items": [{"item": "rice", "n": 100}],
    "world_size": {"x": 4, "y": 4},
    "execution_speed": 2,
    "action_ticks": 200,
    "operation_ticks": 200,
    "seed": 1,
    "exclude_unlocks": ["watering", "fertilizer", "mushrooms", "coal"]
}
#SETUP
move(North)
move(East)
#CODE
till()
plant(Entities.Bamboo)
print(measure())
move(East)
}}

Największy plon bambusa uzyskasz, gdy wykonasz `harvest()`, znajdując się dronem bezpośrednio nad kwiatem. Każdy blok różnicy zmniejsza plon ośmiokrotnie.
Jeśli na przykład kwiat znajduje się na wysokości 3, ale zbierzesz bambus dwa bloki wyżej, plon zostanie podzielony przez 64.

Aby zebrać kwiaty znajdujące się wyżej, wleć w bambus, gdy dron jest na odpowiedniej wysokości. Pomaga w tym nowo odblokowane polecenie `place()`.

Użyj `place(Grounds.Dirt)`, aby ułożyć obok bambusa stos bloków i wspiąć się wyżej. Następnie użyj `move()`, aby wlecieć w bambus z boku. Podczas wywoływania `harvest()` dron powinien znajdować się bezpośrednio nad kwiatem.

`place(Grounds.Dirt)` kosztuje 1 blok! Możesz umieszczać także inne podłoża, takie jak `Grounds.Rock`, ale nie specjalne bloki, takie jak `Grounds.Clay`.

Bambus rośnie dokładnie o 1 blok na sekundę.

{{codeexample 
{
    "camera_position": {"x": -1, "y": 0, "z": 8},
    "show_image": true,
    "image_size": {"x": 1000, "y": 500},
    "show_code": true,
    "show_inventory": true,
    "show_output": false,
    "collapsing": true,
    "autoplay": false,
    "items": [{"item": "block", "n": 100}, {"item": "rice", "n": 100}],
    "world_size": {"x": 4, "y": 4},
    "execution_speed": 2,
    "action_ticks": 200,
    "operation_ticks": 200,
    "seed": 1,
    "exclude_unlocks": ["watering", "fertilizer", "mushrooms", "coal"]
}
#SETUP
move(North)
move(East)
#CODE
till()
plant(Entities.Bamboo)
print(measure())
move(East)
place(Grounds.Dirt)
do_a_flip() # poczekaj chwilę
do_a_flip()
move(West)
harvest()
}}

---

[Statystyki](docs/stats.md)      [Pętla For](docs/scripting/for.md)      [Zmienne](docs/scripting/variables.md)      [If](docs/scripting/if.md)      [Funkcje](docs/scripting/functions.md)      [Ryż](docs/unlocks/rice.md)

[harvest()](functions/harvest)      [plant()](functions/plant)      [move()](functions/move)      [till()](functions/till)      [place()](functions/place)      [measure()](functions/measure)
