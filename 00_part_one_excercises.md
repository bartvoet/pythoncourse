## Basis-oefeningen

### Oefening: Blackjack

#### Opdracht 1

Maak een command-line-spel black-jack:

> (command-line-spel = interactief spel in een console)

De regels:

* Je trekt kaarten, die elke een aantal punten voorstellen:
* De volgende punten-regels tellen:
  * Koning, Vrouw, Boer (de 'plaatjes'): 10 punten
  * De rest van de kaarten zijn zoveel waard als het cijfer dat op de kaart staat.
* Als je 21 hebt win je
* Als je er boven zit verlies je

Om de willekeurige kaart te trekken kan je de volgende code gebruiken:

~~~python
import random

kaart_waarde = random.randint(1, 13)
~~~


Als je start dien je het volgende te verschijnen:

~~~
Welkom: 
* Je trekt kaarten, die elke een aantal punten voorstellen:
* De volgende punten-regels tellen:
  * Koning, Vrouw, Boer (de 'plaatjes'): 10 punten
  * De rest van de kaarten zijn zoveel waard als het cijfer dat op de kaart staat.
* Als je 21 hebt win je
* Als je er boven zit verlies je

Type N voor een nieuwe spel, X om af te sluiten

>
~~~

~~~python
def clear_console():
    os.system('cls' if os.name=='nt' else 'clear')
~~~

Als je start dien je het volgende te verschijnen:

~~~
Welkom: 
* Je trekt kaarten, die elke een aantal punten voorstellen:
* De volgende punten-regels tellen:
  * Koning, Vrouw, Boer (de 'plaatjes'): 10 punten
  * De rest van de kaarten zijn zoveel waard als het cijfer dat op de kaart staat.
* Als je 21 hebt win je
* Als je er boven zit verlies je

(Type N voor een nieuwe spel, X om af te sluiten)

>
~~~

Vervolgens type je N in om te starten:

~~~
Welkom: 
* Je trekt kaarten, die elke een aantal punten voorstellen:
* De volgende punten-regels tellen:
  * Koning, Vrouw, Boer (de 'plaatjes'): 10 punten
  * De rest van de kaarten zijn zoveel waard als het cijfer dat op de kaart staat.
* Als je 21 hebt win je
* Als je er boven zit verlies je

N: Nieuw spel
X: Afsluiten

> N
~~~

Het spel start en een eerste kaart is getrokken:

~~~
Je hebt 5 getrokken
Je huidige totaal is 5

N: Nieuw spel
X: Afsluiten
K: Trek kaart

> K
~~~

Wanneer je K typt krijg je een volgende kaart:

~~~
Je hebt 7 getrokken
Je huidige totaal is 12

N: Nieuw spel
X: Afsluiten
K: Trek kaart

> K
~~~

Indien de volgende kaart voldoende is om 21 te halen heb je gewonnen:

~~~
Je hebt 9 getrokken
Je hebt 21 punten en hebt gewonnen!!!

N: Nieuw spel
X: Afsluiten
K: Trek kaart

> K
~~~


Indien de volgende kaart voldoende is om 21 te halen heb je gewonnen:

~~~
Je hebt een Boer (1O) getrokken
Je hebt 23 punten en hebt gewonnen!!!

N: Nieuw spel
X: Afsluiten
K: Trek kaart

> K
~~~

#### Opdracht 2

Alleen spelen is saai, zorg nu dat je met dezelfde regels met 2 kan spelen

~~~
Welkom: 
* Je trekt kaarten, die elke een aantal punten voorstellen:
* De volgende punten-regels tellen:
  * Koning, Vrouw, Boer (de 'plaatjes'): 10 punten
  * De rest van de kaarten zijn zoveel waard als het cijfer dat op de kaart staat.
* Als je 21 hebt win je
* Als je er boven zit verlies je

Je speelt met 2 spelers A en B

Type N voor een nieuwe spel, X om af te sluiten

> N
~~~

Speler A start en krijgt automatisch een kaart

~~~
Speler A:
Je hebt 6 getrokken
Je huidige totaal is 6
Speler B:
Je huidige totaal is 0

N: Nieuw spel
X: Afsluiten
K: Trek kaart

