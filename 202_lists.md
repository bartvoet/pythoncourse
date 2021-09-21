## Lists

### Collecties

Tot nog toe hebben we enkelvoudige types gewerkt (ook wel primitieve genoemd), variabelen van dit type bevatten 1 waarde 

In het 2de deel van de cursus bekijken we datatypes die meerdere waardes kunnen bevatten:

* Collecties: Lists, Dictionaries, Tuples en 
* Abstracte datatypes en concepten: klasses, modules, ...

Collecties zijn generieke datatypes waarin je meer dan 1 waarde in kan plaatsen, een beetje zoals een container die verschillende goederen kan bevatten.


### List

I
Het eerste, en meest éénvoudige type is de List (lijst).

> *Nota:*  
>In de meeste programmeertalen starten met het concept van een array als we over collecties spreken.  
>Dit bestaat echter niet in Python, we komen hier later nog op terug in de cursus Embedded Programmeren 

Praktisch uitgedrukt een list in python is:

* Een **verzameling** of collectie van elementen 
* Elk **element** van zo'n array kan **gelezen of gewijzigd** via een **index**
* Een list heeft een **grootte of dimensie** (die we voor de gemakkelijkheid aanduiden als n)
* Deze grootte of dimensie kan wijzigen over de duurtijd van een programma
* Deze index **start** bij **0** (1ste element) en **eindigt** bij de index **n-1***

### Voorbeeld Lijst

Een lijst kan je aanmaken als een gewone variabele met onderstaande syntax.
Dit doe je door een List-literal aan te maken:

* Een variabele
* Een lijst van waardes
    * Omsloten door vierkante haakjes []
    * De waardes gescheiden komma's

~~~python
x = [1.0, 2.0, 3.0]
y = ["a","list","of","strings"]
z = ["a",1,"mixed",3.0,"list"]
~~~

### Waardes van een lijst

Deze lijst kan alle soorten data-elementen bevatten.  
In de meeste gevallen ga je hetzelfde type gebruiken, maar dit is niet verplicht (zie z in het voorbeeld)

Je kan zelf een lijst van lijsten maken...

~~~python
x = [[1.0, 2.0, 3.0],["a",1,"mixed",3.0,"list"]]
~~~

### Dimensie van de lijst

Een eeste actie die we kunnen uitvoeren is de grootte of dimensie van deze lijst opvragen.  
Daarvoor bestaat een generieke (niet alleen voor lists) functie len()z

~~~python
x = [1.0, 2.0, 3.0]
y = ["a","list","of","strings"]
z = []
print(len(x)) # prints 3
print(len(y)) # prints 4
print(len(z)) # prints 0
~~~

### Lege lijst

Ook een lege lijst is dus mogelijk ...

~~~python
x = []
len(x) # prints 0
~~~

dat is dan gewoon een lijst met lengte

### Data uit een lijst halen (index)

Om met zo'n lijst te kunnen werken moet je er data kunnen uithalen.  
Om data uit een lijst te kunnen aanspreken werken we met het concept van **indexering**

Met **index** bedoelen we de **positie** van het **element binnen** deze **list**.  

~~~python
x = [1.0, 2.0, 3.0]
y = ["a","list","of","strings"]
print(x[0])
print(y[1])
~~~

Door de **naam** van de **list-variabele** te combineren met een **index** die je tussen vierkante haken plaats kan je de waarde uit deze positie ophalen en gebruiken in je code.

### Alles begint bij 0

... en **eindigt bij n-1**

~~~python
x = [1, 2, 3]
print(x[0])   # prints 1
print(x[1])   # prints 2
print(x[2])   # prints 3
print(len(x)) # prints 3
~~~

De **index** van het **eerste element** uit een lijst is **niet 1** (zou logisch kunnen zijn) maar is O

~~~
 """            -----------------
 We starten     | 0 | 1 | 2 | 3 | """
 bij O          -----------------   En eindigen bij 2
       """      | 1 | 2 | 3 | / |   Index 22 bestaat niet
                -----------------                      """
~~~

De index van het **laatste element** is n-1, of in dit geval 2 (lengte 3 - 1)


### Indexering vs range

