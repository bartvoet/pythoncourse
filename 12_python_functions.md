## Functies

De laatste grote blok die we bespreken in de basis introductie is het hergebruik van uitvoering.

~~~

                    _
                     \          +------------------------------+
                ______\         |                              |             * functies
                      /         |     Hergebruik uitvoering    |             * modules (implementatie 2de deel cursus)
                    _/          |                              |             * classes en objecten (2de deel cursus)
                            +---+------------------------------+---+
                            |                                      |         * while+loops
                            |        Repetitieve uitvoering        |         * loop+state
                            |                                      |         * for+loops
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

Hergebruik van uitvoering bestaat uit 3 grote stukken:

* Functies
    * **Stuk code** dat je **meermaals** kan **aanroepen**
    * Heeft een **naam** zoals een variabele
* Modules
    * (Logische) **groepering** van **functies**, klassen en variabelen
    * Bijvoorbeeld math, serial, random, ...
    * Gebruik voor dit deel van cursus
    * Ontwikkeling voor volgend deel
* Objecten en klassen
    * Groepering van **variabelen** en **functies**
    * Verschillende **instanties** mogelijk
    * Voor **2de deel van cursus**

### Functies en hergebruik

Het **sleutelwoord** bij **functies** is dus **hergebruik**
We hebben we al **eerder** **hergebruik** gezien ... namelijk met **variabelen**:

* voorzien **hergebruik** van **data/geheugen**
* **tussen** verschillende **statements**
* en je kan via de naam deze variabelen gebruiken

Nu bekijken we **ander soort hergebruik**, namelijk **hergebruik van statements** of functionaliteit.


### Ingebouwde functies

Python heeft een aantal **ingebouwde functies** die we reeds hebben gebruikt.
We hebben al eerdere functies gebruikt zoals input, int, str en print:

~~~python
# input() gets a string from the user
input_a = input("Number a: ")
# int() converts the input-string into an int we can use to calculate
a = int(input_a)
# str() converts an int back to a string
output_a = str(a + 1)
# the concatenated result is printed back through the string-function
print(input_a + " + 1  = " + output_a)
~~~

### Gebruiken van functies

We hebben al eerder function-calls (statements) gebruikt.  
Hoe gebruik je deze?

Om te starten, voor een functie-call gebruik je de **naam**, **gevolgd** door **haakjes**.

> Nota: de functies hieronder is enkel een voorbeeld om het gebruik te illustreren
> We zien zo dadelijk echte voorbeelden

Stel dat er een functie "an_example_function" zou bestaan, dan je de inhoud van deze functie uitvoeren als volgt:

~~~python
an_example_function()
~~~

### Return-waardes

Sommige functies geven een **waarde terug**, deze kan je dan **opvangen** in een variabele, we noemen dit ook de **return-value** van de functie.
Bijvoorbeeld een **(fictieve) functie hour** die het uur teruggeeft als String.

~~~python
result = hour()
print(result) # prints e.g. 12:12
~~~

Een return-waarde is de eerste manier van communiceren met de code in de functie.

### Argumenten

Daarnaast kan je een parameter of  **argument** meegeven aan een functie, voor zover deze functie argument(en) definieert.

~~~
                         """Functie kan meerdere
                            inputs hebben (argumenten)
     +-------------------+  maar slechts 1 output"""  +--------------------+
     |      INPUT        |                            |     OUTPUT         |
     +-------------------+                            +--------------------+
     |  +------------+   |                            |                    |
     |  | Argument 1 +---+--+                         |                    |
     |  +------------+   |  |      +-------------+    |   +------------+   |
     |                   |  |----->+   FUNCTIE   +----+-->+   return   |   |
     |  +------------+   |  |      +-------------+    |   +------------+   |
     |  | Argument 2 +---+--+                         |                    |
     |  +------------+   |                            |                    |
     |   ...             |                            |                    |
     +-------------------+                            +--------------------+
~~~

Deze wordt dan door de code van de functie gebruikt om iets mee te doen (zoals een bewerking).  
Stel dat je een functie maakt die een getal maal 2 doet.

~~~python
result = times_two(1)
print(result) # print 2
~~~

Je kan een waarde, variabele (of andere expressies) meegeven als argument

### Meerdere argumenten

Je ben ook trouwens **niet beperkt tot 1 argument**, een functie kan van **0 tot oneindig aantal argumenten** definieren.

~~~python
result = multiply(3,2)
print(result) # prints 6
~~~

Deze argumenten zijn "by default verplicht" maar sommige functies hebben ook nog optionele argumenten (we komen hier zo dadelijk op terug...)

### Gebruik Python-modules

int(), str(), print(), input() zijn direct beschikbaar in Python
Andere - meer gespecialiseerde - functies zijn gegroepeerd in modules

