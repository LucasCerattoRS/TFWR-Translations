[<- Zucche](docs/unlocks/pumpkins.md) <right>[Dinosauri ->](docs/unlocks/dinosaurs.md)
---
# Cactus
Come le altre piante, i [cactus](objects/cactus) possono essere coltivati sulla terra e raccolti come al solito.

Tuttavia, esistono in varie dimensioni e hanno uno strano senso dell'ordine.

Se raccogli un cactus completamente cresciuto e tutti i cactus vicini sono in ordine, raccoglierà ricorsivamente anche tutti i cactus vicini.

Un cactus è considerato in ordine se tutti i cactus vicini a `North` e `East` sono completamente cresciuti e di dimensioni maggiori o uguali, mentre tutti quelli a `South` e `West` sono completamente cresciuti e di dimensioni minori o uguali.

Il raccolto si propagherà solo se tutti i cactus adiacenti sono completamente cresciuti e in ordine.
Questo significa che se un quadrato di cactus cresciuti è ordinato per dimensione e ne raccogli uno, raccoglierà l'intero quadrato.

Un cactus completamente cresciuto apparirà marrone se non è ordinato. Una volta ordinato, tornerà verde.

Riceverai una quantità di cactus pari al quadrato del numero di cactus raccolti. Se raccogli contemporaneamente `n` cactus, riceverai `n**2` `Items.Cactus`.

La dimensione di un cactus può essere misurata con `measure()`.
È sempre uno di questi numeri: `0,1,2,3,4,5,6,7,8,9`.

Puoi anche passare una direzione a `measure(direction)` per misurare la casella vicina in quella direzione del drone.

Puoi scambiare un cactus con il suo vicino in qualsiasi direzione usando il comando `swap()`.
`swap(direction)` scambia l'oggetto sotto il drone con l'oggetto a una casella di distanza nella `direction` del drone.

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

## Esempi Numerici
In ognuna di queste griglie, tutti i cactus sono in ordine e il raccolto si propagherà su tutto il campo:
`3 4 5    3 3 3    1 2 3    1 5 9
2 3 4    2 2 2    1 2 3    1 3 8
1 2 3    1 1 1    1 2 3    1 3 4`

In questa griglia, solo il cactus in basso a sinistra è in ordine, il che non è sufficiente per far propagare il raccolto:
`1 5 3
4 9 7
3 3 2`

<spoiler=mostra suggerimento 1>
Se ogni riga è già ordinata indipendentemente, ordinare ciascuna colonna non disordinerà le righe.
</spoiler>
<spoiler=mostra suggerimento 2>
Esistono molti algoritmi di ordinamento ingegnosi e ben noti. Se non li conosci, potresti documentarti e valutare quali si possono adattare a questo problema. Ricorda che non tutti funzionano qui, perché puoi scambiare solo cactus adiacenti.
</spoiler>
<spoiler=mostra suggerimento 3>
Il "bubble sort" è forse l'algoritmo di ordinamento più semplice. L'idea è scorrere ripetutamente gli elementi, scambiando quelli adiacenti che si trovano nell'ordine sbagliato finché non ne rimane nessuno.

Ecco come si presenta con i cactus:
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
Naturalmente ci sono molti modi per migliorare questa strategia!
Dopo essere riuscito a ordinare una singola riga, puoi usare il Suggerimento 1 per ordinare l'intero campo.
</spoiler>

---

[Statistiche](docs/stats.md)

[harvest()](functions/harvest)      [plant()](functions/plant)      [move()](functions/move)      [till()](functions/till)      [swap()](functions/swap)      [measure()](functions/measure)
