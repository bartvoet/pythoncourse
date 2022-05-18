## Python modules

### Modulariteit

**Modulair** programmeren of modulariteit houdt in dat je leert je **code** te **ordenen**  en te groeperen.  
Tot nu toe hebben we al 2 elementen gezien die ons daarbij kunnen helpen, namelijk **functies** en **klasses**.

#### Modulariteit met functies

**Functies** stelde ons in staat stukken code te isoleren:

* Om code **op te delen** in logische onderdelen (en je code leesbaar te houden)
* Om code te **hergebruiken** en herhalingen te vermijden
  
#### Modulariteit met objecten...

**Klasses** stelde ons in staat data te groeperen in een structuur.  
Herinner bijvoorbeeld de student met een naam, labo-punten en theorie-punten.  

~~~python
class Student:
    def __init__(self)
        self.name = ""
        self.labo = 0
        self.theory = 0

bart = Student()
bart.labo = 16
bart.theory = 12
~~~

Wat klasses nog bijzonder maakt is de mogelijkheid functies te koppelen aan deze data.  
Zo konden we bijvoorbeeld een functie average die - via de self-referentie - kon opereren op de data ban het object

~~~python
class Student:
    def __init__(self)
        self.name = ""
        self.labo = 0
        self.theory =

    def points(self):
        return self.labo / self.theory

bart = Student()
bart.labo = 16
bart.theory = 12

print(bart.points()) # prints 14
~~~

### Python modules

Een module zit nog een niveau **hoger** dan **functies** en **klassen**.  
Een module is een **geheel/verzameling** van klassen, functies en variabelen die **logisch bij elkaar horen**.  

De reden om deze te groeperen zijn divers:

* Je programma logisch onder te verdelen te groeperen om het overzichtelijk en onderhoudsvriendelijk te houden
* Je code te laten herbruiken binnen andere programma's
* Een stuk van je code te isoleren om het gemakkelijker te testen
* ... en vele andere redenen die je nog zal ontdekken

### Python modules in praktijk

Een Python module aanmaken is **zeer éénvoudig**, een **Python-file** is een **module**
Stel **onderstaande code**...

~~~python
def hello():
    print("hello")

def world():
    print("world")
~~~

... we bewaren deze file onder de **naam hello.py**  

**Let op, deze naam (hello.py) moeten we onthouden voor de volgende stap**

### Een module hergebruiken via import

Als we een Python console openen vanuit dezelfde locatie waar deze python-file is bewaard kunnen we deze **functies importeren**:

~~~python
>>> import hello
>>> hello.hello()
hello
>>> hello.world()
world
~~~

De eerste statement "import hello" zorgt ervoor dat de functies (en ook variabelen als die er zijn) beschikbaar worden gesteld.  

De naam van deze import dient overéén te komen met de naam van de file (op voorwaarde dat deze in dezelfde file staat)

Let wel, om deze aan te roepen ben je wel verplicht deze te prefixen met de naam van deze module.  
Als je dit niet doet zal Python een error te voorschijn toveren (van het type NameError):

~~~python
>>> hello()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'hello' is not defined
~~~

### Import vanuit een andere python-file

Het voorgaand voorbeeld was vanit de **console** maar je kan dat ook het zelfde doen vanuit een andere Python-file.

Maar hiervoor - opnieuw binnen dezelfde directory - een andere file aan (bijvoorbeeld met de naam hello_application.py)

~~~python
import hello

hello.hello()
hello.world()
~~~

> *Nota:*  
> Probeer voor leesbaarheid een lege lijn tussen de imports (meestal bovenaan de code)
> en de rest van je code

Vanuit deze file kan je dan respectievelijk beide functies hergebruiken:

~~~bash
$ ls 
hello_application.py hello.py
$ python hello_application.py
hello
world
~~~

### De naam van modules

Een module krijgt ook **automatisch** een **naam** mee (die dan ook **overeenkomt** me de naam die je gebruikt om deze te **importeren**)

~~~python
>>> import hello
>>> hello.__name__
'hello'
>>> __name__
'__main__'
>>> 
~~~

