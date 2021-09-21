## Conditionele uitvoering

### Van sequentiële naar conditionele uitvoering

~~~
                            +------------------------------+
                            |                              |
                            |     Hergebruik uitvoering    |
                            |                              |
                        +---+------------------------------+---+
                        |                                      |
                        |        Repetitieve uitvoering        |
                        |                                      |
           _        +---+--------------------------------------+---+
            \       |                                              |     * if-elif-else
       _____ \      |           Conditionele uitvoering            |     * clausules
             /      |                                              |     * blocks
           _/   +---+----------------------------------------------+---+
                |                                                      | * Statements 
                |                Sequentiële uitvoering                |    * Function-calls
                |                                                      |    * Assignments
                |   +------------+   +------------+   +------------+   | * Expressions
                |   | Statements |   | Variabelen |   | Expressies |   | * Variables
                +---+------------+---+------------+---+------------+---+
~~~

We hebben nu kennis gemaakt met een aantal basiselementen uit de sequentiële uitvoering:

* **Statements**: assignment, function-call, ...
* **Variabelen**: int, string
* Rekenkundig **Expressies**

We starten nu aan meer **complexere code**, namelijk we gaan nu naar **conditionele uitvoering** kijken.  
Dit principe bouwt zich **bovenop sequentiële uitvoering** gebouwd maar voegt het element van **keuze** toe.

Door een combinatie van **relationele expressies** en de **if-else-statements** kunnen we kiezen - at runtime - welke
blok van code er wordt uitgevoerd (waar we deze keuze niet hadden bij zuiver sequentiële uitvoering).  
Deze combinatie benoemen we als een **conditie**.

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

Dankzij deze **conditie** kunnen we vanuit de code een keuze maken welke **block** (van statements) we uit te voeren (afhankelijk van de conditie).


### Relationele expressies

Het eerste element zijn de **relationele expressies**.  

| Operator   |   Betekenis            |
|------------|------------------------|
| ==         | gelijk aan             |
| !=         | niet gelijk aan        |
| <          | kleiner dan            |
| >          | groter dan             |
| <=         | kleiner of gelijk aan  |
| >=         | groter of gelijk aan   |

Dit zijn expressies die een **vergelijking** maken **tussen** **2 variabelen** (in meeste gevallen **numerieke variabelen**).  
Deze expressies geven aan of een vergelijking **waar** of **onwaar** is 

~~~
1 == 1  => waar
1 != 1  => niet waar
5 >  6  => niet waar
6 >= 6  => waar
...
~~~

Onderstaand Python-voorbeeld illustreert het gebruik van een relationele expressies:

~~~python
a = 5
b = 6
c = a < b 
print(c)   # prints False
d = a > b
print(d)   # prints True
~~~

Als men **a (5) vergelijkt met b (6)** voor de **relatie kleiner** dan (a < b) verkrijgt men de waarde **True**.  
Daarna vergelijken we de zelfde variabelen  voor de **relatie groter** dan en verkrijgen we de waarde **False**

### Variabelen van het type boolean

**True** en **False** zijn de **enige mogelijke** resultaten van relationele expressies.   
Hier is in Python een specifiek type voorgecreerd namelijk het type boolean.  

Als je **onderstaande code** start om het **type** te weten te komen

~~~python
print(type(c))
~~~

geeft deze het type **bool** (of **boolean**) aan

~~~
<class 'bool'>
~~~

Dit **data-type bool** heeft slechts 2 mogelijk waardes en gaan we gebruiken in **conditionele** en **repititieve statements**.


### Gebruik van booleans

We kunnen dus deze relationele expressies (of vergelijking) gebruiken om 2 getallen (variabelen, literals, resultaat expressies, ...) te gebruiken.

Stel bijvoorbeeld je wil een programma schrijven dat 2 getallen gaat vergelijken (groter/kleiner) kunnen we al gebruik maken van wat we daarnet hebben geleerd.

~~~python
a = int(input("Enter number a: "))
b = int(input("Enter number b: "))

print(a > b)
~~~

Afhankelijk van wat je intypt zal dit **True** of **False** afdrukken:

