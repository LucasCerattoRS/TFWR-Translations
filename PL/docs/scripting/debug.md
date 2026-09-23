[<- Sadzenie](docs/unlocks/plant.md) <right>[Debugowanie 2 ->](docs/unlocks/debug2.md)
<right>[Czas ->](docs/unlocks/timing.md)
---
# Debugowanie
Czasami twój kod po prostu nie działa i musisz dowiedzieć się, dlaczego. Jest kilka narzędzi, które mogą ci w tym pomóc.

Pierwszym z nich jest wykonywanie programu krok po kroku. 
Możesz przejść do trybu krok po kroku za pomocą przycisku obok przycisku Wykonaj lub ustawiając punkt przerwania (breakpoint).

Punkty przerwania można dodawać, klikając panel punktów przerwania po lewej stronie kodu.
![|x227](Breakpoints)
Gdy wykonanie dotrze do wiersza z punktem przerwania, automatycznie przełączy się w tryb krok po kroku.

Gdy najedziesz myszą na zmienną, wyświetli się jej aktualna wartość.

Funkcja `print()` również może być bardzo przydatna. Wypisze każdą przekazaną jej wartość bezpośrednio w powietrzu.

Przykłady:

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
print(0.24)
}}

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
print(can_harvest())
}}

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
print(get_pos_x(), get_pos_y())
}}

Funkcja `print()` wyświetla wartość bezpośrednio w powietrzu i na stronie [Dane wyjściowe](docs/output.md).

Wypisywanie w powietrzu może być czasami trochę wolne, jeśli chcesz wyświetlić wiele wartości.
W takim przypadku możesz użyć funkcji `quick_print()`, która wyświetla dane tylko w oknie wyjściowym.

Okno wyjściowe rejestruje również ostrzeżenia i błędy, więc warto je sprawdzić, jeśli coś nie działa zgodnie z oczekiwaniami.

Gdy wykonanie się zatrzyma, dane wyjściowe są również zapisywane w pliku [output.txt](persistent_data_path/output.txt) w folderze gry.

---

[Dane wyjściowe](docs/output.md)      [Komentarze](docs/scripting/comments.md)      [Debugowanie 2](docs/unlocks/debug2.md)      [Kolorowe bloki](docs/unlocks/debug_place.md)      [Symulacja](docs/unlocks/simulation.md)

[print()](functions/print)      [quick_print()](functions/quick_print)
