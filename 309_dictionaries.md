
## Werken met dictionaries

### Korte herhaling lijsten

#### Lijst is een verzameling

We hebben reeds kennis gemaakt met lijsten binnen Python.  

Deze liet ons toe verschillende dataelementen te verzamelen onder 1 variabele.  
In onderstaand voorbeeld verzamelen we bijvoorbeeld de punten van een 5-tal studenten

~~~python
punten = [20,15,16,17]
print(f'student {0} heeft {punten[0]} punten')
print(f'student {3} heeft {punten[3]} punten')
~~~

#### Een lijst is geindexeerd

De individuele elementen kan je bereiken via een **index** (in bovenstaand voorbeeld 0 en 3) met als resultaat:

~~~
student 0 heeft 20 punten
student 3 heeft 17 punten
~~~

Deze index kan variëren tussen **0** en **n-1** (waar n de dimensie is van deze lijst)

#### Een element updaten

Via deze index-operator kan je ook een element updaten...

~~~python
punten = [20,15,16,17]
punten[0]=18
print(f'student {0} heeft {punten[0]} punten')
~~~

met als resultaat

~~~
student 0 heeft 18 punten
~~~

#### Een element toevoegen

Toevoegen kan via de append-methode

~~~python
punten = [20,15,16,17]
print(punten)
punten.append(19)
print(punten)
~~~

met als resultaat

~~~
[18, 15, 16, 17]
[18, 15, 16, 17, 19]
~~~

#### for-loop

We konden ook gemakkelijk door een lijst "loopen" met een for-loop

~~~python
punten = [18, 15, 16, 17]
for punt in studenten:
  print(f'student heeft {punt} punten')
~~~

met als resultaat:

~~~
student heeft 18 punten
student heeft 15 punten
student heeft 16 punten
student heeft 17 punten
~~~

#### for-loop met enumerate

Dikwijls will je ook de index naast dev value...

~~~python
i = 0
for punt in punten:
  print(f'student {i} heeft {punt} punten')
  i = i + 0
~~~

met als resultaat

~~~
student 0 heeft 18 punten
student 1 heeft 15 punten
student 2 heeft 16 punten
student 3 heeft 17 punten
~~~

Gezien dit zeer veel gebruikt binnen programmeren heeft Python de enumerate-functie toegevoegd.  
Deze zorgt er voor dat je naast elk element ook nog de index kan opvragen.

~~~python
for i, punt in enumerate(punten):
  print(f'student {i} heeft {punt} punten')
~~~

> De toekenning van 2 variabelen noemt unpacking  
> We komen hier nog later toe binnen de cursus als we tuples bekijken.

### Dictionaries => key en value

