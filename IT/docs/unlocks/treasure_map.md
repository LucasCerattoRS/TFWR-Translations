[<- Ferro](docs/unlocks/iron.md)
---
# Mappa del Tesoro

Le leggende narrano di un tesoro inafferrabile nascosto da un pirata smemorato morto da tempo... o qualcosa del genere. E se avesse tracciato il percorso verso il tesoro su una mappa e poi l'avesse persa? Forse la lasciò cadere quando fu messo alle strette da un fiume di lava, e la mappa si è conservata sotto uno strato di basalto. Misurare il basalto potrebbe rivelare qualcosa.

<spoiler=dimmi di più>
Cerca uno strato di `Grounds.Basalt`. Prova a misurare il basalto e scopri cosa ti dice. L'indizio potrebbe condurti alla mappa del tesoro; misurando la mappa otterrai sicuramente il percorso verso il tesoro, ma riuscirai a decifrarne le istruzioni?
</spoiler>

<spoiler=dimmi come fare>
Ecco come funziona: trova lo strato di `Grounds.Basalt` e il blocco `Grounds.Treasure_Map` subito sotto di esso. Puoi usare `measure()` sul basalto per ottenere la posizione `(x, y)` del blocco della mappa sottostante.

Chiama `measure()` sul blocco della mappa per ottenere il percorso del tesoro come stringa di lettere direzionali. N, E, S e W indicano rispettivamente `North`, `East`, `South` e `West`, mentre D significa "Down" o "Dig". Queste lettere descrivono un percorso composto da blocchi `Grounds.Treasure_Path` che conduce al tesoro.

```
path = measure()
for letter in path:
    do_something(letter)
```

Il drone che scava nel blocco della mappa del tesoro è quello che deve trovare il tesoro. Deve rimanere sempre sopra i blocchi `Grounds.Treasure_Path`. Se si sposta su un altro terreno, il percorso si interrompe e il tesoro va perduto.

Alla fine del percorso si trova un blocco `Grounds.Treasure_Goal`. Se il drone non si è allontanato dal percorso, sopra di esso apparirà un `Entities.Underground_Treasure`. Il drone può usare `harvest()` sul forziere per raccoglierne l'oro.

La quantità d'oro è proporzionale alla lunghezza del percorso del tesoro. Potenziare lo sblocco Mappa del Tesoro aumenta la profondità del percorso, mentre potenziare Espandi gli dà più spazio per muoversi lateralmente. Entrambi i potenziamenti aumentano la lunghezza del percorso e la quantità d'oro che troverai.
</spoiler>

---

[Statistiche](docs/stats.md)      [Ciclo For](docs/scripting/for.md)      [Tuple](docs/scripting/tuples.md)      [Sensi Sotterranei](docs/unlocks/underground_senses.md)

[harvest()](functions/harvest)      [move()](functions/move)      [dig()](functions/dig)      [measure()](functions/measure)