Speler B> K
~~~

Vervolgens speler B:

~~~
Speler A:
Je huidige totaal is 6
Speler B:
Je hebt een Heer getrokken
Je huidige totaal is 13

N: Nieuw spel
X: Afsluiten
K: Trek kaart

Speler A> K
~~~

En terug speler A:

~~~
Speler A:
Je hebt een Dame getrokken
Je huidige totaal is 18
Speler B:
Je huidige totaal is 13

N: Nieuw spel
X: Afsluiten
K: Trek kaart

Speler B> K
~~~


Uiteindelijk trekt speler B nog een kaart waarmee het totaal
op 21 komt en is gewonnen.

~~~
Speler A:
Je huidige totaal is 18
Speler B:
Je hebt een 8 getrokken
Je huidige totaal is 21

Speler B is gewonnen!!!

N: Nieuw spel
X: Afsluiten

> 
~~~

Of de Speler B trekt een te hoge kaart en verliest!!

~~~
Speler A:
Je huidige totaal is 18
Speler B:
Je hebt een 9 getrokken
Je huidige totaal is 22

Speler B is gewonnen!!!

N: Nieuw spel
X: Afsluiten

> 
~~~

#### Opdracht 3

Zorg er nu voor dat een speler de optie bijkrijgt om geen kaarten meer te trekken: (zolang er geen 21 is)

~~~
Speler A:
Je hebt een Dame getrokken
Je huidige totaal is 18
Speler B:
Je huidige totaal is 19

N: Nieuw spel
X: Afsluiten
K: Trek kaart
S: Stop met kaarten trekken

Speler B> S
~~~

Vervolgens is enkel Speler A nog maar aan de beurt

~~~
Speler A:
Je hebt een Dame getrokken
Je huidige totaal is 18
Speler B:
Je huidige totaal is 19 en wenst geen kaarten meer

N: Nieuw spel
X: Afsluiten
K: Trek kaart
S: Stop met kaarten trekken

Speler A> 
~~~

Vanaf dat de andere speler er boven zit heeft deze gewonnen!!

~~~
Speler A:
Je hebt een 2 getrokken
Je huidige totaal is 20
Speler B:
Je huidige totaal is 19 en wenst geen kaarten meer

Speler A is gewonnen!!!

N: Nieuw spel
X: Afsluiten
~~~

#### Opdracht 4

Hou er nu rekening mee dat een aas (zowel 1 als 11 kan zijn...)
De regels zijn nu als volgt:

* Je trekt kaarten, die elke een aantal punten voorstellen:
* De volgende punten-regels tellen:
  * Een Aas is 1 of 11 waard
  * Koning, Vrouw, Boer (de 'plaatjes'): 10 punten
  * De rest van de kaarten zijn zoveel waard als het cijfer dat op de kaart staat.
* Als je 21 hebt win je
* Als je er boven zit verlies je

#### Opdracht 5

Zorg ervoor dat je niet 2 maal dezelfde kaart uitdeelt...

##### Opdracht 6

Zorg ervoor dat je meerdere spelers kunt laten meedoen.

### Oefening: Calculator

Simuleer een rekenmachine in Python

~~~
(type number, command or x to close)
       M+    M-    MR    C
       7     8     9     /
       4     5     6     x
       1     2     3     -
       0          (-)    +
       x     =     %     ^

0
> 
~~~

### Oefening: Oppervlakte tuin

#### Deel A

Schrijf een programma dat de oppervlakte van een tuin berekent op basis van de totale oppervlakte en de tuin-oppervlakte.

Je geeft als input de breedte van de tuin en de breedte van het huis in, ga er vanuit dat je tuin en huis vierkant zijn.

~~~
             15 m
        +--------------+
        |     8 m      |
        |   +-----+    |
        |   |HUIS |8 m |15 m
        |   |     |    |
        |   +-----+    |
        |    TUIN      |
        +--------------+

Oppervlakte totaal = 15 m * 15 m = 225 m^2
Oppervlakte huis   = 10 m *  8 m =  64 m^2
                                  - -------
Oppervlakte thuis                = 161 m^2
~~~

Kijk na of de breedte van de tuin grootter is dan die van het huis.
Als deze niet correct beeindig het programma.

