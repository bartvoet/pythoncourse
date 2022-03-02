## Errors en excepties

### Syntax-error

Het **uitvoeren** van Python-code gebeurt in **2 fases**:

* **Parsen en interpreteren** van de Python-code
* Het eigenlijke **uitvoeren**

Als er **fouten** in de **code-syntax** kan dit **geweten** zijn bij de **start** van het **programma**  
Bijvoorbeeld bij volgende code **vergeten** we (expres) een **":"** te plaatsen **na de for-clausule**:

~~~python
a = [1,2,3,4,5,6,7]
print("From 1 until 7")
for i in a
	print(i)
~~~

Dit is **ongeldige code**, **wat** gebeurt er dan **als je deze code probeert uit te voeren?**

~~~
  File "test.py", line 2
    for i in a
             ^
SyntaxError: invalid syntax
~~~

Er gebeurt niets... buiten een indicatie van de interpreter

### Programma wordt niet uitgevoerd

De Python-interpreter **bespeurt de error**  -in de 1ste fase van **parsing** - en zal **niet starten** met de code uit te voeren.

Dat de code niet wordt uitgevoerd zie je aan het feit dat de print-statement ("From 1 until 7") - die voor de error voorkomt - niet wordt uitgevoerd.

De Python-interpreter zal de **volledige code** eerst **inladen** en **nakijken** op fouten **alvorens** deze **uit te voeren**. 

Als er dan een fout in de code is geplaatst wordt de code niet uitgevoerd.

### Runtime error => exceptie

De syntax-errors worden dus snel gedetecteerd.  
Er kunnen echter ook errors gebeuren **"at runtime"** zoals **bijvoorbeeld**:

* Een functie-call die niet bestaat
* Een string die niet kan omgezet worden naar een integer (bijvoorbeeld int("6abc"))
* Delen door 0 (bijvoorbeeld a = 5/0)

Deze "runtime error" benoemen we ook als **excepties**

De onderstaande code bijvoorbeeld...

~~~python
print("Hello")
a = 0/0
print(a)
~~~

...veroorzaakt de volgende error...

~~~
Hello
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ZeroDivisionError: integer division or modulo by zero
~~~

In dit geval zien we dat er ook duidelijk een **error** wordt aangegeven, in dit geval een **ZeroDivisionError**.  

### Een exceptie stopt het programma

Bemerk wel dat de **code** die **voor de error** (a = 0/0) komt wel **wordt uitgevoerd** (print("Hello")).

Het programma **start** wel degelijk **maar stopt** bij het **aangegeven punt van error**.

In tegenstelling tot een syntax-error kan een python-programma niet bij het parsen van de Python-code bepalen dat er eer error is.

### Excepties en functies

Er is ook geen verschil als je deze **error genereert** binnen een functie, deze **error** wordt **gepropageerd** zolang deze niet wordt opgevangen.

~~~python
def divide(a,b):
  return a/b

print("Hello")
a = divide(0,0)
print(a)
~~~

met als resultaat

~~~
Hello
Traceback (most recent call last):
  File "tmp.py", line 5, in <module>
    a = divide(0,0)
  File "tmp.py", line 2, in divide
    return a/b
ZeroDivisionError: division by zero

~~~

### Excepties opvangen

Je kan in je code ervoor zorgen dat deze **excepties** worden **opgevangen** zonder dat ze het programma beëindigen.

Dit kan via een **try-block** in combinatie met **except-block**  
In onderstaande code proberen we een variabele af te printen die niet bestaat.  

~~~python
print("Before try-catch")
try:
  print(x)
  print("After error")
except:
  print("An exception occurred")
print("After try-catch")
~~~

We kunnen dit doen aan de hand van een default **except-block**, deze gaat eender welke error (buiten SyntaxError) opvangen.

Dit heeft volgende uitvoering als resultaat...

~~~
Before try-catch
An exception occured
After try-catch
~~~

We zien hier dat:

* Het **programma** wordt **uitgevoerd**
* De **try-block** wordt **onderbroken** (bij print(x))
* De **except** wordt **uitgevoerd**
* De **code verder** loopt **na** de **except**

### Excepties opvangen per type

Je kan ook het **type van exceptie aangeven** dat je wil opvangen.  
In dit geval beperk je het opvangen tot een specifieke error, de NameError

~~~python
print("Before try-catch")
try:
  print(x)
  print("After error")
except NameError:
  print("An exception occurred")
print("After try-catch")
~~~

Het volstaan hier het type te definieren na het except-keyword.

Als je echter een andere error genereert (bijvoorbeeld een ZeroDivisionError)...

~~~python
print("Before try-catch")
try:
  print(0/0)
  print(x)
  print("After error")
