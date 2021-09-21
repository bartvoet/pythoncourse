## Herhaling Deel 1

* **Herhaling** van de **belangrijkste concepten**  
* Zowel in **slide-vorm** als in de **cursus beschikbaar**

--------------------------------------

### Computer-programma

* Leest **input** (scherm, netwerk, ...)
* **Verwerkt** deze **input** (of data)
* **Gebruikt** het **geheugen** voor tussen-resultaten
* **Schrijft** deze weg (console-output, file, ...)

~~~
                     +-------------+
+---------+          |             |          +----------+
|  INPUT  +--------->| VERWERKING  +--------->|  OUTPUT  |
+---------+          |             |          +----------+
 """                 +------+------+           """
 Bijvoorbeeld               |                  Bijvoorbeeld
 input()-functie            v                  print()-functie
 """                 +------+------+           """
                     |  GEHEUGEN   |
                     +-------------+
                       """
                       Gebruik van variabelen
                       in je programma 
                       """
~~~

--------------------------------------

### Een eerste Python-programma

~~~
Code:
~~~

~~~python
    print("hello")
    print("world")
~~~

~~~
Uitvoering:
~~~

~~~bash
    $ python hello.py
    hello
    world
~~~

--------------------------------------

### Sequentiele uitvoering

~~~bash
    $ python hello.py
    hello
    world
~~~


~~~
(1)            Python leest het script
(2)-(3)-(...)  Blijft statements uitvoeren tot dat deze gedaan zijn
               Sequentieel: in de volgorde zoals ze in het script staan

                                                        +------------------+
     +-----------------+        +--------------+        | CONSOLE/OUTPUT   |
     | hello.py        +--(1)-->+              |        | +--------------+ |
     +-----------------+        |              |        | |              | |
_||_ | print("hello")  +--(2)-->+  Python      +--(2)-->+ | > hello      | |
\  / | print("world")  +--(3)-->+  Interpreter +--(3)-->+ | > world      | |
 \/  | ...             | (...)  |              | (...)  | | > ...        | |
     +-----------------+        +--------------+        | |              | |
                                                        | +--------------+ |
                                                        +------------------+
~~~

--------------------------------------


### Waardes

* Een **programma** werkt met **data**
* We noemen dit ook **waardes**
    * Bewerken
    * Berekenen
    * Printen
    * Uitlezen


--------------------------------------


### Letterlijke waarde => LITERAL

Een waarde kan je **letterlijk** in je code declareren

~~~python
a = 1
print("test")
~~~

~~~
1 en "test" waardes die letterlijk in je code staat
Dit noemt men literals
(afkorting van literal value of letterlijke waarde)
~~~


------------------------------------

### Type

* Een waarde heeft een **type**
* Elke type heeft zijn specifieke operaties
    * **int** en **float** kan je berekeningen met uitvoeren
    * **string** bevat tekst-karakters die je kan afdrukken, bewerken, doorzoeken, ...

~~~python
a = 1  # 1 is integer
b = 1.5  # 2.5 is float
print("test") # "test" is a string
~~~

~~~
1 is een      integer => gehele getalen
1.5 is een    float   => kommagetallen
"test" is een string  => tekst
~~~
-------------------------------------

### Expressie

* Een waarde hoef niet letterlijk in je code staan
* Kan ook worden opgeleverd door een **expressie**
* Expressie is elk **stuk code** dat een **waarde oplevert**
    * Operator-expressies
        * Rekenkundige expressie
        * Boolean-expressie
        * ...
    * Function-call
    * ...

--------------------------------------

### Rekenkundige expressie

* Bereken via 2 integer-waardes (operanden)

| Operator   |   Betekenis          |
|------------|----------------------|
| +          | optellen             |
| -          | aftrekken            |
| *          | vermenigvuldigen     |
| /          | deling               |
| //         | deling               |
| %          | rest van deling      |
| **         | macht                |

--------------------------------------

### Binaire operatoren


~~~
2 operand
1 operator
       <left-operand>   <operator>    <right-operand>
~~~

~~~python
a = 5 * 6
~~~

~~~
a = 5 * 6 is een statement
    5 * 6 is expressie die waarde oplevert
    5     is linker-operand
      *   is operator die vermenigvuldiging
        6 is rigth-operand
~~~
--------------------------------------

### Unitaire operatoren

~~~
1 operanden
1 operator
     <operator> <operand>
~~~

~~~python
b = 5
a = -b
~~~

~~~
a = -b    is een statement
    -b    is expressie die waarde oplevert
    -     als operator draait waarde om
     b    is operand
~~~

--------------------------------------

### Variabele

* **Koppeling** 
    * van een **waarde** (of het resultaat van een expressie) 
    * aan een **stuk geheugen**
    * via een **symbool** of **naam**

~~~python
a = 1
b = 2
c = a + b
print(c)
~~~

--------------------------------------

### Statements

* **actie** of **commando** 
* dat je aan Python geeft 
* om **uit te voeren**
* Voorbeelden
    * **Function-call**
    * **Assignment-statements**
    * ...

--------------------------------------

#### Statement => function-call

Aanroepen van een bestaande functie

~~~
print("hello world")
~~~

--------------------------------------

#### Statement => assignment-statement

Toekennen van een waarde aan een variabele

~~~
a = "Een tekst"
b = 1
~~~

--------------------------------------


### Literal

Een letterlijke waarde die je aan code toevoegt


### Code-block






### Block-statement

Naast de enkelvoudige statement


op zijn éénvoudigst een lijn code


expressie = eender welk stuk code dat 


code-block = sequentie van code, een blo