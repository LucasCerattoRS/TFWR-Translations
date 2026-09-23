[<- Debugowanie](docs/scripting/debug.md) <right>[Symulacja ->](docs/unlocks/simulation.md)
---
# Czas
Jeśli naprawdę chcesz zoptymalizować swoje metody, musisz zrozumieć, jak w tej grze mierzony jest czas. Temu właśnie służy to odblokowanie.
## Nowe funkcje
Są dwie użyteczne funkcje do mierzenia, ile czasu coś zajmuje:
`get_time()` zwraca czas w sekundach od początku gry.
`get_tick_count()` zwraca liczbę ticków wykonanych od początku działania programu.

Te dwie funkcje, podobnie jak `quick_print()`, są całkowicie darmowe. Nawet ich wywołanie nic nie kosztuje.

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
start_time, start_ticks = get_time(), get_tick_count()
harvest()
time, ticks = get_time(), get_tick_count()
quick_print(time - start_time, ticks - start_ticks)
}}
## Szczegóły działania
### Uwaga
Tak nie działa wydajność w prawdziwym świecie. To są tylko zasady wymyślone na potrzeby tej gry, aby mieć spójny i zrozumiały model czasu.
Prawdopodobnie będzie cię to obchodzić tylko wtedy, gdy będziesz chciał hiperoptymalizować swój kod.


Podstawowa jednostka czasu wykonywania kodu nazywa się „tick”. Bez ulepszeń prędkości i energii kod jest wykonywany z prędkością `400` ticków na sekundę.

Ogólnie rzecz biorąc, operacje łączące dwie wartości, takie jak `+, -, *, /, //, %, and, or, ...`, zajmują jeden tick.
Jednoargumentowe `-` i `not` są darmowe.
Instrukcja `if` również zajmuje jeden tick (oprócz czasu potrzebnego na sprawdzenie wyrażenia warunkowego).
Wywołania funkcji oraz odczyty i zapisy zmiennych są darmowe, ale definicje funkcji zajmują 1 tick.
Instrukcje `import` są darmowe.
Dostęp do zaimportowanego modułu za pomocą operatora `.` jest darmowy.
Jeśli funkcja lub moduł zostały przekazane jako argumenty albo przez przypisanie zmiennej, ich użycie kosztuje 1 tick zamiast 0.
Pętle `for` i `while` zajmują jeden tick na rozpoczęcie, ale iteracje są darmowe (nie licząc czasu sprawdzania wyrażeń warunkowych lub sekwencji).
`return`, `break` i `continue` są darmowe.
`pass` zajmuje jeden tick, więc można go używać do tworzenia precyzyjnych opóźnień.
Indeksowanie struktury danych zajmuje jeden tick dla operatora indeksu, a w przypadku słownika lub zbioru dodatkowe ticki zależne od rozmiaru klucza.

Liczba ticków potrzebnych do wykonania funkcji wbudowanej jest podana na stronie każdej funkcji.

---

[Debugowanie](docs/scripting/debug.md)      [Symulacja](docs/unlocks/simulation.md)      [Tabela wyników](docs/unlocks/leaderboard.md)

[get_time()](functions/get_time)      [get_tick_count()](functions/get_tick_count)      [quick_print()](functions/quick_print)
