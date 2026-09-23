[<- Dynie](docs/unlocks/pumpkins.md)
---
# Uprawa współrzędna
Być może zauważyłeś już, że czasami rośliny dają większy plon, gdy są sadzone razem.
Trawa, krzaki, drzewa i marchewki dają większy plon, gdy mają odpowiedniego towarzysza. Preferencja towarzysza jest inna dla każdej rośliny i nie da się jej przewidzieć. Na szczęście preferencję rośliny pod dronem można sprawdzić za pomocą `get_companion()`. Funkcja zwraca krotkę, której pierwszy element to rodzaj pożądanej rośliny towarzyszącej, a drugi — jej pozycja. Towarzysz nie musi być w pełni wyrośnięty, aby zapewnić premię do plonu.

{{codeexample 
{
    "camera_position": {"x": -1, "y": 1.8, "z": 5},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": true,
    "collapsing": true,
    "autoplay": false,
    "items": [],
    "world_size": {"x": 3, "y": 3},
    "execution_speed": 1,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 20,
    "seed": 1,
    "exclude_unlocks": ["watering", "fertilizer"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
#CODE
plant(Entities.Bush)
plant_type, (x, y) = get_companion()
print(plant_type, (x, y))
move(East)
move(South)
plant(plant_type)
move(West)
move(North)
do_a_flip()
harvest()
}}

Preferowanym towarzyszem rośliny może być `Entities.Grass`, `Entities.Bush`, `Entities.Tree` lub `Entities.Carrot`. Każda roślina wybiera go losowo, ale zawsze będzie to inny rodzaj rośliny niż ona sama. Pozycja może znajdować się w dowolnym miejscu w odległości do 3 ruchów od rośliny, z wyjątkiem jej własnej pozycji.

Jeśli pod dronem nie ma rośliny z preferencją towarzysza, `get_companion()` zwraca `None`.

Przed pierwszym odblokowaniem uprawy współrzędnej mnożnik plonu wynosi `5`. Podwaja się przy każdym ulepszeniu.

---

[Statystyki](docs/stats.md)      [Krotki](docs/scripting/tuples.md)      [Słowniki](docs/scripting/dicts.md)      [Zmysły](docs/unlocks/senses.md)      [Sadzenie](docs/unlocks/plant.md)

[harvest()](functions/harvest)      [plant()](functions/plant)      [move()](functions/move)      [till()](functions/till)      [get_companion()](functions/get_companion)
