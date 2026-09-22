[<- Symulacja](docs/unlocks/simulation.md)
---
# Tabela wyników
Jeśli dotarłeś tak daleko, pokonałeś wiele wyzwań. Ale czy rozwiązałeś je wydajnie?
Możesz konkurować z innymi graczami w różnych tabelach wyników o najbardziej wydajne metody uprawy.

Możesz rozpocząć próbę w tabeli wyników, wywołując `leaderboard_run(leaderboard, filename, speedup)`.
Rozpoczyna to [symulację](docs/unlocks/simulation.md) podobną do `simulate()`, z tym wyjątkiem, że warunki początkowe są stałe. Każda kategoria tabeli wyników ma inne warunki początkowe i warunki powodzenia.

Próba w tabeli wyników kończy się sukcesem, jeśli warunek powodzenia jest `True`, gdy symulacja się kończy.

Symulacja NIE zakończy się automatycznie po osiągnięciu celu. Musisz upewnić się, że program zakończy działanie.
Jeśli próba się powiedzie, twój czas zostanie dodany do tabeli wyników.

Aby zmniejszyć wariancję, wszystkie próby muszą obejmować co najmniej 2 godziny symulowanego czasu. Symulację można przyspieszyć, więc w rzeczywistości nie potrwa to tak długo. Jeśli próba zakończy się wcześniej, będzie powtarzana, aż łączny symulowany czas osiągnie 2 godziny. Jako twój wynik zostanie przesłany średni czas ze wszystkich prób.

Oto przykładowa konfiguracja, która pozwoli ci znaleźć się w tabeli wyników siana.
![|x400](LeaderboardSetup)

## Najszybszy reset
Najszybszy reset to najbardziej prestiżowa kategoria. W tej kategorii całkowicie automatyzujesz grę, zaczynając od jednego pola farmy i kończąc po ponownym odblokowaniu tabel wyników.

Nie musisz wszystkiego odblokowywać. Po prostu spróbuj jak najszybciej odblokować `Unlocks.Leaderboard`.

Pamiętaj, że za pomocą `num_unlocked(unlock) > 0` możesz sprawdzić, czy coś jest odblokowane. Możesz też użyć `get_cost()` na odblokowaniach, aby poznać ich koszt i automatycznie zdobywać odpowiednie przedmioty.

`unlock()` nie uwzględnia zależności w drzewku technologii. Można na przykład odblokować `Unlocks.Fertilizer` przed `Unlocks.Water`.

Wywołanie funkcji:
`leaderboard_run(Leaderboards.Fastest_Reset, filename, speedup)`

Równoważna symulacja:
`unlocks = {}
items = {}
globals = {}
#ujemna wartość zmiennej seed oznacza losowe ziarno
seed = -1
simulate(filename, unlocks, items, globals, seed, speedup)`

Warunek powodzenia:
`num_unlocked(Unlocks.Leaderboard) > 0`

## Labirynt
Zacznij z wszystkim odblokowanym i zbierz `9863168` złota tak szybko, jak potrafisz. To dokładnie tyle złota, ile zarobisz, używając ponownie jednego labiryntu 32x32 `300` razy.

Wywołanie funkcji:
`leaderboard_run(Leaderboards.Maze, filename, speedup)`

Równoważna symulacja:
`unlocks = Unlocks
items = {Items.Weird_Substance : 1000000000, Items.Power: 1000000000}
globals = {}
seed = -1
simulate(filename, unlocks, items, globals, seed, speedup)`

Warunek powodzenia:
`num_items(Items.Gold) >= 9863168`

## Dinozaur
Zacznij z wszystkim odblokowanym i zbierz `33488928` kości tak szybko, jak potrafisz. To dokładnie tyle kości, ile zdobędziesz, jeśli wypełnisz obszar 32x32 ogonem dinozaura.

Wywołanie funkcji:
`leaderboard_run(Leaderboards.Dinosaur, filename, speedup)`

