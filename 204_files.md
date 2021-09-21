## Werken met text-files

### Files

Een programma zal data (in- en output) verwerken, in vele gevallen zal een programma data willen **bewaren** voor **later gebruik**.  
De eerste en meest directe manier om data op te slagen door deze **data** naar een **file** te schrijven.  

Een file is in essentie:

* een **verzameling** van **bytes**
* opgeslagen op een **persistend medium** (harde schijf, usb-stick, ...)
* geadresseerd binnen **een filesysteem**
* met een specifiek **path** en **address**

Er bestaan verschillende soorten files:

* Text-files  
  Bevatten tekst-karakters die je kan lezen
* Executables  
  Bevatten code-instructies
* Media-files  
  Files die afspeelbare media (beelden, audio, video, ...)
* Andere binaire datafils zoals spreadsheet-documenten, teksverwerkings-documenten, databases, ...
* ...
  
### Text-files

In dit deel gaan we leren werken met text-files.  

Text-files bevatten karakters (zoals we deze ook kennen van strings), karakters zijn bytes waarvan de waarde overeenstemt met een specifiek karakter.

#### ASCII-encodering

Een heel veel gebruikte **encodering** die hiervoor wordt gebruikt bijvoorbeeld is ASCII

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

Stel dat we een tekst-file aanmaken met de volgende inhoud

~~~
hello
  world
~~~

zien we (via het programma hexdump) de volgende bytes

~~~
$ cat hello.txt 
hello
	world
$ od -t x1 hello.txt 
0000000 68 65 6c 6c 6f 0a 09 77 6f 72 6c 64 0a
0000015
~~~

Deze bytes (hexadecimaal voorgesteld) kan je mappen naar de tekst volgens de bovenstaande ascii-tabel:

~~~
68 65 6c 6c 6f 0a 09 77 6f 72 6c 64 0a
=
h  e  l  l  o  LF HT w  o  r  l  d  LF
~~~


### Werken met text-files in Python

Gelukkig genoeg moet je niet deze encodering kennen of toepassen om vanuit Python met text te kunnen werken.  
Hiervoor bestaan er een aantal operaties binnen de Python. 

#### Open en close

Werken met text-files start met aanmaken van een file-object
Dit file-object kan je aanmaken met de functie open() als volgt.  

~~~python
f = open("demofile.txt")
# Een aantal operaties...
f.close()
~~~

Na gebruik is het belangrijk dit file-object te sluiten met de operatie close.  
Het operating system kan namelijk de file locken voor gebruik vanuit andere programma's zolang dit file-object open staat.

#### Relatief vs absoluut

Vorig voorbeeld opende een file die in dezelfde directory staat als van waaruit je het python-programma uitvoert.
Je kan ook zeggen dat deze file **relatief** is aan het path waar je applicatie wordt uitgevoerd.

Als er een de file in een subdirectory staat vanwaar je programma wordt uitgevoerd kan je een path beschrijven als volgt:

~~~python
f = open("subdirectory/demofile.txt")
# Een aantal operaties...
f.close()
~~~

Daarnaast als je een exact path wil beschrijven

~~~python
f = open("/home/bart/demofile.txt")
# Een aantal operaties...
f.close()
~~~

(en voor de Windows-gebruikers een plezier te doen)

~~~python
f = open("c:/users/bart/demofile.txt")
f.close()
~~~

#### Automatische close

Het probleem met bovenstaande code is dat als er een exceptie voordoet na open() het file-object mogelijk niet gesloten wordt.
Om dit te vermijden bestaat er de with-statement

~~~python
with open("demofile.txt") as f:
  print(f.read())
# Een aantal operaties...
print(f.closed)
~~~

Deze zal er voor zorgen dat - na het uitvoeren van de code binnen deze statement - het file-object zowiezo wordt gesloten (zelfs al is er een exceptie/crash)

#### Modes

Een eerste notie die je moet kennen is het gebruik van modes bij het openen van een file:

* "r" - Read
* "x" - Create - maakt een file aan, en geeft een error wanneer deze file al bestaat
* "a" - Append - maakt een file aan als deze nog niet bestaat, alle writes zijn toevoegingen
* "w" - Write -  maakt een file aan als deze nog niet bestaat, overschrijft bestaande file

Deze mode kan je meegeven als een 2de (optioneel argument)

~~~python
with open("demofile.txt", "r") as f:
  print(f.read()) 
~~~

Als je dit 2de argument niet toevoegt, is de default-mode is r (read-only) 

### Lezen uit een tekst-file 

Om te demonstreren hoe we met een text-file om kunnen gaan starten met het aanmaken van een file genaamd **demofile.txt** met de volgende (nietszeggende) content:

~~~
Lorem ipsum dolor sit amet, consectetuer adipiscing elit. 
Aenean commodo ligula eget dolor. Aenean massa. 
Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. 
Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim. 
Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu. In enim justo, rhoncus ut, imperdiet a, venenatis vitae, justo. Nullam dictum felis eu pede mollis pretium. 
Integer tincidunt. Cras dapibus. 
Vivamus elementum semper nisi. Aenean vulputate eleifend tellus. 
Aenean leo ligula, porttitor eu, consequat vitae, eleifend ac, enim. 
Aliquam lorem ante, dapibus in, viverra quis, feugiat a, tellus. Phasellus viverra nulla ut metus varius laoreet. 
Quisque rutrum. Aenean imperdiet. Etiam ultricies nisi vel augue. Curabitur ullamcorper ultricies nisi. Nam eget dui
~~~

#### Volledige inhoud uitlezen

Je kan de hele inhoud van een text-file opvragen via de read-functie.