Deze variabele is ook beschikbaar als globale variabele, en deze heeft een specifieke waarde afhankelijk van de modus waar de code zich in bevindt.

In normale omstandigheden zal de waarde van deze functie **__main__** zijn, maar dit kan ook verschillend zijn zoals we zo dadelijk gaan zien...

### name-variabele met verschillende waardes

Om dit te illustreren printen voegen we een lijntje toe aan onze voor Python-file

~~~python
def hello():
    print("hello")

def world():
    print("world")

print("Name: ", __name__)
~~~

Als je deze dan uitvoert print deze zoals verwacht __main__ af

~~~bash
$ python3 hello.py
Name: __main__
~~~

Als we echter nu echter hello_application.py uitvoeren zien we het volgende:

~~~bash
python3 hello_application.py
Name:  hello
hello
world
~~~

Eerst en vooral zien we dat - ondanks dat we enkel importeren - de code effectief wordt uitgevoerd.  
De naam is echter hello en niet __main__ maar hello.  

Bij het importeren van een file wordt dus alle code van deze file uitgevoerd, doordat deze code wordt uitgevoerd worden deze functies dan ook beschikbaar gesteld.

Door dat de globale name-variabele echter op hello staat worden deze functies trouwens gekoppeld aan deze naam en niet aan de globale (main)-namespace (waardoor dat je hello als prefix dient te gebruiken)

### Uitvoerbare modules

Deze name-variabele heeft echter nog een belangrijke functie.  
Stel dat je volgende code schrijft:

~~~python
def hello():
    print("hello")

def world():
    print("world")

hello()
world()
~~~

...dan zal deze inderdaad de functies en hello en world afdrukken...

~~~
$ python3 hello.py
hello
world
$ python3 hello_application.py
hello
world
hello
world
~~~

...maar deze code gaat echter ook worden uitgevoerd als je deze vanuit een andere file importeerd (hello_application.py)  
Om er voor te kunnen zorgen dat je hello.py zowel als module als uitvoerbare file kan gebruiken kan je het volgende toevoegen:

~~~python
def hello():
    print("hello")

def world():
    print("world")

if __name__ == "__main__":
    hello()
    world()
~~~

Door te gaan kijkne of de globale name-variabele main is of hello kan je vermijden dat de code wordt uitgevoerd als je in de import-modus zit.

~~~
$ python3 hello.py
hello
world
$ python3 hello_application.py
hello
world
~~~

### from-keyword

Eerdoer hebben het **import-keyword** gebruikt om de functies vanuit voorgaande module te importeren.  

Om die functies (en klasses als die er zouden zijn) te gebruiken diende je te **prefixen** met de module-naam (hello).  
Dit had als voordeel dat je niet zomaar **conflicten** kan hebben met **functies** uit andere modules (of je eigen code) maar geeft wel wat extra type-werk.

Soms kunnen er situaties zijn waar je de functies in hoofd-namespace van het programma wil krijgen (zonder te moeten prefixen).  
Dit kan je doen met de volgende **from ... import ... constructie** zoals in onderstaande code.

~~~python
from hello import world

world()
~~~

Deze heeft dezelfde eigenschap als import (alle code wordt daar ook uitgevoerd) maar enkel functies aangeduid achter import worden geimporteerd.  
In onderstaande uitvoering zie je 2 zaken:

* Je kan de functie world() aanroepen zonder prefix
* hello() is niet beschikbaar