except  NameError:
  print("An exception occurred")
print("After try-catch")
~~~

...zal dit echter niet worden opgevangen...

~~~
ZeroDivisionError: integer division or modulo by zero
~~~

...en wordt het programma beeindigd (prints daarna worden niet afgedrukt)

### Meerdere except-blokken

Om dit probleem te verhelpen - en meerdere excepties op te vangen - kan je meerdere except-blocks plaatsen.  
Met onderstaande except-block op ZeroDivisionError te plaatsen vermijd je dat het programma wordt beeindigd.

~~~python
print("Before try-catch")
try:
  print(0/0)
  print(x)
  print("After error")
except  NameError:
  print("A NameError-exception occurred")
except  ZeroDivisionError:
  print("A ZeroDivision-exception occurred")
print("After try-catch")
~~~

Je kan ook de de **default** except-block hier aan toevoegen

~~~python
print("Before try-catch")
try:
  print(0/0)
  print(x)
  print("After error")
except  NameError:
  print("A NameError-exception occurred")
except  ZeroDivisionError:
  print("A ZeroDivision-exception occurred")
except:
  print("Another error")
print("After try-catch")
~~~

In dat geval zullen alle error worden opgevangen (maar de boodschap zal verschillen in geval van NameError of ZeroDivisionError)


### else-clausule

Je kan ook een else-clausule toevoegen, deze zal **enkel** uitvoeren als er geen error is uitgevoerd

~~~python
try:
  print("Hello")
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")
~~~

### finally

~~~python
try:
  print(0/0)
except:
  print("Something went wrong when writing to the file")
finally:
  print("Some cleaning)
~~~

~~~python
try:
  f = open("demofile.txt")
  f.write("Lorum Ipsum")
except:
  print("Something went wrong when writing to the file")
finally:
  f.close() 
~~~

### Zelf excepties opwerpen

Naast het afvangen van excepties kan je deze ook zelf opwerpen met het keyword **raise**

Praktisch, stel als je maakt een functie:

* Die de oppervlakte van een circel berekent
* Je wenst echter geen negatieve input

~~~python
import math

def circumference(radius): 
  if radius < 0:
    raise Exception("Sorry, no numbers below zero")
  return 2 * radius * math.pi

circumference(1)  # prints +- 6,283...
circumference(-1) # raises error
~~~

De functie-aanroep op de laaste lijn zal het het programma doen crashen en beindigen.

~~~
6.283185307179586
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 3, in circumference
Exception: Sorry, no numbers below zero
~~~

### Zelf (custom) excepties aanmaken

~~~python
import math

class RadiusException(Exception):
  pass

def circumference(radius): 
  if radius < 0:
    raise RadiusException()
  return 2 * radius * math.pi

circumference(1)  # prints +- 6,283...
circumference(-1) # raises error
~~~

### En opvangen...

Je kan deze exceptie dan ook naar type opvangen zoals we eerder hebben gezien.

~~~python
import math

class RadiusException(Exception):
  pass

def circumference(radius): 
  if radius < 0:
    raise RadiusException()
  return 2 * radius * math.pi

try:
  circumference(1)  # prints +- 6,283...
  circumference(-1) # raises error
except RadiusException:
  print("Problem with radius...")
~~~

Stel dan dat je toch nog een andere exception zou opwerpen...

~~~python
import math

class RadiusException(Exception):
  pass

def circumference(radius): 
  if radius < 0:
    raise RadiusException()
  return 2 * radius * math.pi

try:
  a = 5/0
  circumference(1)  # prints +- 6,283...
  circumference(-1) # raises error
except RadiusException:
  print("Problem with radius...")
~~~

... wordt deze niet opgevangen

### Oefening

~~~python
"""
Volgend programma deelt 2 getallen door elkaar
"""

"""
Vraag 1:
Zorg dat je het resultaat afprint met een f-string
"""

"""
Vraag 2:
Vang de division by zero op (met een try-except)
"""

"""
Vraag 3:
Volgende functie vraagt een number op (command-line).
Het probleem is echter dat deze een ValueError-exceptie 
zal raisen als de gebruiker geen getalingeeft.

Wijzig deze code opdat deze het getal blijft
opvragen zolang dat de gebruiker geen geldig
integer ingeeft.
Je zal hiervoor een loop moeten combineren met
een try-except-statement.
"""

def get_number(message):
    input_user = input(message)
    try:
        return int(input_user)
    except ValueError:
        return 0

a = get_number("Geef een eerste nummer: ")
b = get_number("Geef een 2de nummer: ")

print(str(a) + " / " + str(b) + " = " + str(a / b))
~~~