Stel dat je toch een index adresseert > n -1 zal Python een error genereren.

Volgende code ...

~~~python
x = [1, 2, 3]
print(x[3])   # raises IndexError
~~~

... genereert een IndexError

~~~
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: list index out of range
~~~

### Data in een lijst wijzigen (index) 

Een element van een lijst kan je wijzigen op een vergelijkbare manier.  
Je gebruikt opnieuw het zelfde indexerings-mechanisme, maar past deze toe in een **assignment-statement**

~~~python
x = [1.0, 2.0, 3.0]
print(x[1]) # prints 2.0
x[2]=10
print(x[2]) # prints 10
~~~

### Negatieve indexen

In Python kan je ook negatieve indexen gebruiken, hierbij draai je de indexering gewoon om...  
Het idee is dat je van de dimensie of lengte aftrekt...

~~~python
x = [0,1,2,3,4,5,6,7,8,9]
print(x[-1]) # prints 9 => position/index 10 - 1 = 9
print(x[-3]) # prints 7 => position/index 10 - 3 = 7
~~~

~~~bash
$ python test.python
9
7
~~~


### Lijsten doorlopen (try 0...)

Gezien we:

* De lengte van een lijst kunnen opvragen
* De individuele elementen kunnen opvragen

kunnen we ook een lijst doorlopen 

~~~python
x = [0,1,2,3,4,5,6,7,8,9]
i = 0
while i < len(x):
    print(x[i])
    i = i + 1
~~~

Deze code werkt maar is echter niet echt "Pythonic"

~~~
0
1
2
3
4
5
6
7
8
9
~~~

### Lijsten doorlopen (retry...)

Je kan namelijk ook de for-loop gebruiken, die we eerder gebruikten in combinatie met range

~~~python
x = [0,1,2,3,4,5,6,7,8,9]
for n in x:
    print(n)
~~~

#### Selecteren met "slices"

Je kan ook een stuk nemen uit zo'n list, dit noemt met slicing.

~~~python
x = [0,1,2,3,4,5,6,7,8,9]
for n in x[2:4]:
    print(n)
~~~

De eerste index is de start-index, let wel de 2de index is niet inclusief!!!

~~~bash
$ python test.python
2
3
~~~

#### Slicing met negatieve indexen

Je kan hier ook negatieve indexen gebruiken:

~~~python
x = [0,1,2,3,4,5,6,7,8,9]
for n in x[2:-2]:
    print(n)
~~~


~~~bash
$ python test.python
2
3
4
5
6
7
~~~

### Bewerken van een List 

Een lijst kan je ook nog vergroten éénmaal gecreeerd:

* append(): element toevoegen aan einde van de lijst
* extend(): zelfde maar een ineens een andere lijst of iterable toevoegen 
* count(): aantal elementen met een bepaalde waarde  
* index():	index van het eerste element voor een specifieke waarde
* insert(): element toevoegen op een bepaalde positie
* pop() : verwijderen van element op een inde
* remove() : eerste item met een bepaalde waarde verwijderen   Removes the first item with the specified value
* reverse() : inverteren van volgorde items/elementen
* sort() : sorteren van de lijst

Zie volgende sequentie in de console

~~~python
>>> car_park = ["Lada","Skoda","Lambo"]
>>> print(car_park)
['Lada', 'Skoda', 'Lambo']
>>> print(len(car_park))
3
>>> car_park.append("Ferrari")
>>> print(car_park)
['Lada', 'Skoda', 'Lambo', 'Ferrari']
>>> car_park.remove("Lambo")
>>> print(car_park)
['Lada', 'Skoda', 'Ferrari']
>>> car_park.pop(1)
'Skoda'
>>> print(car_park)
['Lada', 'Ferrari']
>>> car_park.insert(1,"Volvo")
>>> print(car_park)
['Lada', 'Volvo', 'Ferrari']
>>> car_park.reverse()
>>> print(car_park)
['Ferrari', 'Volvo', 'Lada']
>>> car_park.sort()
>>> print(car_park)
['Ferrari', 'Lada', 'Volvo']
>>> del car_park[:]
>>> print(car_park)
[]
>>>
~~~

