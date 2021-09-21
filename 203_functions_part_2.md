## Functies (deel 2)

Hier bekijken we nog een aantal zaken die we nog niet hebben gezien in het eerste gedeelte van functies:

* Optionele argumenten
* pass-statement
* Arguments by name
* kwargs (varargs in andere talen)

### Optionele argumenten

Je kan voor een functie **default waardes** meegeven aan een argument.  
Zie bijvoorbeeld hieronder waar je een functie zie om de macht van een getal te berekenen:

~~~python
def power_of(base,exponent = 2):
~~~

Bij het aanroepen van deze functie heb je de mogelijkheid het 2de argument weg te laten:

~~~python
def power_of(base,exponent = 2):
    return base ** exponent

print(power_of(2))   # prints 4
print(power_of(2,2)) # prints 4
print(power_of(2,3)) # prints 8
~~~

maw het exponent wordt dan **optioneel**, als je het dan niet invult zal 2 worden gebruikt als exponent.
Samengevat, dit kan interessant zijn in situaties waar je in vele gevallen al de waarde weet, maar hier wel wil kunnen van afwijken

### pass-statement

**Python** laat **geen lege blocks** toe.  
Onderstaande code is in Python niet toegelaten

~~~python
def a_function_not_yet_impemented():
#functie is doing nothing...

a_function_not_yet_impemented()
~~~

Als ook bij andere blocks (if,while, for, ...) is dit het geval

~~~python
a = input("give number")
if(a > 10):
    print("Number is bigger than 10")
else:
    # I need to think on the message
~~~

Als je dus nog niet weet wat te implementeren (en dus een lege block hebt) kan je een **pass-statement** toevoegen, in dat geva

~~~python
def a_function_not_yet_impemented():
    pass
~~~

Idem dito voor andere block...


~~~python
a = input("give number")
if(a > 10):
    print("Number is bigger than 10")
else:
    pass
    # I need to think on the message
~~~

### Access by name

Tot nu toe hebben we functies aangeroepen, door een lijst van argumenten mee te geven, gescheiden door komma's

Er is echter een 2de manier, namelijk de de parameters **per naam** door geven.

~~~python
def power_of(base,exponent = 2):
    return base ** exponent

print(power_of(base=2,exponent=4)) # prints 16
print(power_of(exponent=4,base=2)) # prints 16
print(power_of(2,exponent=4)) # prints 16
##print(power_of(base=2,4)) => not possible!!!
~~~

Je kan in dat geval zelfs **kiezen** in welke **volgorde** je deze meegeeft (als je per naam meegeeft).  

Je kan ook **combineren** met de **standaard** manier van **argumenten** passeren, maar dat kan dan enkel voor de **laatste argumenten**.

### kwargs

In een aantal library-functies (zoals bijvoorbeeld **printf**) heb je de mogelijkheid om een **variabel aantal argumenten** mee te geven.  

Je kan dit ook zelf doen door een sterretje te plaatsen voor je argument waarna je dit argument kan behandelen zoals een lijst (zie lessen met list en for-loop)

~~~python
def print_students(*students):
    for student in students:
        print(student)

print_students("Jan", "Piet", "Joris","Korneel")
~~~

Met als resultaat:

~~~
Jan
Piet
Joris
Korneel
~~~

Je zou dit ook kunnen implementeren via een lijst maar dit heeft als nadeel dat je aanroepende code extra symbolen ([...]) moet plaatsen voor deze lijst.

~~~python
def print_students(students):
    for student in students:
        print(student)

print_students(["Jan", "Piet", "Joris","Korneel"])
~~~

Met als zelfde resultaat:

~~~
Jan
Piet
Joris
Korneel
~~~

Let ook dat je bij de kwargs-versie geen lijst kan meegeven:

~~~python
def print_students(*students):
    for student in students:
        print(student)

print_students(["Jan", "Piet", "Joris","Korneel"])
~~~

Want dan krijg je als resultaat, dat de code een lijst krijgt met 1 element (een lijst zelf)

~~~
['Jan', 'Piet','Joris','Korneel']
~~~


### recursie

De volgende functie/code telt af vanaf 10

~~~python
def countdown_function(count):
    for i in range(count,0,-1):
        print(i)

countdown_function(10)
~~~

Je kan deze ook recursief schrijven.
Dit is een techniek waarbij je een functie zichzelf laat aanroepen waar je telkens de loop-state meegeeft als argument.

~~~python
def countdown_function(count):
    if(count > 0):
        print(count)
        countdown_function(count - 1)

countdown_function(10)
~~~

> NOTA: dit stuk over recursie in enkel ter introductie en zal later in de cursus verder worden behandeld
