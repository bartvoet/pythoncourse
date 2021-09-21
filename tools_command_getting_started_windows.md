## Terminal op Windows (DOS-prompt)

Elk operating system bevat een CLI, Windows bevat hiervoor het programma CMD, dat je kan vinden in het windows-menu onder "administrative tools".  

> De CMD-tool heeft zijn beperkingen, voor een meer geavanceerde omgeving op Windows is het interessant Powershell te bekijken...  
> Daarnaast bestaan er ook alternatieven bestaan zoals **Cygwin** en  **MingW/MSYS** die je een Bash-compatibele omgeving meebrengen (zodat je gelijkaardige commando's als Linux kan uitvoeren)

### Windows commando's voorbeelden

We gaan nu een overzicht maken van de meest gebruikte commando en principes.  
We doen dit aan de hand van een concreet voorbeeld, dat we achteraf terug gebruiken voor onze eerste oefening met een compiler.  

### Windows shell openen

Afhankelijk van de windows-versie open je via het menu (onder "accessoires" of "administrative tools") het programma CMD.  
Eenmaal gestart krijg je een scherm zoals hieronder:  

~~~
Microsoft Windows [Version 6.1.7601]
Copyright (c) 2009 Microsoft Corporation.  All rights reserved.

C:\Users\bart>
~~~

Deze **promp** *C:\Users\bart>*:

* geeft aan welk **path** momenteel is gereferenceerd
* geeft je mogelijkheid om een **commando** in te typen

### File en directories

#### Een directory aanmaken

We starten met het aanmaken van een **directory** waarin we onze C-code gaan plaatsen.

~~~
C:\Users\bart>mkdir een_eerste_programma

C:\Users\bart>dir
 Volume in drive C is System
 Volume Serial Number is E687-8D34

 Directory of C:\Users\bart

...
02/02/2017  14:08    <DIR>          een_eerste_programma
...
~~~

Hier zien we in 1 klap 2 commando's:

* **mkdir** gevolg door het path **een_eerste_programma**  
  Dit maakt een nieuwe folder of directory deze naam.  
* Het commando **dir**  
  Laat ons toe de **inhoud** na te kijken van de huidige **directory**


#### Navigeren door directories

Als je deze directory hebt aangemaakt kan je hiernaartoe navigeren via het commando **cd**  
(hetgeen staat voor change directory)

~~~
C:\Users\bart>cd een_eerste_programma

C:\Users\bart\een_eerste_programma>
~~~

Het gebruik is éénvoudig, je navigeert door cd te typen gevolgd door het path naar deze directory.

#### Relatieve vs absolute path

*mkdir* en *cd* nemen - net zoals de meeste commando's op de DOS-prompt - als input een **path**.    
Zo'n path is de verwijzing naar een (target-)directory waarop je dit commando wil op uitvoeren.  

Er zijn een aantal manieren waarop je een path kan construeren, het grootste onderscheid dat we hier maken is  absoluut of relatief:

* **absoluut** is een path dat start vanaf de root-directory, dit path start namelijk vanaf de schijf waar je wil naar verwijzen

~~~
C:\Users\>cd C:\Users\bart\een_eerste_programma>

C:\Users\bart\een_eerste_programma>49>
~~~

Dit start altijd me een verwijzing naar de root-directory (in het geval van Windows is dit een schijf)

* **relatief** verwijst naar een locatie relatief naar je huidige directory

~~~
C:\Users\bart>cd een_eerste_programma

C:\Users\bart\een_eerste_programma>cd ..

C:\Users\bart>cd ..\een_andere_directory

C:\Users\een_andere_directory>
~~~

Dit verwijst van je huidige directory naar een path relatief tov je huidige directory.  
Het symbool **..** (2 dots na elkaar) kan je altijd gebruiken om naar de super-directory te verwijzen

#### Home-directory

Elke user in Windows heeft een home-directory, Windows voorzien een environment-variabele waarmee je terug kan gaan naar deze directory.

~~~
C:\Users\bart>cd C:\

C:\Users> cd %HOMEPATH%

C:\Users\bart>
~~~


#### Directories verwijderen

Een directory kan verwijderd worden door het commando rmdir.  
Deze directory mag wel geen files bevatten anders zal deze een fout-code opleveren

~~~
C:\Users\bart>rmdir een_eerste_programma

C:\Users\bart>cd een_eerste_programma
The system cannot find the path specified.
~~~

Als je nadien naar deze directory probeert te gaan krijg je een boodschap dat deze directory niet bestaat.

#### Files in een directory

We maken opnieuw een directory aan, deze keer navigeren we ook naar deze directory.

~~~
C:\Users\bart>mkdir mijn_eerste_programma

C:\Users\bart>cd mijn_eerste_programma

C:\Users\bart\mijn_eerste_programma>dir
 Volume in drive C is System
 Volume Serial Number is E687-8D34

 Directory of C:\Users\bart\mijn_eerste_programma

02/02/2017  14:15    <DIR>          .
02/02/2017  14:15    <DIR>          ..
               0 File(s)              0 bytes
               2 Dir(s)  123.086.462.976 bytes free
~~~

Vervolgens maken we via een **texteditor** (bijvoorbeeld notepad++ zoals eerder besproken) aan, en copieren we volgende inhoud (ons eerste C-programma) naar een file:

~~~python
print("Hello World")
~~~

Deze file bewaren we onder de eerder aangemaakte directory onder de naam hello.c.  
Nadien kijken we na met het DIR-commando of deze file correct is aangemaakt.  

~~~
C:\Users\bart\mijn_eerste_programma>dir
 Volume in drive C is System
 Volume Serial Number is E687-8D34

 Directory of C:\Users\bart\mijn_eerste_programma

02/02/2017  14:25    <DIR>          .
02/02/2017  14:25    <DIR>          ..
02/02/2017  14:24                77 hello.py
               2 File(s)            471 bytes
               2 Dir(s)  123.097.833.472 bytes free
~~~

#### Inhoud van een file tonen op command-line

Stel dat je deze file alleen wil lezen bestaat er ook de mogelijkheid vanuit de command-line deze file te lezen.  
Dit kan door de inhoud van deze file naar de command-line af te drukken via het commmando **type**

~~~
C:\Users\bart\mijn_eerste_programma>type hello.c
print("hello")
C:\Users\bart\mijn_eerste_programma>t
~~~

#### Copieren van een file

Je kan ook een file via de terminal copieren via het commando COPY

~~~
C:\Users\bart\mijn_eerste_programma>copy hello.py hello.txt
        1 file(s) copied.

C:\Users\bart\mijn_eerste_programma>dir
 Volume in drive C is System
 Volume Serial Number is E687-8D34

 Directory of C:\Users\bart\mijn_eerste_programma

02/02/2017  14:34    <DIR>          .
02/02/2017  14:34    <DIR>          ..
02/02/2017  14:24                77 hello.py
02/02/2017  14:24                77 hello.txt
               2 File(s)            154 bytes
               2 Dir(s)  123.095.646.208 bytes free
~~~

#### Verwijderen van een file

Gezien we deze file niet nodig hebben (voor het vervolg van onze cursus) gaan we deze verwijderen.  
We gebruiken hiervoor het **DEL**-commando op nieuw gevolgd door het path naar deze file.

~~~bat
C:\Users\bart\mijn_eerste_programma>del hello.txt

C:\Users\bart\mijn_eerste_programma>dir
 Volume in drive C is System
 Volume Serial Number is E687-8D34

 Directory of C:\Users\bart\mijn_eerste_programma

02/02/2017  14:35    <DIR>          .
02/02/2017  14:35    <DIR>          ..
02/02/2017  14:24                77 hello.py
               1 File(s)             77 bytes
               2 Dir(s)  123.094.589.440 bytes free

C:\Users\bart\mijn_eerste_programma>
~~~

> **Nota:**  
> Net zoals bij andere commando's kan je een file aanduiden met zowel een relatief als een absoluut path

### Uitvoeren van programma's

Naast het bekijken en manipuleren van je file-systeem kan je ook programma's uit voeren.  
In onderstaand voorbeeld voeren we via de python-interpreter hello.py uit

~~~bat
C:\Users\bart>cd mijn_eerste_programma

C:\Users\bart\mijn_eerste_programma>dir
 Volume in drive C is System
 Volume Serial Number is E687-8D34

 Directory of C:\Users\bart\mijn_eerste_programma

02/02/2017  14:35    <DIR>          .
02/02/2017  14:35    <DIR>          ..
02/02/2017  14:24                77 hello.py
02/02/2017  14:24                77 hello               1 File(s)            77 bytes
               2 Dir(s)  123.094.589.440 bytes free

C:\Users\bart\mijn_eerste_programma>python hello.py
Hello World
~~~

### Environment-variabelen

Een shell laat toe om - zoals in een programmmeer-taal - variabelen aan te maken en te gebruiken.

### Een environment-variabele definieren

Een environment-variabele is een variabele (eigenlijk een stuk tekst) die door de shell wordt bijgehouden gedurende de terminal-sessie.  

Het volgende voorbeeld gebruikt bijvoorbeeld dit mechanisme om een het path naar je project bij te houden

~~~bat
C:\Users\bart\mijn_eerste_programma>set MIJN_PROJECT=C:\Users\bart\mijn_eerste_programma

C:\Users\bart\mijn_eerste_programma>echo MIJN_PROJECT

C:\Users\bart\mijn_eerste_programma>cd C:\

C:\> cd %MIJN_PROJECT%

C:\Users\bart\mijn_eerste_programma>
~~~

* Zo'n variabele kan je initialiseren via het keyword **set**
* Gevolgd door de **naam** van deze variabele
* Je kan de inhoud van zo'n **variabele** afdrukken naar de console met het commando **echo** (gevolgd door de naam)
* Je kan de inhoud hergebruiken bij andere commando's door deze naam te omringen door een **%**-terugkomen   
  (de shell zal dan de tekst achter deze variabele vervangen)

> **Let op**, als deze variabele al bestaat dan wordt deze overschreven

#### Systeem-variabelen

Naast je eigen variabelen houdt je operating systeem ook een aantal variabelen bij.  

~~~bat
C:\Users\bart\mijn_eerste_programma>cd een_directory_die_niet_bestaat

C:\Users\bart\mijn_eerste_programma>echo %ERROR_LEVEL%
11
~~~

De variabele **ERROR_LEVEL** bijvoorbeeld houdt de error-code van de laatst uitgevoerde applicatie bij.

### Alle environment-variabelen zien

Als je alle variabelen willen zien moet je gewoon SET typen

~~~
C:\Users\bart\mijn_eerste_programma>SET
ALLUSERSPROFILE=C:\Documents and Settings\All Users
APPDATA=C:\Documents and Settings\bart\Application Data
CLIENTNAME=Console
CommonProgramFiles=C:\Program Files\Common Files
COMPUTERNAME=V-HJLVYI8TKYLPA
ComSpec=C:\WINDOWS\system32\cmd.exe
FP_NO_HOST_CHECK=NO
HOMEDRIVE=C:
HOMEPATH=\Documents and Settings\bart
KMP_DUPLICATE_LIB_OK=TRUE
LOGONSERVER=\\V-HJLVYI8TKYLPA
MKL_SERIAL=YES
NIEXTCCOMPILERSUPP=C:\Program Files\National Instruments\Shared\ExternalCompi
Support\C\
NUMBER_OF_PROCESSORS=1
OS=Windows_NT
Path=C:\WINDOWS\system32;C:\WINDOWS;C:\WINDOWS\System32\Wbem
PATHEXT=.COM;.EXE;.BAT;.CMD;.VBS;.VBE;.JS;.JSE;.WSF;.WSH;.py;.pyw
PROCESSOR_ARCHITECTURE=x86
PROCESSOR_IDENTIFIER=x86 Family 6 Model 42 Stepping 7, GenuineIntel
PROCESSOR_LEVEL=6
...
~~~
