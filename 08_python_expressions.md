## Expressies

### Expressie geeft een waarde

We hebben reeds **statements** gezien in **Python**, die je kan beschouwen als een soort van **commando** of **actie** die Python voor jou moet uitvoeren zoals het afdrukken van een tekst (function-call) of het initialiseren van een variabele (assigment statement).

Een 2de element dat we introduceren zijn **expressies**, heel simpel is een expressie (in Python maar ook daarbuiten) alles wat een **waarde** teruggeeft.  
Een eerste voorbeeld van expressie dat we al veel hebben gebruikt zijn **literals** (of letterlijke waarde):

~~~python
a = "test"
b = 2
~~~

**"test" en 2** zijn hier **literals** of  **letterlijke expressies** die een waarde geven die in een variabele worden opgeslagen via de assignment-operator (en -statement).


Een andere expressie is bijvoorbeeld wanneer je de naam van een variabele typt als argument van een functie.

~~~python
a = "test"
print(a)
~~~

Hier geldt a - op de 2de lijn - als een expressie die de waarde van de variabele a ("test") oplevert.

### Rekenkundige expressies

Een andere soort **expressie** waar we normaal gezien vanuit de wiskunde al met vertrouwd zijn **mathematische** of rekenkundige **expressies**.

~~~python
print(4 / 2) # prints 2
print(2 - 6) # prints -4
print(5 * 2) # prints 10 
print(5 % 2) # prints 1
print(2 ** 8) # prints 256
print(2 ** 8) # prints 256
~~~

Het **overzicht** van deze **rekenkundige operatoren** vindt je hier onder:

| Operator   |   Betekenis          |
|------------|----------------------|
| +          | optellen             |
| -          | aftrekken            |
| *          | vermenigvuldigen     |
| /          | deling               |
| //         | deling               |
| %          | rest van deling      |
| **         | macht                |


De operatoren in Python komen grotendeels overeen met wat je gewoon bent uit de klassieke wiskunde en hebben geen verdere verklaring nodig, met uitzondering misschien van de deel-operator.

### Delen van integers

Voor het **delen** van getallen in **Python 3** heb je namelijk **2 operatoren**:

* **//** ofwel **floor-division-operator**, zal afronden naar beneden
* **/** ofwel **true-division-operators** zal niet afronden maar de werkelijke decimale waarde geven

Bijvoorbeeld bij het delen van 2 integers zie je het verschil duidelijk

~~~
print(5/2) # prints 2.5
print(type(5/2)) # prints <class 'float'>
print(5//2) # prints 2
print(type(5//2)) # prints <class 'int'>
~~~

De eerste bewerking met **true division** zal een **niet afgeronde uitkomst** opleveren.  
Gezien het resultaat een komma-getal is, is het resultaat een waarde van het **type float** 
(gezien je geen komma-resulaten in een integer kan opslaan.


### Delen met floats

Daarentegen bij de **floor division** wordt er afgerond naar beneden en is het **resultaat een integer**  
Bewerkingen waarbij een float is betrokken (ook voor andere rekenkundige operatoren) zullen altijd in een float-resultaat resulteren (ongeacht het andere getal een integer is of niet).

~~~
print(3.50 / 2) # prints 1.75
print(type(5/2)) # prints <class 'float'>
print(3.50 // 2) # prints 1.0
print(type(5//2)) # prints <class 'float'>
~~~

Wel zullen de operatoren het resultaat afronden of niet naargelang het om floor-division of true-division gaat

### Operatoren en operanden (terminologie)

Er zijn verschillende soorten expressies of bewerkingen, naast de **rekenkundige** hebben we ook **logische**, **relationele** en **binaire** expressies die we gedurende deze cursus nader zullen bekijken.

Wat deze wel gemeenschappelijk hebben is dat deze allen uit **operatoren** en **operanden** bestaan:

* Een **operator** zijnde het symbool dat de bewerking voorstelt
* De **operanden** zijnde de waardes (of andere expressies) die aan de **linker- en rechterkant** staan van de **operator**

Bijvoorbeeld als ik de **variabele a** vermenigvuldig met de **literal 2** als volgt:

~~~
a = 5
b = a * 2
print(b) # prints 10
~~~

Dan is **a** de **linker-operand** en **2** de **rechter-operand**  
Een **operand** dient altijd zelf een **expressie** te zijn, in dit geval een **literal** en een **variabele**, maar dit kan ook andere mathematische expressie zijn.

~~~
a = 5
b = a * ( 2 + a)
print(b) # prints 35
~~~

### Operator-precedence en haakjes

Net zoals in klassieke wiskunde kan je ook **haakjes** gebruiken om **volgorde van berekening** af te dwingen.  
Als je dit niet doet zal Python de voorrang van bewerking bepalen aan de basis mathematische regels.

~~~python
a = 5
b = a * 2 + a
print(b) # prints 15
~~~

In bovenstaand geval zal eerst worden vermenigvuldigd (a * 2) en dan pas de som worden gemaakt met a.

De volgende volgorde wordt gerespecteerd:

* alles binnen de haakjes
* machten uitwerken
* vermenigvuldigen, delen en rest
* optellen en aftrekken

Binnen de zelfde "precedence" (bijvoorbeeld *, /, // en %) wordt er van links naar rechts gewerkt.  
Bijvoorbeeld:

~~~python
print(260 / 10 * 2) # prints 52 and not 13
print(35 - 10 + 4) # prints 29 and not 21
~~~

Als je van **links naar rechts** uitrekent tussen operatoren met de **zelfde precedence** (of **voorrang**) krijg je een **wiskundig correct** resultaat:

~~~
260 / 10 * 2 = 26 * 2 = 52
35  - 10 + 4 = 25 + 4 = 29
~~~

Dit is dus het zelfde als Python voor jou doet.  
Daarentegen als van links naar rechts uitrekent krijg je ander (foutief) resultaat:

~~~
260 / 10 * 2 = 260 / 20 = 13
35  - 10 + 4 = 35 - 14 = 21
~~~
