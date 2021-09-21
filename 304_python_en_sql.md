## Databases met Python

We hebben nu een eerste basis-introductie gehad in 

* Principe van een **database** en SQL
* **Toegepast** op een SQL-datbase, in dit geval de embedded database **Sqlite**
* Het **aanmaken** van zo'n **database** en **creatie** van **tabellen**
* Het **ondervragen** en **aanvullen** van data via **CRUD-statements**

### Voorbereiding 1: Hernemen van studenten-applicatie

Als voorbeeld We hernemen we de applicatie die we eerder in de cursus hebben gemaakt rond studenten.  

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
~~~

Deze applicatie laat ons toe studenten-gegevens in een lijst op te slagen en deze te hergebruiken.

~~~
Student Jan Janssens has 15 for lab and 0 for theory, so average of 7.5
Student Piet Pieters has 15 for lab and 0 for theory, so average of 7.5
~~~

### Voorbereiding 2: Interactiviteit toevoegen

We breiden deze ook uit door er wat **interactiviteit** aan toe te voegen door middel van een **éénvoudig menu**...

~~~python
class Student:
    def __init__(self,name,lab=0,theory=0):
        self.name = name
        self.lab_points = lab
        self.theory_points = theory

    def points(self):
        return (self.lab_points + self.theory_points) // 2

    def succeeded(self):
        return points(self) >= 10    
        
    def __str__(self):
        return "Student {} has {} for lab and {} for theory, so average of {}".format(
            self.name, self.lab_points,self.theory_points,self.points())

students = []

def input_number(request):
    number_input = input(request)
    return int(number_input)   

menu = """
1. Voeg student toe
2. Toon studenten
3. Stop applicatie
"""
while True:

    menu_input = input(menu)
    
    if menu_input == "1":
        student_name = input("Naam student(e): ")
        lab_points = input_number("Labo-punten: ")
        theory_points = input_number("Theorie-punten: ")
        students.append(Student(student_name,lab=lab_points,theory=theory_points))
    elif menu_input == "2":
        for student in students:
            print(student)
    elif menu_input == "3":
        print("")
        quit()
    else:
        print("ongekende input")
~~~

Hiermee kan je deze dan vanuit een éénvoudige command-line-interface **bewerken**

~~~
python3 students.py 

1. Voeg student toe
2. Toon studenten
3. Stop applicatie
1
Naam student(e): Jan Jannssens
Labo-punten: 15
Theorie-punten: 12

1. Voeg student toe
2. Toon studenten
3. Stop applicatie
1
Naam student(e): Bart Voet
Labo-punten: 15
Theorie-punten: 16

1. Voeg student toe
2. Toon studenten
3. Stop applicatie
2
Student Jan Jannssens has 15 for lab and 12 for theory, so average of 13
Student Bart Voet has 15 for lab and 16 for theory, so average of 15

1. Voeg student toe
2. Toon studenten
3. Stop applicatie
~~~

Groot nadeel is natuurlijk dat - **éénmaal** deze **afgesloten** - je **niet meer** aan de **data** kan geraken.  
Hiervoor gaan we deze **code omvormen** om de data in een database bij te houden.

### sqlite in python - basis

De sql-commando's die we eerder hebben gezien, kan je vanuit een api doorsturen naar een database.

~~~
+---------------+---+---------+----------------+
|               |   |         |                |
|               |   +-------->|                |
|               | A |   SQL   |                |
|  Applicatie   | P |         |  Database      |
|               | I |   DATA  |                |
|               |   |<--------+                |
|               |   |         |                |
+---------------+---+---------+----------------+
~~~

ipv een sql-editor te gebruiken kan je dus **vanuit je python code met sql praten**...

> Nota: Gedetailleerde documentatie rond het gebruik hiervan vind je te https://docs.python.org/3/library/sqlite3.html maar we proberen de basis-principes te hernemen.


#### Connectie maken met een database

De eerste stap die je dient te doen is een **connectie-object** aan te maken.  
Dit doe je met de volgende code:

~~~python
import sqlite3
con = sqlite3.connect('student.db')
cur = con.cursor()
# ...code to interrogate the database
con.close()
~~~

Dit gaat aan een database connecteren die zich in dezelfde folder bevindt als vanwaar je code uitvoert.  
Als deze nog niet bestaat zal de library een lege database aanmaken.

