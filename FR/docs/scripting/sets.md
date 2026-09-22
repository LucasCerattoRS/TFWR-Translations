[<- Dictionnaires](docs/scripting/dicts.md)
---
# Sets
Les sets sont comme les [dictionnaires](docs/scripting/dicts.md), mais sans valeurs. Ce sont juste un ensemble non ordonné de clés.

Ils sont créés comme des dictionnaires, mais sans valeurs.
`set = {North, East, West}`

Utilise `set()` pour créer un set vide. Note que `{}` crée un dictionnaire vide.

Utilise `set.add(elem)` pour ajouter un nouvel élément au set.

Utilise `set.remove(elem)` pour supprimer un élément d'un set.

Utilise `if elem in set:` pour vérifier si le set contient un élément.

Utilise `for elem in set:` pour itérer sur tous les éléments du set.
Pour les grands sets, l'opérateur `in` est beaucoup plus rapide que sur une liste.

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
    print("North est dans le set")
else:
    print("North n'est pas dans le set")
for element in my_set:
    print(element)
}}

Tout comme les dictionnaires, les sets sont non ordonnés, il n'y a donc aucune garantie sur l'ordre dans lequel les éléments sont itérés.

De plus, les éléments dans les sets sont uniques, donc ajouter un élément qui est déjà dans le set ne changera pas le set.

---

[Dictionnaires](docs/scripting/dicts.md)      [Listes](docs/scripting/lists.md)      [Boucle for](docs/scripting/for.md)

[len()](functions/len)
