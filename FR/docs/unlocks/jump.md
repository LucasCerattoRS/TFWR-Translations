[<- Charbon](docs/unlocks/coal.md)
---
# Saut

Ton drone a débloqué la commande `jump()`.

Cette commande te permet de cibler certains déblocages et de sauter directement jusqu’à eux. Elle est particulièrement utile pour le débogage ou pour revenir à un filon de minerai que tu viens de manquer. Pour l’utiliser, passe-lui un déblocage en argument, par exemple `Unlocks.Iron`.

`jump()` ne fonctionne qu’avec les déblocages qui apparaissent sous terre, comme `jump(Unlocks.Rice)` ou `jump(Unlocks.Iron)`.

{{codeexample 
{
    "camera_position": {"x": -1, "y": 0, "z": 8},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": false,
    "collapsing": true,
    "autoplay": false,
    "items": [],
    "world_size": {"x": 4, "y": 4},
    "execution_speed": 1,
    "digging_speed": 3,
    "action_ticks": 200,
    "operation_ticks": 200,
    "seed": 1,
    "exclude_unlocks": ["watering", "fertilizer", "mushrooms"],
    "starting_chunk": 0
}
#CODE
dig()
dig()
dig()
jump(Unlocks.Iron)
do_a_flip()
}}

Il n’est pas garanti que le saut t’amène directement au déblocage ciblé. Tu devras peut-être encore chercher un peu, mais la cible se trouvera forcément à proximité.

`jump()` ne peut être utilisée qu’une seule fois par exécution du programme.

---

[jump()](functions/jump)