~~~python
Python 3.8.5 (default, Jan 27 2021, 15:41:15) 
[GCC 9.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> from hello import world
>>> world()
world
>>> hello()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'hello' is not defined
~~~

Als je wilt dat hello ook beschikbaar is kan je dit op 2 manieren.  
Of je importeert beide (gescheiden door komma's)

~~~python
from hello import hello,world

world()
hello()
~~~

...met als resultaat...

~~~python
Python 3.8.5 (default, Jan 27 2021, 15:41:15) 
[GCC 9.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> from hello import world
>>> world()
world
>>> hello()
hello
~~~

...of je gebruik \* om alle functies te importeren (met hetzelfde resultaat)

> Let op:  
> !!! Het gebruik van import \* is meestal geen goed idee
> dit kan zorgen voor conflicten met functies of klassen
> uit andere modules!!!

~~~python
from hello import *

world()
hello()
~~~

### Herwerken van studenten-applicatie

Als voorbeeld van een modularisatie gaan we onze voorgaande studenten-applicatie modulariseren.  
Als je de code bekijkt zou je deze kunnen verknippen in 3 delen:

* **student_command.py**   
  Code die zich bezig houdt met de command-line-interactie
* **student_service.py**  
  Code die zich bezig houtd met de applicatie-logica en het opslagen in de database
* **student_entities.py**  
  Code die de studenten-datatypes bevatten.

Elk stuk code heeft zijn eigen verantwoordelijkheid.

#### Afhankelijkheden

In onderstaand diagram zien je ook de relaties en afhankelijkheden tussen de modules onderling.

* Bovenaan staat de command-line-module, deze heeft de service-module nodig om de studenten in de database op te slagen
* Zowel de command- als de service- zijn op hun beurt afhankelijk van de entities
* entities staat op zich zelf en heeft geen afhankelijheden

~~~
                             +-------------------------------+
                             |                               |
                +------------+       STUDENT_COMMAND         +------------+
                |            |                               |            |
                |            +-------------------------------+            |
                v                                                         |
+---------------+--------------+                                          |
|                              |                                          |
|        STUDENT_SERVICE       |                                          |
|                              |                                          |
+---------------+--------------+                                          V
                |                                         +---------------+--------------+
                |                                         |                              |
                +---------------------------------------->+        STUDENT_ENTITIES      |
                                                          |                              |
                                                          +------------------------------+
~~~

#### Nut van modules

Modules zijn zeer nuttig voor verschillende doeleinden: 

* Code (bij grotere projectjes) op te splitsten in kleinere beheersbare delen zodat.
* Code te herbruiken binnen andere applicaties
* Code individueel testen (je wil bijvoorbeeld je service-applicatie testen zonder de command-line)
  
Stel nu dat we naast onze command-line-module nu ook een web-api willen maken dan kan deze nieuwe module ook de service-module gebruiken

(we passen dit toe in het volgend hoofdstuk)

~~~
                     +-------------------------------+
                     |                               |
                +----+       STUDENT_API             +--------------------+
                |    |                               |                    |
                |    +-------------------------------+                    |
                |                                                         |
                |                    +-------------------------------+    |
                |                    |                               |    |
                +--------------------+       STUDENT_COMMAND         +----+
                |                    |                               |    |
                |                    +-------------------------------+    |
                v                                                         |
+---------------+--------------+                                          |
|                              |                                          |
|        STUDENT_SERVICE       |                                          |
|                              |                                          |
+---------------+--------------+                                          V
                |                                         +---------------+--------------+
                |                                         |                              |
                +---------------------------------------->+        STUDENT_ENTITIES      |
                                                          |                              |
                                                          +------------------------------+
~~~

#### student_entities.py

~~~python
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
~~~

#### student_db.py

~~~python
import sqlite3 as sl
from student_entities import *

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

init_database()
~~~

#### student_cmd.py

~~~python
from students import *
from students_db import *

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

### Andere weetjes

Een aantal andere interessante weetjes ivm modules zijn

#### Waar vindt Python modules

Om je een module te gebruiken moesten de python-module-file in dezelfde directory plaatsen.  

Python voorziet echter - naast je eigen modules - ook een veel standaard-modules, waar bevinden zich deze modules nu.

De locaties waar Python deze gaan halen bevindt zich in een variable binnen de standard-module sys.path

~~~python
>>> import sys
>>> print(sys.path)
['', '/usr/lib/python38.zip', '/usr/lib/python3.8', '/usr/lib/python3.8/lib-dynload', '/home/bart/.local/lib/python3.8/site-packages', '/usr/local/lib/python3.8/dist-packages', '/usr/lib/python3/dist-packages', '/usr/lib/python3.8/dist-packages']
~~~


#### dir-functie

De dir-functie kan je gebruiken om de verschillende onderdelen (functies, klassen, variabelen, ...) 

~~~python
>>> dir(hello)
['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'hello', 'world']
~~~

De dir-functie kan je trouwens ook gebruiken op klasses, hieronder zie alle functies die betaan voor het type bytearray

~~~python
>>> dir(bytearray)
['__add__', '__alloc__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'capitalize', 'center', 'clear', 'copy', 'count', 'decode', 'endswith', 'expandtabs', 'extend', 'find', 'fromhex', 'hex', 'index', 'insert', 'isalnum', 'isalpha', 'isascii', 'isdigit', 'islower', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'pop', 'remove', 'replace', 'reverse', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
~~~

Voor het type list...

~~~python
>>> dir(list)
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
>>> a = [1,2,3]
>>> dir(a)
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
>>> type(a)
<class 'list'>
>>> 
~~~

### PIP en PyPi

Een groot deel van programmeren is leren herbruiken van bestaande code.  
We hebben net gezien hoe je code kan afzonderen in aparte files en herbruiken om deze functionaliteit te isoleren en eventueel te herbruiken in verschillende applicaties.  

Om code te herbruiken van andere ontwikkelaars (over heel de wereld) hebben veel programmeeromgevingen het concept van packagemanagers.  
Dit zijn tools die in staat zijn andere modules (en eventuele dependencies) automatisch te downloaden zoals bijvoorbeeld:

* Maven in Java
* Nuget in C#
* NPM in Javascript
* ...

In Python is dit **pip** (acrononiem voor **p**ip **i**nstalls **p**ackages), een tool die standaard wordt **meegeleverd** met **Python** (toch vanaf versie 3.4)

PIP gaat typisch modules downloaden over het internet, hiervoor werkt het standaard samen met Python Package Index, ook wel bekend als PyPI (spreek uit als Pie Pea Eye).

Deze website bevindt zich te https://pypi.org/

PyPI is een webservice die een een uitgebreide verzameling packages (frameworks, tools en libraries) host.  
De vind je te 
2 van deze libraries (Flask en request) 

Om een package te installeren gebruik je het commando "pip install" gevolgd door de libra

~~~
[student@fedora ~]$ pip install requests
Defaulting to user installation because normal site-packages is not writeable
Requirement already satisfied: requests in /usr/lib/python3.10/site-packages (2.27.1)
Requirement already satisfied: idna<4,>=2.5 in /usr/lib/python3.10/site-packages (from requests) (3.2)
Requirement already satisfied: urllib3<1.27,>=1.21.1 in /usr/lib/python3.10/site-packages (from requests) (1.26.7)
Requirement already satisfied: charset-normalizer~=2.0.0 in /usr/lib/python3.10/site-packages (from requests) (2.0.4)
~~~


~~~
[student@fedora ~]$ pip install flask
Defaulting to user installation because normal site-packages is not writeable
Collecting flask
  Downloading Flask-2.1.2-py3-none-any.whl (95 kB)
     |████████████████████████████████| 95 kB 549 kB/s 
Collecting itsdangerous>=2.0
  Downloading itsdangerous-2.1.2-py3-none-any.whl (15 kB)
Requirement already satisfied: click>=8.0 in /usr/lib/python3.10/site-packages (from flask) (8.0.1)
Collecting Jinja2>=3.0
  Downloading Jinja2-3.1.2-py3-none-any.whl (133 kB)
     |████████████████████████████████| 133 kB 52.5 MB/s 
Collecting Werkzeug>=2.0
  Downloading Werkzeug-2.1.2-py3-none-any.whl (224 kB)
     |████████████████████████████████| 224 kB 3.8 MB/s 
Requirement already satisfied: MarkupSafe>=2.0 in /usr/lib64/python3.10/site-packages (from Jinja2>=3.0->flask) (2.0.0)
Installing collected packages: Werkzeug, Jinja2, itsdangerous, flask
Successfully installed Jinja2-3.1.2 Werkzeug-2.1.2 flask-2.1.2 itsdangerous-2.1.2
[student@fedora ~]$ 
~~~


~~~
[student@fedora ~]$ pip install serial pandas
Defaulting to user installation because normal site-packages is not writeable
Collecting serial
  Downloading serial-0.0.97-py2.py3-none-any.whl (40 kB)
     |████████████████████████████████| 40 kB 2.7 MB/s 
Collecting pandas
  Downloading pandas-1.4.2-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (11.7 MB)
     |████████████████████████████████| 11.7 MB 2.9 MB/s 
Collecting future>=0.17.1
  Downloading future-0.18.2.tar.gz (829 kB)
     |████████████████████████████████| 829 kB 13.4 MB/s 
Collecting iso8601>=0.1.12
  Downloading iso8601-1.0.2-py3-none-any.whl (9.7 kB)
Collecting pyyaml>=3.13
  Downloading PyYAML-6.0-cp310-cp310-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_12_x86_64.manylinux2010_x86_64.whl (682 kB)
     |████████████████████████████████| 682 kB 20.7 MB/s 
Collecting pytz>=2020.1
  Downloading pytz-2022.1-py2.py3-none-any.whl (503 kB)
     |████████████████████████████████| 503 kB 21.5 MB/s 
Requirement already satisfied: python-dateutil>=2.8.1 in /usr/lib/python3.10/site-packages (from pandas) (2.8.1)
Collecting numpy>=1.21.0
  Downloading numpy-1.22.3-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (16.8 MB)
     |████████████████████████████████| 16.8 MB 101.6 MB/s 
Requirement already satisfied: six>=1.5 in /usr/lib/python3.10/site-packages (from python-dateutil>=2.8.1->pandas) (1.16.0)
Using legacy 'setup.py install' for future, since package 'wheel' is not installed.
Installing collected packages: pyyaml, pytz, numpy, iso8601, future, serial, pandas
    Running setup.py install for future ... done
Successfully installed future-0.18.2 iso8601-1.0.2 numpy-1.22.3 pandas-1.4.2 pytz-2022.1 pyyaml-6.0 serial-0.0.97
[student@fedora ~]$ 
~~~


~~~
student@fedora ~]$ pip list 
Package            Version
------------------ ---------
argcomplete        1.12.3
Beaker             1.10.0
beautifulsoup4     4.11.0
...
fedora-third-party 0.8
Flask              2.1.2
fros               1.1
gpg                1.15.1
...
regex              2022.3.15
requests           2.27.1
requests-file      1.5.1
requests-ftp       0.3.1
...
urllib3            1.26.7
Werkzeug           2.1.2
[student@fedora ~]$ 
~~~

~~~
[student@fedora ~]$ python
Python 3.10.4 (main, Mar 25 2022, 00:00:00) [GCC 11.2.1 20220127 (Red Hat 11.2.1-9)] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import requests
>>> requests.__version__
'2.27.1'
>>> import Flask
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ModuleNotFoundError: No module named 'Flask'
>>> import flask
>>> flask.__version__
'2.1.2'
>>> 
~~~


~~~
[student@fedora ~]$ pip show flask
Name: Flask
Version: 2.1.2
Summary: A simple framework for building complex web applications.
Home-page: https://palletsprojects.com/p/flask
Author: Armin Ronacher
Author-email: armin.ronacher@active-4.com
License: BSD-3-Clause
Location: /home/student/.local/lib/python3.10/site-packages
Requires: click, itsdangerous, Jinja2, Werkzeug
Required-by: 
[student@fedora ~]$
~~~

~~~
[student@fedora ~]$ pip uninstall flask
Found existing installation: Flask 2.1.2
Uninstalling Flask-2.1.2:
  Would remove:
    /home/student/.local/bin/flask
    /home/student/.local/lib/python3.10/site-packages/Flask-2.1.2.dist-info/*
    /home/student/.local/lib/python3.10/site-packages/flask/*
Proceed (Y/n)? Y
  Successfully uninstalled Flask-2.1.2
[student@fedora ~]$ 
~~~