Wel belangrijk is het om de database vrij te geven voor gebruik via de **close()-functie**!!!!

#### Automatisch sluiten met with

Een **good practice** wanneer je werkt met connectie-georienteerde objecten zoals files, database- of netwerk-connecties is gebruik maken van het **with-keyword**  (binnen Python maar gelijkaardig bestaat ook in andere talen).

Het probleem met voorgaande code is dat als je er een error of exceptie wordt gegenereerd de close()-functie niet aangeroepen.  
Om dit te vermijden kan je - zoals we eerder bij het het openen van een file hebben gezien - with kunnen gebruiken als volgt:

~~~python
import sqlite3
with sqlite3.connect('student.db') as con:
    cur = con.cursor()
    # ...other code to interrogate the database
~~~

Na het uitvoeren van deze with-block zal de **close()-functie** op het connectie-object automatisch worden aangeroepen en wordt dus de connectie en zijn resources automatisch gesloten.

Meer gedetailleerde informatie hieromtrent kan je vinden te https://www.python.org/dev/peps/pep-0343/.  
De essentie is als je een klasse (in bijvoorbeeld een sql-library) aanmaakt die 2 functies implementeerd je deze met een with-statement kan gebruiken.

~~~python
class SomeConnection:

    def __enter__(self):
        # called before running the with-block
        # 
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        # make sure the dbconnection gets closed
~~~


#### Uitvoeren van een query

Voortgaande op bovenstaande code kan je een cursor-object aanmaken.  
Dit object kan je dan gebruiken om queries uit te voeren via de functie execute() 

~~~python
with sqlite3.connect('student.db') as con:
    cur = con.cursor()
    query_result = cur.execute('SELECT student_id, name, lab, theory FROM student')
~~~

Het resultaat van dit - een lijst van records - wordt voor de python-code ter beschikking gesteld als een iterator.

~~~python
    for row in query_result:
        print(Student(row[1],"met id",row[0]))
~~~

#### Gebruik van parameter-substution

Eerder hadden we gezien dat we binnen een where-clausule condities konnen bepalen om een filtering/selectie toe te passen.  
Hiervoor voorziet de api de mogelijkheid van substutie, stel dat je enkel studenten wil query-en die meer dan 10 punten hebben kan je dit als volgt doen.

~~~python
query_result = cur.execute('SELECT student_id, name, lab, theory FROM student where lab > ?', [10])

for row in query_result:
    print(Student(row[1],"met id",row[0]))

con.close()
~~~

De conventie is dat je op de plek waar je een parameter wil toevoegen een vraagteken plaatst, en de parameter als opeenvolgende paramzeter opgeeft van de execute-functie.  
Niets weerhoud je ervan van meerdere parameters toe te voegen/combineren

~~~python
query_result = cur.execute('SELECT student_id, name, lab, theory FROM student where lab > ? and theory > ?', [10,12])

for row in query_result:
    print(Student(row[1],"met id",row[0]))

con.close()
~~~

### Oefening 2: Persisteren van studenten-applicatie

Onderstaande code is een toepassing van bovenstaande uitleg rond het gebruik van een connectie en cursor binnen Python.  
Onder deze code overlopen we elke wijziging...

~~~python
import sqlite3 as sl

class Student:
    def __init__(self,name,lab=0,theory=0,id=0):
        self.name = name
        self.lab_points = lab
        self.theory_points = theory

    def points(self):
        return (self.lab_points + self.theory_points) // 2

    def succeeded(self):
        return points(self) >= 10    
        
    def __str__(self):
        return "Student {} has {} for lab and {} for theory, so average of {}".format(
            self.name, self.lab_points,self.theory_points,self.points())

STUDENT_DB_FILE_NAME = "students.db"

def init_database():
    con = sl.connect(STUDENT_DB_FILE_NAME)
    with con:
        con.execute("""
            CREATE TABLE IF NOT EXISTS student (
                student_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                lab INTEGER,
                theory INTEGER
            );
        """)

def get_students():
    with sl.connect(STUDENT_DB_FILE_NAME) as con:
        query_result = con.execute('SELECT student_id, name, lab, theory FROM student')
        students = []
        for row in query_result:
            students.append(Student(row[1],row[2],row[3],row[0]))
    return students