Bij een lijst gebruikten de index als **sleutel** om een element op te vragen...  
In geval van studenten zou het bijvoorbeeld natuurlijker zijn de namen van de studenten te gebruiken om deze mapping uit te voeren (dan moet je de id's niet onthouden).  

Hiervoor bestaan **dictionaries** (equivalent in Java is de Map).  
Dit zijn - net zoals lijsten - **datastructuren** waar je **meerdere objecten of items** kan aan toevoegen.  

Het verschil echter is dat elke **waarde** die je toevoegt vergezeld moet zijn van een **sleutel**.  
Deze gebruik je dan nadien om deze waardes op te halen zoals gedemonstreerd in onderstaande code:

~~~python
student_points = {
  "Jan": 12,
  "Piet": 15,
  "Joris": 16,
  "Korneel": 18
}

print(student_points["Jan"])
print(student_points)
~~~

De dictionary hierboven (student_points) mapt de namen van de studenten aan punten, we spreken hier van **keys** (of sleutels) tov de **values** of waardes.

Bij uitvoering van de code zie je:

* Je kan de **waarde** **opvragen** van een entry door de **sleutel** te plaatsen **tussen** **vierkante haakjes**
* De volgende ouput print de volledige inhoud van de dictionarry af

~~~bash
$ python dictionary_demo.py
12
{'Jan': 12, 'Piet': 15, 'Joris': 16, 'Korneel': 18}
~~~

Zowel de keys als de values kunnen eender welk type zijn, er is **geen beperking van type**.  
In dit geval hebben we strings gebruikt als key maar dit kan ook een integer of zelfs een object zijn.

### Keys zijn uniek

Wat wel belangrijk is dat er **geen 2 verschillende entries** met dezelfde **key** kunnen zijn **binnen** een **dictionary**.  
Onderstaande code demonstreert dit:

~~~python
student_points = {
  "Jan": 12,
  "Piet": 15,
  "Joris": 16,
  "Korneel": 18,
  "Jan":14
}

print(student_points["Jan"])
print(student_points)
~~~

Jan is hier 2 maal gedefinieerd als sleutel.  
In onderstaande code zie je dat de **laatste** value (14) de **eerste** value zal **overschrijven** (12).

~~~bash
$ python dictionary_demo.py
14
{'Jan': 14, 'Piet': 15, 'Joris': 16, 'Korneel': 18}
~~~

### Waarde toevoegen aan een dictionary

Een student **toevoegen** aan deze **dictionary** kan ook, hieronder voegen we bijvoorbeeld een student met de sleutel (naam) "Bart" toe

~~~python
student_points = {
  "Jan": 12,
  "Piet": 15,
  "Joris": 16,
  "Korneel": 18
}

print(student_points["Jan"])
print(student_points)

student_points["Bart"] = 12
print(student_points["Bart"])
print(student_points)
~~~

Met als resultaat dat er een extra studenten-punt is **toegevoegd**.

~~~bash
$python3 dictionary_demo.py
12
{'Jan': 12, 'Piet': 15, 'Joris': 16, 'Korneel': 18}
12
{'Jan': 12, 'Piet': 15, 'Joris': 16, 'Korneel': 18, 'Bart': 12}
~~~

### Waarde updaten binnen een dictionary

Je kan naast het **toevoegen** ook dezelfde waarde **updaten**.

~~~python
student_points = {
  "Jan": 12,
  "Piet": 15,
  "Joris": 16,
  "Korneel": 18
}

print(student_points["Piet"])
student_points["Piet"] = 16
print(student_points["Piet"])
~~~

Hierbij gaat de **vorige waarde** vanzelfspekend **overschreven** worden...

~~~bash
$python3 dictionary_demo.py
15
16
~~~

### Waarde verwijderen van een dictionary

Naast **toevoegen** en **wijzigen** kan je zo'n key/value-pair ook **verwijderen**.  
Hier voor bestaat in Python het **keyword** **del**.

Stel dat we hieronder een student willen verwijderen kan dit als volgt:

~~~python
student_points = {
  "Jan": 12,
  "Piet": 15,
  "Joris": 16,
  "Korneel": 18
}
print ("Before: ", student_points)
del student_points["Piet"]
print ("After: ", student_points)
~~~

Na het verwijdern van de entry met de key Piet verdwijnt deze uit de dictionary

~~~bash
$ python3 dictionary_demo.py
Before:  {'Jan': 12, 'Piet': 15, 'Joris': 16, 'Korneel': 18}
After:  {'Jan': 12, 'Joris': 16, 'Korneel': 18}
~~~

### Wat als de key niet bestaat?

We hebben nu gezien hoe je een entry verwijdert...  
Wat als je een value opvraagt met een **onbestaande key** zoals hieronder?

~~~python
student_points = {
  "Jan": 12,
  "Piet": 15,
  "Joris": 16,
  "Korneel": 18
}

print(student_points["Hans"])
~~~

Zoals je ziet in de trace zal er in dit geval een error worden opgeworpen.  

~~~bash
$python3 dicationary_demo.py
Traceback (most recent call last):
  File "dicationary_demo.py", line 8, in <module>
    print(student_points["Hans"])
KeyError: 'Hans'
~~~

Python dictionaries vereisen dat je correcte sleutels doorgeeft, als je dit niet doet zal deze een error opgeven.  
Hoe kan je dit vermijden?

### Nakijken of een entry binnen de dictionary bestaat

Om zulke situaties te vermijden heb je 2 opties.  
Ofwel vang je deze error op via een **try-except-constructie**

~~~python
student_points = {
  "Jan": 12,
  "Piet": 15,
  "Joris": 16,
  "Korneel": 18
}

search_key = "Hans"

try:
    print(student_points["Hans"])
except KeyError:
    print(search_key + " bestaat niet")
~~~

...met als resultaat...

~~~bash
$python3 dicationary_demo.py
Hans bestaat niet
~~~

Ofwel **vermijd** je deze **error** door gebruik te maken van de **in-operator**

~~~python
student_points = {
  "Jan": 12,
  "Piet": 15,
  "Joris": 16,
  "Korneel": 18
}

search_key = "Hans"

if search_key in student_points:
    print(student_points["Hans"])
else:
    print(search_key + " bestaat niet")
~~~

...met hetzelfde resultaat...

~~~bash
$python3 dictionary_demo.py
Hans bestaat niet
~~~

Welke moet je nu gebruiken?  
De **in-operator** in dit geval is de **geprefereerde oplossing**, het is hier duidelijker wat de intentie is in het programma.  

Dit is een algemene regel in het werken met excepties trouwens, je probeert **eerder** te **voorkomen** dan te **genezen**.
Je probeert het gebruik van excepties te vermijden als er een manier bestaat om dit op voorhand na te kijken.  

Excepties dienen enkel gebruikt te worden als geen mogelijkheid hebt een "exeptionele situatie" op te vangen (ook hebben excepties in sommige gevallen ).
