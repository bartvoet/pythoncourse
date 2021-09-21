## Data opslaan met databases

Software-applicatie dienen in de meeste gevallen data op te slagen, we noemen dit process ook wel **persisteren**.  

Een eerste manier is data opslagen via een file (zoals eerder gezien).   
Als we echter veel of complexe data willen opslagen kunnen we gebruik maken van databases.  

### Wat is een database?

Een **database** is een apart stuk **software of service** dat:

* **data** kan opslaan
* op een **gestructureerde manier** 
* op een **duurzame** manier (**persisteren**)
* en deze nadien terug kan **ondervragen** of **querien**

#### CRUD en queries

Een database voorziet voor het opslagen van data in **CRUD**-operaties:

* **C**reate: je kan **nieuwe data** aanmaken
* **R**ead: je kan deze data opnieuw **opvragen** via **zoekopdrachten** of **queries**
* **U**pdate: je kan deze data - die je eerder hebt gecreerd - opnieuw **wijzigen**
* **D**elete: je kan de data ook (selectief indien nodig) verwijderen

### Client-server vs embedded databases

**DBMS** (Database Management Systems) zijn meestal beschikbaar als een **client-server-service** op een netwerk en worden gedeeld door meerdere gebruikers.

#### Client-server

Zo'n applicatie maakt dan over het **netwerk** **verbinding** met een **database** om data op te vragen of te manipuleren (via SQL of anders) en krijgt data terug.

~~~
+-------------------+  NETWORK   +----------------+
|                   |            |                |
|                   +----------->|                |
|                 A |    SQL     |                |
|  Applicatie     P |            |    Database    |
|                 I |    DATA    |                |
|                   |<-----------+                |
|                   |            |                |
+-------------------+            +----------------+
~~~

Bekende voorbeelden van zulke databases zijn bijvoorbeeld MySQL, MariaDB, Oracle DB, SqlServer, ...  

#### Database (SQL)-api's

Een applicatie gaat meestal **niet rechtstreeks** praten met de database, om **complexiteit** te **verbergen** (netwerk-verbinding, sql en parameters aanbrengen, ....) bieden de meeste datatabases een **API** (en/of **driver**) aan om de **communicatie** te verzorgen met de database.

~~~
+---------------+---+  NETWORK   +----------------+
|               |   |            |                |
|               |   +----------->|                |
|               | A |    SQL     |                |
|  Applicatie   | P |            |    Database    |
|               | I |    DATA    |                |
|               |   |<-----------+                |
|               |   |            |                |
+---------------+---+            +----------------+
~~~

#### Embedded databases

In vele gevallen kan het zijn dat de data niet noodzakelijk moet gedeeld worden tussen verschillende applicaties or devices op het netwerk.  
Een voorbeeld is een Smartphone (of een applicatie of de smartphone) die wat lokale applicatie-gegevens of configuratie wenst bij te houden, de historiek van een browser, ...

Deze tegenhanger van  **client-server-systemen** noemen we een **embedded database**.  
In dit geval draait de database **op dezelfde machine** en in **meeste gevallen** is de database ook **ingebed** (embedded) is in dezelfde **applicatie**.

~~~
+---------------+---+------------+----------------+
|               |   |            |                |
|               |   +----------->|                |
|               | A |    SQL     |                |
|  Applicatie   | P |            |    Database    |
|               | I |    DATA    |                |
|               |   |<-----------+                |
|               |   |            |                |
+---------------+---+------------+----------------+
~~~

### Relationele databases (of databanken)

Voorgaande opdeling was op basis van **infrastructuur**.  
Daarnaast kan je ook een opdeling maken tussen database op basis van **technologie**, zoals er zijn **relationele**, **grafische**, **document-gebaseerde**, ...  

De database-technologie die wij gaan **gebruiken** zijn **relationele databases**, of ook wel **RDBMS** (relational database management system) genoemt.

Zo'n database is in de **kern** gebaseerd op een aantal **basisprincipes**:

* Data wordt gestructuureerd opgeslagen in **tabellen**
* Deze tabellen bestaan uit **kolommen** of **velden**
* Men kan **relaties** ofverbanden leggen **tussen** deze **tabellen**  
  dit is het **relationeel** gedeelte...
