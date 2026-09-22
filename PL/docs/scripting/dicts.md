[<- Listy](docs/scripting/lists.md) <right>[Koszty ->](docs/unlocks/costs.md)
---
# Słowniki
Słowniki to struktura danych, która mapuje klucze na wartości, podobnie jak prawdziwy słownik mapuje słowa na ich definicje. Pozwala bardzo szybko wyszukiwać te wartości.

Słownik można utworzyć w ten sposób:

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
    "operation_ticks": 100,
    "seed": 0,
    "exclude_unlocks": ["watering", "fertilizer"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
#CODE
right_of = {North:East, East:South, South:West, West:North}
}}

Wyrażenie przed dwukropkiem to klucz, a wyrażenie po dwukropku to wartość, na którą mapuje klucz.
Powyższy słownik mapuje każdy kierunek na kierunek po jego prawej stronie.

Oto inny słownik, który mapuje pozycję drona na obiekt znajdujący się pod nim.
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
    "operation_ticks": 100,
    "seed": 0,
    "exclude_unlocks": ["watering", "fertilizer"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
#CODE
x, y = get_pos_x(), get_pos_y()
entity_dict = {(x,y):get_entity_type()}
}}

Dostęp do wartości mapowanej na klucz jest podobny do dostępu do elementu na liście:
`value = dict[key]`

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
    "operation_ticks": 100,
    "seed": 0,
    "exclude_unlocks": ["watering", "fertilizer"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
#CODE
right_of = {North:East, East:South, South:West, West:North}
print(right_of[South])
}}

Możesz dodać nową parę klucz-wartość do słownika w ten sposób:
`dict[key] = value`

{{codeexample 
{
    "camera_position": {"x": 0, "y": 1.5, "z": 4},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": true,
    "collapsing": true,
    "autoplay": false,
    "items": [],
    "world_size": {"x": 3, "y": 1},
    "execution_speed": 1,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 100,
    "seed": 1,
    "exclude_unlocks": ["watering", "fertilizer"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
move(East)
plant(Entities.Bush)
move(East)
plant(Entities.Tree)
move(East)
#CODE
entity_dict = {}
for _ in range(3):
	entity_dict[(get_pos_x(), get_pos_y())] = get_entity_type()
	move(East)
print(entity_dict)
}}

Klucze są unikalne, więc dodanie klucza, który już istnieje w słowniku, nadpisze poprzednią wartość.

Użyj `dict.pop(key)`, aby usunąć parę klucz-wartość ze słownika `dict`.

`key in dict` zwraca `True`, jeśli `key` jest kluczem w słowniku `dict`, i `False` w przeciwnym razie.
Więc możesz użyć `if key in dict:`, aby sprawdzić, czy `dict` zawiera dany klucz.

Umieszczenie słownika w pętli `for` pozwala iterować po wszystkich jego kluczach:
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
    "operation_ticks": 100,
    "seed": 0,
    "exclude_unlocks": ["watering", "fertilizer"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
#CODE
right_of = {North:East, East:South, South:West, West:North}
print(North in right_of)
for key in right_of:
	value = right_of[key]
	print(key, ":", value)
}}

Nie ma gwarancji co do kolejności, w jakiej klucze są iterowane.

Zobacz również [Zbiory](docs/scripting/sets.md)
---

[Listy](docs/scripting/lists.md)      [Zbiory](docs/scripting/sets.md)      [Krotki](docs/scripting/tuples.md)      [Koszty](docs/unlocks/costs.md)

[len()](functions/len)