Równoważna symulacja:
`unlocks = Unlocks
items = {Items.Cactus : 1000000000, Items.Power: 1000000000}
globals = {}
seed = -1
simulate(filename, unlocks, items, globals, seed, speedup)`

Warunek powodzenia:
`num_items(Items.Bone) >= 33488928`

## Pozostałe tabele wyników zasobów
Każda roślina ma własną tabelę wyników dotyczącą jak najszybszej uprawy. Zaczynasz ze wszystkimi odblokowaniami, zasobami potrzebnymi do wzrostu rośliny i dużym zapasem energii. Celem jest zebranie określonej ilości wytwarzanego przez nią zasobu.

Jak zawsze musisz upewnić się, że program zakończy działanie po osiągnięciu celu. Próba nie kończy się, dopóki program nie przestanie działać, nawet jeśli cel został już osiągnięty.

### `Leaderboards.Cactus`
`leaderboard_run(Leaderboards.Cactus, filename, speedup)`
Warunek powodzenia: `num_items(Items.Cactus) >= 33554432`

### `Leaderboards.Sunflowers`
`leaderboard_run(Leaderboards.Sunflowers, filename, speedup)`
Warunek powodzenia: `num_items(Items.Power) >= 100000`

### `Leaderboards.Pumpkins`
`leaderboard_run(Leaderboards.Pumpkins, filename, speedup)`
Warunek powodzenia: `num_items(Items.Pumpkin) >= 200000000`

### `Leaderboards.Wood`
`leaderboard_run(Leaderboards.Wood, filename, speedup)`
Warunek powodzenia: `num_items(Items.Wood) >= 10000000000`

### `Leaderboards.Carrots`
`leaderboard_run(Leaderboards.Carrots, filename, speedup)`
Warunek powodzenia: `num_items(Items.Carrot) >= 2000000000`

### `Leaderboards.Hay`
`leaderboard_run(Leaderboards.Hay, filename, speedup)`
Warunek powodzenia: `num_items(Items.Hay) >= 2000000000`

## Tabele wyników jednego drona
Istnieją również tabele wyników dla uprawy jednym dronem. Otrzymujesz tylko jednego drona i farmę 8x8, a twoim zadaniem jest jak najszybsze zebranie określonej ilości zasobów.

### `Leaderboards.Maze_Single`
`leaderboard_run(Leaderboards.Maze_Single, filename, speedup)`
Warunek powodzenia: `num_items(Items.Gold) >= 616448`

### `Leaderboards.Cactus_Single`
`leaderboard_run(Leaderboards.Cactus_Single, filename, speedup)`
Warunek powodzenia: `num_items(Items.Cactus) >= 131072`

### `Leaderboards.Sunflowers_Single`
`leaderboard_run(Leaderboards.Sunflowers_Single, filename, speedup)`
Warunek powodzenia: `num_items(Items.Power) >= 10000`

### `Leaderboards.Pumpkins_Single`
`leaderboard_run(Leaderboards.Pumpkins_Single, filename, speedup)`
Warunek powodzenia: `num_items(Items.Pumpkin) >= 10000000`

### `Leaderboards.Wood_Single`
`leaderboard_run(Leaderboards.Wood_Single, filename, speedup)`
Warunek powodzenia: `num_items(Items.Wood) >= 500000000`

### `Leaderboards.Carrots_Single`
`leaderboard_run(Leaderboards.Carrots_Single, filename, speedup)`
Warunek powodzenia: `num_items(Items.Carrot) >= 100000000`

### `Leaderboards.Hay_Single`
`leaderboard_run(Leaderboards.Hay_Single, filename, speedup)`
Warunek powodzenia: `num_items(Items.Hay) >= 100000000`

---

[Symulacja](docs/unlocks/simulation.md)      [Czas](docs/unlocks/timing.md)      [Automatyczne odblokowania](docs/unlocks/auto_unlock.md)      [Koszty](docs/unlocks/costs.md)      [Statystyki](docs/stats.md)

[get_cost()](functions/get_cost)      [num_unlocked()](functions/num_unlocked)      [leaderboard_run()](functions/leaderboard_run)
