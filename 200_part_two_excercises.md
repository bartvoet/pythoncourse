## Oefeningen

### Oefening rond maanden

Deze oefening focust zich op het lezen uit een list.     
Het idee is dat we een aantal functies schrijven rond het aantal dagen in de maanden, dit op basis een list die voor elke maand het aantal dagen bevat.  

#### Functie "get_days_of_month" 

Voor deze oefening maak je een list (als globale variabele) aan  die het aantal dagen bevat per maand.
Deze lijst heeft een lengte 12, het 1ste element (0) bevat 31 (dagen Januari), het 2de element (1) 28 (dagen Februari), ...

> In volgorde => 31,28,31,30,31,30,31,31,30,31,30,31


Maak een functie **get_days_of_month** die aangeeft **hoeveel dagen** er **in een gegeven maand** zitten.  
Deze functie heeft als argument de maand waarvan je het aantal dagen wil eten en als return-waarde het aantal dagen.

Test deze functie uit door deze functie een aantal maal aan te roepen.

~~~python
print(get_days_of_month(1))  # prints 31
print(get_days_of_month(2))  # prints 28 
print(get_days_of_month(12)) # prints 31
~~~

> Hint: gebruik hiervoor de index van deze lijst om het aantal dagen op te vragen

#### Kijk na op ongeldige waardes

Bij een **ongeldige waarde** - **kleiner of gelijk aan 0 of groter dan 12** - zal de voorgaande functie de waarde **0 teruggeven**.

~~~python
print(get_days_of_month(-5))  #prints 0 because 0 <= 0
print(get_days_of_month(0))   #prints 0 because 0 <= 0
print(get_days_of_month(13))  #prints 0 because 13 > 12
~~~

Maakt gebruik van de functie "len" om het maximum maandaantal maanden te weten te komen

#### Functie "days_from_start_year"

Vul de zelfde python-file aan met een een volgende functie **days_from_start_year**.  
Deze telt uit **hoeveel dagen** er **verlopen** zijn **vanaf** de **start** van het **jaar** tot en met het einde van de betreffende maand.

~~~python
print(days_from_start_year(1))   # prints 31
print(days_from_start_year(2))   # prints 59
print(days_from_start_year(3))   # prints 90
print(days_from_start_year(12))  # prints 365 
~~~

Zorg er ook voor dat net zoals voorgaande functie nakijkt of je een **geldige input** hebt.  
Bij een ongeldige input geeft de functie 0 terug.

#### Functie "days_until_end_year"

Een gelijkaardige functie **days_until_end_year**, maar je rekent uit hoeveel dagen tot het einde van het jaar overblijven startende van een maand....

~~~python
print(days_until_end_year(1))   # prints 334
print(days_until_end_year(2))   # prints 306
print(days_until_end_year(12))  # prints 0
~~~

#### Functie "days_between_months"

Maak een functie **days_between_months** die uitrekent hoeveel dagen er zitten tussen het einde van de 1ste maand en het einde van de 2de maand.

~~~python
print(days_between_months(1,2))   # prints 28 
print(days_between_months(1,3))   # prints 59
~~~

Input validatie, geeft 0 terug als de 1ste maand groter is dan de 2de dan 0.
O is toegelaten, in het geval dat 0 het eerste argument reken je gewoon het aantal dagen vanaf het begin van het jaar (zoals days_from_start_year).

### Car management

Implementeer een python-programma dat voertuigen gaat beheren

~~~
$ python carmanagement.py 
Welkom, gelieve keuze te maken
1. Voertuig toevoegen
2. Voertuigen printen
3. Afsluiten
> 1
Geef merk: Lada
Geef kleur: Geel
Geef brandstof 1 voor Diesel, 2 voor Benzine: 1
Geef kw: 50
Welkom, gelieve keuze te maken
1. Voertuig toevoegen
2. Voertuigen printen
3. Afsluiten
1
Geef merk: Ferrari
Geef kleur: Rood
Geef brandstof 1 voor Diesel, 2 voor Benzine: 1
Geef kw: 500
Welkom, gelieve keuze te maken
1. Voertuig toevoegen
2. Voertuigen printen
3. Afsluiten
2
Lada, kleur = Geel, brandstof = Benzine, KW = 50
Ferrari, kleur = Rood, brandstof = Benzine, KW = 500
~~~