## Input (en output)

### Input vragen aan de gebruiker

**Tot nog toe** hebben enkel **literals** gebruikt om **variabelen** te initialiseren.  
Om **input** van de **gebruiker** te verkrijgen voorzien Python 3 de **input-functie**.  

~~~python
text = input("Enter text: ")
print("text " + text)
~~~

Bovenstaand **voorbeeld** gebruikt de **input-functie **om een **tekst** op te vragen aan de gebruiker.  
Als parameter geef je een (optionele) prompt-tekst mee en als return ontvang je de tekst als een string-object

~~~
                                                       +-------------------------+
                                                       |      CONSOLE/OUTPUT     |
+----------+                                           | +---------------------+ |
| text     |            +------------------+           | |                     | |
+----------+            | Statement 2:     +--+input+--> | > Enter text: hello | |
| 11       <--+write+---+ function+call    |           | |                     | |
+----+-----+            +-------+----------+           | |                     | |
     |                          |                      | |                     | |
     |                          |                      | |                     | |
     |                  +-------v----------+           | |                     | |
     +--------+read+----> Statement 3:     |           | |                     | |
                        | function+call    +--+print+--> | > Entered text      | |
                        +------------------+           | +---------------------+ |
                                                       +-------------------------+

~~~

Als je dit uitvoert zal de (python-)console wachten tot je input inbrengt, gevolgd door een enter

~~~
$ python enter_test.py
Enter text: hello
Entered hello
~~~

### Input geeft een string

Deze functie geeft een resultaat terug dat je kan opvangen in een variabele.  

~~~python
number = input ("Enter number")
number_two = input("Enter another number")

print("Printing type of input value")

print ("type of number ", type(number))
print ("type of number_two ", type(number_two ))
~~~

Het type van deze **return value** is een **String**, zoals je hieronder ziet.

~~~
Enter number 22
Enter another number Elvis
Printing type of input value
type of number <class 'str'>
type of number_two<class 'str'>
~~~

### Wat als je met nummers wil werken? Gebruik de int-functie

Je kan echter een **string** omvormen naar een integer-getal, om te kunnen bewerken als een getal.  
Je kan dit doen het resultaat van input te converteren via de functie **int**.

~~~python
number_input = input ("Enter number: ")
number = int(number_input)
number_two = input("Enter another number")

print("Printing type of input value")

print ("type of number ", type(number))
print ("type of number_two ", type(number_two ))
~~~

Om te vermijden een extra variabele te moeten gebruiken (number_input) kan je de aanroep van input nesten in de aanroep van int.

~~~python
number = int(input ("Enter number: "))
number_two = input("Enter another number")

print("Printing type of input value")

print ("type of number ", type(number))
print ("type of number_two ", type(number_two ))
~~~

Als je dan een nummer ingeeft dan zie je dat variabele number ook echt een int is (waar je bewerkingen mee kan uitvoeren)

~~~
Enter number: 22
Enter another number Elvis
Printing type of input value
type of number <class 'int'>
type of number_two<class 'str'>
~~~

### Wat als je geen nummer ingeeft?

Als je geen nummer ingeeft dan zal de **functie int** een error genereren.  

~~~
$ python3 a.py
Enter number: arzez
Traceback (most recent call last):
  File "a.py", line 1, in <module>
    number = int(input ("Enter number"))
ValueError: invalid literal for int() with base 10: 'arzez'
~~~

Ga er (voorlopig) van uit dat je het programma gebruikt op ideale manier.  
Later in de cursus gaan we zien hoe we hier vanuit onze code moeten mee omgaan.