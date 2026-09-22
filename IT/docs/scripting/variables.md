[<- Operatori](docs/scripting/operators.md) <right>[Liste ->](docs/scripting/lists.md)
<right>[Funzioni ->](docs/scripting/functions.md)
---
# Variabili
Le variabili possono essere pensate come dei contenitori con un nome che possono contenere un valore.
L'operatore `=` si usa per dichiarare una variabile e memorizzarvi un valore.

`variable_name = value`

Il lato sinistro dell'operatore è il nome della variabile. Puoi assegnarle qualsiasi nome valido.
Il lato destro è un'espressione il cui valore risultante verrà memorizzato nella variabile.

Dichiara una variabile chiamata `a` e memorizzaci il valore `5`:
`a = 5`
Dichiara una variabile chiamata `b` e memorizzaci il valore di ritorno di `can_harvest()`:
`b = can_harvest()`

Non confondere l'operatore `=` con l'operatore `==`. 
L'operatore `==` controlla se due valori sono uguali e restituisce `True` o `False`.
L'operatore `=` assegna il valore a destra al nome a sinistra.

Dopo aver assegnato una variabile, puoi usarla nel codice per recuperare il valore che contiene.

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

Il ciclo qui sopra viene eseguito 5 volte perché `a` è impostato a `5`.
Anche la `i` del ciclo `for` è una variabile. A ogni iterazione le viene assegnato automaticamente il valore corrente della sequenza. Non deve per forza chiamarsi `i`: puoi darle qualsiasi nome di variabile valido.

Le variabili ti permettono di fare la stessa cosa anche con un ciclo while:

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

Questo fa la stessa cosa del ciclo `for` precedente, ma dobbiamo incrementare `i` manualmente.
Per incrementare `i`, la impostiamo al suo valore corrente più `1`. Modificare una variabile in base al suo valore precedente è molto comune.
Si può abbreviare usando questi operatori: `+=, -=, *=, /=, %=`

`i = i + 1` è la stessa cosa di `i += 1`
`a = a / 3` è la stessa cosa di `a /= 3`

---

[Operatori](docs/scripting/operators.md)      [Ciclo While](docs/scripting/while.md)      [Ciclo For](docs/scripting/for.md)      [Funzioni](docs/scripting/functions.md)      [Scope dei Nomi](docs/scripting/scopes.md)
