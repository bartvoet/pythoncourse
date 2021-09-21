## Werken met Flask

### Installatie

Vooraleer aan de uitleg te starten laten even starten met het instaleren van Flask, het framework dat we gaan gebruiken om te communiceren over http.  
Normaal gezien is pip reeds voorgeinstalleerd bij installatie van Python.

pip stelt je de package-installer voor Python. pip of **p**ackage **i**nstaller for **P**ython.
Je kan pip gebruiken om packages te installeren die je kan terugvinden in de Python Package Index (en andere)

~~~
$ pip install Flask
~~~

### Eerste programma

Het eerste dat we gaan doen is het installeren van een hello world packages

~~~python
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'
~~~

### Programma draaien

Om dit te draaien dien je te doen vanaf de command line

~~~
$ export FLASK_APP=hello.py
$ python -m flask run
 * Running on http://127.0.0.1:5000/
~~~

De flask-module zal zoeken naar deze environment-variabele

~~~
$ export FLASK_APP=hello.py
$ flask run
 * Running on http://127.0.0.1:5000/
~~~
Als je nu een brower opent en suft naar http://127.0.0.1:5000/
Als alles goed gegaan is krijg je een venster

### HTTP

~~~
+--------------+               +--------------+
|              |               |              |
|              |               |              |
|              |               |              |
|              |<--------------+              |
|  SERVER      |               |    CLIENT    |
|              |               |              |
|              |               |              |
|              +-------------->|              |
|              |               |              |
|              |               |              |
+--------------+               +--------------+
~~~

* Browser die een html-pagina afhaalt
* Een python-programma dat data afhaalt (xml of json)

* get - read
* put - update
* post - create
* delete - delete

#### static vs dynamic

~~~
python3 -m http.server
~~~

### Werken met routes

Om een iets geavanceerder voorbeeld te tonen voegen we een module students_flask.py toe aan de student-applicatie.

~~~python
from flask import Flask, request, url_for,jsonify
from markupsafe import escape
import json

from students_entities import Student, StudentGroup
from students_service import *

app = Flask(__name__)

@app.route('/')
def index():
    return 'index'

def group_to_json(group):
    return group.__dict__

def student_to_json(student):
    return student.__dict__

@app.route('/groups', methods=['GET'])
def groups():
    groups = list(map(group_to_json, get_groups()))
    return jsonify(groups)

@app.route('/groups',  methods=['POST'])
def group_post():
    group_name = request.json["name"]
    teacher = request.json["teacher"]
    room = request.json["room"]
    save_new_group(group_name, teacher, room)
    return jsonify(group_to_json(get_group(group_name)))

@app.route('/groups/<groupname>')
def group(groupname):
    return group_to_json(get_group(groupname))

@app.route('/groups/<groupname>/students', methods=['GET'])
def students(groupname):
    print("a")
    students = list(map(student_to_json, get_students_for_group(groupname)))
    return jsonify(students)

@app.route('/groups/<groupname>/students', methods=['POST'])
def student_post(groupname):
    name = request.json["name"]
    lab = int(request.json["lab_points"])
    theory = int(request.json["theory_points"])
    student = save_new_student(Student(name, lab, theory), groupname)
    return jsonify(student_to_json(student))
~~~

### Client-code

~~~bash
$ curl http://localhost:5000/groups

$ curl http://localhost:5000/groups/hello/students

$^curl curl -d '{"name":"hello", "room":"D118", "teacher":"Jos"}' -X POST -H "Content-Type: application/json" -X POST http://localhost:5000/groups

^curl curl -d '{"name":"hello", "theory_points":"D118", "teacher":"Jos"}' -X POST -H "Content-Type: application/json" -X POST http://localhost:5000/groups

$ curl http://localhost:5000/groups/1/students 

$ curl -d  '{"lab_points":10,"name":"bb","theory_points":15}'  -X POST -H "Content-Type: application/json" -X POST http://localhost:5000/groups/1/students
$ curl -d  '{"lab_points":10,"name":"cc","theory_points":15}'  -X POST -H "Content-Type: application/json" -X POST http://localhost:5000/groups/1/students
$ curl -d  '{"lab_points":10,"name":"cc","theory_points":15}'  -X POST -H "Content-Type: application/json" -X POST http://localhost:5000/groups/1/students
{"id":3,"lab_points":10,"name":"cc","student_id":0,"theory_points":15}

~~~

~~~python
>>> response = requests.post("http://localhost:5000/groups/1/students",json={"lab_points":12,"name":"dd","theory_points":15})
>>> response
<Response [200]>
>>> response.con
response.connection  response.content     
>>> response.con
response.connection  response.content     
>>> response.content
b'{"id":4,"lab_points":12,"name":"dd","student_id":0,"theory_points":15}\n'
>>> response.json
<bound method Response.json of <Response [200]>>
>>> response.json()
{'id': 4, 'lab_points': 12, 'name': 'dd', 'student_id': 0, 'theory_points': 15}
>>> 
~~~