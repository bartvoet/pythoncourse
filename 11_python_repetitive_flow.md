## Repitieve uitvoering (loops)

~~~
                             +------------------------------+
                             |                              |
                             |     Hergebruik uitvoering    |
            _                |                              |
             \           +---+------------------------------+---+
        _____ \          |                                      |         * while-loops
              /          |        Repetitieve uitvoering        |         * loop-state
            _/           |                                      |         * for-loops
                     +---+--------------------------------------+---+
                     |                                              |     * if+elif+else
                     |           Conditionele uitvoering            |     * clausules
                     |                                              |     * blocks
                 +---+----------------------------------------------+---+
                 |                                                      | * Statements
                 |                Sequentiële uitvoering                |    * Function+calls
                 |                                                      |    * Assignments
                 |   +------------+   +------------+   +------------+   | * Expressions
                 |   | Statements |   | Variabelen |   | Expressies |   | * Variables
                 +---+------------+---+------------+---+------------+---+

~~~


### Naar contionele uitvoering

Via **condities** hebben we met de **if-else-structuur** **beslissingen** kunnen maken in onze code.  

~~~
                                          +----------------+
                                          |      ...       |
                                          +-------+--------+
                                                  |
                                                  V
                                                 **
                                               **  **
                                    True     **      **     False
                                  +-------+** CONDITIE **+----------+
                                  |          **      **             |
                                  |            **  **               |
                                  |              **                 |
                  +---    +-------V--------+                +-------V--------+   ---+
                  |       |   Statement    |                |   Statement    |      |
                  |       +-------+--------+                +-------+--------+      |
                  |               |                                 |               |
           BLOCK  |       +-------V--------+                +-------V--------+      |   BLOCK
           TRUE --+       |   Statement    |                |   Statement    |      +-- FALSE
                  |       +-------+--------+                +-------+--------+      |
                  |               |                                 |               |
                  |       +-------V--------+                +-------V--------+      |
                  |       |      ...       |                |      ...       |      |
                  +---    +-------+--------+                +-------+--------+   ---+
                                  |                                 |
                                  +---------------+-----------------+
                                                  |
                                          +-------V--------+
                                          |      ...       |
                                          +-------+--------+
                                                  |
                                                  V
                                                 ...
~~~

Je kiest al dan niet een een **stuk code** of **block** uit te voeren.  
Optioneel kan je dan ook een **ander stuk code** uitvoeren als de conditie onwaar (False) is (else- en elif clausules)

### Naar repititieve uitvoering

Waar je echter bij conditionele uitvoering kiest om een block code 1 maal uit te voeren  
kan je bij repititieve code kiezen om deze te blijven uitveroen zolang een conditie waar is.

~~~
                                          +----------------+
                                          |      ...       |
                                          +-------+--------+
                                                  |
                                                  V         "Zolang de conditie
                                                 *+          waar (True) is blijven de
                                               **  **        block-statement uitvoeren"
                                     False   **      **
                        +------------------+* CONDITIE +<-------------+
                        |                    **      **               |
                        |                      **  **                 |
                        |                        *+                   |
                        |                         | True              |
                        |                         |                   |
                        |         +--+    +-------v--------+          |
                        |         |       |   Statement    |          |
                        |         |       +-------+--------+          |
                        |         |               |                   |
                        |  BLOCK  |       +-------V--------+          |
                        |  TRUE +-+       |   Statement    |          |
                        |         |       +-------+--------+          |
                        |         |               |                   |
                        |         |       +-------V--------+          |
                        |         |       |      ...       +----------+
                        |         +--+    +----------------+
                        |                                    "Bij de laatste statement
                        |                                     van de block keren we terug
                        +-------------------------+           naar de conditie"
                                                  |
                                                  |
                                          +-------v--------+
                                          |      ...       |
                                          +-------+--------+
                                                  |
                                                  V
                                                 ...
~~~

Waar bij een **if-statement** (direct) wordt **verder gegaan** naar de **volgende statement** wordt er bij een **loop terug**
naar de **conditie** gegaan op het **einde** van de **block**.

In **Python** doen we dit aan de hand van **loop-constructies**, we bekijken er er 2 soorten; while en for-loops.

### while-loop met teller

Om de while loop te illustreren starten we met een éénvoudig voorbeeld:

* Afdrukken van een aantal sterren op de console
* Je geeft het aantal in dat je wil afdrukken

~~~python
number_of_stars = int(input("Number of stars to print? "))
counter = 0

while counter < number_of_stars:
    print("*")
    counter = counter + 1
~~~

Een while-loop is **net** zoals de **if-statements** een **block-statement**

* zal de loop de **inhoud van de block uitvoeren**
* **eindigt** de while-clausule op een **:**
* is deze block **geindenteerd**