* Om deze **verbanden** te kunnen leggen maakt men gebruik van **sleutels** of **keys**
* Men kan een aantal **regels** of constraints toekennen op deze tabellen of velden
* Deze data kan worden ondervraagd via **SQL** (Structured Query Language)

#### Tabellen, kolommen en rijen

Een database bestaat uit **1 of meerdere tabellen**:

* Een tabel kan je best vergelijken met een tabel zoals je ze uit documenten of excels kent
* Zo'n tabel definieert **kolommen of velden**, die hebben een **naam** en een **type**
* Dataéénheden noemen we **rijen**, deze bevatten een waarde voor elke kolom-definitie

Ter illustratie zie je hier een voorbeeld van een tabel **student** met 3 kolommen en 5 rijen met (studenten-)data.

~~~
        Tabel: student
            kolom 1         kolom 2          kolom 3
            type: text      type: int        type: int 
               |               |                |
         +---------------+---------------+---------------+
         | student_name  |      lab      |     theory    |
         +---------------+---------------+---------------+  
  rij -- |  Bart Voet    |      15       |      16       |
         +---------------+---------------+---------------+  
  rij -- | Jan Janssens  |      17       |      14       |
         +---------------+---------------+---------------+
  rij -- | Piet Pieters  |      15       |      14       |
         +---------------+---------------+---------------+
  rij -- | Korneel Kos   |      11       |      12       |
         +---------------+---------------+---------------+
  rij -- | Joris Jos     |      10       |      14       |
         +---------------+---------------+---------------+
~~~

#### Sleutels, relaties en verbanden

Een database is vanzelfsprekend niet beperkt tot 1 tabel.  
Er kunnen meerdere tabellen worden gedefinieerd en gebruikt

Stel dat bijvoorbeeld informatie wil bijvoegen over de klas zelf waar deze studenten aan verbonden zijn?  
Een eerste probeersel - maar **niet zo'n efficiente** manier - is deze data **toe te voegen** aan **dezelfde tabel**.

~~~
         +---------------+                                                      
         | student       | 
         +---------------+---------------+---------------+---------------+---------------+---------------+     
         | student_name  |      lab      |     theory    |  class_name   |    teacher    |     room      |
         +---------------+---------------+---------------+---------------+---------------+---------------+  
         |  Bart Voet    |      15       |      16       |      1        |    Wim        |      A        |
         +---------------+---------------+---------------+---------------+---------------+---------------+
         | Jan Janssens  |      17       |      14       |      1        |    Wim        |      A        |
         +---------------+---------------+---------------+---------------+---------------+---------------+
         | Piet Pieters  |      15       |      14       |      2        |    Thierry    |      B        |
         +---------------+---------------+---------------+---------------+---------------+---------------+
         | Korneel Kos   |      11       |      12       |      2        |    Thierry    |      B        |
         +---------------+---------------+---------------+---------------+---------------+---------------+
         | Joris Jos     |      10       |      14       |      2        |    Thierry    |      B        |
         +---------------+---------------+---------------+---------------+---------------+---------------+
~~~

Hier krijg je echter het **probleem** dat je de klas-informatie (leeraar en lokaal) moet **dupliceren** voor elke student.  

Een andere mogelijkheid is dat een **aparte tabel** bij te houden die enkel de **klas-informatie** bijhoudt (gemeenschappelijk voor alle studenten van dezelfde klas).  
Zo'n tabel zou er dan zo uit kunnen zien:

~~~
          **PRIMARY KEY**
         +---------------+                                                      
         |    class      |                                                      
         +---------------+---------------+---------------+                      
         | class_name (*)|    Teacher    |     Room      |                      
         +---------------+---------------+---------------+                      
         |      1        |      Wim      |      A        |
         +---------------+---------------+---------------+
         |      2        |    Thierry    |      B        |
         +---------------+---------------+---------------+
~~~

Bemerk het **sterretje** dat ik in de tekening heb geplaast naast de **kolom class_name**.  
Hiermee duid ik aan dat de waarde van deze kolom **uniek** is (en moet zijn) **over alle rijen** heen... 

Dit is wat we ook noemen in relationele databases als een **primary key**.  
Wat is het **nut** van zo'n primaire of unieke sleutel nodig?

