[<- Kaktus](docs/unlocks/cactus.md)
---
# Dinosaurier
Dinosaurier sind uralte, majestätische Kreaturen, die für uralte Knochen gefarmt werden können.

Leider sind Dinosaurier vor langer Zeit ausgestorben, also ist das Beste, was wir jetzt tun können, uns als einer zu verkleiden.
Zu diesem Zweck hast du den neuen Dinosaurier-Hut erhalten.

Der Hut kann ausgerüstet werden mit
`change_hat(Hats.Dinosaur_Hat)`

Leider sieht er nicht ganz so aus wie in der Werbung...

Wenn du den Dinosaurier-Hut ausrüstest und genügend Kakteen hast, wird automatisch ein [Apfel](objects/apple) gekauft und unter der Drohne platziert.
Wenn die Drohne über einem Apfel ist und sich wieder bewegt, frisst sie den Apfel und ihr Schwanz wächst um eins. Wenn du es dir leisten kannst, wird ein neuer Apfel gekauft und an einem zufälligen Ort platziert.
Der Apfel kann nicht erscheinen, wenn an seiner gewünschten Stelle etwas anderes gepflanzt ist.

Der Schwanz des Dinosauriers wird hinter der Drohne hergezogen und füllt die Felder, über die sich die Drohne zuvor bewegt hat. Wenn eine Drohne versucht, sich auf den Schwanz zu bewegen, schlägt `move()` fehl und gibt `False` zurück.
Das letzte Segment des Schwanzes wird während der Bewegung aus dem Weg geräumt, sodass du dich darauf bewegen kannst. Wenn die Schlange jedoch die gesamte Farm ausfüllt, kannst du dich nicht mehr bewegen. Du kannst also prüfen, ob die Schlange ausgewachsen ist, indem du prüfst, ob du dich nicht mehr bewegen kannst.
Während des Tragens des Dinosaurier-Huts kann sich die Drohne nicht über den Farmrand bewegen, um auf die andere Seite zu gelangen.

Die Verwendung von `measure()` auf einem Apfel gibt die Position des nächsten Apfels als Tupel zurück.

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

Wenn der Hut wieder abgelegt wird, indem ein anderer Hut ausgerüstet wird, wird der Schwanz geerntet.
Du erhältst Knochen in Höhe der Schwanzlänge zum Quadrat. Für einen Schwanz der Länge `n` erhältst du also `n**2` `Items.Bone`.
Zum Beispiel:
Länge 1 => 1 Knochen
Länge 2 => 4 Knochen
Länge 3 => 9 Knochen
Länge 4 => 16 Knochen
Länge 16 => 256 Knochen
Länge 100 => 10000 Knochen

Der Dinosaurier-Hut ist sehr schwer. Wenn du ihn ausrüstest, dauert `move()` 400 Ticks statt 200. Jedes Mal, wenn du einen Apfel aufhebst, wird die Anzahl der von `move()` verbrauchten Ticks um 3% reduziert (abgerundet), weil ein längerer Schwanz dir beim Bewegen helfen kann.

Die folgende Schleife gibt die Anzahl der von `move()` verwendeten Ticks nach einer beliebigen Anzahl von Äpfeln aus:

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
    quick_print("Ticks nach ", i, " Äpfeln: ", ticks)
    ticks -= ticks * 0.03 // 1
}}

Du hast nur einen Dinosaurier-Hut, also kann ihn nur eine Drohne tragen.

<spoiler=zeige Hinweis 1>
Wenn du dich immer auf demselben Pfad bewegst, der das gesamte Feld abdeckt, kannst du leicht eine Schlange bekommen, die jedes Mal das gesamte Feld bedeckt. Es ist nicht sehr effizient, aber es funktioniert.
Eine sehr große Farm vollständig zu durchqueren kann lange dauern, und vielleicht brauchst du gar nicht so viele Knochen. Mit `set_world_size()` kannst du die Farm auf eine passendere Größe einstellen.</spoiler>

---

[Statistiken](docs/stats.md)      [Tupel](docs/scripting/tuples.md)      [Listen](docs/scripting/lists.md)

[change_hat()](functions/change_hat)      [move()](functions/move)      [measure()](functions/measure)
