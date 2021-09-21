## Starten met Python

Als we eerder vermelde installaties hebben uitgevoerd kunnen we starten met ons eerste programma.  
Alle voorbeelden op "dag 1" worden uitgevoerd op de command line, zoals eerder vermeld als je daar nog verduidelijking gelieve naar de bijlagen te kijken.

### Python is een scripting-taal

Een script daarentegen wordt door een speciaal programma - de **interpreter** - gelezen en uitgevoerd.  
De code/instructies worden als het ware **"at runtime" geïnterpreteerd** en **uitgevoerd** op de computer als tekst.  
Deze instructies noemen we ook wel **statements**

### Uitvoeren van Python-code

Python-code kan je uitvoeren op 2 manieren:

* **File-based:** python-statements vanuit in een file uitvoeren
* **Interactief:** van uit een shell statement per statement uitvoeren

Voor de **eerste voorbeelden** gaan we ons **beperken** tot het **file-based** uitvoeren  
**Nadien** gaan we **beide manieren afwisselen** in de cursus

### File-based "Hello World"

Nu eindelijk, het **langverwachte allereerste Python-programma**...  

**Stap 1:** Open je favoriete **text-editor** en type de **volgende tekst** in:

~~~python
print("hello world")
~~~

**Stap 2:** **Bewaar** dit op je harde schijf als **hello.py**  
Bijvoorbeeld in je home-folder in een subfolder "python_projects"

> Nota: zie vooral dat je het in een gemakkelijk bereikbare folder zet

**Stap 3:** **Navigeer** op de **command-line** naar deze **folder**:

~~~
C:\users\python> cd my_first_programm
C:\users\python\my_first_programm> 
~~~

**Stap 4:** **Voer** dit programma **uit**.  
Dit doe je door de **python-interpreter** aan te roepen met als argument **hello.py** (naam van het python-programma)

~~~
C:\users\python\my_first_programm> python hello_world.py
Hello World
C:\users\python\my_first_programm> 
~~~

> Nota: afhankelijk van de installatie (op Windows) kan het zijn dat je py moet typen ipv python

> Weetje: "Hello World" is de klassieker om de basiswerking van een programmeer-taal te demonstreren

### Wat hebben we zo net gedaan...

We hebben de **Python-interpreter**  
- het programma met de naam Python dat verantwoordelijk voor het uitvoeren van deze Python-scripts -  
aangeroepen met deze text-file als argument.  

Python-scripts eindigen altijd met de **extensie ".py"**.  
Dit is technisch gezien niet verplicht, maar er is geen reden om deze conventie te negeren dus in de kader van de cursus is dit wel verplicht...

### Programmeertalen zijn voor fouten

Een **programmeer-taal is gevoelig voor fouten**, nog meer als mensen (en lectoren...)  
Als je bijvoorbeeld de syntax niet respecteert zoals gedemonstreerd hieronder:

~~~python
print("hello world"
~~~

dan zal de Python-interpreter het programma afbreken en aanduiden waar het in de mist gaat

~~~
C:\users\python\my_first_programm> python hello_world.py
  File "<stdin>", line 1
    print("hello world
                     ^
SyntaxError: EOL while scanning string literal
~~~

De Python-interpreter gaat ook meestal naar goed vermogen proberen aan te duiden:

* **Waar het probleem** zich in de code is voorgekomen
    * Lijnnummer code
    * Positie binnen lijn
* Welke **soort fout** je hebt gemaakt
* Eventueel een **hint** wat je moet doen om te corrigeren

Er zijn **verschillende soorten fouten** die in je in een Python-programma kan maken.  
Voor nu **volstaat** het om te **zeggen** dat je hier als **programmeur** moet met **rekening** **houden**.  
Gedurende de cursus gaan we nog **veel stilstaan** met de **verschillende soorten fouten** (bv. syntax-fouten vs runtime-errors- en hoe je hier mee moet met omgaan.