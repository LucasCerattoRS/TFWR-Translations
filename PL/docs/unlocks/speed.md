[<- Pętla While](docs/scripting/while.md) <right>[Ekspansja 1 ->](docs/unlocks/expand_1.md)
<right>[Sadzenie ->](docs/unlocks/plant.md)
---
# Ulepszenie prędkości
Prędkość wykonywania została podwojona. Problem w tym, że dron zbiera teraz szybciej, niż trawa może rosnąć, przez co nie uzyskuje żadnego plonu. Aby temu zaradzić, odblokowano instrukcje warunkowe [if](docs/scripting/if.md) oraz funkcję [can_harvest()](functions/can_harvest).

## Sprawdzanie przed zbiorem
Instrukcja `if` wykonuje swój blok kodu raz, jeśli podany warunek ma wartość `True`.

Nowa funkcja `can_harvest()` zapewnia użyteczny warunek. `can_harvest()` zwraca `True`, jeśli roślinę pod dronem można zebrać, a w przeciwnym razie `False`.

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
do_a_flip()
#CODE
if can_harvest():
	do_a_flip()
}}

Możesz wyobrazić sobie tę wartość zwracaną tak, jakby podczas sprawdzania instrukcji `if` wywołanie `can_harvest()` zostało zastąpione zwróconą wartością `True`.

Co dzieje się po uruchomieniu powyższego kodu:
- Wykonywana jest instrukcja `if`.
- Wywoływana jest funkcja `can_harvest()`.
- `can_harvest()` zwraca `True`, ponieważ trawa jest w pełni wyrośnięta.
- Instrukcja ma teraz postać `if True:`.
- Blok zostaje wykonany, ponieważ wartość wynosi `True`.

Gdyby trawa nie była w pełni wyrośnięta, dron nie wykonałby obrotu.

Teraz możemy użyć `if`, aby zapobiec zbyt wczesnemu zbieraniu przez drona.
---

[If](docs/scripting/if.md)      [Pętla While](docs/scripting/while.md)

[harvest()](functions/harvest)      [can_harvest()](functions/can_harvest)
