[<- Funzioni](docs/scripting/functions.md)
---
# Scope dei Nomi
Gli scope determinano dove è possibile accedere alle variabili. Uno scope è essenzialmente un'associazione tra nomi e valori.
Funzionano in modo molto simile a Python.

C'è uno scope globale, e ogni funzione ha uno scope locale.
Quando definisci una variabile, viene aggiunta allo scope corrente.
Tutto ciò che è al di fuori di una definizione di funzione è considerato parte dello scope globale.

`x = 1`
Assegna un valore di `1` al nome `x` nello scope globale.

Questa istruzione `def` assegna una funzione al nome `f` nello scope globale.
`def f():
    `Assegna il valore `1` al nome `y` nello scope locale di `f`.`
    y = 1

    `Assegna una funzione al nome `g` nello scope locale di `f`.`
    def g():
        pass`

`f()`
Recupera la funzione memorizzata in `f` dallo scope globale e la chiama.

`print(y)`
Questa istruzione `print` nello scope globale genera un errore perché `y` non è mai stata dichiarata nello scope globale, quindi qui non possiamo leggerla.
Esisteva solo nello scope locale di `f`.

## La Parola Chiave global
Per impostazione predefinita, tutte le variabili nelle funzioni vengono associate allo scope locale, anche se nello scope globale esiste una variabile con lo stesso nome.

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
x = 0

def f():
    x = 1
f()
print(x)
}}

Questo codice stampa `0` perché la `x` locale all'interno di `f` non è la stessa variabile della `x` globale, quindi la `x` globale rimane invariata. È importante, perché altrimenti una chiamata di funzione potrebbe sovrascrivere accidentalmente una variabile globale che ha lo stesso nome di una delle variabili locali della funzione.

Se vuoi scrivere su una variabile globale, devi farlo esplicitamente usando la keyword `global`.

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
x = 0

def f():
    global x
    x = 1
f()
print(x)
}}

In questo esempio, `global x` associa `x` alla variabile globale `x` definita sopra. Ora il codice stamperà `1`.
Nota che modificare le variabili globali è solitamente il primo passo verso il codice spaghetti, dove ogni parte del programma influenza ogni altra parte del programma, quindi non abusarne.

## Cicli e Rami
Cicli e ramificazioni non creano i propri scope, quindi qualsiasi cosa dichiarata al loro interno può ancora essere usata all'esterno.

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
for i in range(3):
    pass
print(i)
}}

Questo stampa `2` perché l'ultima iterazione del ciclo `for` ha assegnato `2` a `i`.

---

[Variabili](docs/scripting/variables.md)      [Funzioni](docs/scripting/functions.md)      [Import](docs/scripting/import.md)      [Mega Fattoria](docs/unlocks/megafarm.md)
