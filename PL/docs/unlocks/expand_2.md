[<- Ekspansja 1](docs/unlocks/expand_1.md)
---
# Ekspansja 2
Twoja farma znów się powiększyła! Teraz pola nie są już w ładnym rzędzie, więc musisz znaleźć sposób na przemierzanie kwadratowej siatki.

Z pętlą `while` nie jest to możliwe, dopóki nie odblokujesz zmysłów i operatorów.
Nadszedł czas na wprowadzenie pętli `for`.

Możesz przeczytać wszystko o pętli `for` na stronie [Pętla For](docs/scripting/for.md), ale na razie będziesz jej potrzebować tylko do powtarzania kodu stałą liczbę razy.

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
for i in range(5):
	do_a_flip()
}}

`range(n)` tworzy sekwencję `n` liczb od `0` do `n - 1`. Pętla `for` wykonuje swoje ciało raz dla każdego elementu sekwencji. W tym przykładzie `do_a_flip()` zostanie wywołane `5` razy.

Dostępna jest teraz również funkcja `get_world_size()`. Zwraca ona długość boku twojej farmy. W ten sposób możesz pisać kod, który nie zepsuje się przy następnym ulepszeniu ekspansji.

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
    "items": [],
    "world_size": {"x": 3, "y": 3},
    "execution_speed": 2,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 1,
    "seed": 1,
    "exclude_unlocks": ["watering", "fertilizer"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
do_a_flip()
#CODE
for i in range(get_world_size()):
	harvest()
	move(North)
}}

Ten przykład zbiera plony z jednej kolumny farmy dla dowolnego rozmiaru farmy.

Jeśli nie wiesz, jak poruszać dronem po farmie, zajrzyj do poniższej podpowiedzi.
<spoiler=pokaż podpowiedź>Oczywiście farmę można przemierzać na kilka sposobów.
Szukamy systematycznego sposobu, który nie przestanie działać, gdy farma znów urośnie.
Aby dotrzeć do każdego miejsca na farmie, można bez końca powtarzać następujące dwa kroki:

1. Poruszaj się na `North`, aż dron pojawi się po drugiej stronie.
2. Porusz się na `East`.

`for i in range(get_world_size()):` może pomóc przekształcić ten pomysł w kod.
</spoiler>
<spoiler=pokaż możliwe rozwiązanie>
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
    "items": [],
    "world_size": {"x": 3, "y": 3},
    "execution_speed": 2,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 1,
    "seed": 1,
    "exclude_unlocks": ["watering", "fertilizer"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
do_a_flip()
#CODE
for i in range(get_world_size()):
	for j in range(get_world_size()):
		#wykonaj obrót na każdym polu
		do_a_flip()
		move(North)
	move(East)
}}
</spoiler>
---

[Pętla For](docs/scripting/for.md)      [Pętla While](docs/scripting/while.md)      [Zmienne](docs/scripting/variables.md)

[move()](functions/move)      [get_world_size()](functions/get_world_size)
