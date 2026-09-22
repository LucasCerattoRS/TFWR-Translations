[<- Kaktus](docs/unlocks/cactus.md)
---
# Dinozaury
Dinozaury to starożytne, majestatyczne stworzenia, które można hodować dla starożytnych kości.

Niestety dinozaury wyginęły dawno temu, więc najlepsze, co możemy teraz zrobić, to przebrać się za jednego.
W tym celu otrzymałeś nowy kapelusz dinozaura.

Kapelusz można założyć za pomocą
`change_hat(Hats.Dinosaur_Hat)`

Niestety nie wygląda on całkiem tak jak w reklamie...

Jeśli założysz kapelusz dinozaura i masz wystarczająco dużo kaktusów, [jabłko](objects/apple) zostanie automatycznie zakupione i umieszczone pod dronem.
Gdy dron znajdzie się nad jabłkiem i ponownie się poruszy, zje jabłko i jego ogon urośnie o jeden. Jeśli cię na to stać, nowe jabłko zostanie zakupione i umieszczone w losowej lokalizacji.
Jabłko nie może się pojawić, jeśli coś innego jest posadzone tam, gdzie chce być.

Ogon dinozaura ciągnie się za dronem, zajmując pola, nad którymi dron wcześniej się poruszał. Jeśli dron spróbuje wejść na własny ogon, `move()` nie powiedzie się i zwróci `False`.
Ostatni segment ogona usunie się z drogi podczas ruchu, więc możesz na niego wejść. Jeśli jednak wąż wypełni całą farmę, nie będzie można się już poruszyć. Możesz więc sprawdzić, czy wąż jest w pełni wyrośnięty, sprawdzając, czy nie możesz się już poruszać.
Nosząc kapelusz dinozaura, dron nie może przekroczyć granicy farmy, aby przejść na drugą stronę.

Użycie `measure()` na jabłku zwróci pozycję następnego jabłka jako krotkę.

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

Gdy kapelusz zostanie zdjęty przez założenie innego, ogon zostanie zebrany.
Otrzymasz liczbę kości równą kwadratowi długości ogona. Za ogon o długości `n` otrzymasz `n**2` `Items.Bone`.
Na przykład:
długość 1 => 1 kość
długość 2 => 4 kości
długość 3 => 9 kości
długość 4 => 16 kości
długość 16 => 256 kości
długość 100 => 10000 kości

Kapelusz dinozaura jest bardzo ciężki, więc jeśli go założysz, wykonanie `move()` zajmie 400 ticków zamiast 200. Jednak za każdym razem, gdy podniesiesz jabłko, liczba ticków używanych przez `move()` jest zmniejszana o 3% (zaokrąglone w dół), ponieważ dłuższy ogon może pomóc w poruszaniu się.

Poniższa pętla wyświetla liczbę ticków używanych przez `move()` po dowolnej liczbie jabłek:

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
    quick_print("ticków po ", i, " jabłkach: ", ticks)
    ticks -= ticks * 0.03 // 1
}}

Masz tylko jeden kapelusz dinozaura, więc tylko jeden dron może go nosić.

<spoiler=pokaż podpowiedź 1>
Jeśli będziesz poruszać się po tej samej ścieżce, która obejmuje całe pole, możesz łatwo uzyskać węża, który za każdym razem obejmuje całe pole. Nie jest to bardzo wydajne, ale działa.
Pełne przemierzenie bardzo dużej farmy może zająć dużo czasu i być może nie potrzebujesz aż tylu kości. Możesz użyć `set_world_size()`, aby zmienić rozmiar farmy na coś wygodniejszego.</spoiler>

---

[Statystyki](docs/stats.md)      [Krotki](docs/scripting/tuples.md)      [Listy](docs/scripting/lists.md)

[change_hat()](functions/change_hat)      [move()](functions/move)      [measure()](functions/measure)
