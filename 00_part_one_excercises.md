## Basis-oefeningen

### Oppervlakte tuin

### Deel A

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

### Deel B

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

### Loopje

Schrijf een programma dat telt tot een getal x
Vraag dit getal aan bij het opstarten van het programma en controleer dat het groter is dan 0


### Min, max, totaal en gemiddelde

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

### Faculteit van een getal

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

### BTW berekenen

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

### Priemgetal berekenen

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

### Teken een vierkant

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

### Teken een driehoek

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


### Grootste gemene deler

Maak een functie die de grootste gemene deler berekent, deze functie geeft 1 terug als er geen andere gemene deler is

~~~python
def common_divider(a,b):
        #TODO
print(common_divider(10,15))  #rprints 5
print(common_divider(9,15))   #prints 3
print(common_divider(13,18))  #prints 1
~~~