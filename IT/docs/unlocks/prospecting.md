[<- Ferro](docs/unlocks/iron.md)
---
# Prospezione del Ferro

Avrai notato che a volte è difficile trovare le vene di ferro. Potresti scavare a caso sperando di incontrarle, ma c'è un modo migliore: dato che il ferro è magnetico, possiamo rilevarlo da molto lontano.

Il comando `prospect_iron()` serve proprio a questo. `prospect_iron()` restituisce la direzione cardinale (`North`, `East`, `South` o `West`) in cui il drone deve muoversi per compiere un passo verso il minerale di ferro più vicino. Eseguire il comando costa 1 carbone.

`prospect_iron()` restituisce `None` se il drone si trova già direttamente sopra il minerale di ferro più vicino, se non hai abbastanza carbone per eseguire il comando o se non c'è ferro nel raggio d'azione.

Puoi usare il codice seguente per avvicinarti di un passo al prossimo minerale di ferro:

`if prospect_iron() != None:
    move(prospect_iron())
`

Potresti ottimizzare questo codice con una variabile, perché al momento chiama `prospect_iron()` due volte e costa 2 unità di carbone.

Il minerale di ferro più vicino viene calcolato in base al numero di passi che il drone deve compiere. Se un minerale si trova 2 blocchi a est e 3 blocchi a nord del drone, la distanza è 5, perché servono cinque passi per raggiungerlo.

Anche scavare conta come un passo. Quindi, se il ferro è inoltre sepolto 7 blocchi più in profondità, la distanza è 12: servono cinque passi per portarsi sopra il ferro e poi sette scavi per raggiungerlo.

---

[Ferro](docs/unlocks/iron.md)      [Sensi Sotterranei](docs/unlocks/underground_senses.md)

[move()](functions/move)      [dig()](functions/dig)      [prospect_iron()](functions/prospect_iron)