def save_new_student(student):
    with sl.connect(STUDENT_DB_FILE_NAME) as con:
        cur = con.cursor()
        cur.execute('insert into student(name, lab, theory) values(?,?,?)', [student.name,student.lab_points,student.theory_points])
        con.commit()

def input_number(request):
    number_input = input(request)
    return int(number_input)   

menu = """
1. Voeg student toe
2. Toon studenten
3. Stop applicatie
"""

init_database()

while True:
    menu_input = input(menu)

    if menu_input == "1":
        student_name = input("Naam student(e): ")
        lab_points = input_number("Labo-punten: ")
        theory_points = input_number("Theorie-punten: ")
        save_new_student(Student(student_name,lab=lab_points,theory=theory_points))
    elif menu_input == "2":
        for student in get_students():
            print(student)
    elif menu_input == "3":
        print("")
        quit()
    else:
        print("ongekende input")
~~~

#### Toevoegen van de sqlite-library

~~~python
import sqlite3 as sl
~~~


#### Inialiseren van de database

We maken de database aan bij opstarten van de applicatie.  
Het keyword "if not exists" zorgt ervoor dat de create niet opnieuw wordt aangemaakt als deze reeds bestaat.

~~~python
STUDENT_DB_FILE_NAME = "students.db"

def init_database():
    con = sl.connect(STUDENT_DB_FILE_NAME)
    with con:
        con.execute("""
            CREATE TABLE IF NOT EXISTS student (
                student_id INTEGER PRIMARY KEY,
                name TEXT,
                lab INTEGER,
                theory INTEGER
            );
        """)
~~~

We voegen deze initialisatie toe bij het opstarten van de applicatie

~~~python
menu = """
1. Voeg student toe
2. Toon studenten
3. Stop applicatie
"""

init_database()

while True:
~~~

#### Ophalen van studenten-data

We maken een fucntie die het **resultaat** van een **query** gaat omzetten naar een **object**

~~~python
def get_students():
    with sl.connect(STUDENT_DB_FILE_NAME) as con:
        query_result = con.execute('SELECT student_id, name, lab, theory FROM student')
        students = []
        for row in query_result:
            students.append(Student(row[1],row[2],row[3],row[0]))
    return students
~~~

En **roepen** dit **aan** bij optie **2**

~~~python
    elif menu_input == "2":
        for student in get_students():
            print(student)
~~~

#### Aanmaken van een student

Een nieuwe student aanmaken doe we via een functie **save_new_student** (met als argument een Student-object)

Deze functie neemt als **argument** een object (van de klasse student) schrijft deze naar de database weg

~~~python
def save_new_student(student):
    with sl.connect(STUDENT_DB_FILE_NAME) as con:
        cur = con.cursor()
        cur.execute('insert into student(name, lab, theory) values(?,?,?)', [student.name,student.lab_points,student.theory_points])
        con.commit()
~~~

Deze wordt dan **aangeroepen** vanuit **optie 1**:

~~~python
    if menu_input == "1":
        student_name = input("Naam student(e): ")
        lab_points = input_number("Labo-punten: ")
        theory_points = input_number("Theorie-punten: ")
        save_new_student(Student(student_name,lab=lab_points,theory=theory_points))
~~~

### Oefening 2: updaten en verwijderen

We kunnen studenten toevoegen en bekijken, we voegen nu 3 functies toe:

* Update van de punten van een student
* Verwijderen van een student
* Een student individueel opzoeken

~~~python
import sqlite3 as sl

class Student:
    def __init__(self,name,lab=0,theory=0,id=0):
        self.name = name
        self.lab_points = lab
        self.theory_points = theory
        self.student_id=id

    def points(self):
        return (self.lab_points + self.theory_points) // 2

    def succeeded(self):
        return self.points() >= 10    
        
    def __str__(self):
        return "Student {} - {} has {} for lab and {} for theory, so average of {}".format(
            self.student_id, self.name, self.lab_points,self.theory_points,self.points())

students = []

STUDENT_DB_FILE_NAME = "students.db"

def init_database():
    with sl.connect(STUDENT_DB_FILE_NAME) as con:
        con.execute("""
            create table if not exists student_group
            (
                group_name text primary key,
                teacher text,
                room text
            );
        """)

