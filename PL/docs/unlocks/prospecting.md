[<- Żelazo](docs/unlocks/iron.md)
---
# Poszukiwanie żelaza

Być może zauważyłeś, że żyły żelaza czasem trudno znaleźć. Można kopać na oślep i liczyć na szczęście, ale istnieje lepszy sposób: żelazo jest magnetyczne, więc możemy wykrywać je z dużej odległości.

Właśnie do tego służy polecenie `prospect_iron()`. Funkcja `prospect_iron()` zwraca kierunek świata (`North`, `East`, `South` lub `West`), w którym dron musi się poruszyć, aby zrobić krok w stronę najbliższej rudy żelaza. Wykonanie polecenia kosztuje 1 węgiel.

`prospect_iron()` zwraca `None`, jeśli dron znajduje się już bezpośrednio nad najbliższą rudą żelaza, nie masz wystarczająco dużo węgla albo w zasięgu nie ma żelaza.

Poniższy kod przesuwa drona o jeden krok bliżej następnej rudy żelaza:

`if prospect_iron() != None:
    move(prospect_iron())
`

Warto zoptymalizować ten kod za pomocą zmiennej, ponieważ obecnie wywołuje `prospect_iron()` dwukrotnie, co kosztuje 2 sztuki węgla.

Najbliższa ruda żelaza jest wyznaczana na podstawie liczby kroków, które musi wykonać dron. Jeśli ruda znajduje się 2 bloki na wschód i 3 bloki na północ od drona, odległość wynosi 5, ponieważ dotarcie tam wymaga pięciu kroków.

Kopanie również liczy się jako krok. Jeśli dodatkowo żelazo jest zakopane 7 bloków pod ziemią, odległość wynosi 12, ponieważ dron musi zrobić pięć kroków, aby znaleźć się nad rudą, a następnie wykopać siedem bloków, aby do niej dotrzeć.

---

[Żelazo](docs/unlocks/iron.md)      [Podziemne zmysły](docs/unlocks/underground_senses.md)

[move()](functions/move)      [dig()](functions/dig)      [prospect_iron()](functions/prospect_iron)
