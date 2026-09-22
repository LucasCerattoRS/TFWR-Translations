[<- Podlewanie](docs/unlocks/watering.md) <right>[Labirynty ->](docs/unlocks/mazes.md)
---
# Nawóz
W pewnym momencie czekanie na wzrost roślin przestaje być wystarczająco wydajne.
Tak jak w przypadku wody, co 10 sekund automatycznie otrzymasz 1 nawóz. Ilość ta podwaja się z każdym ulepszeniem.

Nawóz może sprawić, że rośliny będą rosły natychmiast. `use_item(Items.Fertilizer)` skraca pozostały czas wzrostu rośliny pod dronem o 2 sekundy.

{{codeexample 
{
    "camera_position": {"x": 0, "y": 1, "z": 5},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": false,
    "collapsing": true,
    "autoplay": false,
    "items": [{"item": "fertilizer", "n": 10}],
    "world_size": {"x": 1, "y": 1},
    "execution_speed": 2,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 1,
    "seed": 1,
    "exclude_unlocks": ["watering"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
#CODE
plant(Entities.Tree)
use_item(Items.Fertilizer)
use_item(Items.Fertilizer)
use_item(Items.Fertilizer)
harvest()
}}

Ma to pewne skutki uboczne.
Rośliny uprawiane z nawozem zostaną zainfekowane.

Gdy roślina jest zainfekowana, połowa jej plonu zamienia się w `Items.Weird_Substance` podczas zbioru.
Dziwna Substancja może być również używana na roślinach, co ma efekt przełączania statusu infekcji rośliny i wszystkich sąsiednich roślin.

Jeśli wywołasz `use_item(Items.Weird_Substance)` na zainfekowanej roślinie, zostanie ona wyleczona; użycie jej na zdrowej roślinie ją zainfekuje.

Jeśli użyjesz jej na zainfekowanej roślinie, która ma zdrowych sąsiadów, uleczy roślinę, ale zainfekuje sąsiadów i na odwrót.
{{codeexample 
{
    "camera_position": {"x": -1, "y": 1.8, "z": 5},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": false,
    "collapsing": true,
    "autoplay": false,
    "items": [{"item": "weird_substance", "n": 10}],
    "world_size": {"x": 3, "y": 3},
    "execution_speed": 1,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 1,
    "seed": 1,
    "exclude_unlocks": ["watering"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
for _ in range(3):
    for _ in range(3):
        plant(Entities.Tree)
        move(East)
    move(North)

move(North)
move(East)

for _ in range(60):
    do_a_flip()
#CODE
for _ in range(6):
    use_item(Items.Weird_Substance)
    move(East)
}}

---

[Statystyki](docs/stats.md)      [Podlewanie](docs/unlocks/watering.md)      [Labirynty](docs/unlocks/mazes.md)

[use_item()](functions/use_item)