~~~
                +---------------------+
                |                     |
                |  Module             |
                |                     |
                |   +------------+    |
                |   | Functie    |    |
                |   +------------+    |
                |                     |
                |   +------------+    |
                |   | Functie    |    |
                |   +------------+    |
                |                     |
                |   +------------+    |
                |   | Functie    |    |
                |   +------------+    |
                |                     |
                +---------------------+
~~~

Bijvoorbeeld als je wiskundige functies wil gebruiken kan je bijvoorbeeld gebruik maken van de math-module (die standaard voorzien is in Python)

Bijvoorbeeld onderstaande gebruikt een aantal functies en constanten van deze module.

~~~python
import math
print(math)
degrees = 45
radians = degrees / 360.0 * 2 * math.pi
math.sin(radians)
math.sqrt(2) / 2.0
~~~

Om een module te kunnen gebruiken dien je een import-clause toe te voegen, deze maakt de functies in je applicatie beschikbaar.

Om dan de functies te gebruiken volstaat het niet de naam van deze functies te gebruiken

* je moet deze naam prefixen met de module-naam
* gevolgd door een **punt**

Voor de math-module specifiek kan je volgende gebruiken.
https://docs.python.org/3/tutorial/stdlib.html#mathematics

Een ander voorbeeld is de random-module.  
Onderstaande code demonstreert het gebruik van deze module.

~~~python
import random

x = random.random()
print(x) # prints a float between 0 and 1 (not included)
x = random.randint(0, 100)
print(x) #prints an int between 0 and 100 (not included)
~~~

Voor een volledig overzicht van de standaard-functies (en andere dingen) kan je terecht https://docs.python.org/3/tutorial/stdlib.html (RTFM...)

### Zelf functies schrijven

Later gaan we nog zien hoe we zelf modules kunnen ontwikkelen, maar laten we al starten met lokale functies...  
We starten met een functie die je naam afdrukt:

~~~python
def greeting(): # <----------- function-header def + name + () + :
    print("hello ")     #|<--- function-body ==> block
    print(" from bart") #|
~~~

### header en body

Deze functie bevat 2 onderdelen:

* Een **functie-definitie** of **-header**
    * Start met keyword **def**
    * Een **naam** (net zoals bij een variabele)
    * **Haakjes** (waar je argumenten kan tussenplaatsen)
    * **Eindigend** op een **dubbel punt** (dat een code-block aankondigt)
* Een **block** (van statements)
    * Geindenteerd tov de functie

Dit dubbel punt hadden we al eerder gezien bij condities en loops.   
Dit teken duidt altijd het einde aan van een clausule die vooraf gaat aan een code-block.

> Nota: een functie is een herbruikbare block van statements.  
> Op zich zelf is het echter geen statement, want deze wordt niet uitgevoerd als je deze niet aanroept.

### Gebruik van (zelfgeschreven) functies

Een functie op zich zal nooit uitgevoerd worden, dus als je deze niet aanroept zal er niet veel gebeuren.  
Je kan deze functie aanroepen net zoals andere functies.

~~~python
def greeting():
    print("hello ")
    print(" from bart")
greeting()
~~~

Met als resultaat:

~~~
$ python3 greeting.py
hello
 from bart
$
~~~

### Volgorde is belangrijk

Belangrijk is dat je functie gedeclareerd is voor dat je ze aanroept.  
Stel dat je de functie "greeting" zou aanroepen voor de declaraite...

~~~python
greeting()
def greeting():
    print("hello ")
    print(" from bart")
~~~

...dan zal de python-interpreter een error genereren zoals hieronder...

~~~
$ python3 test.py
Traceback (most recent call last):
  File "test.py", line 1, in <module>
    greeting()
NameError: name 'greeting' is not defined
~~~

Opdat code een functie kan aanroepen/gebruiken betekent dit ook dat deze eerder in de "sequentiele uitvoering" dient te worden uitgevoerd.

### Argumenten

Je kan een functie **flexibeler** maken door er **argumenten** of parameters er aan toe te voegen.  
In onderstaand voorbeeld voegen we een argument *"name"* toe, met dit argument kan je de naam bepalen van uit de 

~~~python
def greeting(name):
    print("hello ")
    print(" from " + name)
greeting("Bart")
~~~

Dit **argument** gedraagt zich als (en is in feite) een soort van variabele.   
Je kan als gevolg dezelfde functie meerdere malen **hergebruiken** met een verschillende naam.

~~~python
def greeting(name):
    print("hello ")
    print(" from " + name)
greeting("Bart")
greeting("Fons")
~~~

Als je deze code dan uitvoert krijg je 2 maal de zelfde uitvoering maar met een andere naam.