#### Deel B

Doe hetzelfde maar ga er nu vanuit dat zowel thuis als tuin niet noodzakelijk een vierkant is...

~~~
                20 m
        +-----------------+
        |       10 m      |
        |    +------+     |
        |    | HUIS | 8 m |  15 m
        |    |      |     |
        |    +------+     |
        |      TUIN       |
        +-----------------+

Oppervlakte totaal = 20 m * 15 m = 300 m^2
Oppervlakte huis   = 10 m *  8 m =  80 m^2
                                  - -------
Oppervlakte thuis                = 220 m^2
~~~

### Oefening: Minuten

Schrijf een programma dat een aantal minuten opvraagt en omzet in het aantal dagen, uren en seconden.

### Oefening: Random getallen

#### Basis-oefening

Maak een programma dat de gebruiker laat raden naar een getal.
Telkens bij een foute gok geef aan of het getal te laag of te hoog is.
Het programma blijft vragen tot dat de gebruiker een correct oplossing heeft.

Om dit getal op te vragen dien je de random-module te gebruiken.  
Dit kan je doen met onderstaande code:

~~~python
import random

print(random.randint(1,100)) # Zal een getal printen tussen 1 en 100
~~~

#### Uitbreiding

Beperk het aantal poginen dat je kan raden.

### Circel

Schrijf code die de oppervlakte van een cirkel berekent, gebruik makend van
variabelen straal en pi = 3.14159. 
Voor het geval je het vergeten bent, de formule is straal
keer straal keer pi. Toon de uitkomst als volgt: “De oppervlakte van een cirkel met straal ...
is ...”

Zet deze code in een functie...


### Oefening: Getallen opvragen

Schrijf een programma dat de gebruiker vraagt om 10 getallen, en dan de
grootste, de kleinste, en het aantal deelbaar door 3 afdrukt.


### Oefening: Som 2 kwadraten...

Schrijf een programma dat alle gehele getallen tussen 1 en 100 afdrukt
die geschreven kunnen worden als de som van twee kwadraten. De uitvoer is een lijst van
regels van de vorm z = x**2 + y**2 , bijvoorbeeld, 58 = 3**2 + 7**2.  

### Oefening: Loopje

Schrijf een programma dat telt tot een getal x
Vraag dit getal aan bij het opstarten van het programma en controleer dat het groter is dan 0

### Oefening: Min, max, totaal en gemiddelde

Schrijf een programma dat 

* in een loop getallen opvraagt
* stopt wanneer je een negatief getal ingeeft
* een aantal statistieken bijhoudt over (de positieve) getallen

Zie onderstaand voorbeedl van uitvoering.

~~~
$ python3 number.py
Enter a number (negative stops the loop): 3
Enter a number (negative stops the loop): 8
Enter a number (negative stops the loop): 1
Enter a number (negative stops the loop): 2
Enter a number (negative stops the loop): 1
Enter a number (negative stops the loop): -5
Loop handed ended due to number -5
Max number is 8
Min number is 1
Total is 15
Average is 3
~~~

Print bij het beeindigen:

* Het grootste getal
* Het kleinste getal
* Het totaal
* Het gemiddelde

### Oefening: Faculteit van een getal

De **faculteit** van een getal **n**, genoteerd als **n!**, is het **product van de getallen 1 tem n**.   
Bijvoorbeeld:

* Voor het getal 0 is dit 1 = 1
* Voor het getal 1 is dit 1 = 1
* Voor het getal 2 is dit 2 = 1 * 2
* Voor het getal 3 is dit 6 = 1 * 2 * 3
* Voor het getal 5 is dit 120 = 1 * 2 * 3 * 4 * 5
* ...

Zie ook https://nl.wikipedia.org/wiki/Faculteit_(wiskunde) voor meer info.  

#### Deel 1: factorial-functie

Maak een functie die een faculteit berekent voor een getal en test dit uit.

~~~python
def factorial(number):
        #TODO => code...

print(factorial(5)) #prints 120
print(factorial(6)) #prints 720
~~~

#### Deel 2: factorial van command line

~~~
$ python factorial.py
Give a number to caluclate the factorial: 5
!5 = 120
$
~~~

