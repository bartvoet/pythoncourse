## Werken met de console

Python-code kan je uitvoeren op 2 manieren:

* **File-based:** python-statements vanuit in een file uitvoeren
* **Interactief:** van uit een shell statement per statement uitvoeren en direct resultaten doen

### Interactief code uitvoeren (of REPL)

Voor sommige programmeertalen -en/of omgevingen is een **REPL** voorzien.  
Dit staat voor **R**ead **E**val **P**rint **L**oop:

* **R**ead: lezen van een expressie van de gebruiker
* **E**val: evaluatie van deze expressie en uiteindelijk uitvoering hiervan
* **P**rint: uitprinten van het resultaat van deze expressie (als er één is)
* **L**oop: wacht (continue) opnieuw op de volgende expressie of statement

Je krijgt als het ware onmiddelijk **feedback op je statements**...

### Interactieve "Hello World"

De REPL open je gewoon door het **python-commando** te typen (python3 op Linux Mint in het voorbeeld hieronder)

~~~bash
$ python3
Python 3.4.2 (default, Oct  8 2014, 10:45:20) 
[GCC 4.9.1] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> 
~~~

Vanaf dat er **>>>** verschijnt (voorafgegaan door wat systeem-info) kan je aan de slag en Python-statement of commando's uitvoeren.  
We gaan verder met een aantal commandos:

### Expressies

Een eerste gebruik is het aanroepen van een expressie

~~~
$ python3
Python 3.4.2 (default, Oct  8 2014, 10:45:20) 
[GCC 4.9.1] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> 5 + 5
10
>>>
~~~

In dit voorbeeld typen we een een expressie *"5 + 5"*, gevolgd door een enter.   
De interpreter zal:

* deze expressie uitvoeren 
* het resultaat hiervan opvangen
* en afdrukken op de volgende lijn.  


~~~
$ python3
Python 3.4.2 (default, Oct  8 2014, 10:45:20) 
[GCC 4.9.1] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> 5 + 5
10
>>>
~~~


### Geldige code

Vanzelfsprekend moet je geldige expressies en/of statements ingeven, anders zal er een error-boodschap blijven.  

