[<- Operatory](docs/scripting/operators.md) <right>[Listy ->](docs/scripting/lists.md)
<right>[Funkcje ->](docs/scripting/functions.md)
---
# Zmienne
Zmienne można traktować jak nazwane pojemniki, które mogą przechowywać wartość.
Operator `=` służy do deklarowania zmiennej i przechowywania w niej wartości.

`nazwa_zmiennej = wartość`

Lewa strona operatora to nazwa zmiennej. Możesz nadać jej dowolną prawidłową nazwę.
Prawa strona to wyrażenie, którego wynikowa wartość zostanie przechowana w zmiennej.

Zadeklaruj zmienną o nazwie `a` i przechowaj w niej wartość `5`:
`a = 5`
Zadeklaruj zmienną o nazwie `b` i przechowaj w niej wartość zwracaną przez `can_harvest()`:
`b = can_harvest()`

Nie myl operatora `=` z operatorem `==`. 
Operator `==` sprawdza, czy dwie wartości są równe i zwraca `True` lub `False`.
Operator `=` przypisuje wartość po prawej stronie do nazwy po lewej stronie.

Po przypisaniu zmiennej można jej użyć w kodzie, aby pobrać wartość, którą zawiera.

{{codeexample 
{
    "camera_position": {"x": 0, "y": 1.5, "z": 4},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": false,
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
a = 5
for i in range(a):
	do_a_flip()
}}

Powyższa pętla jest wykonywana 5 razy, ponieważ `a` ma wartość `5`.
`i` w pętli `for` jest również zmienną. Podczas każdej iteracji automatycznie przypisywana jest jej bieżąca wartość z sekwencji. Nie musi nazywać się `i`; możesz nadać jej dowolną prawidłową nazwę zmiennej.

Zmienne pozwalają również na to samo z pętlą while:

{{codeexample 
{
    "camera_position": {"x": 0, "y": 1.5, "z": 4},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": false,
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
a = 5
i = 0
while i < a:
	do_a_flip()
	i = i + 1
}}

To robi to samo co powyższa pętla `for`, ale musimy ręcznie zwiększać `i`.
Aby zwiększyć `i`, ustawiamy je na jego bieżącą wartość plus `1`. Zmienianie zmiennej na podstawie jej poprzedniej wartości jest bardzo częste.
Można to skrócić za pomocą tych operatorów: `+=, -=, *=, /=, %=`

`i = i + 1` to to samo co `i += 1`
`a = a / 3` to to samo co `a /= 3`
---

[Operatory](docs/scripting/operators.md)      [Pętla While](docs/scripting/while.md)      [Pętla For](docs/scripting/for.md)      [Funkcje](docs/scripting/functions.md)      [Zasięgi nazw](docs/scripting/scopes.md)
