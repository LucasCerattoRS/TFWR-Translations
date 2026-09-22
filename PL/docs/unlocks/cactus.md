[<- Dynie](docs/unlocks/pumpkins.md) <right>[Dinozaury ->](docs/unlocks/dinosaurs.md)
---
# Kaktus
Podobnie jak inne rośliny, [kaktusy](objects/cactus) można uprawiać na glebie i zbierać jak zwykle.

Jednak występują w różnych rozmiarach i mają dziwne poczucie porządku.

Jeśli zbierzesz w pełni wyrośniętego kaktusa, a wszystkie sąsiednie kaktusy są posortowane, rekurencyjnie zbierze on również wszystkie sąsiednie kaktusy.

Kaktus jest uznawany za posortowany, jeśli wszystkie sąsiednie kaktusy na `North` i `East` są w pełni wyrośnięte i większe lub równe mu rozmiarem, a wszystkie sąsiednie kaktusy na `South` i `West` są w pełni wyrośnięte i mniejsze lub równe mu rozmiarem.

Zbiór rozprzestrzeni się tylko wtedy, gdy wszystkie sąsiadujące kaktusy są w pełni wyrośnięte i posortowane.
Oznacza to, że jeśli kwadrat wyrośniętych kaktusów jest posortowany według rozmiaru i zbierzesz jeden kaktus, zbierze on cały kwadrat.

W pełni wyrośnięty kaktus będzie brązowy, jeśli nie jest posortowany. Gdy zostanie posortowany, znów stanie się zielony.

Otrzymasz kaktusy w liczbie równej kwadratowi liczby zebranych kaktusów. Jeśli zbierzesz `n` kaktusów jednocześnie, otrzymasz `n**2` `Items.Cactus`.

Rozmiar kaktusa można zmierzyć za pomocą `measure()`.
Jest to zawsze jedna z tych liczb: `0,1,2,3,4,5,6,7,8,9`.

Możesz również przekazać kierunek do `measure(direction)`, aby zmierzyć sąsiednie pole w tym kierunku od drona.

Możesz zamienić kaktusa z jego sąsiadem w dowolnym kierunku za pomocą polecenia `swap()`.
`swap(direction)` zamienia obiekt pod dronem z obiektem o jedno pole w kierunku `direction` od drona.

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

## Przykłady liczbowe
W każdej z tych siatek wszystkie kaktusy są posortowane, a zbiór rozprzestrzeni się na całe pole:
`3 4 5    3 3 3    1 2 3    1 5 9
2 3 4    2 2 2    1 2 3    1 3 8
1 2 3    1 1 1    1 2 3    1 3 4`

W tej siatce tylko lewy dolny kaktus jest posortowany, co nie wystarcza, aby zbiór się rozprzestrzenił:
`1 5 3
4 9 7
3 3 2`

<spoiler=pokaż podpowiedź 1>
Jeśli każdy wiersz jest już niezależnie posortowany, niezależne sortowanie każdej kolumny nie zaburzy porządku wierszy.
</spoiler>
<spoiler=pokaż podpowiedź 2>
Istnieje wiele pomysłowych i dobrze znanych algorytmów sortowania. Jeśli ich nie znasz, możesz je wyszukać i zastanowić się, które da się dostosować do tego problemu. Pamiętaj, że nie wszystkie tu działają, ponieważ możesz zamieniać tylko sąsiednie kaktusy.
</spoiler>
<spoiler=pokaż podpowiedź 3>
„Sortowanie bąbelkowe” jest prawdopodobnie najprostszym algorytmem sortowania. Polega na wielokrotnym przechodzeniu po elementach i zamianie sąsiednich elementów ustawionych w złej kolejności, aż nie pozostanie żadna taka para.

Tak wygląda to w przypadku kaktusów:
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
Oczywiście tę strategię można ulepszyć na wiele sposobów!
Gdy uda ci się posortować pojedynczy wiersz, możesz użyć Podpowiedzi 1, aby posortować całe pole.
</spoiler>

---

[Statystyki](docs/stats.md)

[harvest()](functions/harvest)      [plant()](functions/plant)      [move()](functions/move)      [till()](functions/till)      [swap()](functions/swap)      [measure()](functions/measure)
