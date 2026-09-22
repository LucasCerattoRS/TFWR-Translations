[<- Dizionari](docs/scripting/dicts.md)
---
# Set
I set sono come i [dizionari](docs/scripting/dicts.md), ma senza valori. Sono solo un insieme non ordinato di chiavi.

Vengono creati come i dizionari, ma senza valori.
`set = {North, East, West}`

Usa `set()` per creare un set vuoto. Nota che `{}` crea un dizionario vuoto.

Usa `set.add(elem)` per aggiungere un nuovo elemento al set.

Usa `set.remove(elem)` per rimuovere un elemento da un set.

Usa `if elem in set:` per verificare se il set contiene un elemento.

Usa `for elem in set:` per iterare su tutti gli elementi del set.
Per i set più grandi, l'operatore `in` è molto più veloce rispetto a una lista.

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
my_set = set()
print(my_set)
my_set.add(1)
my_set.add(North)
print(my_set)
my_set.remove(North)
print(my_set)
if North in my_set:
    print("North è nel set")
else:
    print("North non è nel set")
for element in my_set:
    print(element)
}}

Proprio come i dizionari, i set non sono ordinati, quindi non ci sono garanzie sull'ordine in cui gli elementi vengono iterati.

Inoltre, gli elementi di un set sono unici, quindi aggiungere un elemento già presente non modifica il set.

---

[Dizionari](docs/scripting/dicts.md)      [Liste](docs/scripting/lists.md)      [Ciclo For](docs/scripting/for.md)

[len()](functions/len)
