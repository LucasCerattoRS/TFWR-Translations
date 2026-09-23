[<- Simulação](docs/unlocks/simulation.md)

---

# Placar de Líderes

Se você chegou até aqui, superou muitos desafios. Mas você os resolveu de forma eficiente? 
Você pode competir com outros jogadores em vários placares de líderes pelos métodos de cultivo mais eficientes.

Você pode iniciar uma tentativa no placar de líderes chamando `leaderboard_run(leaderboard, filename, speedup)`.
Isso inicia uma [simulação](docs/unlocks/simulation.md) parecida com `simulate()`, mas com condições iniciais fixas. Cada categoria do placar tem condições iniciais e de sucesso diferentes.

A tentativa no placar de líderes é bem-sucedida se a condição de sucesso for `True` quando a simulação terminar. 

A simulação NÃO terminará automaticamente quando o objetivo for alcançado. Você deve garantir que o programa termine.
Se a tentativa for bem-sucedida, seu tempo será adicionado ao placar de líderes.

Para reduzir a variação, todas as tentativas devem abranger pelo menos 2 horas de tempo simulado. Você pode acelerar a simulação, então ela não levará tudo isso em tempo real. Se uma tentativa terminar antes, ela será repetida até o tempo simulado total chegar a 2 horas. A média de tempo de todas as tentativas será enviada como sua pontuação.

Aqui está um exemplo de configuração que colocará você no placar de feno.
![|x400](LeaderboardSetup)

## Reset Mais Rápido

O reset mais rápido é a categoria de maior prestígio. Nela, você automatiza completamente o jogo, começando com um único quadrado de fazenda e terminando quando desbloqueia os placares de líderes novamente.

Você não precisa desbloquear tudo, apenas tente desbloquear `Unlocks.Leaderboard` o mais rápido possível.

Lembre-se de que você pode usar `num_unlocked(unlock) > 0` para verificar se algo está desbloqueado. Também pode usar `get_cost()` em desbloqueios para consultar o custo deles e produzir automaticamente os itens certos.

`unlock()` não considera as dependências da árvore de tecnologias. Por exemplo, é possível desbloquear `Unlocks.Fertilizer` antes de `Unlocks.Water`.

Chamada de Função:
`leaderboard_run(Leaderboards.Fastest_Reset, filename, speedup)`

Simulação Equivalente:

`unlocks = {}
items = {}
globals = {}
#um valor de semente negativo significa uma semente aleatória
seed = -1
simulate(filename, unlocks, items, globals, seed, speedup)`

Condição de Sucesso:
`num_unlocked(Unlocks.Leaderboard) > 0`

## Labirinto

Comece com tudo desbloqueado e cultive `9863168` de ouro o mais rápido que puder. Esta é exatamente a quantidade de ouro que você ganhará ao reutilizar um labirinto de 32x32 `300` vezes.

Chamada de Função:
`leaderboard_run(Leaderboards.Maze, filename, speedup)`

Simulação Equivalente:

`unlocks = Unlocks
items = {Items.Weird_Substance : 1000000000, Items.Power: 1000000000}
globals = {}
seed = -1
simulate(filename, unlocks, items, globals, seed, speedup)`

Condição de Sucesso:
`num_items(Items.Gold) >= 9863168`

## Dinossauro

Comece com tudo desbloqueado e cultive `33488928` de ossos o mais rápido que puder. Este é exatamente o número de ossos que você obterá se preencher uma área de 32x32 com a cauda do dinossauro.

Chamada de Função:
`leaderboard_run(Leaderboards.Dinosaur, filename, speedup)`

Simulação Equivalente:

`unlocks = Unlocks
items = {Items.Cactus : 1000000000, Items.Power: 1000000000}
globals = {}
seed = -1
simulate(filename, unlocks, items, globals, seed, speedup)`

Condição de Sucesso:
`num_items(Items.Bone) >= 33488928`

## Outros Placares de Líderes de Recursos

Cada planta tem seu próprio placar de líderes para cultivar aquela planta em particular o mais rápido possível. Você começa com todos os desbloqueios, os recursos que precisa para cultivar a planta e muita energia. O objetivo é cultivar uma quantidade definida do recurso produzido pela planta.

Como sempre, você precisa garantir que seu programa termine quando atingir o objetivo. Uma corrida não termina até que o programa termine, mesmo que o objetivo seja alcançado.

### `Leaderboards.Cactus`

`leaderboard_run(Leaderboards.Cactus, filename, speedup)`
Condição de Sucesso: `num_items(Items.Cactus) >= 33554432`

### `Leaderboards.Sunflowers`

`leaderboard_run(Leaderboards.Sunflowers, filename, speedup)`
Condição de Sucesso: `num_items(Items.Power) >= 100000`

### `Leaderboards.Pumpkins`

`leaderboard_run(Leaderboards.Pumpkins, filename, speedup)`
Condição de Sucesso: `num_items(Items.Pumpkin) >= 200000000`

### `Leaderboards.Wood`

`leaderboard_run(Leaderboards.Wood, filename, speedup)`
Condição de Sucesso: `num_items(Items.Wood) >= 10000000000`

### `Leaderboards.Carrots`

`leaderboard_run(Leaderboards.Carrots, filename, speedup)`
Condição de Sucesso: `num_items(Items.Carrot) >= 2000000000`

### `Leaderboards.Hay`

`leaderboard_run(Leaderboards.Hay, filename, speedup)`
Condição de Sucesso: `num_items(Items.Hay) >= 2000000000`

## Placares de Líderes de Drone Único

Também há placares para produzir com um único drone. Você recebe apenas um drone e uma fazenda 8x8 e precisa produzir certa quantidade de recursos o mais rápido possível.

### `Leaderboards.Maze_Single`

`leaderboard_run(Leaderboards.Maze_Single, filename, speedup)`
Condição de Sucesso: `num_items(Items.Gold) >= 616448`

### `Leaderboards.Cactus_Single`

`leaderboard_run(Leaderboards.Cactus_Single, filename, speedup)`
Condição de Sucesso: `num_items(Items.Cactus) >= 131072`

### `Leaderboards.Sunflowers_Single`

`leaderboard_run(Leaderboards.Sunflowers_Single, filename, speedup)`
Condição de Sucesso: `num_items(Items.Power) >= 10000`

### `Leaderboards.Pumpkins_Single`

`leaderboard_run(Leaderboards.Pumpkins_Single, filename, speedup)`
Condição de Sucesso: `num_items(Items.Pumpkin) >= 10000000`

### `Leaderboards.Wood_Single`

`leaderboard_run(Leaderboards.Wood_Single, filename, speedup)`
Condição de Sucesso: `num_items(Items.Wood) >= 500000000`

### `Leaderboards.Carrots_Single`

`leaderboard_run(Leaderboards.Carrots_Single, filename, speedup)`
Condição de Sucesso: `num_items(Items.Carrot) >= 100000000`

### `Leaderboards.Hay_Single`

`leaderboard_run(Leaderboards.Hay_Single, filename, speedup)`
Condição de Sucesso: `num_items(Items.Hay) >= 100000000`

---

[Simulação](docs/unlocks/simulation.md)      [Medição de Tempo](docs/unlocks/timing.md)      [Desbloqueios Automáticos](docs/unlocks/auto_unlock.md)      [Custos](docs/unlocks/costs.md)      [Estatísticas](docs/stats.md)

[get_cost()](functions/get_cost)      [num_unlocked()](functions/num_unlocked)      [leaderboard_run()](functions/leaderboard_run)