~~~
$ python compare_number.py
Enter number a: 10
Enter number b: 11
False
~~~

Het programma drukt in dit geval False af gezien 10 (a) zowiezo niet groter is dan  11 (b).  
Maar wat nu indien we iets anders willen afprinten dan False.

### Gebruik van een relationele expressie binnen een if-statement

Om meer te kunnen doen met dit resultaat (of vergelijkingà introduceren we het **if-statement**.  

Dit soort statement laat je toe van een zo'n **vergelijking** te **evalueren** en te **beslissen** of je al dan niet een **stuk code** zal **uitvoeren**.

In onderstaande code laten we deze **if-statement** beslissen om de tekst "a is bigger then b" al dan niet af te drukken.

~~~python
a = int(input("Enter number a: "))
b = int(input("Enter number b in: "))

if a > b:
    print("a is bigger then b")
~~~

Als je nu dit programma test dan zal deze afdrukken:

~~~
$ python compare_number.py
Enter number a: 11
Enter number b: 10
a is bigger then b
~~~

### Tegengestelde conditie

Probleem echter is dat als a kleiner is dan b (op basis van wat je ingeeft) er niets wordt afgedrukt

~~~
$ python compare_number.py
Enter number a: 10
Enter number b: 11
~~~

Er ontbreekt dus de **tegengestelde conditie**
Een optie zou kunnen zijn deze conditie om te keren in een 2de if-statement die daarop volgt zoals hier onder?

~~~python
a = int(input("Enter number a: "))
b = int(input("Enter number b in: "))

if a > b:
    print("a is bigger then b")
if a <= b:
    print("a is smaller or equal to b")
~~~

Dan krijg je inderdaad de correcte melding.

~~~
$ python compare_number.py
Enter number a: 10
Enter number b: 11
a is smaller or equal to b
~~~

Er is echter een meer elegante oplossing...

### if-statement is eigenlijk if-else-statement

Zo'n if-statement kan je namelijk uitbreiden met een else-clausule.  
Hieronder passen we het vorige voorbeeld aan door de 2de statement te vervangen door een else-clausule:

~~~python
a = int(input("Enter number a: "))
b = int(input("Enter number b in: "))

if a > b:
    print("a is bigger then b")
else:
    print("a is smaller or equal to b")
~~~

### elif

Een derde mogelijkheid is het toevoegen van één (of meerdere) elif-clausule(s)  
Stel dat je ook expliciet wil afdrukken wanneer de parameters aan elkaar gelijk zijn kan je een elif-clausule ("else if") toevoegen.

~~~python
a = int(input("Enter number a: "))
b = int(input("Enter number b in: "))

if a > b:
    print("a is bigger then b")
elif a == b:
    print("a is equal to b")
else:
    print("a is smaller or equal to b")
~~~

### Meerdere elif-clausules

Je kan ook meerdere elif-clausules aan deze statement toevoegen.  
Stel dat je bijvoorbeeld ook nog wil afdrukken als a 1 kleiner is dan b kan je nog een 2de elif-clausule toevoegen.  

> Nota: je kan trouwens zo veel elif-clausules toevoegen als je wil 

~~~python
a = int(input("Enter number a: "))
b = int(input("Enter number b in: "))

if a > b:
    print("a is bigger then b")
elif a == b:
    print("a is equal to b")
elif (b - a) == 1:
    print("a is -1 compared to b")
else:
    print("a is smaller or equal to b")
~~~

### Structuur

Een if-statement is samengesteld uit 2 (soorten) onderdelen of componenten

* 1 of meerdere **clausules**
    * **1 "if"-clausule**
        * **optioneel** **1 "else"**
        * **optioneel 1 of meerdere "elif"**
    * enkel **"if"** is **verplicht**
    * elke **clausule** **eindigend** op een **:**  
      (zoniet zal de interpreter een fout aan geven)
* telkens gevolgd door een **block**
    * die (minimum) **1 of meerdere statements** bevat
    * **geindenteerd** tov de clausule die voorafgaat
    * indentatie betekent **1 tab of 4 spaties**  
      (pas op, geen spaties mixen met tabs)

> Nota: je kan kiezen tussen het gebruik van een tab of 4 spaties
> maar binnen 1 file/programma moet je consequent zijn.
> Als je beiden mixt zal de Python interpreter een error geven.


~~~python
if a > b:  # <--------------------------------- if-clausule (eindigt op :)
    print("a is bigger then b") #         |
    print("2nd time a is bigger then b")# |---- block (3 lines geindenteerd)
    print("3rd time a is bigger then b")# |
elif a == b: # <---------------------------- elif-clausule
    print("a is equal to b")#             |
    print("2nd time a is equal to b")#    |---- block (2 lines) 
elif (b - a) == 1: #                   <---- elif-clausule
    print("a is -1 compared to b") #      |---- block (1 line)
else: #                                   <---- elif-clausule (2nd)
    print("a is smaller or equal to b") # |---- block (1 line)
~~~

Bovenstaande code toont aan dat je **1 of meerdere statements** in zo'n block kan steken

### Geneste if statements

if-statements zijn ook statements, dus naast enkelvoudige statements (1 lijn) kunnen dus ook andere block-statements (if, while, ...) in vervat zijn.

Stel dat we een boodschap wilen afdrukken dat een **getal a** zich **tussen** een getal **b en c** ligt.  
Voorlopig **gaan** we er van **uit** dat we dat **a** altijd **kleiner **is dan **b**.  
Dit houdt in dat je aan 2 vergelijkingen moet voldoen:

* **c** moet **groter** (of gelijk) zijn aan **a**
* **c** moet **kleiner** (of gelijk) zijn aan **b**

~~~python
a = int(input("Enter number a: "))
b = int(input("Enter number b: (should be bigger then a"))
c = int(input("Enter number c: "))

if c  >= a:
    if c <= b:
        print("c is inbetween a and b")
~~~

Door in bovenstaande oplossing de **1ste conditie (c >= a)** te **nesten binnen **de **2de conditie (c <=b)** test je tegen beide combinaties.

### Logische expressies (en operatoren)

De **relationele expressies** die we net hebben bekeken zijn **boolean-expressies** (expressie die een boolean produceert en geen nummer).  
Daarnaast kan je ook nog letterlijk de waarden **True** en **False** als **literal** gebruiken in je code (zelden nodig...).

~~~


                               +--------------------------+  "Logische expressie combineert
                               | Boolean expressies       |   Boolean-expressies met elkaar"
                               | (boolean als resultaat)  +<---------------------+
                               +----------+---------------+                      |
                                          |                                      |
            +-----------------------------+--------------------------------+     |
            |                             |                                |     |
    +-------+----------+       +----------+--------------+       +---------+-----+-----+
    | Boolean-literals |       | Relationele expressies  |       | Logische expressies |
    | (True of False)  |       | (==,>,<,>=,<=,!=)       |       | (and,or,not)        |
    +------------------+       +-------------------------+       +---------------------+


~~~

Een **3de** type boolean-expressie is de **logische expressie**, deze combineert (met uitzondering van not) 2 boolean-expressies met elkaar in een **logische relatie**

### and, or en not

We gaan 3 operatoren/expressies zien:

| Operator   |   Betekenis                              |
|------------|------------------------------------------|
| and        | alle boolean-expressies moeten waar zijn |
| or         | 1 van de ingesloten expressies           |
| not        | omgekeerde van een boolean-expressie     |

**and en or** zijn (zoals de meeste operatoren tot nog toe) **binaire operatoren** waar zij 2 of meerdere (boolean-)expressies commbineren.  
**not** zoals we gaan zien is een **unitaire operator**, met slechte 1 operand

We starten met de and-operator...

### Logische and-operator

Een eerste voorbeeld is de **and**-operator, deze zal **True** als resultaat hebben **enkel en alleen** als de beide logische
expressies True zijn.

~~~
               +-------+                               +-------+
               | True  +<------"Enkel als beide        | False |
               +---+---+        relationele            +---+---+
                   ^            epressies True             ^
                   |            zijn is resultaat          |
               +---+---+        True"                  +---+---+
        +------+  AND  +-------+                +------+  AND  +-------+
        |      +-------+       |                |      +-------+       |
        |                      |                |                      |
    +---+---+              +---+---+        +---+---+              +---+---+
    | True  |              | True  |        |  True |              | False |
    +-------+              +-------+        +-------+              +-------+


               +-------+       "In alle andere         +-------+
               | False |        gevallen False"        | False |
               +---+---+                               +---+---+
                   ^                                       ^
                   |                                       |
               +---+---+                               +---+---+
        +------+  AND  +-------+                +------+  AND  +-------+
        |      +-------+       |                |      +-------+       |
        |                      |                |                      |
    +---+---+              +---+---+        +---+---+              +---+---+
    | False |              | True  |        | False |              | False |
    +-------+              +-------+        +-------+              +-------+
~~~

Ter **verduidelijkig** passen we dit toe op voorgaand **voorbeeld** waar een getal a tussen b en c moest vallen...

~~~python
a = int(input("Enter number a: "))
b = int(input("Enter number b: (should be bigger then a"))
c = int(input("Enter number c: "))

if c >= a and c <= b:
    print("c is inbetween a and b")
~~~

Net zoals daarvoor zal de **print** **enkel uitgevoerd** worden onder de conditie dat **beide vergelijkingen True zijn**  
Nu dat we beide elementen hebben gecombineerd hebben in 1 if-clausule kunnen we ook de tegengestelde boodschap zetten

~~~python
a = int(input("Enter number a: "))
b = int(input("Enter number b: (should be bigger then a"))
c = int(input("Enter number c: "))

if c >= a and c <= b:
    print("c is inbetween a and b")
else:
    print("c is not inbetween a and b")
~~~

Dit laat ons trouwens toe van code-duplicatie te vermijden, anders was je verplicht van de tegengestelde boodschp ("c is not inbetween...")
af te drukken op 2 locataties binnen je code (zoals hieronder).

~~~python
a = int(input("Enter number a: "))
b = int(input("Enter number b: (should be bigger then a"))
c = int(input("Enter number c: "))

if c  >= a:
    if c <= b:
        print("c is inbetween a and b")
    else:
        print("c is not inbetween a and b")
else:
    print("c is not inbetween a and b")

~~~

### Logische or-operator

De **or-operator** kan je gebruiken om te checken of er aan (minstens) **1 van de 2 condities** voldaan is.  
Deze zal **enkel False** teruggeven als **beide expressie ook False (onwaar)** zijn

~~~
               +-------+                               +-------+
               | False +<------"Enkel als beide        | True  |
               +---+---+        relationele            +---+---+
                   ^            epressies False            ^
                   |            zijn is resultaat          |
               +---+---+        False"                 +---+---+
        +------+  OR   +-------+                +------+  OR   +-------+
        |      +-------+       |                |      +-------+       |
        |                      |                |                      |
    +---+---+              +---+---+        +---+---+              +---+---+
    | False |              | False |        |  True |              | False |
    +-------+              +-------+        +-------+              +-------+


               +-------+       "In alle andere         +-------+
               | True  |        gevallen True"         | True  |
               +---+---+                               +---+---+
                   ^                                       ^
                   |                                       |
               +---+---+                               +---+---+
        +------+  OR   +-------+                +------+  OR   +-------+
        |      +-------+       |                |      +-------+       |
        |                      |                |                      |
    +---+---+              +---+---+        +---+---+              +---+---+
    | False |              | True  |        | True  |              | True  |
    +-------+              +-------+        +-------+              +-------+
~~~

Ter illustratie, in onderstaand voorbeeld kijken we na of een getal c groter is dan 1 van beide getallen a of b.  
c moet niet groter zijn van beide maar slecht groter dan 1 van beide, hiervoor kunnen we een or-combinatie gebruiken

~~~python
a = int(input("Enter number a: "))
b = int(input("Enter number b: "))
c = int(input("Enter number c: "))

if a > c or b > c:
    print("c is bigger then a or b")
else:
    print("c is smaller then both a and b")
~~~

Je kan deze or-expressie trouwens uitbriden met meerdere logische operatoren zoals hieronder vermeld

~~~python
a = int(input("Enter number a: "))
b = int(input("Enter number b: "))
c = int(input("Enter number c: "))
c = int(input("Enter number d: "))

if a > d or b > d or c > d:
    print("d is bigger then a or b or c")
else:
    print("d is smaller then both a and b and c")
~~~


### Logische not-operator

De not-operator of logische inverter draait het resultaat van een boolean-expressie om.  

~~~
print(4 >5)      # prints False
print(not(4 > 5)) # prints not False => True
print(5 > 4)     # prints True
print(not(5 > 4)) # prints not True => False 
~~~

> Nota: haakjes rond de expressie die volgt op not is niet verplicht maar vermijdt verwarring bij grotere expressies

Anders gezegd als het resultaat True/Waar is, wijzigt dit naar False/Onwaar en omgekeerd

~~~

            +-------+        +-------+
            |  True |        | False |
            +---+---+        +---+---+
                ^                ^
                |                |
            +---+---+        +---+---+
            |  NOT  |        |  NOT  |
            +---+---+        +---+---+
                ^                ^
                |                |
            +---+---+        +---+---+
            | False |        | True  |
            +-------+        +-------+
~~~

Je kan bijvoorbeeld ook het voorgaande voorbeeld (uit de or-operator) omdraaien door een not te gebruiken:

~~~python
a = int(input("Enter number a: "))
b = int(input("Enter number b: "))
c = int(input("Enter number c: "))

if not(a > c or b > c): # same as a < c and 
    print("c is smaller then both a and b")
else:
    print("c is bigger then a or b")
~~~

### Complexer voorbeeld

We hernemen het voorbeeld "getal a tussen b en c".  
Probleem - met de laatste oplossing - is nog altijd dat b kleiner moet zijn als c om de vergelijking te doen kloppen.

~~~python
a = int(input("Enter number a: "))
b = int(input("Enter number b: (should be bigger then a"))
c = int(input("Enter number c: "))

if c >= a and c <= b:
    print("c is inbetween a and b")
else:
    print("c is not inbetween a and b")
~~~

Bijvoorbeeld het volgende zal worden gedetecteerd (3 tussen 1 en 5)

~~~
a=1 <--- c=3 ---> b=5
~~~

Maar als we onderstaande zouden testen dan zouden we dit met bovenstaande code niet detecteren.  
(zou c is not inbetween a and b) afdrukken

~~~
b=5 <--- c=3 ---> a=1
~~~

Daarvoor zou je volgende code moeten voor schrijven:

~~~python
a = int(input("Enter number a: "))
b = int(input("Enter number b: (should be bigger then a"))
c = int(input("Enter number c: "))

if c >= b and c <= a:
    print("c is inbetween a and b")
else:
    print("c is not inbetween a and b")
~~~

Waar we dan weer niet het eerste geval herkennen (wanneer a kleiner is dan b).  
De oplossing is **beide logische expressies te combineren** met een **logische or-expressie**

~~~python
a = int(input("Enter number a: "))
b = int(input("Enter number b: (should be bigger then a"))
c = int(input("Enter number c: "))

if (c >= a and c <= b) or (c >= b and c <= a):
    print("c is inbetween a and b")
else:
    print("c is not inbetween a and b")
~~~

Als we dit testen zien we dat beide gevallen worden gedekt:

~~~
$ python between.py
Enter number a: 1
Enter number b: 5
Enter number c: 3
print("c is inbetween a and b)
$ python between.py
Enter number a: 5
Enter number b: 1
Enter number c: 3
print("c is inbetween a and b)
$ python between.py
Enter number a: 5
Enter number b: 1
Enter number c: 7
print("c is not inbetween a and b)
~~~

> Nota:  
> Er zijn verschillende algoritmes om na te kijken of een getal tussen 2 andere getallen ligt.  
> Dit voorbeeld heeft als doel relationele en logische expressies samen te stellen.
