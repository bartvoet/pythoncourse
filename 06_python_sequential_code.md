## Sequentiële uitvoering

### Een 2de programma ... met meerdere statements

Je bent **niet beperkt** tot **1 statement**, je kan er meerdere aanroepen.  
Pas het vorige voorbeeld nu aan tot de volgende code:

~~~python
print("hello")
print("world")
~~~

In welke **volgorde** wordt deze aangeroepen?  
Heel eenvoudig, de **statements** worden **uitgevoerd** in de volgorde zoals **jij** ze in de **file** **plaatst**.

~~~bash
$ python hello.py
hello
world
$
~~~

Zoals je ziet zal deze **eerst "hello"** en **dan** pas **"world" afdrukken**.

### Python-interpreter voert statement voor statement uit

De statements uit deze file worden **1 voor 1** uitgevoerd in de **volgorde zoals ze gegeven** zijn.  
Het komt dus neer op:

~~~
                                                               +--------------------------+
    +-----------------+        +----------------------+        |     CONSOLE/OUTPUT       |
    | hello.py        +--(1)-->+                      |        | +----------------------+ |
    +-----------------+        |                      |        | |                      | |
    | print("hello")  +--(2)-->+  Python Interpreter  +--(2)-->+ | > hello              | |
    | print("world")  +--(3)-->+                      +--(3)-->+ | > world              | |
    | ...             | (...)  |                      | (...)  | | > ...                | |
    +-----------------+        +----------------------+        | |                      | |
                                                               | +----------------------+ |
                                                               +--------------------------+
~~~

* *(1)* De Python interpreter die hello.py leest  
  (doordat het script als argument wordt meegegeven
* *(2)* Uitvoeren van de **1ste statement**
* *(3)* Uitvoeren van de volgende 2de statement
* *(...)* Tot dat er geen statements meer zijn

### Basisblok "sequentiële uitvoering"

Dit is wat we noemen **sequentiële uitvoering**  
**Sequentieel** betekent hier, dat alle **statements** die je in een Python-script plaatst:

* **1 voor 1** worden **uitgevoerd**
* In de **volgorde** dat jij ze hebt geplaatst (eerst print("hello") dan print("world"))

Dit is een **basisprincipe (fundering)** waarop (bijna) alle (imperatieve) **programmeertalen** op gebaseerd zijn.  

### Maar het gaat verder...

Het principe van **sequentiële uitvoering** alleen is echter **niet voldoende** om een **volledig functionerend programma** te schrijven.  
**Boven op** dit principe heb je een **aantal andere principes** die we de komende hoofdstukken gaan uitleggen, namelijk:

* **Conditionele** uitvoering  
  statements enkel **uitvoeren** **onder** bepaalde **voorwaarden**  
  We zullen dit zien onder de vorm van **if-else-statements**
* **Repetitieve** uitvoering  
  statements blijven **uitvoeren** **zolang** aan een bepaalde **voorwaarde** is voldaan.  
  In het vakjargon wordt dit ook meestal **looping** genoemd
* **Hergebruik** van uitvoering  
  statements **groeperen** om **herhaaldelijk** te kunnen **uitvoeren**  

Het meest **elementaire hergebruik** vinden we bij **functies**, maar later gaan we ook zien dat we deze functies kunnen groeperen in **modules** en **objectgeoriënteerd programmeren**

### Verschillende basis-uitvoerings-principes

Al deze **basisprincipes** steunen bovenop elkaar of zijn **op elkaar gebouwd**.
Bij het aanleren van de meeste programmeertalen (zoals Python in dit geval) leer je een taal aan in 

Om **conditionele uitvoering** te kunnen doen heb je **sequentiële uitvoering** nodig.  
**Repetitieve uitvoering** heeft **condities** nodig om te weten of deze verder mag worden **uitgevoerd**.  

**Hergebruik van uitvoering** staat hier een beetje **los/onafhankelijk** van maar meestal begin je pas dit te leren als je de andere basisprincipes onder de knie hebt.

~~~
                            +------------------------------+
                            |                              |
                            |     Hergebruik uitvoering    |
                            |                              |
                        +---+------------------------------+---+
                        |                                      |
                        |        Repetitieve uitvoering        |
                        |                                      |
                    +---+--------------------------------------+---+
                    |                                              |
                    |           Conditionele uitvoering            |
                    |                                              |
                +---+----------------------------------------------+---+
                |                                                      |
                |                Sequentiële uitvoering                |
                |                                                      |
                |   +------------+   +------------+   +------------+   |
                |   | Statements |   | Variabelen |   | Expressies |   |
                +---+------------+---+------------+---+------------+---+
~~~

### First thing first...

We moeten echter **eerst leren kruipen alvorens te fietsen**, dus we beginnen bij de **3 basiselementen** van **sequentiële uitvoering**

~~~
                +------------------------------------------------------+
                |                                                      |
                |                Sequentiële uitvoering                |
                |                                                      |
                |   +------------+   +------------+   +------------+   |
                |   | Statements |   | Variabelen |   | Expressies |   |
                +---+------------+---+------------+---+------------+---+
~~~

* **(Enkelvoudige) Statements**  
  Elementaire unit van functionaliteit in python zoals
    * Aanroepen van functies (function-call)
    * Berekening uitvoeren en opslaan in variabele (assignment-statement)
    * Beëindigen van een functie (return-statement)
    * ...
* **Variabelen** (en **literals**)  
  Tussentijds opslaan van waardes in het geheugen om in een latere statement te hergebruiken
* **Expressies**  
    * Eender welk **uitvoering van code** dat een **resultaat** oplevert
    * Bestaat **operatoren** en **operanden**