Het verschil ligt in het feit dat deze constructie de block zal blijven uitvoeren zolang de conditie True geeft 
(zoals in het bovenbeschreven schema).

### Tellers

Als je dit uitvoert zal de code **5 maal** de block **print- en assignment-statement** uitvoeren.

~~~
$ python print_stars.py
Number of stars to print? 5
*
*
*
*
*
~~~

Om dit te bereiken zijn **2 elementen** voor nodig:

* Het **aantal keer** dat je **telt** => number_of_stars
* De **teller** zelf => counter

### State van een loop (loop-state)

Het gebruik van een variabele om een loop te besturen is een **patroon** dat bijna altijd terugkomt wanneer je met **loops** werkt:

* Je houdt een **variabele** bij, een zogenaamde **state**  
  (in vele gevallen een teller)
* Deze state wordt geinitialiseerd (stap **0**)  
  (bijvoorbeeld de teller wordt op 0 gezet bij start)
* Deze state wordt **geëvalueerd** (stap **1**)  
  (bijvoorbeeld teller kleiner dan een maximum)
* Op basis van deze evaluatie wordt de **loop-block uitgevoerd** (stap **3**)  
  (bijvoorbeeld teller is niet meer kleiner dan maximum)
* Deze **state** wordt bijgewerkt in de **block**
  (bijvoorbeeld optellen van de teller...)  
