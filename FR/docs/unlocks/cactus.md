[<- Citrouilles](docs/unlocks/pumpkins.md) <right>[Dinosaures ->](docs/unlocks/dinosaurs.md)
---
# Cactus
Comme les autres plantes, les [cactus](objects/cactus) peuvent être cultivés sur du sol et récoltés comme d'habitude.

Cependant, ils existent en différentes tailles et ont un étrange sens de l'ordre.

Si tu récoltes un cactus adulte et que tous les cactus voisins sont triés, il récoltera aussi récursivement tous les cactus voisins.

Un cactus est considéré comme trié si tous les cactus voisins au `North` et à l'`East` sont adultes et de taille supérieure ou égale, et tous les cactus voisins au `South` et à l'`West` sont adultes et de taille inférieure ou égale.

La récolte ne se propagera que si tous les cactus adjacents sont adultes et triés.
Cela signifie que si un carré de cactus adultes est trié par taille et que tu récoltes un cactus, il récoltera le carré entier.

Un cactus adulte apparaîtra marron s'il n'est pas trié. Une fois trié, il redeviendra vert.

Tu recevras un nombre de cactus égal au carré du nombre de cactus récoltés. Donc si tu récoltes `n` cactus simultanément, tu recevras `n**2` `Items.Cactus`.

La taille d'un cactus peut être mesurée avec `measure()`.
C'est toujours l'un de ces nombres : `0,1,2,3,4,5,6,7,8,9`.

Tu peux aussi passer une direction à `measure(direction)` pour mesurer la case voisine dans cette direction du drone.

Tu peux échanger un cactus avec son voisin dans n'importe quelle direction en utilisant la commande `swap()`.
`swap(direction)` échange l'objet sous le drone avec l'objet situé à une case dans la `direction` du drone.

{{codeexample 
{
    "camera_position": {"x": -1.5, "y": 2.4, "z": 5},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": true,
    "collapsing": true,
    "autoplay": false,
    "items": [{"item": "pumpkin", "n": 32}],
    "world_size": {"x": 4, "y": 4},
    "execution_speed": 1,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 100,
    "seed": 1,
    "exclude_unlocks": ["fertilizer", "watering"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
for _ in range(4):
    for _ in range(4):
        till()
        plant(Entities.Cactus)
        move(East)
    move(North)
for _ in range(4):
    for _ in range(4):
        for _ in range(4):
            x,y = get_pos_x(), get_pos_y()
            if x > 0 and measure(West) > measure():
                swap(West)
            if y > 0 and measure(South) > measure():
                swap(South)
            if x < 3 and measure(East) < measure():
                swap(East)
            if y < 3 and measure(North) < measure():
                swap(North)
            move(East)
        move(North)
move(East)
move(North)
move(North)
swap(West)
swap(South)
swap(East)
swap(North)
#CODE
swap(North)
swap(East)
swap(South)
swap(West)
harvest()
}}

## Exemples numériques
Dans chacune de ces grilles, tous les cactus sont triés et la récolte se propagera sur tout le champ :
`3 4 5    3 3 3    1 2 3    1 5 9
2 3 4    2 2 2    1 2 3    1 3 8
1 2 3    1 1 1    1 2 3    1 3 4`

Dans cette grille, seul le cactus en bas à gauche est trié, ce qui n'est pas suffisant pour que la récolte se propage :
`1 5 3
4 9 7
3 3 2`

<spoiler=afficher l’indice 1>
Si chaque ligne est déjà triée séparément, trier chaque colonne séparément ne désorganisera pas les lignes.
</spoiler>
<spoiler=afficher l’indice 2>
Il existe de nombreux algorithmes de tri célèbres et ingénieux. Si tu ne les connais pas, renseigne-toi et cherche lesquels pourraient être adaptés à ce problème. Tous ne conviennent pas ici, car tu ne peux échanger que des cactus voisins.
</spoiler>
<spoiler=afficher l’indice 3>
Le « tri à bulles » est sans doute l’algorithme de tri le plus simple. Il consiste à parcourir plusieurs fois les éléments et à échanger ceux qui sont voisins et mal ordonnés, jusqu’à ce qu’il n’en reste plus.

Voici ce que cela donne avec des cactus :
{{codeexample 
{
    "camera_position": {"x": -4, "y": 1, "z": 6},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": false,
    "show_inventory": true,
    "show_output": false,
    "collapsing": false,
    "autoplay": true,
    "items": [{"item": "pumpkin", "n": 18}],
    "world_size": {"x": 9, "y": 1},
    "execution_speed": 2,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 1,
    "seed": 1,
    "exclude_unlocks": ["fertilizer", "watering"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
#CODE
for _ in range(9):
    till()
    plant(Entities.Cactus)
    move(East)
sorted = False
while not sorted:
    sorted = True
    for _ in range(9):
        move(East)
        if get_pos_x() > 0 and measure(West) > measure():
            swap(West)
            sorted = False
harvest()
}}
Il existe bien sûr de nombreuses façons d’améliorer cette stratégie !
Une fois que tu sais trier une seule ligne, utilise l’indice 1 pour trier tout le champ.
</spoiler>

---

[Statistiques](docs/stats.md)

[harvest()](functions/harvest)      [plant()](functions/plant)      [move()](functions/move)      [till()](functions/till)      [swap()](functions/swap)      [measure()](functions/measure)
