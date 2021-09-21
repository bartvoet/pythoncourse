## Werken met tekst

Eerder hebben we reeds kennisgemaakt met het dataype string in Python. 

* a
* b
* c


### Literals

#### String als literal

Het eerste gebruik dat we hebben gezien was als **literal**:

~~~python
text = "Hello World"
print(text)
~~~

#### Enkele en dubbele qoutes

Zon'n literal wordt **gedemarkeerd** door quotes, dit kunnen enkele of dubbele quotes zijn.  
Belangrijk is wel als je start met de ene (" of ') ook eindigt met de andere.

~~~python
a = "A string in double quotes can contain 'single quote' characters."
b = 'A string in single quotes can contain "double quote" characters.'
~~~

Dit geeft als voordeel dat je binnen enkele quotes dubbele kan gebruiken en omgekeerd zoals hierboven geillustreerd.

#### Backslash als escape-character

Als je echter toch een een double quote wil gebruiken binnen een double quoted string kan je altijd een backslash gebruiken als escape character.

~~~python
print("\"Double quotes\" with backslash.")
print('\'Singe quotes\' with backslash.')
~~~

Een **escape charachter** laat je toe karakters in een literal te zetten die er normaal niet kunnen instaan.

~~~
\\	      Backslash (\)
\'	      Single quote (')
\"	      Double quote (")
~~~

Naast het escapen van deze quotes, gebruik je de backslash om er voor te zorgen dat je deze backslash zelf in een literal kan plaatsen.

~~~python
print("Een backslash \\ gebruik je in python als escape-character")
~~~

#### Speciale karakters

Een backslash kan ook worden gebruikt om specifieke karakters af te drukken zoals een tab, een nieuwe lijn of een tab... 

~~~
\n	      ASCII Linefeed (LF)
\r	      ASCII Carriage Return (CR)
\t	      ASCII Horizontal Tab (TAB)
~~~

Bijvoorbeeld...

~~~python
print("Deze tekst wordt gevolgd door een tab\t en \n een new line ")
~~~

...zal het volgende afprinten

~~~
Deze tekst wordt gevolgd door een tab	    en 
 een new line 
~~~


#### Triple quotes

Een gewone string-literal kan je maar over 1 lijn worden ingegeven.   

~~~python
print("""This is a triple double quoted string.
It can contain more then one line""")
print('''Same thing for 
single triple single quoted string''')
~~~

#### ASCII-codes

Een stuk tekst bestaat eigenlijk uit cijfers.  
Dit zie je in de encodering van een tekst-file, maar dit wordt evenwel zo intern in het datatype van een python-string.

~~~
Dec Hex    Dec Hex    Dec Hex  Dec Hex  Dec Hex  Dec Hex   Dec Hex   Dec Hex  
  0 00 NUL  16 10 DLE  32 20    48 30 0  64 40 @  80 50 P   96 60 `  112 70 p
  1 01 SOH  17 11 DC1  33 21 !  49 31 1  65 41 A  81 51 Q   97 61 a  113 71 q
  2 02 STX  18 12 DC2  34 22 "  50 32 2  66 42 B  82 52 R   98 62 b  114 72 r
  3 03 ETX  19 13 DC3  35 23 #  51 33 3  67 43 C  83 53 S   99 63 c  115 73 s
  4 04 EOT  20 14 DC4  36 24 $  52 34 4  68 44 D  84 54 T  100 64 d  116 74 t
  5 05 ENQ  21 15 NAK  37 25 %  53 35 5  69 45 E  85 55 U  101 65 e  117 75 u
  6 06 ACK  22 16 SYN  38 26 &  54 36 6  70 46 F  86 56 V  102 66 f  118 76 v
  7 07 BEL  23 17 ETB  39 27 '  55 37 7  71 47 G  87 57 W  103 67 g  119 77 w
  8 08 BS   24 18 CAN  40 28 (  56 38 8  72 48 H  88 58 X  104 68 h  120 78 x
  9 09 HT   25 19 EM   41 29 )  57 39 9  73 49 I  89 59 Y  105 69 i  121 79 y
 10 0A LF   26 1A SUB  42 2A *  58 3A :  74 4A J  90 5A Z  106 6A j  122 7A z
 11 0B VT   27 1B ESC  43 2B +  59 3B ;  75 4B K  91 5B [  107 6B k  123 7B {
 12 0C FF   28 1C FS   44 2C ,  60 3C <  76 4C L  92 5C \  108 6C l  124 7C |
 13 0D CR   29 1D GS   45 2D -  61 3D =  77 4D M  93 5D ]  109 6D m  125 7D }
 14 0E SO   30 1E RS   46 2E .  62 3E >  78 4E N  94 5E ^  110 6E n  126 7E ~
 15 0F SI   31 1F US   47 2F /  63 3F ?  79 4F O  95 5F _  111 6F o  127 7F DEL
~~~

Met python kan je met deze ascii-codes een string construeren.  
Volgend stuk code zal de string hello afdrukken.

~~~python
print("\x68\x65llo")
~~~

### Opvragen van tekst over console

Je kan tekst opvragen van de console met de input-methode

~~~python
name = input("Geef naam aub")
print(name)
~~~

### String-concatenatie

Je kan via de +-operator verschillende strings concateneren

~~~python
text = "Hello"
print(text + " world")
~~~

### Concatenatie met andere types

En je kan zelf concateneren met andere data-types

~~~python
text = "Hello"
a_number = 2
print(text + " world " + str(a_number))
~~~

Dit drukt de tekst "Hello world 2" af.  
Let wel dat je de integer-variabele moet converteren naar een string...

~~~python
text = "Hello"
a_number = 2
print(text + " world " + a_number)
~~~

...als je dit niet doet krijg je een error

~~~
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: must be str, not int
~~~

Je kan geen string optellen met een getal via de +-operator

### Concatenatie via print

De concatenatie kan echter ook wel via de print-methode.  

~~~python
text = "Hello"
a_number = 2
print(text, " world", a_hello)
~~~

Je kan hier alle types gebruiken gezien de print-functie zelf de conversie zal uitvoeren via str()

### String vermenigvuldigen

Naast de +-operator heb je ook de \*-operator

~~~
print("Hello " * 2)
~~~


### Lengte van strings

~~~python
print(len("testje")) # prints 6
print(len("")) # prints 0
~~~

### Formatteren van een string

De nieuwe manier, die zowel in Python 2 als Python 3 gesupporteerd:

~~~python
>>> print("{:d}-{:d}".format(1,2))
1-2
>>> print("{}-{}".format(1,2))
1-2
~~~

Bij dezei (nieuwe) manier ben je niet verplicht een formaat aan tegen een {} is voldoende.  
Optioneel kan je - binnen de string selecteren - welk getal uit de luist je wil selecteren:

~~~python
>>> print("{0}-{1}-{0}".format(1,2))
1-2-1
>>> print("{0:d}-{1:d}-{0:d}".format(1,2))
1-2-1
~~~

Een ander voorbeeld is het uitlijnen van tekst.

~~~python
>>> print("{0:2d}{1:3d}{0:4d}".format(1,2))
 1  2   1
>>> print("{0:2d}{1:3d}{0:4d}".format(10,20))
10 20  10
~~~

Voor een volledig overzicht kan je naar de betreffende python-documentatie gaan kijken:  
https://docs.python.org/2/tutorial/inputoutput.html


> Nota:  
> In dit geval zien we dat we dat we een methode aanroepen op een manier die we nog niet kennen vanuit C, namelijk vanuit een object (string.methode()).  
> Dit is Object-Georienteerd programmeren, hier komen zo direct nog even op terug
