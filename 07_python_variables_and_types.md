## Variabelen

Nu dat we eenmaal weten hoe te printen (en functies aan te roepen) introduceren we **variabelen** en **assignment-statements**.

### Voorbeeld van gebruik variabele

We schrijven de volgende **voorbeeldcode** om het **gebruik van variabelen** te illustreren:

~~~python
say_hello = "hello"
print(say_hello)
print(say_hello)
~~~

Als je deze code uitvoert zal deze **2 maal na elkaar hello printen** naar de console

~~~
hello
hello
~~~

Er zijn hier 2 nieuwe elementen:

* Een **variabele** met de **naam say_hello**
* Een **assignment-statement** dat wordt gebruikt om de variabele say_hello de waarde "hello" toe te kennen (assign)

Door het gebruik van een **variabele** kan je dus een **waarde** in het geheugen steken en deze **hergebruiken** in latere **statements**.

### Variabele is een stuk geheugen

Een **variabele** is dus:

* Een stuk **geheugen** dat je kan hergebruiken
* Dat een **waarde** kan bevatten
* Waaraan een **naam** is gelinkt  
 (of ook wel **symbool** genoemd)

### Doel van een variabele

De **essentie**/**doel** van zo'n **variabele** is 

* het **hergebruiken of delen van data** 
* tussen verschillende **statements** 
* binnen een **sequentiële uitvoering**.

~~~
                        +------------------+
     +------write-------+ Statement 1:     |
     |                  | assignement      |
     |                  +-------+----------+           +------------------------+
     |                          |                      |      CONSOLE/OUTPUT    |
+----v-----+                    |                      | +--------------------+ |
| say_hello|            +-------v----------+           | |                    | |
+----------+            | Statement 2:     +---print---> | > hello            | |
| hello    +---read-----> function-call    |           | |                    | |
+----+-----+            +-------+----------+           | |                    | |
     |                          |                      | |                    | |
     |                          |                      | |                    | |
     |                  +-------v----------+           | |                    | |
     |                  | Statement 3:     +---print---> | > hello            | |
     +---------read-----> function-call    |           | +--------------------+ |
                        +------------------+           +------------------------+
~~~

### Assignment-statement

Om met variabelen te kunnen werken gebruiken we een **nieuw soort statement** (of **commando**), namelijk het **assignment-statement**.   
Zo'n statement kent (of **"assigns"**) een **waarde** (**value**) toe aan een **naam**.  
Deze waarde kan je dan hergebruiken in latere **statements** (de function-calls die de waarde 2 maal afdrukken).

### Vorm assignment-statment

Zo'n assignment-statement heeft altijd de vorm van :

~~~
<naam_variabele> = <waarde>
~~~

* Aan de **linkerkant** zet je de **naam of symbool** van de **variabele**
* In het midden zet je de **assignment-operator**, in python is dit het symbool **=**
* Aan de **rechterkant** zet je de waarde

### Waarde van een variabele kan je wijzigen

Een variabele zou het niet "variabel" zijn als je deze niet kan wijzigen, we beschouwen het volgende voorbeeld:

~~~python
say_hello = "hello"
print(say_hello)
say_hello = "world"
print(say_hello)
~~~

Je kan later **in het zelfde programma of sequentie** variabelen van **waarde wijzigen** (zo veel als je wilt) via deze **assignment-statements**.

~~~
                        +------------------+
     +------write-------+ Statement 1:     |
     |                  | assignement      |
     |                  +-------+----------+           +------------------------+
     |                          |                      |      CONSOLE/OUTPUT    |
+----v-----+                    |                      | +--------------------+ |
| say_hello|            +-------v----------+           | |                    | |
+----------+            | Statement 2:     +--print----> | > hello            | |
| hello    +---read-----> function+call    |           | |                    | |
+----------+            +-------+----------+           | |                    | |
                                |                      | |                    | |
                                |                      | |                    | |
                        +-------v----------+           | |                    | |
     +------write-------+ Statement 3:     |           | |                    | |
     |                  | assignment       |           | |                    | |
     |                  +-------+----------+           | |                    | |
     |                          |                      | |                    | |
+----v-----+                    |                      | |                    | |
| say_hello|            +-------v----------+           | |                    | |
+----------+            | Statement 2:     +--print----> | > world            | |
| world    +---read-----> function+call    |           | +--------------------+ |
+----------+            +------------------+           +------------------------+


~~~

### Een variabele heeft een type

Een variabele heeft dus een naam, aan de hand van deze naam kan je vanuit je code de waarde uitlezen en wijzigen.   
Daarnaast heeft een **variabele** ook van een bepaald **type**.

~~~
+---------------------+           +---------------------+
| Variabele           |           | Type                |
+---------------------+           +---------------------+
|  Naam               |           |  Operaties          |
|  Waarde             +----------->  Grootte            |
|                     |           |  Beperkingen        |
|                     |           |  ...                |
+---------------------+           +---------------------+
~~~

Dit type bepaalt wat je met de waarde (een hoop bytes...) kan doen.  
Python ondersteunt verschillende types, tot nog toe hebben we gebruik gemaakt van het type **String**.

In onderstaand stuk code maken we 3 variabelen aan van verschillende types.  
De functie type zorgt er voor dat we het type van de variabele kunnen opvragen.

~~~python
a = "hello"
b = 10
c = 0.5
print(type(a))
print(type(b))
print(type(c))
~~~

Python leidt direct het type af bij creatie van de variabele (principe wordt soms ook **type inference** genoemd).  
In dit geval kan de python-interpreter vanuit de **literal** afleiden tot **welk type** deze variabele is:

* "hello" is omgeven door quotes
* 10 is niet omgeven door quotes en bestaat enkel uit cijfers
* 0.5 is een getal met een decimaal punt (komma-getal)

Als we dan bovenstaand programma uitvoeren

~~~
<class 'str'>
<class 'int'>
<class 'float'>
~~~

Het eerste type hier is **string** dat we een aantal keren hebben gebruikt.  

### Numerieke types

De 2 andere - int en float - zijn **numerieke types** die je kan gebruiken voor berekeningen uit te voeren.

### Integers

**Integers** kennen we als de groep van **natuurlijke getallen** zoals bijvoorbeeld.

~~~
—1
–3
42
355
888888888888888
–7777777777
~~~

In **Python 3** is er feitelijk **geen limiet** aan hoe lang een **geheel getal** kan zijn.  
Natuurlijk wordt het **beperkt** door de **hoeveelheid geheugen** die je **systeem** heeft, zoals alle dingen.  

Maar verder kan een geheel getal zo lang zijn als je nodig hebt zoals hieronder

~~~python
a = 154646546465465465465465465464
print(a)
~~~

uitgevoerd wordt dit

~~~
154646546465465465465465465464
~~~

vanzelfsprekend kan je hier ook berekeningen meet doen, hier komen we zodra nog op terug:

~~~python
a = 3
b = 4
c = a + b
print(c) #prints 7
~~~

Naast het decimale stelsel is er ook support om deze getallen te binair, octaal of hexadecimaal te noteren.  
Dit doe je door dit getal te typen startende met 0 respectievelijk gevolgd door 

* **o** of O voor **octaal**
* **x** of X voor **hexadecimaal**
* **b** of B voor **binair**

zoals geïllustreerd in onderstaand voorbeeld

~~~
print(0o10) # prints 8 (octal notation)
print(0x10) # prints 16 (hexadecimal notation)
print(0b1110) # prints 14444 (binary notation)
~~~

### Floats

Python gebruikt ook floating-type types.  
Dit wordt gebruikt voor kommagetallen, dus waar je precisie nodig hebt na de komma

~~~
a = -3.0
b = 24.75
print(a)
print(b)
~~~




