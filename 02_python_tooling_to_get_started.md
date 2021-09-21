## Voorbereiding en installatie

Alvorens te kunnen starten heb je op de desbetreffende computer 2 zaken
Om het eerste deel van de cursus te kunnen uitvoeren heb je 2 componenten nodig op je PC:

* **"Python 3"-interpreter**
* **Texteditor**

### Leren met command-line te werken

Alvorens te installeren heb je eerste een minimale kennis nodig van het werken met een **command-line** op je besturingssysteem.  

* Op **Linux/Mac/Unix** is de meest gebruikte command-line omgeving **Bash**
* Op **Windows** heb je keuze tussen de klassieke **CMD-applicatie of** het iets uitgebreidere **Powershell**

Als je jezelf **niet comfortabel** voelt op de **command-line** (of erger je hebt er nog **nooit** van **gehoord**), kan je naar **Appendix A** kijken voor een introductie voor zowel Linux als Windows.

### Installatie van Python

**Eerst** installeren we de **Python-interpreter**, dit is de software die zorgt dat je Python-programma's worden uitgevoerd.

#### Python 3.7

Voor deze cursus gebruiken we als referentie versie **Python 3.7**.  
Als je een eerdere versie mocht hebben van Python 3 is dit ook OK.  

> Nota:  
> Python 2 kan je bij aanvang van de cursus ook gebruiken maar later in de cursus gaan we toch Python 3 moeten gebruiken.

#### Testen installatie

Alvorens te installeren kan je **nakijken** of je systeem **reeds** een **Python-installatie** bevat en **welke versie** deze is.  
Dit kan je doen via de **command-line**:

Op Linux/Mac/Unix:

~~~bash_terminal
a@a:~$ python --version
Python 3.6.8
a@a:~$
~~~

Op Windows komt dit neer op

~~~
C:\users\py> python --version
Python 3.6.8
C:\users\py>
~~~

> Nota:  
> Als je de installatie kan je dit ook gebruiken om je installatie te testen.

#### Installeren op Windows

Zie https://www.python.org/downloads/ en installeer de laatste versie Python-versie

#### Installeren op Mac

Mac komt meestal met Python geïnstalleerd, mocht dit niet het geval zijn of enkel Python 2 is geïnstalleerd, gelieve hier ook de link https://www.python.org/downloads/ te gebruiken.

#### Installeren op Linux

*Debian/Mint/Ubuntu:*

~~~bash
$ sudo apt-get install python3
...
bart@bvomini:~/Projects/ucll_python$ python --version
Python 2.7.15+
bart@bvomini:~/Projects/ucll_python$ python3 --version
Python 3.6.8
...
~~~

Python 3 wordt geïnstalleerd onder het alias python3 dus gelieve deze te gebruiken.

*Fedora/Red Hat:*

Voor Fedora of Red Hat, voor de 2 volgende dnf-commando's uit:

~~~bash
# dnf install python3
~~~

### Texteditor

Om een programma te schrijven hebben we een goede "**text-editor"** nodig.  
Dit is de belangrijkste tool voor een software-ontwikkelaar om code te kunnen schrijven.

Een aantal editors zijn vrij beschikbaar:

* Voor Windows-gebruikers is dit **Notepad++**
* MacOS gebruikers maken veelal gebruik van **TextMate**
* Voor Linux hangt dit af van de distributie (**Gedit**, Xedit, Kate, Vi, ...)

Er zijn buiten deze editors zeer veel goede teksteditor op de markt (Visual Studio Code, Atom, Sublime, Brackets, ...).  

> Nota: als je ervaring mocht hebben met IDE's (integrated development environment) zoals
> Eclipse, PyCharm, ... mag je deze ook gebruiken, deze komen later in de cursus nog aan bod.

Mocht je hier reeds ervaring met hebben mag je deze ook gebruiken.

> Nota:  
> Word, Libreoffice of Pages (Mac) zijn geen text-editors maar tekstverwerkers!!!  
> Deze worden gebruikt voor text-formattering, een text-editor enkel voor "zuivere tekst"