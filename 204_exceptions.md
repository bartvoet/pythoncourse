## Errors en excepties

### Syntax-error

Het uitvoeren van Python-code gebeurt in 2 fases:

* **Parsen en interpreteren** van de Python-code
* Het eigenlijke **uitvoeren**

Als er **fouten** in de **code-syntax** kan dit **geweten** zijn bij de **start** van het **programma**  
Bijvoorbeeld bij volgende code vergeten we een ":"

~~~python
a = [1,2,3,4,5,6,7]
print("From 1 until 7")
for i in a
	print(i)
~~~

Als gevolg herkent de Python-interpreter de error en wordt er geen code uitgevoerd.

~~~
  File "test.py", line 2
    for i in a
             ^
SyntaxError: invalid syntax
~~~

### Programma wordt niet uitgevoerd

Hoewel de print-statement - "From 1 until 7" - voor de error voorkomt wordt deze niet uitgevoerd.  
Dit is omdat de Python-interpreter de volledige code inlaadt en nakijkt alvorens deze uit te voeren.  
Als er dan een fout in de file is geplaatst wordt de code niet uitgevoerd.

### Runtime error

Er kunnen echter ook errors gebeuren "at runtime" zoals bijvoorbeeld

* Een functie-call die niet bestaat
* Een string die niet kan worden omgezet
* Delen door 0

Bijvoorbeeld...

~~~python
print("Hello")
a = 0/0
print(a)
~~~

...veroorzaakt

~~~
Hello
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ZeroDivisionError: integer division or modulo by zero
~~~

In dit geval zien we dat er ook duidelijk een **error** wordt aangegeven, in dit geval een ZeroDivisionError

### Een exceptie stopt het programma

Belangrijk in bovenstaande code, is dat voorgaande code (afprinten van hello) wel degelijk wordt **uitgevoerd**.

Het programma start wel degelijk maar stopt bij het aangegeven punt van error.

In tegenstelling tot een syntax-error kan een python-programma niet bij het parsen van de python-code bepalen dat er eer error is.

### Excepties en functies

Er is ook geen verschil als je deze functie aanroept binnen een functie, deze error zal propageren zolang deze niet wordt opgevangen.

~~~python
def divide(a,b)
  return a/b

print("Hello")
a = divide(0,0)
print(a)
~~~

### Excepties opvangen

Je kan in je code ervoor zorgen dat deze excepties worden **opgevangen** zonder dat ze het programma beeindigen.

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

We kunnen dit doen aan de hand van een default except-block, deze gaat eender welke error (buiten SyntaxError) opvangen.

Dit heeft volgende uitvoering als resultaat...

~~~
Before try-catch
An exception occured
After try-catch
~~~

We zien hier dat:

* Het programma wordt uitgevoerd
* De try-block wordt onderbroken (bij print(x))
* De except wordt uitgevoerd
* De code verder loopt na de except

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