#### Deel 3: factorial-loop

~~~
$ python factorial_loop.py
Give a number to caluclate the factorial: 5
!5 = 120
Give a number to caluclate the factorial: 3
!3= 6
Give a number to caluclate the factorial: 1
!1 = 1
Give a number to caluclate the factorial: -1
End of programm
$
~~~

### Oefening: BTW berekenen

#### Deel A

Schrijf een programma dat btw uitrekent.  
Het programma vraagt het netto-bedrag op via command line.  
Ga uit van een percentage van 6%

Voorbeeld van gebruik:

~~~
Geef het bedrag van het goed in: 50
De BTW bedraagt 3 euro.
~~~

#### Deel B

Laat de gebruiker kiezen tot welke categorie het goed behoort => 6% - 12% of 21%

Voorbeeld van gebruik:

~~~
Geef het bedrag van het goed in: 50
Geef de categorie in (type a voor 6%, b voor 12% en c voor 21%): b
De BTW bedraagt 6 euro.
~~~

#### Deel C

Blijf deze vragen stellen tot dat de gebruiker 0 in geeft.  
Druk daarna de totale btw uit over alle goederen.

Voorbeeld van gebruik:

~~~
Geef het bedrag van het goed in (typ 0 om berekening te stoppen): 50
Geef de categorie in (type a voor 6%, b voor 12% en c voor 21%): b
Geef het bedrag van het goed in (typ 0 om berekening te stoppen): 100
Geef de categorie in (type a voor 6%, b voor 12% en c voor 21%): c
Geef het bedrag van het goed in (typ 0 om berekening te stoppen): 0
De BTW bedraagt 27 euro
~~~

### Oefening: Priemgetal berekenen

#### Deel 1: functie

Schrijf een functie die nakijkt of een getal een priemgetal is

~~~python
print(is_prime(13)) # prints True
print(is_prime(4))  # prints False
~~~

De éénvoudigste (maar niet de efficientste manier) is een loop te schrijven die loopt van 2 tem het getal en kijkt of het getal deelbaar is (maak gebruik van de rest-operator hiervoor)

#### Deel 2: priem

Schrijf een loop die alle priemgetallen afdrukt lager dan een getal dat je ingeeft (gebruik makende van de voorgaande functie).

~~~
$ python prime_numbers.py
Give a number: 20
2
3
7
11
13
17
19
~~~

### Oefening: Teken een vierkant

#### Deel 1

Maak een functie doe een rechthoek print op de console

~~~python
def print_rectangle(rows,columns)
        #TODO write double loop....

print_rectangle(6,5)
~~~


~~~
$ python3 print_rectangle.py
*****
*****
*****
*****
*****
***** 
~~~

#### Deel 2

Maak een functie doe een rechthoek print op de console maar deze niet vult...

~~~
$ python3 print_rectangle.py
*****
*   *
*   *
*   *
*   *
***** 
~~~

### Oefening: Teken een driehoek

#### Deel 1

Maak een functie doe een driehoek print op de console

~~~python
def print_triangle(rows)
        #TODO write double loop....

print_triangle(6)
~~~


~~~
$ python3 print_triangle.py
     *
    * *
   *****
  *******
 *********
***********
$
~~~

#### Deel 2

Maak een variant die een de driehoek niet vult

~~~
$ python3 print_triangle.py
     *
    * *
   *   *
  *     *
 *       *
***********
$
~~~

#### Deel 3 (moeillijker...)

~~~python
def print_multiple_triangles(rows,triangles)
        #TODO

print_multiple_triangles(6,3)
~~~


~~~
$ python3 print_mutliple_triangles.py
     *           *            *      
    * *         * *          * *
   *   *       *   *        *   *
  *     *     *     *      *     *
 *       *   *       *    *       *
*********** ***********  ***********
$
~~~


### Oefening: Grootste gemene deler

Maak een functie die de grootste gemene deler berekent, deze functie geeft 1 terug als er geen andere gemene deler is

~~~python
def common_divider(a,b):
        #TODO
print(common_divider(10,15))  #rprints 5
print(common_divider(9,15))   #prints 3
print(common_divider(13,18))  #prints 1
~~~