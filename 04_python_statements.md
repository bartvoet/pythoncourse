## Statements

### Eerste programma onder de loep

Ons (eerste) programma had dus als **functionaliteit** het **afdrukken** van **een stuk tekst** naar de console.

Dit is min of meer het meest éénvoudige programma dat we kunnen schrijven, namelijk het printen van een stuk tekst.

~~~python
print("hello world")
~~~

### Enkelvoudige of simpele statements

Zo 1 lijn code is wat we noemen een **statement**, simpel gezegd is een statement een stuk code dat min of meer op zich zelf staande iets kan uitvoeren.

Je kan het bekijken als een soort van **opdracht** of **commando** die je aan je computer meegeeft (in dit geval de Python-interpreter).

Dit commando zal dan effectief **een actie uitvoeren** zoals **bijvoorbeeld** 
        
* **printen** van een boodschap naar de **console**
* **input** opvragen van een gebruiker op de **console**
* ...

Een statement dat uit **1 lijn code** bestaat noemen we ook wel enkelvoudige statements:

* De **kleinste éénheid** van **uitvoering** (of **unit of execution**)
* Dat **op zich zelf** staat
* Is altijd **1 lijn code**

> Nota:  
> Later zien we ook nog **complexe of meervoudige statements** (of block-statements) maar dat is voor zo direct

### Sequentiële programmatie

Je kan ook meerdere statements achter elkaar schrijven, dit noemt een **sequentie** of opéénvolging van statements.

~~~python
print("Hello world")
print("Welcome to Python")
print("Make sure to keep track")
~~~

De Python-interpreter zal deze commando's dan 1 voor 1 uitlezen en uitvoeren in volgorde die jij ze hebt ingegeven.

### Function-call

De **statement** dat we hier uitvoeren, is de **aanroep** naar een **functie** ofwel een **function-call**.  

> Naast function-call's zijn er nog meerdere types van statements


**Functies** zijn **herbruikbare** stukken **code** die je kan **aanroepen** vanuit je **programma** onder de volgende vorm.  

~~~
<functie-naam>(<argument>)
~~~

Je schrijft eerst de naam van de functie gevolgd - tussen haakjes - door het argument.  

Je kan ook meerdere argumenten meegeven aan sommige functies maar dan moeten deze gescheiden zijn door komma's.  
Daar komen we zo dadelijk nog op terug...

### Print-functie

In dit geval voorziet Python **standaard** in een hele hoop **functies** vrij voor gebruik.  
De functie die we hier gebruiken heeft als naar **print**.  

Bij deze functie geef je als argument een **stuk tekst**.  

### String-literal als argument

Een stuk tekst dat je "letterlijk" wil gebruiken in Python-code dient altijd omsloten te worden door quotes.  
Dit mogen zowel **enkele** (**'**) als **dubbele** (**"**) zijn.  

Dit is wat noemen een **String-literal** want:

* Het **data-type** voor stukken tekst noemt **String**
* **Literal** omdat de waarde **letterlijk **in de code wordt vermeld  
  (in tegenstelling tot een String die door je programma wordt ingelezen

