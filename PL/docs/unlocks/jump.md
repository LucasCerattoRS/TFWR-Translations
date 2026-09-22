[<- Węgiel](docs/unlocks/coal.md)
---
# Skok

Twój dron odblokował polecenie `jump()`.

To polecenie pozwala wskazać określone odblokowania i przenieść się do nich. Jest szczególnie przydatne podczas debugowania lub do powrotu do niedawno pominiętej żyły rudy. Używa się go, przekazując odblokowanie jako argument, na przykład `Unlocks.Iron`.

`jump()` działa tylko z odblokowaniami występującymi pod ziemią, na przykład `jump(Unlocks.Rice)` lub `jump(Unlocks.Iron)`.

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

Skok nie zawsze przeniesie cię bezpośrednio do docelowego odblokowania, więc być może trzeba będzie trochę się rozejrzeć, ale cel na pewno znajduje się w pobliżu.

`jump()` można użyć tylko raz podczas jednego wykonania programu.

---

[jump()](functions/jump)
