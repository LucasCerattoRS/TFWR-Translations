[<- Fonctions](docs/scripting/functions.md)
---
# Tuples
Les tuples sont un excellent moyen de combiner plusieurs valeurs en une seule.
Pour créer un tuple, il suffit de séparer les valeurs par des virgules :

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
tuple = 1, 2
print(tuple)
}}

Tu peux aussi les décompresser à nouveau en plusieurs variables. Dans le code ci-dessous, le tuple `(1, 2)` est décompressé en deux variables `a` et `b`.

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
a, b = 1, 2
print(a)
a, b = b, a
print(a)
}}

Les tuples peuvent être indexés comme des listes, mais ils sont immuables et ne peuvent pas être modifiés après leur création.

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
tuple = 1, 2
print(tuple[1])

tuple[0] = 3
}}

<unlock=dicts>
Contrairement aux listes, les tuples peuvent servir de clés dans les dictionnaires.

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
d = {(1,2):(4,5)}

print(d[(1,2)])
}}</unlock>

Ils peuvent aussi être utiles pour renvoyer plusieurs valeurs dans une fonction.

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
def f():
    return 1, 2

a, b = f()
}}

---

[Listes](docs/scripting/lists.md)      [Dictionnaires](docs/scripting/dicts.md)      [Fonctions](docs/scripting/functions.md)
