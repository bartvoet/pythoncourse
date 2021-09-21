## Commentaar

Het eerste element was een statement, als het waarde een commando dat je kan geven aan de python-interpreter.  
In python-code kan je ook **tekst** toevoegen die **niet wordt geïnterpreteerd**.

### Single-line comment

Hiervoor volstaat het om deze tekst **vooraf** te laten gaan **door een #** of hash-tag.

~~~python
# This is your very first application
print("hello world") # You can insert comments also after your code
# But please don't exagurate with comment
# Avoid writing more comment than code...
~~~

De regel is simpel, alles wat achter de eerste hash-tag komt op een lijn wordt geïnterpreteerd

### Multi-line comment

Er is een 2de manier om comment te schrijven zonder een hashtag te moeten herhalen over meerdere lijnen.

~~~python
"""
This is a comment over more
than one line.
Everything inbetween 3 subsequents double quotes
is considered comment
"""
# This is your very first application
print("hello world") # You can insert comments also after your code
# But please don't exagurate with comment
# Avoid writing more comment than code...
~~~

### Niet overdrijven met commentaar!!!

Gebruik van **commentaar** ter documentatie **kan nuttig zijn** en kan je **collegas** (of je zelf een tijdje nadat je de code hebt geschreven) **vooruithelpen**.  
Maar zoals bij alle goede dingen in het leven, **gebruik comments met mate**.  

Wees spaarzaam en minimalistisch met commentaar (**enkel wanneer nodig**), vermijd zeker meer comments dan code.  
Te veel documentatie en commentaar is dikwijls een teken van slecht **geschreven/leesbare code** (later in de cursus meer hierover...)