def get_students():
    with sl.connect(STUDENT_DB_FILE_NAME) as con:
        query_result = con.execute('SELECT student_id, name, lab, theory FROM student')
        students = []
        for row in query_result:
            students.append(Student(row[1],row[2],row[3],row[0]))
    return students

def save_new_student(student):
    with sl.connect(STUDENT_DB_FILE_NAME) as con:
        cur = con.cursor()
        cur.execute('insert into student(name, lab, theory) values(?,?,?)', [student.name,student.lab_points,student.theory_points])
        con.commit()

def get_student(id):
    with sl.connect(STUDENT_DB_FILE_NAME) as con:
        query_result = con.execute('select student_id, name, lab, theory FROM student where student_id = ?',str(id))
        row = query_result.fetchone()
    return Student(row[1],row[2],row[3],row[0])

def update_points(id,lab,theory):
    with sl.connect(STUDENT_DB_FILE_NAME) as con:
        update_tatement = 'update student SET lab = ? , theory = ? WHERE student_id = ?'
        con.execute(update_tatement, [lab,theory,id])
        con.commit()

def delete_student(id):
    with sl.connect(STUDENT_DB_FILE_NAME) as con:
        con.execute("delete from student where student_id = ?", [id])
        con.commit()

def input_number(request):
    number_input = input(request)
    return int(number_input)   

menu = """
1. Voeg student toe
2. Toon studenten
3. Toon student
4. Update van punten student
5. Verwijderen van een student
6. Stop applicatie
"""

init_database()

while True:
    menu_input = input(menu)

    if menu_input == "1":
        student_name = input("Naam student(e): ")
        lab_points = input_number("Labo-punten: ")
        theory_points = input_number("Theorie-punten: ")
        save_new_student(Student(student_name,lab=lab_points,theory=theory_points))
    elif menu_input == "2":
        for student in get_students():
            print(student)
    elif menu_input == "3":
        id = input_number("> ")
        student = get_student(id)
        print(student)
    elif menu_input == "4":
        print("Kies student op id")
        for student in get_students():
            print("Student met id",student.student_id,"en naam",student.name)
        id = input_number("> ")
        lab = input_number("Labo-punten:")
        theory = input_number("Theorie-punten:")
        update_points(id,lab,theory)
    elif menu_input == "5":
        print("Verwijder student op id")
        for student in get_students():
            print("Student met id",student.student_id,"en naam",student.name)
        id = input_number("> ")
        delete_student(id)
    elif menu_input == "6":
        print("De applicatie wordt afgesloten")
        quit()
    else:
        print("ongekende input")

~~~

#### Een student individueel opzoeken

Om enkel 1 student te consulteren voegen we een optie 3 toe.  
Binnen get_student() voeren we de code uit om 1 enkele student op te halen

~~~python
    elif menu_input == "3":
        id = input_number("> ")
        student = get_student(id)
        print(student)
~~~

Het belangrijkste verschil met voorgaande code is dat we hier **enkel 1 rij** verwachten van de database.  
Hier hebben we dus geen **iterable** nodig maar slecht 1 rij, de sqlite-api laat dit toe via de functie **fetchone()**.  
ipv dat we dan het resultaat-object itereren met een loop bekomen we dan de enige rij via deze functie

~~~python
def get_student(id):
    with sl.connect(STUDENT_DB_FILE_NAME) as con:
        query_result = con.execute('select student_id, name, lab, theory FROM student where student_id = ?',str(id))
        row = query_result.fetchone()
    return Student(row[1],row[2],row[3],row[0])
~~~

#### Update van de punten van een student

Om een **update-query** te **demonstreren** voegen we een optie die de punten van de student gaat aanpassen

~~~python
    elif menu_input == "4":
        print("Kies student op id")
        for student in get_students():
            print("Student met id",student.student_id,"en naam",student.name)
        id = input_number("> ")
        lab = input_number("Labo-punten:")
        theory = input_number("Theorie-punten:")
        update_points(id,lab,theory)
~~~

De update-query is **gelijkaardig** aan de voorgaande **insert** met het **verschil** dat je hier een **where-clausule** nodig hebt om de student-id mee te geven.

~~~python
def update_points(id,lab,theory):
    with sl.connect(STUDENT_DB_FILE_NAME) as con:
        update_tatement = 'update student SET lab = ? , theory = ? WHERE student_id = ?'
        con.execute(update_tatement, [lab,theory,id])
        con.commit()
