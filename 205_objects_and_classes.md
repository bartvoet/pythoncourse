## Objecten en klasen

Tot nog toe hebben we - lijsten buiten beschouwing genomen -  enkel gewerkt met data-types die één enkele waarde kunnen bevatten zoals oa int, float, boolean, ...

> Nota: String was een uitzondering bij deze gezien die eigenlijk een lijst is van karakters....

In dit deel bekijken we klassen in python, die het ons toelaten data te structuren in 1 data-type

### Voorbeeld: studenten-applicatie

Stel, je wil een een applicatie bouwen die de punten voor een vak wil bijhouden, zoals in de onderstaande tabel-voorstelling.

~~~
    +---------+------------+--------+-----------+
    | Naam    |  Voornaam  |  Labo  |  Theorie  |
+---+---------+------------+--------+-----------+
| 1 | Jan     |  Janssens  |  15    |   16      |
+---+---------+------------+--------+-----------+
| 2 | Piet    |  Pieters   |  15    |   16      |
+---+---------+------------+--------+-----------+
| 3 | Joris   |  Jorissen  |  15    |   16      |
+---+---------+------------+--------+-----------+
| 3 | Korneel |  Korneels  |  15    |   16      |
+---+---------+------------+--------+-----------+
~~~


### Verschillende studenten => Lijst

We weten ondertussen hoe we meerdere elementen van hetzelfde type moeten bijhouden in een Python-programma, namelijk aan de hand van een lijst.

Zo zou je elke student als een apart element in de lijst kunnen bijhouden zoals in onderstaand voorbeeld...  

~~~python
student_list = ["Jan","Piet","Joris","Korneel"]
~~~

### Groeperen van data

Probleem daarbij is dat we enkel 1 van die elementen (in dit geval de naam van de studenten) in de lijst kunnen bijhouden.  
Is er een manier om alle student-data gestructureerd bij elkaar te houden? 

### Gestructureerd programmeren met klassen

In Python kan je dit met klassen.    
Een klasse is een **gestructureerd data-type** dat je toelaat verschillende waardes (of subvariabelen) te **groeperen** onder 1 enkel **object**.  

### Klasse student

Laten we direct van wel steken met ons voorgaande voorbeeld uit te breiden.  
Toegepast op een student ziet zo'n data-type er als volgt uit, je start telkens met:

* Het keyword **class**
* Gevolgd door een **naam** voor dit type   
  (Student in dit geval)
* Gevolgd door een block-indicator **:**

~~~python
class Student:
    name = ""
    lab_points = 0
    theory_points = 0
~~~

Daarna kan je dit laten volgen door 1 of meerdere **attributen**  in dit geval is dit:

* name
* lab_points
* theory_points

Deze attributen zijn **sub-variabelen** die **verbonden** zijn aan een instantie van een **class**.

> Nota: later gaan we zien dat we - naast attributen - ook functies kunnen aanhechten aan een class-type

### Aanmaken van een object

Als je een variabele aanmaakt van zo'n type noemen we dit een **object**.  
Onderstaande code:

* Definieert zo'n type
* Instantieert een object van dit type

~~~python
class Student:
    name = ""
    lab_points = 0
    theory_points = 0

jan = Student()
~~~

Een **object** wordt aangemaakt door een speciale functie (Student()), genaamd de **constructor**. 

### Constructor

Deze **constructor**:

* is een **functie**
* die **automatisch** wordt **aangemaakt**  
  (als je deze zelf niet maakt, zien direct)
* met **dezelfde naam** heeft als de **klasse**
* die je **aanroept** om een **object** (of instantie) van de klasse aan te maken

Zo direct gaan we ook zien dat deze constructor kunnen aanpassen, maar laten we eerst iets doen met het object.

### Werken met attributen

Een object bestaat uit attributen (name, lab_points, theory_points), zoals deze in de klasse werden beschreven.  
Onderstaand voorbeeld illustreert hoe je deze attributen gebruikt.

~~~python
class Student:
    name = ""
    lab_points = 0
    theory_points = 0

jan = Student()
jan.name = "Jan Janssens"
jan.lab_points = 15
jan.theory_points = 17

print(jan.lab_points)     # prints Jan Janssens
print(jan.lab_points)     # prints 15
print(jan.theory_points)  # prints 17
~~~

Je kan dez variabelen via de dot-notatie - object-naam gevolgd door punt gevolgd door naam -  uitlezen en bewerken, net zoals je dit zou doen bij een gewone variabelen.

### Meerdere objecten

Vanzelfsprekend kan je dan meerdere objecten toevoegen

~~~python
class Student:
    name = ""
    lab_points = 0
    theory_points = 0

jan = Student()
jan.name = "Jan Janssens"
jan.lab_points = 15
jan.theory_points = 17

print(jan.lab_points)
print(jan.lab_points)
print(jan.theory_points)

