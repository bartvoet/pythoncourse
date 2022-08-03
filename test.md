## Probeer-examen...

Dit is een proefexamen met eenzelfde moeillijkheidsgraad als we op het examen zouden vragen...

* Uitwerking op eigen computer
* Enkel programmeren
* Open boek
* Wel alleen werken

### Onderwerp: Festival-beheer

In het vooruitzicht van een COVID-vrije toekomst is de opdracht het ontwikkelen van een applicatie om een
festival te beheren.  

De proef bestaat uit 3 onderdelen:

* Basis => herhaling van we in het eerste semester hebben gezien (lijsten en objecten)
* SQL => de applicatie omzetten in een database
* Onderscheiding => een aantal extra opdrachten om het maximum er uit te halen (niet verplicht)

### Basis: boeken van groepen (16/20)

In eerste stap ontwikkelen we een applicatie die groepen kan boeken voor een festival.
Bedoeling is dat je groepen kan boeken, kan verwijderen en consulteren.

Dit eerste deel laad je op in een **file** genaamd **festival.py**
Belangrijk: start niet aan de volgende opgave als deze nog niet gedan is, deze opgave is verplicht de volgende
is enkel ter onderscheiding.

In dit eerste deel doe je dit gewoon met een lijst...  
Je maakt ook een klasse met de naam Boeking waar je de volgende info in bijhoudt:

* groepnaam
* startuur
* einduur
* id (dat tel je op)


#### Het basis-menu

We starten met een basis-menu dat 3 menu-items bevat.  
Schrijf een eenvoudige main (event-loop) met onderstaand menu.

~~~
$ python festival.py
Beheer festival.
A> Groep boeken
B> Groep verwijderen
C> Boekingen bekijken
Q> Verlaten
 > 
~~~

#### Een groep boeken

Als je een groep boekt voer je 3 gegevens in:

* de naam
* het start-uur
* einde van het optreden.

Zorg naast deze 3 velden ook voor een integer als primary key (maak gebruik van autoincrement hiervoor).

> Nota: uren worden gewoon als integer ingevuld

Volgende sequentie geeft aan welke groepen er beschikbaar zijn.

~~~
Beheer festival.
A> Groep boeken
B> Groep verwijderen
C> Boekingen bekijken
Q> Verlaten
> A
Groep: Rolling Stones
Uur start: 15
Uur einde: 17

Beheer festival.
A> Groep boeken
B> Groep verwijderen
C> Boekingen bekijken
Q> Verlaten
> A
Groep: Beatles
Uur start: 17
Uur einde: 18
~~~

Belangrijke nota:

* Uren zijn van 0 tem 23, controleer dit en geef een foutboodschap
* Voer controles uit dat het start-uur niet na het eind-uur komt

#### Een overzicht geven

Zorg ervoor dat met optie C de boekingen kan zien:
Beheer festival.

~~~
A> Groep boeken
B> Groep verwijderen
C> Boekingen bekijken
Q> Verlaten
> C
1 - Rolling Stones van 15 tot 17 uur
2 - Beatles van 17 tot 18 uur
~~~

Print hier ook de primary key zoals hierboven geïllustreerd.

#### Contole op dubbele boekingen

Als laatste controleer dat je geen dubbele boeking verkrijgt voor een bepaald tijdstip...

~~~
Beheer festival.
A> Groep boeken
B> Groep verwijderen
C> Boekingen bekijken
Q> Verlaten
 > B
1 - Rolling Stones van 15 tot 17 uur
2 - Beatles van 17 tot 18 uur
Verwijder
> 1

A> Groep boeken
B> Groep verwijderen
C> Boekingen bekijken
Q> Verlaten
> A
Groep: U2
Uur start: 17
Uur einde: 19
Boeking kan niet toegestaan worden conflicteerd met "Beatles van 17 tot 18 uur"
~~~

### Database (4/20)

Bewaar deze gegevens in een database

### Onderscheiding: Verschillende podia (beslist over 19 of 20 punten)

Dit onderdeel is enkel ter ondscheiding.
Als je voor bovenstaande opdracht het maximum krijgt wordt dit gedeelte gebruikt ter onderscheiding
(19 of 20 punten op 20).

* Voorzie verschillende podia
	* Voorzie een aparte tabel (bijvoorbeeld stage)
	* Extra opties in het menu om podia aan te maken of te verwijderen
* Een groep kan over meerdere podia worden geboekt
	* De groep-tabel bevat geen start en einde meer
	* Deze bevinden zich op niveau van een nieuwe tabel (bijvoorbeeld boeking of stage_reservation)
	* Met een link naar de groep en podium
	* Je voorziet een aparte menu-entry om een podium te beheren
* Voorzie een rider per groep (lijst van goederen die een groep wenst)
	* Aparte tabel met telkens een beschrijving van het gewenste item op de rider