Dat wordt duidelijk als we de 2 tabellen naast (of onder) elkaar zetten.  
Je kan u namelijk - relationele - **verbanden** **tussen** de verschilldende **tabellen** (student en class) gaan leggen.  

In onderstaand voorbeeld zie je dat we aan de class-tabel een kolom (class_name) hebt toevoegt.  
Deze kolom bevat een waarde die **verwijst** naar de kolom class_name in de tabel class, we noemen dit ook wel een **foreign key**

~~~
         +---------------+                                                      
         | student       |                               **FOREIGN KEY**
         +---------------+---------------+---------------+---------------+     
         | student_name  |      lab      |     theory    |  class_name   |
         +---------------+---------------+---------------+---------------+  
         |  Bart Voet    |      15       |      16       |      1        +-------+
         +---------------+---------------+---------------+---------------+       |
         | Jan Janssens  |      17       |      14       |      1        +-------+
         +---------------+---------------+---------------+---------------+       |
         | Piet Pieters  |      15       |      14       |      2        +---+   |
         +---------------+---------------+---------------+---------------+   |   |
         | Korneel Kos   |      11       |      12       |      2        +---+   |
         +---------------+---------------+---------------+---------------+   |   |
         | Joris Jos     |      10       |      14       |      2        +---+   |
         +---------------+---------------+---------------+---------------+   |   |
                                                                             |   |
+--------------------------------------<-------------------------------------+   |
|                                                                                |
|   +----------------------------------<-----------------------------------------+
|   |
|   |     **PRIMARY KEY**
|   |    +---------------+                                                      
|   |    |    class      |                                                      
|   |    +---------------+---------------+---------------+                      
|   |    | class_name (*)|    Teacher    |     Room      |                      
|   |    +---------------+---------------+---------------+                      
|   +--->|      1        |      Wim      |      A        |
|        +---------------+---------------+---------------+
+------->|      2        |    Thierry    |      B        |
         +---------------+---------------+---------------+
~~~

#### Normalisatie

Wat je hier ziet is het proces van **normalisatie**, we vermijden duplicatie van data door herhaalde of gemeenschappelijke data in een aparate tabel te plaatsten 

#### Constraints

Elke relationele database zal deze begrippen van **primary key** en **foreign key** ondersteunen en dit zelfs **garanderen**.
Deze **garantie** zorgt voor **consistentie** tussen de **verschillende tabellen** wordt ook wel **referentiele integriteit**:

* Zo'n primary key is **gegarandeerd** uniek binnen een tabel, dus je kan maar naar 1 lijn verwijzen
* Elke foreign key moet naar een geldige/bestaande waarde uit een **unique** of **primary key** van de andere tabel verwijzen

Het garanderen van deze regels noemen we in een database ook wel **contstraints**

#### Joins

Op deze manier kan je zien (zoals we later gaan zien met SQL) de informatie **samenvoegen** via een **join**-informatie als je de database ondervraagt of een query uitvoert.  
Hoe dit gebeurt, gaan een beetje verder bekijken als we SQL uitleggen.

~~~sql
select student.student_name, student.lab, student.theory, class.class_name, class.teacher, class.room
from student, class
where student.class_name = student.class_name
~~~

Met als **resultaat** de gegevens van beide tabellen **gecombineerd** met elkaar

~~~
         +---------------+                                                      
         | student-query | 
         +---------------+---------------+---------------+---------------+---------------+---------------+     
         | student_name  |      lab      |     theory    |  class_name   |    teacher    |     room      |
         +---------------+---------------+---------------+---------------+---------------+---------------+  
         |  Bart Voet    |      15       |      16       |      1        |    Wim        |      A        |
         +---------------+---------------+---------------+---------------+---------------+---------------+
         | Jan Janssens  |      17       |      14       |      1        |    Wim        |      A        |
         +---------------+---------------+---------------+---------------+---------------+---------------+
         | Piet Pieters  |      15       |      14       |      2        |    Thierry    |      B        |
         +---------------+---------------+---------------+---------------+---------------+---------------+
         | Korneel Kos   |      11       |      12       |      2        |    Thierry    |      B        |
         +---------------+---------------+---------------+---------------+---------------+---------------+
         | Joris Jos     |      10       |      14       |      2        |    Thierry    |      B        |
         +---------------+---------------+---------------+---------------+---------------+---------------+
~~~