piet = Student()
piet.name = "Piet Pieters"
piet.lab_points = 15
piet.theory_points = 17

print(piet.lab_points)
print(piet.lab_points)
print(piet.theory_points)
~~~

In dit voorbeeld kan je duidelijk zien dat de attributen verbonden zijn aan het object.  
jan.lab_points is niet het zelfde piet.lab_points

### Meerdere objecten in een lijst

Laten we het principe van classes combineren met lists.   
Dit stelt je in staat een dynamische collectie van studenten bij te houden.

~~~python
class Student:
    name = ""
    lab_points = 0
    theory_points = 0

students = []

jan = Student()
jan.name = "Jan Janssens"
jan.lab_points = 15
jan.theory_points = 17
students.append(jan)


piet = Student()
piet.name = "Piet Pieters"
piet.lab_points = 15
piet.theory_points = 17
students.append(piet)

for student in students:
    print(student.lab_points)
    print(student.theory_points) 
~~~
### Constructor met argumenten

De constructor-functie kan je uitbreiden met argumenten.  
Deze argumenten kan je gebruiken om de attributen te initialiseren

~~~python
class Student:
    def __init__(self, name, lab, theory):
        self.name = name
        self.lab_points = lab
        self.theory_points = theory

students = []

jan = Student("Jan Janssens",15,17)
students.append(jan)
piet = Student("Piet Pieters",15,17)
students.append(piet)

for student in students:
    print(student.name + ":")
    print(student.lab_points)
    print(student.theory_points) 
~~~

Let ook dat niet meer nodig is de attributen te definieren, het is voldoende deze te koppelen aan self.  
**self** is een alias/verwijzing naar de huidige instantie van deze class (Student) en is altijd verplicht als het 1ste argument bij eender welke **object-methode**.
### Constructor (2)

Gezien je een lijst bijhoudt is het niet meer nodig aparte variabelen bij te houden.  
Je kan via de constructor direct de student-objecten/instanties toevoegen aan de lijst.

~~~python
class Student:
    def __init__(self,name,lab,theory):
        self.name = name
        self.lab_points = lab
        self.theory_points = theory

students = []

students.append(Student("Jan Janssens",15,17))
students.append(Student("Piet Pieters",15,17))

for student in students:
    print(student.name + ":")
    print(student.lab_points)
    print(student.theory_points) 
~~~

### Constructor (3)

We kunnen hier ook nog default-argumenten aan toekennen...

~~~python
class Student:
    def __init__(self,name,lab=0,theory=0):
        self.name = name
        self.lab_points = lab
        self.theory_points = theory

students = []

students.append(Student("Jan Janssens",15,17))
students.append(Student("Piet Pieters",15,17))
students.append(Student("Student zonder theori",15))

for student in students:
    print(student.name + ":")
    print(student.lab_points)
    print(student.theory_points) ) 
~~~

### Classes en Methodes

Naast attributen kan je ook methodes toevoegen.  
Dit zijn functies die gekoppeld worden aan een instantie van een object, de constructor was een eerste speciaal voorbeeld.  

In onderstaand voorbeeld voegen we een methode toe die de uiteindelijke punten berekent van de studenten.

~~~python
class Student:
    def __init__(self,name,lab=0,theory=0):
        self.name = name
        self.lab_points = lab
        self.theory_points = theory

    def points(self):
        return (self.lab_points + self.theory_points)/2

students = []

students.append(Student("Jan Janssens",15,17))
students.append(Student("Piet Pieters",15,17))

for student in students:
    print(student.name + ":")
    print(student.lab_points)
    print(student.theory_points) 
    print(student.points())
~~~

### __str__

Een andere speciale methode (eerder hadden we al reeds de constructor gezien) is de string-methode.  
Als je de methode __str__ toevoegt zal deze automatisch worden aangeroepen als je een naar een string wil converteren:

* Door de str()-operator te gebruiken
* Door het object mee te geven aan de print-functie (die op zijn beurt str() aanroept)

~~~python
class Student:
    def __init__(self,name,lab=0,theory=0):
        self.name = name
        self.lab_points = lab
        self.theory_points = 0

    def points(self):
        return (self.lab_points + self.theory_points)/2

    def succeeded(self):
        return points(self) >= 10    
        
    def __str__(self):
        return "Student {} has {} for lab and {} for theory, so average of {}".format(
            self.name, self.lab_points,self.theory_points,self.points())

students = []

students.append(Student("Jan Janssens",15,17))
students.append(Student("Piet Pieters",15,17))

for student in students:
    print(student)
    # of alternatief print(str(student))
~~~

Geeft volgend resultaat:

~~~
Student Jan Janssens has 15 for lab and 0 for theory, so average of 7
Student Piet Pieters has 15 for lab and 0 for theory, so average of 7
~~~