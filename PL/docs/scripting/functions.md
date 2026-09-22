[<- Zmienne](docs/scripting/variables.md) <right>[Import ->](docs/scripting/import.md)
---
# Funkcje
Użyj słowa kluczowego `def`, aby zdefiniować nową funkcję:
`def f(arg1, arg2 = False):
	#kod funkcji`

Możesz użyć operatora wywołania `()`, aby wywołać funkcję:
`f(42)`

Zobacz także [Zasięgi](docs/scripting/scopes.md), aby dowiedzieć się o zmiennych lokalnych i globalnych w funkcjach.

## Wprowadzenie
Widziałeś już wbudowane funkcje, takie jak `harvest()`.
Możesz także definiować własne funkcje, co pozwala porządkować kod w modułowy sposób. Funkcja nadaje nazwę blokowi kodu, dzięki czemu możesz go wywołać wszędzie, gdzie go potrzebujesz.

## Definicje funkcji
Na przykład, możesz zdefiniować funkcję, która przesuwa drona kilka razy.

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
def move_n_dir(n, dir):
	for i in range(n):
		move(dir)
}}

Słowo kluczowe `def` sygnalizuje, że jest to definicja funkcji. 
`move_n_dir` to nazwa, do której funkcja zostanie przypisana. Może to być dowolna prawidłowa nazwa zmiennej i będzie używana do wywołania funkcji.
`n` i `dir` to parametry. Są to zmienne przechowujące wartości przekazywane do funkcji; wartości te nazywa się także argumentami. Do definicji funkcji możesz dodać tyle parametrów, ile chcesz.
Po znaku `:` następuje blok kodu, który zostanie wykonany po wywołaniu funkcji.

Poniższy kod przesuwa następnie drona o `2` pola na `North` i `2` pola na `East`.

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
    "operation_ticks": 100,
    "seed": 1,
    "exclude_unlocks": ["watering", "fertilizer"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
#CODE
def move_n_dir(n, dir):
	for i in range(n):
		move(dir)

move_n_dir(2, North)
move_n_dir(2, East)
}}

Kiedy widzisz `def function():`, powinieneś myśleć o tym jak o przypisaniu zmiennej:
`function = create_new_function_object()`
Tak jak w przypadku każdego przypisania, nie możesz użyć zmiennej, zanim zostanie do niej przypisana wartość!
Instrukcja `def` musi zostać wykonana przed jakimkolwiek wywołaniem funkcji.
Ten kod zgłosi błąd:

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
func()
def func():
	pass
}}

## Wartości zwracane
Użyj słowa kluczowego `return`, aby funkcja zwracała wartość. 
Na przykład poniższa funkcja definiuje operację alternatywy wyłączającej (XOR). Alternatywa wyłączająca zwraca `True`, jeśli jedna wartość jest `True`, a druga `False`:

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
    "world_size": {"x": 1, "y": 1},
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
#CODE
def xor(a, b):
	return a != b

if xor(True, False):
	do_a_flip()
}}

[Krotki](docs/scripting/tuples.md) pozwalają na zwracanie wielu wartości.

## Argumenty domyślne
Możesz również przypisać wartości domyślne, które zostaną użyte, gdy odpowiadające im argumenty zostaną pominięte.

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
    "world_size": {"x": 1, "y": 1},
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
#CODE
def f(a = False):
	if a:
		do_a_flip()

f()

f(True)
}}

Argument bez wartości domyślnej nie może następować po argumencie z wartością domyślną.

## Zaawansowane użycie funkcji
Funkcje są wartościami, tak jak każda inna wartość, a instrukcja `def` działa jak instrukcja przypisania, przypisując funkcję do dowolnej nazwy, jaką jej nadasz.
Pozwala to na robienie takich rzeczy:

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
    "world_size": {"x": 1, "y": 1},
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
#CODE
def f():
	def d():
		do_a_flip()
	return d

f()()
}}

Tutaj `f()` wywołuje funkcję `f`, która definiuje i zwraca nową funkcję `d`. Drugie `()` wykonuje następnie zwróconą funkcję i obrót.
(Robienie tego typu rzeczy zazwyczaj nie jest dobrym pomysłem, ponieważ trudno jest zobaczyć, co się dzieje.)

Funkcje, które przyjmują inne funkcje jako argumenty, pozwalają na dużą kreatywność:

{{codeexample 
{
    "camera_position": {"x": -2, "y": 1.5, "z": 4},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": true,
    "collapsing": true,
    "autoplay": false,
    "items": [{"item": "fertilizer", "n": 4}],
    "world_size": {"x": 5, "y": 1},
    "execution_speed": 1,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 100,
    "seed": 1,
    "exclude_unlocks": ["watering"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
#CODE
def f(g, arg):
	for _ in range(4):
		g(arg)

f(move, East)
plant(Entities.Tree)
f(use_item, Items.Fertilizer)
}}

---

[Zmienne](docs/scripting/variables.md)      [Zasięgi nazw](docs/scripting/scopes.md)      [Krotki](docs/scripting/tuples.md)      [Import](docs/scripting/import.md)
