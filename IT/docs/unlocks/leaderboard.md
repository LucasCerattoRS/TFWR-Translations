[<- Simulazione](docs/unlocks/simulation.md)
---
# Classifica
Se sei arrivato fin qui, hai superato molte sfide. Ma le hai risolte in modo efficiente? 
Puoi competere con altri giocatori in varie classifiche per i metodi di coltivazione più efficienti.

Puoi avviare una partita per la classifica chiamando `leaderboard_run(leaderboard, filename, speedup)`.
Questo avvia una [simulazione](docs/unlocks/simulation.md) simile a `simulate()`, ma con condizioni iniziali fisse. Ogni categoria della classifica ha condizioni iniziali e di successo diverse.

La partita per la classifica ha successo se la condizione di successo è `True` quando la simulazione termina. 

La simulazione NON terminerà automaticamente quando l'obiettivo viene raggiunto. Devi assicurarti che il programma termini.
Se la partita ha successo, il tuo tempo verrà aggiunto alla classifica.

Per ridurre la variabilità, tutte le run devono coprire almeno 2 ore di tempo simulato. Puoi accelerare la simulazione, quindi non servirà altrettanto tempo reale. Se una run termina prima, verrà ripetuta finché il tempo simulato totale non raggiunge 2 ore. La media dei tempi di tutte le run viene quindi caricata come punteggio.

Ecco un esempio di configurazione che ti porterà nella classifica del fieno.
![|x400](LeaderboardSetup)

## Reset più Veloce
Il reset più veloce è la categoria più prestigiosa. Devi automatizzare completamente il gioco, partendo da un'unica casella di fattoria e terminando quando sblocchi di nuovo le classifiche.

Non devi sbloccare tutto, cerca solo di sbloccare `Unlocks.Leaderboard` il più velocemente possibile.

Ricorda che puoi usare `num_unlocked(unlock) > 0` per controllare se qualcosa è sbloccato. Puoi anche usare `get_cost()` sugli sblocchi per conoscerne il costo e raccogliere automaticamente gli oggetti giusti.

`unlock()` ignora le dipendenze dell'albero tecnologico. Per esempio, puoi sbloccare `Unlocks.Fertilizer` prima di `Unlocks.Water`.

Chiamata di Funzione:
`leaderboard_run(Leaderboards.Fastest_Reset, filename, speedup)`

Simulazione Equivalente:
`unlocks = {}
items = {}
globals = {}
#un valore di seed negativo significa un seed casuale
seed = -1
simulate(filename, unlocks, items, globals, seed, speedup)`

Condizione di Successo:
`num_unlocked(Unlocks.Leaderboard) > 0`

## Labirinto
Inizia con tutto sbloccato e coltiva `9863168` oro il più velocemente possibile. Questa è esattamente la quantità di oro che guadagnerai riutilizzando un labirinto 32x32 per `300` volte.

Chiamata di Funzione:
`leaderboard_run(Leaderboards.Maze, filename, speedup)`

Simulazione Equivalente:
`unlocks = Unlocks
items = {Items.Weird_Substance : 1000000000, Items.Power: 1000000000}
globals = {}
seed = -1
simulate(filename, unlocks, items, globals, seed, speedup)`

Condizione di Successo:
`num_items(Items.Gold) >= 9863168`

## Dinosauro
Inizia con tutto sbloccato e coltiva `33488928` ossa il più velocemente possibile. Questo è esattamente il numero di ossa che otterrai riempiendo un'area 32x32 con la coda del dinosauro.

Chiamata di Funzione:
`leaderboard_run(Leaderboards.Dinosaur, filename, speedup)`

Simulazione Equivalente:
`unlocks = Unlocks
items = {Items.Cactus : 1000000000, Items.Power: 1000000000}
globals = {}
seed = -1
simulate(filename, unlocks, items, globals, seed, speedup)`

Condizione di Successo:
`num_items(Items.Bone) >= 33488928`

## Altre Classifiche di Risorse
Ogni pianta ha la sua classifica per coltivarla il più velocemente possibile. Inizi con tutti gli sblocchi, le risorse necessarie per far crescere la pianta e molta energia. L'obiettivo è coltivare una determinata quantità della risorsa prodotta dalla pianta.

Come sempre, devi assicurarti che il tuo programma termini quando raggiungi l'obiettivo. Una partita non è finita finché il programma non termina, anche se l'obiettivo è stato raggiunto.

### `Leaderboards.Cactus`
`leaderboard_run(Leaderboards.Cactus, filename, speedup)`
Condizione di Successo: `num_items(Items.Cactus) >= 33554432`

### `Leaderboards.Sunflowers`
`leaderboard_run(Leaderboards.Sunflowers, filename, speedup)`
Condizione di Successo: `num_items(Items.Power) >= 100000`

### `Leaderboards.Pumpkins`
`leaderboard_run(Leaderboards.Pumpkins, filename, speedup)`
Condizione di Successo: `num_items(Items.Pumpkin) >= 200000000`

### `Leaderboards.Wood`
`leaderboard_run(Leaderboards.Wood, filename, speedup)`
Condizione di Successo: `num_items(Items.Wood) >= 10000000000`

### `Leaderboards.Carrots`
`leaderboard_run(Leaderboards.Carrots, filename, speedup)`
Condizione di Successo: `num_items(Items.Carrot) >= 2000000000`

### `Leaderboards.Hay`
`leaderboard_run(Leaderboards.Hay, filename, speedup)`
Condizione di Successo: `num_items(Items.Hay) >= 2000000000`

## Classifiche a Drone Singolo
Esistono anche classifiche per la coltivazione con un solo drone. Hai a disposizione un solo drone e una fattoria 8x8 e devi raccogliere una certa quantità di risorse il più rapidamente possibile.

### `Leaderboards.Maze_Single`
`leaderboard_run(Leaderboards.Maze_Single, filename, speedup)`
Condizione di Successo: `num_items(Items.Gold) >= 616448`

### `Leaderboards.Cactus_Single`
`leaderboard_run(Leaderboards.Cactus_Single, filename, speedup)`
Condizione di Successo: `num_items(Items.Cactus) >= 131072`

### `Leaderboards.Sunflowers_Single`
`leaderboard_run(Leaderboards.Sunflowers_Single, filename, speedup)`
Condizione di Successo: `num_items(Items.Power) >= 10000`

### `Leaderboards.Pumpkins_Single`
`leaderboard_run(Leaderboards.Pumpkins_Single, filename, speedup)`
Condizione di Successo: `num_items(Items.Pumpkin) >= 10000000`

### `Leaderboards.Wood_Single`
`leaderboard_run(Leaderboards.Wood_Single, filename, speedup)`
Condizione di Successo: `num_items(Items.Wood) >= 500000000`

### `Leaderboards.Carrots_Single`
`leaderboard_run(Leaderboards.Carrots_Single, filename, speedup)`
Condizione di Successo: `num_items(Items.Carrot) >= 100000000`

### `Leaderboards.Hay_Single`
`leaderboard_run(Leaderboards.Hay_Single, filename, speedup)`
Condizione di Successo: `num_items(Items.Hay) >= 100000000`

---

[Simulazione](docs/unlocks/simulation.md)      [Tempi](docs/unlocks/timing.md)      [Sblocchi Automatici](docs/unlocks/auto_unlock.md)      [Costi](docs/unlocks/costs.md)      [Statistiche](docs/stats.md)

[get_cost()](functions/get_cost)      [num_unlocked()](functions/num_unlocked)      [leaderboard_run()](functions/leaderboard_run)
