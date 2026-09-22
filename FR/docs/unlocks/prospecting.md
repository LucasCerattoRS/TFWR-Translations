[<- Fer](docs/unlocks/iron.md)
---
# Prospection du fer

Tu as peut-être remarqué qu’il est parfois difficile de trouver des filons de fer. Tu pourrais creuser au hasard en espérant tomber dessus, mais il existe une meilleure méthode : le fer étant magnétique, nous pouvons le repérer à grande distance.

La commande `prospect_iron()` sert précisément à cela. `prospect_iron()` renvoie la direction cardinale (`North`, `East`, `South` ou `West`) dans laquelle le drone doit se déplacer pour faire un pas vers le minerai de fer le plus proche. L’exécution de la commande coûte 1 charbon.

`prospect_iron()` renvoie `None` si le drone se trouve déjà directement au-dessus du minerai de fer le plus proche, si tu n’as pas assez de charbon pour exécuter la commande ou s’il n’y a aucun fer à portée.

Tu peux utiliser le code suivant pour te rapprocher d’un pas du prochain minerai de fer :

`if prospect_iron() != None:
    move(prospect_iron())
`

Tu peux optimiser ce code avec une variable, car il appelle actuellement `prospect_iron()` deux fois et coûte donc 2 charbons.

La distance du minerai de fer le plus proche correspond au nombre de pas que le drone doit effectuer. Si un minerai se trouve 2 blocs à l’est et 3 blocs au nord du drone, la distance est de 5, car le drone doit faire cinq pas pour l’atteindre.

Forer compte également comme un pas. Si ce fer est en plus enfoui à 7 blocs de profondeur, la distance est de 12 : le drone doit faire cinq pas pour se placer au-dessus du fer, puis forer sept fois pour l’atteindre.

---

[Fer](docs/unlocks/iron.md)      [Sens souterrains](docs/unlocks/underground_senses.md)

[move()](functions/move)      [dig()](functions/dig)      [prospect_iron()](functions/prospect_iron)