~~~python
with open("demofile.txt", "r") as f:
  print(f.read()) 
~~~
Bovenstaande zal de volledige tekst afprinten (zoals hierboven).

Je kan je ook beperken tot het aantal bytes (in geval van tekstfiles de characters)

~~~python
with open("demofile.txt", "r") as f:
  print(f.read(5)) 
  print(f.read(5)) 
~~~

Bemerk ook dat de positie tot waar je al hebt gelezen wordt bijgehouden in het file-object

~~~
Lorem
 ipsu
~~~

#### Lijn per lijn lezen

Je kan ook kiezen om lijn per lijn uit te lezen.

~~~python
with open("demofile.txt", "r") as f:
  print(f.readline())
  print(f.readline()) 
~~~

Bovenstaande code zal de 2 eerste lijnen afdrukken.

~~~
Lorem ipsum dolor sit amet, consectetuer adipiscing elit. 
Aenean commodo ligula eget dolor. Aenean massa.
~~~

#### Loopen door alle lijnen

Het file-object kan zich ook gedragen zoals een lijst van lijnen;  
Op dit object kan je dan een loop uitvoeren door de ganse file.

~~~python
with open("demofile.txt", "r") as f:
  for x in f:
    print(x) 
~~~

~~~
Lorem ipsum dolor sit amet, consectetuer adipiscing elit. 

Aenean commodo ligula eget dolor. Aenean massa. 

Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. 

Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim.

...
~~~

### Schrijven naar een een file

Voor het schrijven naar een file zijn er 3 belangrijke modi die we moeten begrijpen:

* Een nieuwe file schrijven  => x
* Een bestaande file overschrijven => w
* Toevoegen aan het einde van een file => a

#### Een nieuwe file aanmaken

Het eerste scenario is dat we een nieuwe file willen aanmaken.  
In dit geval gebruiken we de modus **x**
* "x" - Create - maakt een file aan, en geeft een error wanneer deze file al bestaat

~~~python
with open("hello.txt", "x") as f:
  f.write("Dit is een nieuwe file!!!")
with open("hello.txt", "r") as f:
  print(f.read()) 
~~~

Als de file nog niet mocht bestaan zal er een nieuwue file hello.txt worden aangemaakt

~~~
$ python3 create_new_file.py
Dit is een nieuwe file!!!
$
~~~

Mocht deze file reeds bestaan, bijvoorbeeld door het programma een 2de maal te runnen zal er een exceptie worden opgeworpen door de open-functie

~~~
$ python3 create_new_file.py
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
FileExistsError: [Errno 17] File exists: 'hello.txt'
$
~~~

#### Nieuwe file of bestaande file overschrijven

Als we dezelfde code wijzigen om de modus **w** te gebruiken:

* zal er **geen error** worden opgeworpen als de **file reeds bestaat**
* maar wordt deze **overschreven**
* als deze toch **niet bestaat** wordt deze **aangemaakt**

Onderstaande code:

~~~python
with open("hello.txt", "w") as f:
  f.write("Dit is een nieuwe file!!!")
with open("hello.txt", "r") as f:
  print(f.read()) 

with open("hello.txt", "w") as f:
  f.write("De file is overschreven!!!")
with open("hello.txt", "r") as f:
  print(f.read()) 
~~~

* Zal de file eerst aanmaken (als deze nog niet bestaat)
* En vervolgens de inhoud overschrijven

~~~
$ python3 create_new_file.py
Dit is een nieuwe file!!!

De file is overschreven

$
~~~

#### Toevoegen aan de einde van de text-file

~~~python
with open("hello.txt", "w") as f:
  f.write("Dit is een nieuwe file!!!")
with open("hello.txt", "r") as f:
  print(f.read()) 

with open("hello.txt", "a") as f:
  f.write("Deze lijn is toegevoegd!!!")
with open("hello.txt", "r") as f:
  print(f.read()) 
~~~

~~~
$ python3 append_to_file.py
Dit is een nieuwe file!!!

Dit is een nieuwe file!!!
Deze lijn is toegevoegd!!!
$
~~~


### Andere file-operaties

Naast het lezen en schrijven van een file kan je ook nog andere operaties uitvoeren op files
#### Deleten van files

Het verwijderen van een file kan je via de functie remove.  
Hiervoor dien je wel de os-library te importeren

~~~python
import os
os.remove("hello.txt") 
~~~

Hou er natuurlijk rekening mee dat als de file niet bestaat deze code een error zal opwerpen:

~~~python
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
FileNotFoundError: [Errno 2] No such file or directory: 'hello.txt'
~~~

#### Testen of de file bestaat

Deze exceptie kan je vermijden door na te gaan of deze file reeds betaat, die kan je met de exists()-functie
Zo kan je bovenstaande code verbeteren door de remove()-call af te schermen met een if-clausule

~~~python
import os
if os.path.exists("demofile.txt"):
  os.remove("demofile.txt")
else:
  print("The file does not exist") 
~~~

#### Verwijderen van een directory

Om een directory te verwijderen dien je de rmdir()-functie te gebruiken

~~~python
import os
os.rmdir("a_folder") 
~~~

Let wel, deze zal falen 

* als de directory niet bestaat 

~~~
...
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
FileNotFoundError: [Errno 2] No such file or directory: 'a_folder'
>>> 
~~~

> Om dit te vermijden kan je os.path.exists() gebruiken)

* Als de directory niet leeg is

~~~
...
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
OSError: [Errno 39] Directory not empty: 'a_folder'
~~~

### Verdere info

Er zijn nog vele mogelijkheden om files en directories te bewerken.  
Om deze te leren kennen kan je terecht bij https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files