~~~

#### Verwijderen van een student

De laaste toevoeging is als je een student wil verwijderen:

~~~sql
    elif menu_input == "5":
        print("Verwijder student op id")
        for student in get_students():
            print("Student met id",student.student_id,"en naam",student.name)
        id = input_number("> ")
        delete_student(id)
~~~

In dit geval:

~~~python
def delete_student(id):
    with sl.connect(STUDENT_DB_FILE_NAME) as con:
        con.execute("delete from student where student_id = ?", [id])
        con.commit()
~~~

### Oefening 3: Werken met meerdere groepen

In het voorgaande deel - waar we sql introduceerde - hebben gezien dat we ook met meerdere tabellen konden werken.

~~~python
import sqlite3 as sl

class Student:
    def __init__(self,name,lab=0,theory=0,id=0):
        self.name = name
        self.lab_points = lab
        self.theory_points = theory
        self.student_id=id

    def points(self):
        return (self.lab_points + self.theory_points) // 2

    def succeeded(self):
        return self.points() >= 10    
        
    def __str__(self):
        return "Student {} - {} has {} for lab and {} for theory, so average of {}".format(
            self.student_id, self.name, self.lab_points,self.theory_points,self.points())

class StudentGroup:
    def __init__(self, name, teacher, room):
        self.name = name
        self.teacher = teacher
        self.room = room

    def __str__(self):
        return "Group with name '{}' and teacher {} at room {}".format(
            self.name, self.teacher, self.room)    

students = []

STUDENT_DB_FILE_NAME = "students.db"

def init_database():
    with sl.connect(STUDENT_DB_FILE_NAME) as con:
        con.execute("""
            create table if not exists student_group
            (
                group_name text primary key,
                teacher text,
                room text
            );
        """)

        con.execute("""
            create table if not exists student
            (
                student_id INTEGER PRIMARY KEY,
                name TEXT,
                lab INTEGER,
                theory INTEGER,
                fk_student_group text references student_group
            );
        """)

def get_students():
    with sl.connect(STUDENT_DB_FILE_NAME) as con:
        query_result = con.execute('SELECT student_id, name, lab, theory FROM student')
        students = []
        for row in query_result:
            students.append(Student(row[1],row[2],row[3],row[0]))
    return students

def get_students_for_group(group_name):
    with sl.connect(STUDENT_DB_FILE_NAME) as con:
        query_result = con.execute('SELECT student_id, name, lab, theory FROM student where fk_student_group = ?',[group_name])
        students = []
        for row in query_result:
            students.append(Student(row[1],row[2],row[3],row[0]))
    return students

def get_groups():
    with sl.connect(STUDENT_DB_FILE_NAME) as con:
        query_result = con.execute('SELECT group_name, teacher, room FROM student_group')
        groups = []
        for row in query_result:
            groups.append(StudentGroup(row[0],row[1],row[2]))
    return groups

def save_new_student(student, group_name):
    with sl.connect(STUDENT_DB_FILE_NAME) as con:
        cur = con.cursor()
        cur.execute('insert into student(name, lab, theory,fk_student_group) values(?,?,?,?)', [student.name,student.lab_points,student.theory_points,group_name])
        con.commit()

def save_new_group(group_name, lector, room):
    with sl.connect(STUDENT_DB_FILE_NAME) as con:
        cur = con.cursor()
        cur.execute("insert into student_group(group_name, teacher, room) values(?,?,?)", [group_name, lector, room])
        con.commit()

def get_student(id):
    with sl.connect(STUDENT_DB_FILE_NAME) as con:
        query_result = con.execute('select student_id, name, lab, theory FROM student where student_id = ?',str(id))
        row = query_result.fetchone()
    return Student(row[1],row[2],row[3],row[0])

def update_points(id,lab,theory):
    with sl.connect(STUDENT_DB_FILE_NAME) as con:
        update_tatement = 'update student SET lab = ? , theory = ? WHERE student_id = ?'
        con.execute(update_tatement, [lab,theory,id])
        con.commit()

def delete_student(id):
    with sl.connect(STUDENT_DB_FILE_NAME) as con:
        con.execute("delete from student where student_id = ?", [id])
        con.commit()

def input_number(request):
    number_input = input(request)
    return int(number_input)   

