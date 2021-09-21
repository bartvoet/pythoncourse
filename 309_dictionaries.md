
## Werken met dictionaries

### Index binnen een lijst

Ter herhaling, met een **lijst** konden **meerdere items** of objecten **groeperen** in **1 variabele**.  
Het voorbeeld hieronder houdt men de **studenten-punten** bij in een **lijst**.

~~~~python
student_points = [12,15,16,18]

def print_points(student_id):
    print("Student", student_id , "has" ,  student_points[student_id], "points" )

print_points(1) #prints 12
print_points(3) #prints 18
~~~~

### Dictionaries => key en value

In dit geval is de **sleutel** hier de **index** van deze lijst, maar wat als je bijvoorbeeld **namen** wil **mappen** aan deze **punten**, dat zou het gemakkelijker maken om met te werken (dan moet je de id's niet onthouden).  

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

### Waarde update aan een dictionary

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

### Nakijken of een dictionary bestaat

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
