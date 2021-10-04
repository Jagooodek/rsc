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

Przedział w pociągu jest 6 osób. Wśród tych pasażerów mogą być pary które się znają i które się nie znają.

### Teza:
- wsród 6 osób zawsze jest taka trójka która się nawzajem zna
- lub zawsze jest taka trójka która się nawzajem nie zna

(rozkmina na temat definicji znania się) Ważne jest tylko to że relacja znajomości jest symetryczna jeśli A zna B to B zna A

#### Dowód
Weźmy trochę czerwonych sznurków i trochę zielonych i każdej parze A i B znającej się każmy trzymać końce zielonego sznurka, a każdej parze nie znającej się każmy trzymać końce     czerwonego sznurka. ("Zabrakło by rąk" komentarz z sali, można trzymać więcej niż jeden w ręce, a jak coś to w zębach też XD)
Sznurki mają 30 końców, simple math.
Żeby udowodnić twierdzenie musi powstać monochromatyczny trójkąt.

Ustalmy sobie jakiegoś pasażera, nazwijmy go A, złapaliśmy go możemy go przesłuchiwać. Pomieważ trzyma on 5 sznurków które mogą mieć jeden z dwóch kolorów to będzie istniał kolor K którego pasażer będzie trzymał przynajmniej 3 sznurki. Popatrzmy teraz na tych trzech kolesi którzy trzymają te 3 sznurki, nawijmy ich B C D. 
2 opcje z tego:
1. Jeżeli między którąś parą z nich jest sznurek tego samego kolor K co tworzy trójkąt monochromatyczny.
2. Jeżeli żaden z B, C, D nie jest połączony między sobą sznurkiem koloru K, wtedy oni tworzą trójką monochromatyczny koloru przeciwnego do K.

>Najlepiej to sobie rozrysować, więc to zrób, nie umiem rysować w md XD.

Był to brutalny dowód polegający na przejrzeniu wszystkich przypadków.


## O liczbach Ramseya

>To jest do niczego nie jest przydatne, ale matematycy lubią takie rzeczy.

Minimalna liczba n taka, że wsród n ludzi znajdzie się zawsze k takich którzy się nawzajem znają lub m takich którzy na wzajem się nie znają. Nazywa się liczbą Ramseya od(k, m)
Wykazaliśmy że R(3,3) <= 6, prowadzący twierzi że =6, nie pokazał dowodu.

Na ćwiczeniach pokażemy że R(4,4) = 18

R(5,5) jest nieznane

R(6,6) też

R(k,m) = R(m,k)
>Właśnie powiedział że nie chuja warto notować XDD

## O zasadzie szufladkowej
Jeżeli do k szufladek włożymy więcej niż n*k kulek to znajdzie się szufladka w które będzie więcej niż n kulek. ("całkiem oczywiste" ~Prowdzący)

>Przykład: Jeżeli do  2 szufladek włożymy więcej niż 2*2 kulek to znajdzie się szufladka w które będzie więcej niż 2 kulek. Wykorzystane w 6 osobach w przedziale.


Ta zasada będzie eksplatowana na tych zajęciach. I w poprzednich podpunktach notki nie koniecznie pisane są chronologicznie.

## IDK zmianiał plan wykładu i zgubiłem się w tym jak nazwya się ten podpunkt.
Mamy ogrodnika który ma 101 drzew każde ma inną wysokość. Innymi słowy rozważmy ciag 101 liczb (nieujemnych, bez znaczenia) a0, ... a101, parami różnych tzn. dla kazdych i,j taki że i!=j a~i~!=a~j~

Ogrodnik chciałby wyciąć jaknajmniej drzew tak żeby "posegregować ten ciąg (w dowolną stronę)".
Pokaż żę w tym ciągu istnieje podciąg monotonicznych o conajmniej 11 drzewach.
Na każdym drzewie napiszemy 2 liczby różnymi kolorami:
- Liczbe oznaczającą długość najdłużeszgo rosnącego podciągu który może rozpocząć się w tym miejscu. (Trochę ssie ta notka bez rysunku)
- Liczbe oznaczającą długość najdłużeszgo niemalejącego podciągu który może rozpocząć się w tym miejscu.
  
Mam udowodnić że istnieje drzewo na którym jest napisana liczba 11, lub większa.

### Dowód
>Apel o zaszczepienie się żebyśmy mogli bezpiecznie podawać sobie kartki.

W sumie wyżej to też część dowodu ale już mi się nie chce zmieniać.
Dowód będzie nie wprost. Załóżmy że obie liczby na każdym drzewie są należą do {1, 2, ... , 10}.

Wezmę teraz 100 szufladek, każda będzie oznaczona parą liczb z tego przedziału, wrzucimy każe drzewo do szufladki zgodnej z liczbami napisanymi na tym drzewie. Więc w przynajmniej jednej szufladce będzie więcej niż 1 drzewo. Teraz wykazujemy że dwa drzewa nie mogą mieć tej samej pary liczb.~~Nie umiem zanotować tego wykazania bez rysunku :(~~ Weźmy dwa drzewa o tych samych liczbach a i b, jeżeli drzewo po prawej będzie wyższe to na pewno od drzewa po lewej ta się zbudować ciąg rosnący o jeden dłuższy niż z drzewa po lewej, a jeżeli będzie niższe to z drzewa po prawej na pewno da się zbudować ciąg malejący o jednen dłuższy niż z drzewa po lewej. Co wykazuje że w żadnej szufladce nie może być dwóch drzew, co oznacza sprzeczność i kończy dowód nie wprost.

## Natrudniejsze zadanie
>Ono nie jest wcale tak trudne powiedział prowadzący chwile po tym jak powiedział że jest najtrudniejsze.

Jest impreza na której jest 20 paszczaków i 20 migotek. Każdy paszczak wita się z każdą migotką którą zna przez pocałowanie w czoło. Mamy detektor pocałunków w czoło który wykrył że nastąpiło 99 powitań. Wykaż że są 2 takie paszczaki p i p' i takie 2 migotki m i m' że p zna m i m' i p' zna m i m'.
>Prowadzący jest przerażony że pomylił liczby.

To się robi zasadą szufladkową, można to wyczuć ale dojście do tego co jest szufladką a co jest kulką nie jest takie oczywiste.
Szufladkami będą pary migotek (albo pary paszcaków to wszystko jest symetryczne) jest ich 190, więc mamy 190 szuflad. Paszczak wrzuci swoje zdjęcie do każdej szufladki oznaczonej przez y i y' takie że pocałował y i y'. Trzeba wykazać że istnieje szufladka z dwoma zdjęciami. 
>W sumie to pada mi lapek więc jeżelk to jest koniec to to nie jest koniec XD

Wystarczy pokazać że jest przynajmniej 191 zdjęć wrzuconych do szufladek.
Nie ma czasu żeby powiedział to porządnie więc mówi byle jak.
Zadrzy się paszczak który zna n >= 6 i taki który zna m <= 4, jak na ilość zdjęć wpłynie oddanie przez n jednej znajomości temu co zna m.

Przed operacją było n(n-1)/2 + m(m-1)/2 a po jest n+1(n)/2 + m+1(m)/2 więc liczba par się zmniejszy. (na czuja bo czasu nie ma)
najmniej zdjęć będzie gdy 19 paszczaków zna po 5 migotek a 1 zna 4 migotki co daje 196 zdjęć. 