menu = """
a. Maak studenten-groep aan
b. Toon groepen
1. Voeg student toe
2. Toon studenten
3. Toon student
4. Update van punten student
5. Verwijderen van een student
6. Stop applicatie
"""

sub_menu_students = """
a. Alle studenten
b. Studenten voor groep
"""

init_database()

while True:
    menu_input = input(menu)

    if menu_input == "a":
        group_name = input("Naam groep: ")
        lector = input("Lector: ")
        room = input("Lokaal ")
        save_new_group(group_name, lector, room)
    elif menu_input == "b":
        for student_group in get_groups():
            print(student_group)    
    elif menu_input == "1":
        student_name = input("Naam student(e): ")
        lab_points = input_number("Labo-punten: ")
        theory_points = input_number("Theorie-punten: ")
        print("Kies uit volgende groepen: ")
        for student_group in get_groups():
            print(student_group.name)  
        group_name = input("> ")
        save_new_student(Student(student_name,lab=lab_points,theory=theory_points), group_name)
    elif menu_input == "2":
        choice = input(sub_menu_students)
        if choice == "a":
            students = get_students()
        else:
            print("Kies uit volgende groepen: ")
            for student_group in get_groups():
                print(student_group.name)
            group_name = input("Kies groep> ")
            students = get_students_for_group(group_name)
            
        for student in get_students():
            print(student)

    elif menu_input == "3":
        id = input_number("> ")
        student = get_student(id)
        print(student)
    elif menu_input == "4":
        print("Kies student op id")
        for student in get_students():
            print("Student met id",student.student_id,"en naam",student.name)
        id = input_number("> ")
        lab = input_number("Labo-punten:")
        theory = input_number("Theorie-punten:")
        update_points(id,lab,theory)
    elif menu_input == "5":
        print("Verwijder student op id")
        for student in get_students():
            print("Student met id",student.student_id,"en naam",student.name)
        id = input_number("> ")
        delete_student(id)
    elif menu_input == "6":
        print("De applicatie wordt afgesloten")
        quit()
    else:
        print("ongekende input")
~~~

#### Extra tabel

Eerste wijziging die we moeten uitvoeren is zorgen dat er een nieuwe tabel wordt aangemaakt.  

~~~python
        con.execute("""
            create table if not exists student
            (
                student_id INTEGER PRIMARY KEY,
                name TEXT,
                lab INTEGER,
                theory INTEGER,
                fk_student_group text references student_group
            );
        """)
~~~

#### Extra opties voor het aanmaken van groepen

~~~python
    if menu_input == "a":
        group_name = input("Naam groep: ")
        lector = input("Lector: ")
        room = input("Lokaal ")
        save_new_group(group_name, lector, room)
    elif menu_input == "b":
        for student_group in get_groups():
            print(student_group)  
~~~

#### Opvragen van de groepen

~~~python
def get_groups():
    with sl.connect(STUDENT_DB_FILE_NAME) as con:
        query_result = con.execute('SELECT group_name, teacher, room FROM student_group')
        groups = []
        for row in query_result:
            groups.append(StudentGroup(row[0],row[1],row[2]))
    return groups
~~~

#### Bewaren van een nieuwe groep

~~~python
def save_new_group(group_name, lector, room):
    with sl.connect(STUDENT_DB_FILE_NAME) as con:
        cur = con.cursor()
        cur.execute("insert into student_group(group_name, teacher, room) values(?,?,?)", [group_name, lector, room])
        con.commit()
~~~

#### Aanpassing bij het aanmaken van een student

~~~python
    elif menu_input == "1":
        student_name = input("Naam student(e): ")
        lab_points = input_number("Labo-punten: ")
        theory_points = input_number("Theorie-punten: ")
        print("Kies uit volgende groepen: ")
        for student_group in get_groups():
            print(student_group.name)  
        group_name = input("> ")
        save_new_student(Student(student_name,lab=lab_points,theory=theory_points), group_name)
~~~

~~~python
def save_new_student(student, group_name):
    with sl.connect(STUDENT_DB_FILE_NAME) as con:
        cur = con.cursor()
        cur.execute('insert into student(name, lab, theory,fk_student_group) values(?,?,?,?)', 
        [student.name,student.lab_points,student.theory_points,group_name])
        con.commit()
~~~