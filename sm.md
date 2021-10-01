# Szkoła myślenia

## Pewno jakiś wstęp
W opini prowadzącego nazwa jest kretyńska i obciachowa XD
### O czym jest kurs?
- Ludzie piszący maturę umieją wzory a nie matematykę
- Matma mieści się w informatyce stąd to wprowadzenie
- Matematyka składa się z:
- + Mnóstwo wiedzy o różnych szczegółowych faktach (tej wiedzy macie odrobinę)
- + Mechanizm, tz. matematyczny mechanizm poznawania świata. Ten składnik powinien być mniejszy ale za to ważniejszy. I o tym mechaniźmie będą te zajęcia i będziemy się nim bawić
- (Prowadzący nie ogarnia mikrofonu XD)
-  Profesorzy w garniturach byli przerażeni że ludzie po maturze nie umieli odróżnic pszenicy od żyta, a w opinii prowadzącego powinni umieć odróżnić dobra od zła i prawdę od nieprawdy, a reszty da się nauczyć.
-  Najważniejsze słowo w matematyce to DOWÓD.
-  + W szkole uczą dowodzenia na przykładzie geometrii.
-  + Dzis wolimy o tym opowiadać na przykładzie matematyki dyskretnej. (tłumaczenie czym jest dyskretna, to sobie pominę XD)
-  + Będziemy przypominać sobie czym jest dowód na przykładzie m dyskretnej, gadać o niej na wykładach i bawić się dowodami na ćwiczeniach.
-  Dostaniemy listy najlepiej zmierzyć się z nimi przed ćwiczeniami.
-  Dostaniemy 2 listy łatwiejsze i trudniejsze, żebyśmy cały weekend mogli bawić się fajnymi zadaniami. Plan jest taki żebyśmy byli zajęci od rana do nocy.
-  Żeby czegoś się nauczyć nie wystarczy wystawić się na wiedzę i chodzić na wykłady, jedyny sposób to przyłożyć się samemu, uczenie to indywidualny proces. On może sobie pieprzyć przez 2 godziny, ale najważniejszy czas to po wykładzie i przed ćwiczeniami kiedy my możemy się zmagać samodzielnie na podstawie wskazówek z jego pieprzenia.
  
## Bardzo prosta historia o 6 osobach w przedziale kolejowym

Przedział w pociągu jest 6 osób. Okazuje się że spośród tych 6 pasażerów są pary które się znają i są pary które się nie znają. I znajomości są różne.

### Przykład:
- wsród 6 osób zawsze jest taka trójka która się nawzajem zna
- lub zawsze jest taka trójka która się nawzajem nie zna

(rozkmina na temat definicji znania się) Ważne jest tylko to że relacja znajomości jest symetryczna jeśli A zna B to B zna A

#### Dowód
Weźmy trochę czerwonych sznurków i trochę zielonych i każdej parze A i B znającej się każmy trzymać końce zielonego sznurka, a każdej parze nie znającej się każmy trzymać końce     czerwonego sznurka. ("Zabrakło by rąk" komentarz z sali, można trzymać więcej niż jeden w ręce, a jak coś to w zębach też XD)
Sznurki mają 30 końców, simple math.
Żeby udowodnić twierdzenie musi powstać monochromatyczny trójkąt.

Ustalmy sobie jakiegoś pasażera, nazwijmy go A, złapaliśmy go możemy go przesłuchiwać. Będzie kolor K którego będzie trzymał przynajmniej 3 sznurki. Popatrzmy teraz na tych trzech kolesi, nawijmy ich B C D. 
2 opcje z tego:
1. Jeżeli między którymyś z nich jest sznurek tego samego kolor K co tworzy trójkąt monochromatyczny.
2. Żadna z B, C, D nie jest połączona między sobą sznurkiem koloru K, i wtedy oni tworzą trójką monochromatyczny koloru przeciwnego do K.

>Najlepiej to sobie rozrysować, więc to zrób, nie umiem rysować w md XD.

Był to brutalny dowód polegający na przejrzeniu wszystkich przypadków.


## O liczbach Ramseya

>To jest do niczego nie jest przydatne, ale matematycy lubią takie rzeczy.

Minimalna n takie że wsród n ludzi znajdzie się zawsze k takich którzy się nawzajem znają lub m takich którzy na wzajem się nie znają. Nazywa się liczbą Ramseya od(k, m)
Wykazaliśmy że R(3,3) <= 6, prowadzący twierzi że =6, chyba bez dowod

Na ćwiczeniach pokażemy że R(4,4) = 18

R(5,5) jest nieznane

R(6,6) też

R(k,m) = R(m,k)
>Właśnie powiedział że nie chuja warto notować XDD

## O zasadzie szufladkowej
Jeżeli do k szufladek włożymy więcej niż n*k kulek to znajdzie się szufladka w które będzie więcej niż n kulek. ("całkiem oczywiste" ~Prowdzący)

>Przykład: Jeżeli do  2 szufladek włożymy więcej niż 2*2 kulek to znajdzie się szufladka w które będzie więcej niż 2 kulek. Wykorzystane w 6 osobach w przedziale.


Ta zasada będzie eksplatowana na tych zajęciach. I w poprzednich podpunktach notki nie koniecznie pisane są chronologicznie.

## (o Paszczakach i Migotkach) IDK zmianiał plan wykładu i zgubiłem się w tym jak nazwya się ten podpunkt.
Mamy ogrodnika który ma 101 drzew każde ma inną wysokość. Innymi słowy rozważmy ciag 101 liczb (nieujemnych, bez znaczenia) a0, ... a101, parami różnych tzn. dla kazdych i,j taki że i!=j ai!=aj

Ogrodnik chciałby wyciąć jaknajmniej drzew tak żeby "posegregować ten ciąg (w dowolną stronę)".
Pokaż żę w tym ciągu istnieje podciąg monotonicznych o conajmniej 11 drzewach.
Na każdym drzewie napiszemy 2 liczby różnymi kolorami:
- Liczbe oznaczającą długość najdłużeszgo rosnącego podciągu który może rozpocząć się w tym miejscu. (Trochę ssie ta notka bez rysunku)
- Liczbe oznaczającą długość najdłużeszgo niemalejącego podciągu który może rozpocząć się w tym miejscu.
  
Mam udowodnić że istnieje drzewo na którym jest napisana liczba 11, lub większa.