~~~
$ python3 greeting.py
hello
 from bart
hello
 from fons
$
~~~

### Meerdere argumenten

Een functie is niet enkel enkel beperkt tot 1 argument maar kan er meerdere gebruiken.  
In volgend voorbeeld geven we zowel een voor- als achternaam mee...

~~~python
def greeting(name,surname):
    print("hello ")
    print(" from " + name + " " + surname)
greeting("Bart","Voet")
greeting("Fons","Student")
~~~

Met als resulaat:

~~~
$ python3 greeting.py
hello
 from Bart Voet
hello
 from Fons Student
$
~~~

### Output via een return-statement

Naast input kan zo'n functie ook een output hebben.

~~~
                         """Functie kan meerdere
                            inputs hebben (argumenten)
     +-------------------+  maar slechts 1 output"""  +--------------------+
     |      INPUT        |                            |     OUTPUT         |
     +-------------------+                            +--------------------+
     |  +------------+   |                            |                    |
     |  | Argument 1 +---+--+                         |                    |
     |  +------------+   |  |      +-------------+    |   +------------+   |
     |                   |  |----->+   FUNCTIE   +----+-->+   return   |   |
     |  +------------+   |  |      +-------------+    |   +------------+   |
     |  | Argument 2 +---+--+                         |                    |
     |  +------------+   |                            |                    |
     |   ...             |                            |                    |
     +-------------------+                            +--------------------+
~~~

In de code kan dit via een **return-statement**

Stel dat je een (onnodige) functie schrijf om de som van 2 variabelen te bereken kan je dit al volt.

~~~python
def sum(a,b)
    result = a + b
    return result
~~~

Via het **return-statement** kan je dan het resultaat van deze som teruggevren aan de aanroepende code opdat deze die kan opvangen in bijvoorbeeld een variabele.

~~~python
def sum(a,b)
    result = a + b
    return result
a = sum(2,5)
print(a) # prints 7
~~~

### Nog een voorbeeld...

We kunnen bijvoorbeeld ook ons eerder voorbeeld (printen van naam en naam) ook nog omvormen naar een functie die - na het geven vna de naam- ook nog de naam opvraagt.  
We noemen deze voor de gelegenheid "polite_conversation"

~~~python
def polite_conversation(surname,last_name):
    print("hello ")
    print(" from " + surname + " " + last_name)
    name = input("What's your name?")
    return name
your_name = polite_conversation("Bart","Voet")
print("OK, thank you, so your name is " + name)
~~~

### Opsplitsen van functies

Een functie kan natuurlijk ook nog een anderen functie aanroepen.

~~~python
def greeting(name,surname):
    print("hello ")
    print(" from " + name + " " + surname)

def polite_conversation(surname,name):
    greeting(surname,name)
    name = input("What's your name?")
    return name

polite_conversation("bart","voet")
~~~

### Lokale variabelen

Je kan binnen een functie variabelen declareren.  

~~~python
def sum(a,b):
    c = a + b
    return c

result = sum(2,5)
print(result)
~~~

Je hebt deze vaak nodig - zoals in bovenstaand voorbeeld - om tussenresultaten in op te slagen.  
Wel kan je deze **lokale variabelen** **niet buiten** deze **functie** gebruiken, zoals in de functie hieronder...

~~~python
def sum(a,b):
    c = a + b
    return c

sum(2,5)
print(c) #renders NameError
~~~

Deze code probeert c (intern voor functie sum) rechtstreeks te gebruiken.  
Als je deze code echter uitvoert zal de python-interpreter de volgende error genereren:

~~~
$python3 test.py
Traceback (most recent call last):
  File "/home/bart/test.py", line 6, in <module>
    print(c) #renders NameError
NameError: name 'c' is not defined
~~~

### Scope

Variabelen **binnen een functie** zijn dus **niet bereikbaar** vanuit aanroepende code.   

Variabelen hebben - afhankelijk waar ze worden gedefineerd - een **scope**.  
Deze scope vanuit welke code deze variabele **bereikbaar** is maar ook de **levenduur** van de variabele.  
Een lokale variabele wordt namelijk telkens opnieuw geinstantieerd bij het aanroepen van de functie.

### En verder...

We gaan hier dieper op in het 2de deel van de cursus, onthoudt voorlopig dat **lokale variabelen alleen bestaan binnen het bereik/scope van een functie**

In het volgende deel van de cursus gaan we hier nog verder op in samen met wat meer geavanceerde toepassingen met functies.

Onthoudt vooral ook waarom (en wanneer) je functies moet gebruiken.

* **Leesbaarheid** en **modulariteit** -> Opdelen van je code in stukken
* **Hergebruik** -> Code die je meerdere malen wil gebruiken zonder copy/paste

