[<- Labirynty](docs/unlocks/mazes.md)
---
# Megafarma
To niezwykle potężne odblokowanie daje ci dostęp do wielu dronów. 
{{codeexample 
{
    "camera_position": {"x": -3, "y": 2.1, "z": 7},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": false,
    "show_inventory": true,
    "show_output": true,
    "collapsing": false,
    "autoplay": true,
    "items": [],
    "world_size": {"x": 7, "y": 7},
    "execution_speed": 21,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 1,
    "seed": 1,
    "exclude_unlocks": ["fertilizer", "watering"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
move(North)
move(North)
move(North)
move(East)
move(East)
move(East)
change_hat(Hats.Wizard_Hat)
#CODE
def harvest_spiral(radius):
    for i in range(1, radius, 2):
        harvest()
        move(West)
        for j in range(i):
            harvest()
            move(South)
        for j in range(i+1):
            harvest()
            move(East)
        for j in range(i+1):
            harvest()
            move(North)
        for j in range(i+1):
            harvest()
            move(West)

while True:
    spawn_drone(harvest_spiral, 7)
    do_a_flip()
}}

Tak jak poprzednio, nadal zaczynasz z jednym dronem. Dodatkowe drony muszą być najpierw stworzone i znikną po zakończeniu programu.
Każdy dron wykonuje swój własny, oddzielny program. Nowe drony można tworzyć za pomocą funkcji `spawn_drone(function)`.

{{codeexample 
{
    "camera_position": {"x": -0.5, "y": 1.5, "z": 4},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": false,
    "collapsing": true,
    "autoplay": false,
    "items": [],
    "world_size": {"x": 2, "y": 1},
    "execution_speed": 1,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 200,
    "seed": 1,
    "exclude_unlocks": ["watering", "fertilizer"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
#CODE
def drone_function():
    move(East)
    do_a_flip()

spawn_drone(drone_function)
do_a_flip()
}}

Tworzy to nowego drona w tej samej pozycji co dron, który wykonał polecenie `spawn_drone(function)`. Nowy dron zaczyna następnie wykonywać wskazaną funkcję. Po jej zakończeniu zniknie automatycznie, chyba że jest ostatnim istniejącym dronem.

Drony nie zderzają się ze sobą. 

Użyj `max_drones()`, aby uzyskać maksymalną liczbę dronów, które mogą istnieć jednocześnie.
Użyj `num_drones()`, aby uzyskać liczbę dronów, które już są na farmie.


## Przykład
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
    "items": [],
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
#CODE
def harvest_column():
    for _ in range(get_world_size()):
        harvest()
        move(North)

while True:
    if spawn_drone(harvest_column):
        move(East)
}}

Spowoduje to, że twój pierwszy dron będzie poruszał się poziomo i tworzył kolejne drony. Stworzone drony będą następnie poruszać się pionowo i zbierać wszystko na swojej drodze.

Jeśli wszystkie dostępne drony zostały już stworzone, `spawn_drone()` nic nie zrobi i zwróci `None`.

Oto inny przykład, który przekazuje każdemu dronowi inny kierunek.
{{codeexample 
{
    "camera_position": {"x": -1, "y": 2, "z": 5},
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
    "operation_ticks": 100,
    "seed": 1,
    "exclude_unlocks": ["fertilizer", "watering"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
move(North)
move(East)
#CODE
for dir in [North, East, South, West]:
    def task():
        move(dir)
        do_a_flip()
    spawn_drone(task)
}}

## Wszystkie drony są równe
Nie ma specjalnego „głównego” drona. Wszystkie drony mogą tworzyć inne drony i wszystkie wliczają się do limitu dronów. Wszystkie drony znikają po zakończeniu działania. Jeśli pierwszy dron zakończy swój program wcześniej, wykonanie innego drona zostanie pokazane przez podświetlanie kodu. Każdy dron może wywołać punkt przerwania. W takim przypadku podświetlanie kodu przełącza się na niego.

<spoiler=pokaż podpowiedź> Sprawdź tę super przydatną, równoległą funkcję `for_all`, która przyjmuje dowolną funkcję i uruchamia ją na każdym polu farmy. Wykorzystuje do tego wszystkie dostępne drony.

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
    "items": [],
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
#CODE
def for_all(f):
	def row():
		for _ in range(get_world_size()-1):
			f()
			move(East)
		f()
	for _ in range(get_world_size()):
		if not spawn_drone(row):
			row()
		move(North)

for_all(harvest)
}}

Szczególnie użytecznym wzorcem jest stworzenie drona, jeśli jest dostępny, a w przeciwnym razie zrobienie tego samemu.

`if not spawn_drone(task):
	task()`
</spoiler>

## Oczekiwanie na innego drona
Użyj funkcji `wait_for(drone)`, aby poczekać na zakończenie pracy innego drona. Otrzymujesz uchwyt `drone`, gdy tworzysz drona.
`wait_for(drone)` zwraca wartość zwróconą przez funkcję, którą wykonywał inny dron.

{{codeexample 
{
    "camera_position": {"x": -0.5, "y": 1.5, "z": 4},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": false,
    "collapsing": true,
    "autoplay": false,
    "items": [],
    "world_size": {"x": 2, "y": 1},
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
plant(Entities.Tree)
move(West)
#CODE
def get_entity_type_in_direction(dir):
    move(dir)
    return get_entity_type()

drone = spawn_drone(get_entity_type_in_direction, East)
print(wait_for(drone))
}}

Zauważ, że tworzenie dronów zajmuje czas, więc nie jest dobrym pomysłem tworzenie nowego drona dla każdej drobnej rzeczy.

Możesz użyć `has_finished(drone)`, żeby sprawdzić, czy dron skończył, bez czekania.

## Brak współdzielonej pamięci
Każdy dron ma własną pamięć i nie może bezpośrednio odczytywać ani zapisywać zmiennych globalnych innego drona.

{{codeexample 
{
    "camera_position": {"x": -0.5, "y": 1.5, "z": 4},
    "show_image": false,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": false,
    "show_output": true,
    "collapsing": true,
    "autoplay": false,
    "items": [],
    "world_size": {"x": 2, "y": 1},
    "execution_speed": 1,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 200,
    "seed": 1,
    "exclude_unlocks": ["watering", "fertilizer"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
#CODE
x = 0

def increment():
    global x
    x += 1

wait_for(spawn_drone(increment))
print(x)
}}

To wyświetli `0`, ponieważ nowy dron zwiększył własną kopię globalnej zmiennej `x`, co nie wpływa na `x` pierwszego drona.

## Przekazywanie argumentów

`spawn_drone()` przyjmuje dodatkowe opcjonalne argumenty, które zostaną przekazane do wywołanej funkcji:

Pamiętaj, że zasada braku współdzielonej pamięci nadal obowiązuje. Oznacza to, że wywołana funkcja działa na kopii argumentów:

{{codeexample 
{
    "camera_position": {"x": -0.5, "y": 1.5, "z": 4},
    "show_image": false,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": false,
    "show_output": true,
    "collapsing": true,
    "autoplay": false,
    "items": [],
    "world_size": {"x": 2, "y": 1},
    "execution_speed": 1,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 200,
    "seed": 1,
    "exclude_unlocks": ["watering", "fertilizer"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
#CODE
def modify(list):
	list.append('zielony')
	print(list)

l = ['czerwony']
wait_for(spawn_drone(modify, l))
print(l)
}}

## Warunki wyścigu
Wiele dronów może oddziaływać na to samo pole farmy w tym samym czasie. Jeśli dwa drony oddziałują na to samo pole w tym samym ticku, obie interakcje wystąpią, ale wyniki mogą się różnić w zależności od kolejności interakcji.

Na przykład, wyobraź sobie, że drony `0` i `1` znajdują się nad tym samym, prawie w pełni wyrośniętym drzewem.
Dron `0` wywołuje
`use_item(Items.Fertilizer)`
Dron `1` wywołuje
`harvest()`

Jeśli te akcje wystąpią w tym samym czasie, drzewo zostanie najpierw nawiezione, a następnie zebrane. W takim przypadku otrzymasz z niego drewno. Jednakże, jeśli Dron `1` jest nieco szybszy, drzewo zostanie zebrane, zanim zostanie nawiezione, i nie otrzymasz drewna.
Nazywa się to „warunkiem wyścigu”. Jest to powszechny problem w programowaniu równoległym, gdzie wynik zależy od kolejności, w jakiej wykonywane są operacje.

Oto inna problematyczna sytuacja, która może się zdarzyć, gdy wiele dronów wykonuje ten sam kod jednocześnie w tej samej pozycji.
`if get_water() < 0.5:
    use_item(Items.Water)`

Jeśli wiele dronów uruchomi to jednocześnie, wszystkie wykonają pierwszą linię, co umieści je w bloku `if`. Następnie wszystkie użyją wody, marnując jej dużo.
Zanim dron dotrze do drugiej linii, `get_water()` może już nie być mniejsze niż `0.5`, ponieważ inny dron w międzyczasie podlał pole.
---

[Funkcje](docs/scripting/functions.md)      [Zasięgi nazw](docs/scripting/scopes.md)      [Symulacja](docs/unlocks/simulation.md)

[spawn_drone()](functions/spawn_drone)      [num_drones()](functions/num_drones)      [max_drones()](functions/max_drones)      [wait_for()](functions/wait_for)      [has_finished()](functions/has_finished)
