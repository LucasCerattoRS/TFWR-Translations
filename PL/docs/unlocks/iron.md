[<- Węgiel](docs/unlocks/coal.md) <right>[Kwarc ->](docs/unlocks/quartz.md)
<right>[Poszukiwanie żelaza ->](docs/unlocks/prospecting.md)
<right>[Mapa skarbu ->](docs/unlocks/treasure_map.md)
---
# Żelazo

Odkryłeś żyły żelaza w warstwie skał pod gliną.

Żyły żelaza są początkowo małe, a ich znalezienie wymaga odrobiny szczęścia. Kolejne poziomy tego odblokowania zwiększają maksymalny rozmiar żyły rudy. Jeśli potrzebujesz bardziej niezawodnej metody znajdowania żelaza, sprawdź także odblokowanie poszukiwania rud.

Żyła żelaza jest zawsze ciągła i nie łączy się po przekątnej. Jeśli znajdziesz kawałek żelaza, szukaj kolejnych pod nim lub obok niego, aby wydobyć całą żyłę.

{{codeexample 
{
    "camera_position": {"x": -1, "y": 0, "z": 8},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": false,
    "collapsing": false,
    "autoplay": true,
    "items": [{"item": "hay", "n": 100}, {"item": "wood", "n": 100}],
    "world_size": {"x": 5, "y": 5},
    "execution_speed": 1,
    "digging_speed": 4,
    "action_ticks": 200,
    "operation_ticks": 200,
    "seed": 9,
    "exclude_unlocks": ["watering", "fertilizer", "mushrooms", "coal", "quartz"]
}
#SETUP
jump(Unlocks.Iron)
#CODE
for i in range(4):
    dig()
do_a_flip()
}}

---

[Statystyki](docs/stats.md)      [Górnictwo](docs/unlocks/mining.md)      [Poszukiwanie żelaza](docs/unlocks/prospecting.md)      [Podziemne zmysły](docs/unlocks/underground_senses.md)

[move()](functions/move)      [dig()](functions/dig)
