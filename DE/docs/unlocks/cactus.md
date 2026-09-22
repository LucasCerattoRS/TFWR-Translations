[<- Kürbisse](docs/unlocks/pumpkins.md) <right>[Dinosaurier ->](docs/unlocks/dinosaurs.md)
---
# Kaktus
Wie andere Pflanzen können [Kakteen](objects/cactus) auf Ackerboden angebaut und wie gewohnt geerntet werden.

Allerdings gibt es sie in verschiedenen Größen und sie haben einen seltsamen Sinn für Ordnung.

Wenn du einen ausgewachsenen Kaktus erntest und alle benachbarten Kakteen in sortierter Reihenfolge sind, werden auch alle benachbarten Kakteen rekursiv geerntet.

Ein Kaktus gilt als in sortierter Reihenfolge, wenn alle benachbarten Kakteen im `North` und `East` ausgewachsen und größer oder gleich groß sind und alle benachbarten Kakteen im `South` und `West` ausgewachsen und kleiner oder gleich groß sind.

Die Ernte breitet sich nur aus, wenn alle angrenzenden Kakteen ausgewachsen und in sortierter Reihenfolge sind.
Das bedeutet, wenn ein Quadrat aus gewachsenen Kakteen nach Größe sortiert ist und du einen Kaktus erntest, wird das gesamte Quadrat geerntet.

Ein ausgewachsener Kaktus erscheint braun, wenn er nicht sortiert ist. Sobald er sortiert ist, wird er wieder grün.

Du erhältst Kakteen in Höhe der Anzahl der geernteten Kakteen zum Quadrat. Wenn du also `n` Kakteen gleichzeitig erntest, erhältst du `n**2` `Items.Cactus`.

Die Größe eines Kaktus kann mit `measure()` gemessen werden.
Es ist immer eine dieser Zahlen: `0,1,2,3,4,5,6,7,8,9`.

Du kannst auch eine Richtung an `measure(direction)` übergeben, um das benachbarte Feld in dieser Richtung der Drohne zu messen.

Du kannst einen Kaktus mit seinem Nachbarn in jede Richtung mit dem `swap()`-Befehl tauschen.
`swap(direction)` tauscht das Objekt unter der Drohne mit dem Objekt ein Feld in `direction` der Drohne.

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

## Zahlenbeispiele
In jedem dieser Gitter sind alle Kakteen in sortierter Reihenfolge und die Ernte wird sich über das gesamte Feld ausbreiten:
`3 4 5    3 3 3    1 2 3    1 5 9
2 3 4    2 2 2    1 2 3    1 3 8
1 2 3    1 1 1    1 2 3    1 3 4`

In diesem Gitter ist nur der Kaktus unten links in sortierter Reihenfolge, was nicht ausreicht, damit sich die Ernte ausbreitet:
`1 5 3
4 9 7
3 3 2`

<spoiler=zeige Hinweis 1>
Wenn jede Zeile bereits unabhängig sortiert ist, wird das unabhängige Sortieren jeder Spalte die Zeilen nicht unsortieren.
</spoiler>
<spoiler=zeige Hinweis 2>
Es gibt viele ausgeklügelte, bekannte Sortieralgorithmen. Wenn du sie noch nicht kennst, kannst du sie recherchieren und überlegen, welche sich an dieses Problem anpassen lassen. Beachte, dass hier nicht alle funktionieren, da du nur benachbarte Kakteen vertauschen kannst.
</spoiler>
<spoiler=zeige Hinweis 3>
„Bubble Sort“ ist wahrscheinlich der einfachste Sortieralgorithmus. Dabei gehst du wiederholt alle Elemente durch und vertauschst benachbarte Elemente in der falschen Reihenfolge, bis keine mehr übrig sind.

So sieht das mit Kakteen aus:
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
Natürlich gibt es viele Möglichkeiten, diese Strategie zu verbessern!
Sobald du eine einzelne Zeile sortieren kannst, kannst du mit Hinweis 1 das gesamte Feld sortieren.
</spoiler>

---

[Statistiken](docs/stats.md)

[harvest()](functions/harvest)      [plant()](functions/plant)      [move()](functions/move)      [till()](functions/till)      [swap()](functions/swap)      [measure()](functions/measure)
