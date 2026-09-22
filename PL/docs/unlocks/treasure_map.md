[<- Żelazo](docs/unlocks/iron.md)
---
# Mapa skarbu

Legendy mówią o nieuchwytnym skarbie ukrytym przez dawno zmarłego, zapominalskiego pirata — albo jakoś tak. A co, jeśli zapisał drogę do skarbu na mapie, a potem ją zgubił? Może upuścił mapę, gdy odcięła mu drogę rzeka lawy, i zachowała się ona pod warstwą bazaltu. Pomiar bazaltu może coś ujawnić.

<spoiler=powiedz mi więcej>
Wypatruj warstwy `Grounds.Basalt`. Spróbuj zmierzyć bazalt i sprawdź, co ci powie. Wskazówka może zaprowadzić cię do mapy skarbu, a zmierzenie mapy z pewnością zwróci drogę do samego skarbu — tylko czy uda ci się rozszyfrować jej instrukcje?
</spoiler>

<spoiler=po prostu powiedz jak>
Dobrze, sprawa wygląda tak: znajdź warstwę `Grounds.Basalt` i blok `Grounds.Treasure_Map` znajdujący się bezpośrednio pod nią. Możesz użyć `measure()` na bazalcie, aby uzyskać pozycję `(x, y)` leżącego niżej bloku mapy.

Wywołaj `measure()` na bloku mapy, aby otrzymać drogę do skarbu jako ciąg liter oznaczających kierunki. N, E, S i W oznaczają odpowiednio `North`, `East`, `South` i `West`, natomiast D oznacza „Down” lub „Dig”. Litery te opisują drogę złożoną z bloków `Grounds.Treasure_Path`, która prowadzi do skarbu.

```
path = measure()
for letter in path:
    do_something(letter)
```

Dron, który dokopie się do bloku mapy skarbu, musi również odnaleźć skarb. Przez cały czas musi pozostawać na blokach `Grounds.Treasure_Path`. Jeśli przemieści się na inne podłoże, droga zniknie, a skarb zostanie utracony.

Na końcu drogi znajduje się blok `Grounds.Treasure_Goal`. Jeśli dron nie zboczył z drogi, pojawi się na nim `Entities.Underground_Treasure`. Dron może użyć `harvest()` na skrzyni, aby zebrać złoto.

Ilość złota jest proporcjonalna do długości drogi do skarbu. Ulepszanie odblokowania Mapy skarbu zwiększa jej głębokość, a ulepszanie Rozszerzenia daje jej więcej miejsca na ruch w poziomie. Oba ulepszenia wydłużają drogę do skarbu i zwiększają ilość znalezionego złota.
</spoiler>

---

[Statystyki](docs/stats.md)      [Pętla for](docs/scripting/for.md)      [Krotki](docs/scripting/tuples.md)      [Podziemne zmysły](docs/unlocks/underground_senses.md)

[harvest()](functions/harvest)      [move()](functions/move)      [dig()](functions/dig)      [measure()](functions/measure)
