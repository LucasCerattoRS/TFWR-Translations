[<- Ulepszenie prędkości](docs/unlocks/speed.md) <right>[Marchewki ->](docs/unlocks/carrots.md)
<right>[Debugowanie ->](docs/scripting/debug.md)
<right>[Operatory ->](docs/scripting/operators.md)
---
# Sadzenie
Trawa jest fajna, bo rośnie automatycznie. Wszystkie inne rośliny muszą być sadzone za pomocą funkcji `plant()`. Jedyną rośliną, którą możesz teraz sadzić, jest krzak.
Możesz przekazać typ rośliny, którą chcesz posadzić, do funkcji w ten sposób:

{{codeexample 
{
    "camera_position": {"x": 0, "y": 1.5, "z": 4},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": false,
    "collapsing": true,
    "autoplay": false,
    "items": [],
    "world_size": {"x": 1, "y": 1},
    "execution_speed": 1,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 100,
    "seed": 1,
    "exclude_unlocks": ["watering", "fertilizer"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
#CODE
plant(Entities.Bush)
}}

To posadzi krzak pod dronem.

Wywołaj `clear()`, aby zresetować farmę do samej trawy i zresetować pozycję drona.

Wygląda na to, że jeśli uprawiasz więcej niż jeden rodzaj rośliny na farmie w tym samym czasie, czasami możesz uzyskać wyższy plon. Będziesz musiał zbadać uprawę współrzędną, aby dowiedzieć się więcej.
---

[Statystyki](docs/stats.md)      [If](docs/scripting/if.md)      [Zmysły](docs/unlocks/senses.md)      [Uprawa współrzędna](docs/unlocks/polyculture.md)

[harvest()](functions/harvest)      [plant()](functions/plant)