* We gaan terug naar stap 1 (en stoppen ermee als de evaluatie False is

~~~

            +------------+
            | CODE       |
            | BEFORE     +----(0) INITIALIZE STATE----------------------+
            +-+----------+                                              |
              |               "while+clause voert een                   |
              |                een vergelijking uit op de state         |
              |                (bv. een teller) en beslist              |
            +-+----------+     of de block wordt uitgevoerd"      +-----------+
            | WHILE+     |                                        |-----------|
            | CLAUSULE   +---+(1)EVALUATES STATE and DECIDES +-----|  STATE  ||
            +-+----------+                                        |-----------|
              |                                                   +-----------+
              +                                                         |
             / \  (2)TRUE(1)    +------------+                          |
            +   +-+RUNS BLOCK +-> BLOCK MET  +---+(3)UPDATES STATE +----+
             \ /                | STATEMENTS |
              +( 2)FALSE(1)     +------------+
              |    STOPS
              |    THE LOOP
              |
            +-v----------+
            | REST OF    |
            | THE CODE   |
            +------------+

~~~

### while-loop met teller en state

state-variabelen wordt niet alleen gebruikt om te evalueren.  
In het volgende voorbeeld berekenen we de macht van een getal (basis en exponent)

> Nota:  
> Vanzelfsprekend is deze code nutteloos gezien er al een operator bestaat in python ~~~**~~~
> die een macht berekent, de bedoeling is het gebruik van een loop te demonstreren.

De state die wordt geëvalueerd is de exponent-counter die wordt uitgevoerd zolang deze kleiner is dan de de exponent.

~~~python
base = int(input("Give base: "))
exponent = int(input("Give exponent: "))
result = 1
exponent_counter = 0

while exponent_counter < exponent:
    result = result * base
    exponent_counter = exponent_counter + 1

print(result)
~~~

### while-loop met teller en input

Een voorbeeld dat niet met tellers werkt is bijvoorbeeld is het herhalen van een stuk code
zolang de input een bepaalde waarde is.

In onderstaand voorbeeld hernemen we de code die nakijkt of een getal c tussen a en b ligt:

~~~python
is_still_inbetween = True

while is_still_inbetween:
    a = int(input("Enter number a: "))
    b = int(input("Enter number b: (should be bigger then a"))
    c = int(input("Enter number c: "))

    is_still_inbetween = c >= a and c <= b
    if is_still_inbetween:
        print("c is inbetween a and b")
else:
    print("c is not inbetween a and b")
~~~

Als state wordt hier het resultaat van de vergelijking genomen.  
Zolang c tussen a en b ligt zal deze loop getallen blijven vragen.

### Niet eindigende loops

Wat iedereen als fout maakt in de code is een een loop die niet stopt.  
Bijvoorbeeld als we in onderstaande code:

~~~python
number_of_stars = int(input("Number of stars to print? "))
counter = 0

while counter < number_of_stars:
    print("*")
    counter = counter + 1
~~~

een **foutje** introduceren

~~~python
number_of_stars = int(input("Number of stars to print? "))
counter = 0

while counter < number_of_stars:
    print("*")
counter = counter + 1
~~~

Zie je het **verschil**!!!  
In de laatste lijn is de **indentatie** namelijk **weggenomen**, 
dit zorgt er namelijk voor dat de **update** van de **state** wordt **weggenomen** ...

Het gevolg ervan is dat counter **voor eeuwig 0** blijft en de loop nooit wordt beindigd.

### Geen paniek ctrl+c

Als dit gebeurt hoef je niet je console af te sluiten, het volstaat namelijk van de combinatie
"ctrl + c" te gebruiken om het Python-proces af te sluiten

### for-loop

Heel veel loops zijn counter-loops, de bedoeling hiervan is de code een exact aantal uit te voeren.  
We introduceren - naast de while-loop - een **2de soort loop**, de **for-loop** die dikwijls meer aangewezen dan de while-loop.  
De **voorgaande teller-code**:

~~~python
number_of_stars = int(input("Number of stars to print? "))
counter = 0

while counter < number_of_stars:
    print("*")
    counter = counter + 1
~~~

vervangen we door een **equivalente for-loop**

~~~python
number_of_stars = int(input("Number of stars to print? "))

for counter in range(number_of_stars) :
    print("*")
~~~

De **for-loop-clausule** heeft 2 componenten:

* Een **teller-variabele** volgend op het **keyword for** die je kan gebruiken vanuit de block-code
* Een **range-functie** die bepaalt hoeveel je moet tellen **gevolgd door** het **keyword in**

Net zoals bij een while-loop zal deze **blijven de block-statement uit te voeren**, maar dan **tot** dat de **gehele range is afgelopen**.

### Voordelen for-loop

Zowel de **state-update** als de **state-evaluatie** wordt door de for-loop uitgevoerd, dit brengt ons 2 voordelen:

* De code is **compacter**
* De loop is ook **veiliger**  
  want de **state-update** gebeurt **automatisch**  
  => minder riscio op eindeloze loops

### 2de voorbeeld for-loop: exponent

Als we dit toepassen op het **exponent-voorbeeld**:

~~~python
base = int(input("Give base: "))
exponent = int(input("Give exponent: "))
result = 1
exponent_counter = 0

while exponent_counter < exponent:
    result = result * base
    exponent_counter = exponent_counter + 1

print(result)
~~~

kunnen we dit **herwerken** naar

~~~python
base = int(input("Give base: "))
exponent = int(input("Give exponent: "))
result = 1

for exponent_counter in range(exponent):
    result = result * base

print(result)
~~~

### range-functie

De range-functie genereert een range, meer bepaald een iterator-implementatie.  

Met range zal je  tellen van **0** tot een **eindwaarde - 1**.  
range(5) zal 5 maal tellen van 0 tem 4 (niet tem 5)

> Nota:  
> In het volgende deel bekijken we dit verder hoe dit werkt en waar het vandaan komt, voorlopig moet je er van uit gaan dat deze range bepaalt tot waar je telt.

### 3de voorbeeld: range van/tot

De range-functie kan ook worden ingesteld met een start-waarde.  
Stel dat je bijvoorbeeld wil tellen tem van een bepaald getal tot een ander getal kan je 2 argumenten geven aan range:

~~~python
start = int(input("Count from: "))
from = int(input("Count to: "))
for counter in range(start,stop+1):
    print(counter)
~~~

Het eerste deel is waar je begint tellen, het 2de deel tot welke waarde.  
Let wel, dit **2de** argument **telt tot**, **niet tot en met**

~~~
$ python count_from_to.py
Count from: 5
Count to: 10
5
6
7
8
9
10
~~~

### Geneste loop

Binnen een for- of while-loop kan je ook **andere block-statements** toevoegen.  
In onderstaand voorbeeld drukken we bijvoorbeeld de **maaltafels** door een **geneste for-loop**.

~~~python
for left_part in range(1,10):
    for right_part in range(1,10):
        print(str(left_part) + " * " + str(right_part) + " = " + str(left_part * right_part))
~~~

De **1ste loop** is wat we noemen de **outer-loop**, deze zal het linker-gedeelte laten optellen van **1 tem 9**.  
De **2de loop** daarentegen noemen we de **inner-loop**, deze zal telkens van 1 tem 9 tellen voor **iedere waarde** van de **outer-loop** een rechter-gedeelte geven.

~~~
$ python multiplication_table.py
1 * 1 = 1
1 * 2 = 2
...
9 * 6 = 54
9 * 7 = 63
9 * 8 = 72
9 * 9 = 81
~~~

### String-concatenation

De +-operator voert **string-concatenation** uit, deze **plakt** letterlijk verschillende strings aan elkaar.

~~~python
...
        print(str(left_part) + " * " + str(right_part) + " = " + str(left_part * right_part))
~~~

Om deze string-concatenation te kunnen uitvoeren moet elke operand van de +-operator van het type string zijn.  
Gezien dat de waardes van het integer-type zijn we de str-functie om elke deel te converteren naar een string.