~~~
$ python3
Python 3.6.8 (default, Oct  7 2019, 12:59:55) 
[GCC 8.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> 3 +
  File "<stdin>", line 1
    3 +
      ^
SyntaxError: invalid syntax
>>> 
~~~

Interessant is wel dat de interpreter niet wordt afgesloten en je je code opnieuw kan proberen.   
Bij het file-based programmeren zou het programma beeindigd worden... 

Voorgaand voorbeeld was een ongeldige syntax, volgend voorbeeld is een geldige syntax maar het verwijzen naar een niet gedefinieerde variabele.

~~~
$ python3
Python 3.6.8 (default, Oct  7 2019, 12:59:55) 
[GCC 8.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> a = 5
>>> print(b)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'b' is not defined
>>> print(a)
5
>>>
~~~

Na de error kan je de code corrigeren, en de juiste variabele - a- afdrukkken.

### Handige rekenmachine

~~~python
>>> x = 5 + 2 - 3 * 2
>>> x
1
>>> x = 5 + (2 - 3) * 2
>>> x
3
>>> 5 / 2
2
>>> 5 // 2
2
>>> 5.5 / 2
2.75
>>> 2 ** 8
256
>>> 5 % 2
1
>>>
~~~

### Sequentiele uitvoering

Naast zuivere expressies kan je ook gewone statements invoeren net als een programma.

~~~python
>>> message = "Hello World"
>>> print(message)
Hello World
>>>
~~~

In dit geval voeren we 2 statements uit:

* initialiseer je een variabele
* print je deze variabele aan

Deze statements worden - net zoals bij file-based uitvoering - uitgevoerd in de volgorde dat je ze hebt ingegeven.

### Complexere voorbeelden

Naast sequentiele statements kan je ook complexere structuren maken zoals functies en block-statements.   
Onderstaand voorbeeld bevat een functie gevolgd door een loop

~~~python
>>> def print_number(i):
...     print("hello " + str(i))
...
>>> loops = 5
>>> for i in range(loops):
...     print_number(i)
...
hello 0
hello 1
hello 2
hello 3
hello 4
>>>
~~~

Wanneer de interpreter herkent dat er een block volgt (bij de functie en for) verandert de prompt in een **block-modus**, je herkent dit aan de **...** ipv de **>>>**.  
In deze modus kan je code typen zonder dat deze niet wordt uitgevoerd na een enter.

Om uit deze modus te geraken moet je 2 maal enter typen, daarna wordt deze code uitgevoerd (of in geval van een functie wordt deze aangemaakt en ter beschikking gesteld).

### De console verlaten

Om de REPL te verlaten roep je de functie exit() aan

~~~
$ python3
>>> exit()
$
~~~

### Tips...

De REPL is een ongelooflijk handige tool die je toelaat op een korte tijd iets uit te testen of te proberen.  
We komen hier in het 3de deel nog op terug met wat extra tips en tricks, een aantal zaken die je al kan uitproberen:

#### Tab completion

Python vult code aan waar mogelijk als je een tab typt...  

~~~
Python 3.6.7 (default, Oct 22 2018, 11:32:17)
[GCC 8.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> wh
~~~

Als je na deze wh een tab typt  verschijnt er 

~~~
Python 3.6.7 (default, Oct 22 2018, 11:32:17)
[GCC 8.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> while
~~~

Als er meerdere mogelijkheden zijn wordt die deze getoond, bijvoorbeeld als we enkel een w typen

~~~
Python 3.6.7 (default, Oct 22 2018, 11:32:17)
[GCC 8.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> w
while   with
>>> w
~~~

#### History

De REPL onhoudt de voorgaande commando's die je hebt getypt, door met de pijltjes-toetsen te werken kan je door de eerder ingetypte commando's browsern.


#### Help!!!

Er is ook een help-functie voorzien, als je deze aanroept zonder arment kom  je in een nieuwe interactieve console.  
Een volledige uitleg valt buiten het bestek van een introductie maar op basis van deze initiele commentaar kan je al een aantal zaken opzoeken
Je kan deze verlaten met het keyword quit.

~~~
>>> help()

Welcome to Python 3.4's help utility!

If this is your first time using Python, you should definitely check out
the tutorial on the Internet at http://docs.python.org/3.4/tutorial/.

Enter the name of any module, keyword, or topic to get help on writing
Python programs and using Python modules.  To quit this help utility and
return to the interpreter, just type "quit".

To get a list of available modules, keywords, symbols, or topics, type
"modules", "keywords", "symbols", or "topics".  Each module also comes
with a one-line summary of what it does; to list the modules whose name
or summary contain a given string such as "spam", type "modules spam".

help>
~~~

Je kan ook een argument meegeven om meer info te krijgen over functies ...

~~~
>>> help("print")
Help on built-in function print in module builtins:

print(...)
    print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)

    Prints the values to a stream, or to sys.stdout by default.
    Optional keyword arguments:
    file:  a file-like object (stream); defaults to the current sys.stdout.
    sep:   string inserted between values, default a space.
    end:   string appended after the last value, default a newline.
    flush: whether to forcibly flush the stream.
(END)
~~~

Of data-types

~~~
Help on class int in module builtins:

class int(object)
 |  int(x=0) -> integer
 |  int(x, base=10) -> integer
 |
 |  Convert a number or string to an integer, or return 0 if no arguments
 |  are given.  If x is a number, return x.__int__().  For floating point
 |  numbers, this truncates towards zero.
 |
 |  If x is not a number or if base is given, then x must be a string,
 |  bytes, or bytearray instance representing an integer literal in the
 |  given base.  The literal can be preceded by '+' or '-' and be surrounded
 |  by whitespace.  The base defaults to 10.  Valid bases are 0 and 2-36.
 |  Base 0 means to interpret the base from the string as an integer literal.
 |  >>> int('0b100', base=0)
 |  4
 |
 |  Methods defined here:
 |
 |  __abs__(self, /)
 |      abs(self)
 |
 |  __add__(self, value, /)
 |      Return self+value.
 |
 |  __and__(self, value, /)
 |      Return self&value.
 |
 |  __bool__(self, /)
 |      self != 0
 |
 |  __ceil__(...)
 |      Ceiling of an Integral returns itself.
 |
 |  __divmod__(self, value, /)
 |      Return divmod(self, value).
 |
 |  __eq__(self, value, /)
 |      Return self==value.
 |
:
~~~

> Om deze schermen te verlaten dien je "q" te typen.
