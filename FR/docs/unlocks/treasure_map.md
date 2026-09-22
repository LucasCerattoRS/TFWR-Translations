[<- Fer](docs/unlocks/iron.md)
---
# Carte au trésor

Les légendes parlent d’un trésor insaisissable caché par un pirate distrait mort depuis longtemps — ou quelque chose comme ça. Et s’il avait tracé le chemin vers son trésor sur une carte avant de la perdre ? Peut-être l’a-t-il laissée tomber au bord d’une rivière de lave, et la carte a-t-elle été préservée sous une couche de basalte. Mesurer le basalte pourrait révéler quelque chose.

<spoiler=dis-m’en plus>
Cherche une couche de `Grounds.Basalt`. Essaie de mesurer le basalte pour voir ce qu’il t’indique. L’indice pourrait te mener à la carte au trésor, et mesurer la carte te donnera certainement le chemin du trésor lui-même — mais sauras-tu déchiffrer ses instructions ?
</spoiler>

<spoiler=dis-moi simplement comment faire>
D’accord, voici le principe : trouve la strate de `Grounds.Basalt` et le bloc de `Grounds.Treasure_Map` situé directement dessous. Tu peux appeler `measure()` sur le basalte pour obtenir la position `(x, y)` du bloc de carte en dessous.

Appelle `measure()` sur le bloc de carte pour obtenir le chemin du trésor sous forme d’une chaîne de lettres indiquant des directions. N, E, S et W correspondent respectivement à `North`, `East`, `South` et `West`, tandis que D signifie « Down » ou « Dig ». Ces lettres décrivent un chemin de blocs `Grounds.Treasure_Path` menant au trésor.

```
path = measure()
for letter in path:
    do_something(letter)
```

Le drone qui fore le bloc de carte au trésor est celui qui doit trouver le trésor. Il doit rester sur les blocs `Grounds.Treasure_Path` pendant tout le trajet. S’il passe sur un autre type de sol, le chemin se brise et le trésor est perdu.

Au bout du chemin se trouve un bloc `Grounds.Treasure_Goal`. Si le drone ne s’est pas écarté du chemin, une entité `Entities.Underground_Treasure` apparaîtra dessus. Le drone peut appeler `harvest()` sur le coffre pour récupérer son or.

La quantité d’or est proportionnelle à la longueur du chemin du trésor. Améliorer le déblocage Carte au trésor augmente la profondeur du chemin, tandis qu’améliorer Agrandir lui donne plus d’espace pour se déplacer latéralement. Ces deux améliorations augmentent la longueur du chemin et la quantité d’or que tu trouveras.
</spoiler>

---

[Statistiques](docs/stats.md)      [Boucle for](docs/scripting/for.md)      [Tuples](docs/scripting/tuples.md)      [Sens souterrains](docs/unlocks/underground_senses.md)

[harvest()](functions/harvest)      [move()](functions/move)      [dig()](functions/dig)      [measure()](functions/measure)
