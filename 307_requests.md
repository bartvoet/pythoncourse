## Werken met REST en web-api's

In dit deel leggen we uit **hoe** met **web-api's** te werken vanuit als client-side.

We doen dit via het **Requests-framework**, daaropvolgend zullen we naar de serverkant kijken via **Flask**-framework

### URL

Gegeven bijvoorbeeld de volgende URL: http://hypothetical.ora.com:80/

Een browser interpreteert de URL as volgend:

* http://  => protocol is Hypertext Transfer Protocol.
* hypothetical.ora.com => contacteer een computer/server met dns-naam hypothetical.ora.com.
* :80 de poort waar de server aan het luisteren is, by default is dit 80



~~~~
${protocol}://${address}:${port}/${path}
~~~~

### query-parameters


~~~~
${protocol}://${address}:${port}/${path}?{id}
~~~~


~~~~
${protocol}://${address}:${port}/${path}?${var1}=${val1}&${var2}=${val2}
~~~~

~~~~
https://www.google.com/search?q=flask&oq=flask&sourceid=chrome&ie=UTF-8
~~~~


### HTTP


~~~
                +-----------------------------------+
                |         HTTP                      |
+-------+-------+----------+------------------------+
|       |       |          |                        |
|  TCP  |  IP   |  HEADER  |         BODY           |
|       |       |          |                        |
+-------+-------+----------+------------------------+
                           | OPTIONEEL VOOR REQUEST |                         
                           +------------------------+ 

~~~

~~~
GET /wiki/Hoofdpagina HTTP/1.1
Host: nl.wikipedia.org
Connection: close
User-Agent: Mozilla/5.0 (Windows; U; Windows NT 5.1; nl; rv:1.8.0.3) Gecko/20060426 Firefox/1.5.0.3
Accept: text/xml,text/html,text/plain,image/png,image/jpeg,image/gif
Accept-Charset: ISO-8859-1,utf-8
~~~

~~~
HTTP/1.1 200 OK
Date: Thu, 08 Apr 2004 18:24:33 GMT
Server: Apache/1.3.29 (Unix) PHP/4.3.4
X-Powered-By: PHP/4.3.4
Content-Language: nl
Content-Type: text/html; charset=iso-8859-1
X-Cache: MISS from wikipedia.org
Connection: close
Content-Type: text/html
Content-Length: 49
<html>
<head>
</head>
<body>
</body>
</html>
~~~



* 200 OK – Het gevraagde document is succesvol opgevraagd.
* 304 Not Modified – T.o.v. de versie in de cache is de pagina niet gewijzigd.
* 400 Bad Request - De gebruiker heeft een fout gemaakt in het verzoek waardoor deze niet verwerkt kan worden.
* 403 Forbidden – Het opgevraagde document mag niet opgevraagd worden.
* 404 Not Found – Het opgevraagde document bestaat niet.
* 405 Method Not Allowed – De gebruikte requestmethode is niet toegestaan.
* 410 Gone – Het opgevraagde document heeft bestaan maar is niet meer beschikbaar. Vergelijkbaar met foutcode 404.
* 451 Unavailable For Legal Reasons - een website niet kan worden weergegeven vanwege juridische redenen
* 500 Internal Server Error – De webserver heeft de gevraagde actie niet kunnen uitvoeren.
* 503 Service Temporarily Unavailable – De webserver is tijdelijk in onderhoud.



~~~python
>>> import requests
>>> requests.get("https://randomuser.me/api/")
<Response [200]>
~~~


~~~python
>>> import requests
>>> response = requests.get("https://randomuser.me/api/")
>>> response.text
'{"results":[{"gender":"female",
"name":{"title":"Ms","first":"Isobel","last":"Wang"}...'
~~~

https://thedogapi.com/

~~~python
>>> import requests
>>> response = requests.get("https://api.thedogapi.com/")
>>> response.text
'{"message":"The Dog API"}'
~~~

~~~python
>>> response
<Response [200]>
>>> response.request
<PreparedRequest [GET]>

>>> request = response.request
>>> request.url
'https://api.thedogapi.com/v1/breeds'
>>> request.path_url
'/v1/breeds'
>>> request.method
'GET'
>>> request.headers
{'User-Agent': 'python-requests/2.24.0', 'Accept-Encoding': 'gzip, deflate',
'Accept': '*/*', 'Connection': 'keep-alive'}

>>> response
<Response [200]>
>>> response.text
'[{"weight":{"imperial":"6 - 13","metric":"3 - 6"},
"height":{"imperial":"9 - 11.5","metric":"23 - 29"},"id":1,
"name":"Affenpinscher", ...}]'
>>> response.status_code
200
>>> response.headers
{'Cache-Control': 'post-check=0, pre-check=0', 'Content-Encoding': 'gzip',
'Content-Type': 'application/json; charset=utf-8',
'Date': 'Sat, 25 Jul 2020 17:23:53 GMT'...}
~~~


~~~python
>>> response = requests.get("https://api.thedogapi.com/v1/breeds")
>>> response
<Response [200]>
>>> response.status_code
200
>>> response.reason
'OK'
~~~

~~~python
>>> response = requests.get("https://api.thedogapi.com/v1/breedz")
>>> response
<Response [404]>
>>> response.status_code
404
>>> response.reason
'Not Found'
~~~

~~~python
>>> response = requests.get("https://api.thedogapi.com/v1/breeds/1")
>>> response.headers
{'Content-Encoding': 'gzip',
'Content-Type': 'application/json; charset=utf-8',
'Date': 'Sat, 25 Jul 2020 19:52:07 GMT'...}
~~~

~~~python
>>> response = requests.get("https://api.thedogapi.com/v1/breeds")
>>> response.text
'[{"weight":{"imperial":"6 - 13","metric":"3 - 6"},"height": ...}]'
~~~

~~~python
>>> response = requests.get("https://api.thedogapi.com/v1/breeds/1")
>>> response.headers.get("Content-Type")
'application/json; charset=utf-8'
~~~


~~~python
>>> response = requests.get("http://placegoat.com/200/200")
>>> response
<Response [200]>
>>> response.headers.get("Content-Type")
'image/jpeg'
~~~

~~~python
>>> response = requests.get("https://api.thedogapi.com/v1/breeds/1")
>>> response.headers.get("Content-Type")
'application/json; charset=utf-8'
>>> response.content
b'{"weight":{"imperial":"6 - 13","metric":"3 - 6"}...'
>>> response.json()
{'weight': {'imperial': '6 - 13', 'metric': '3 - 6'},
'height': {'imperial': '9 - 11.5', 'metric': '23 - 29'}
...}
>>> response.json()["name"]
'Affenpinscher'
~~~


~~~python
>>> response = requests.get("http://placegoat.com/200/200")
>>> response
<Response [200]>
>>> response.headers.get("Content-Type")
'image/jpeg'
>>> response.content
b'\xff\xd8\xff\xe0\x00\x10JFIF\x00\x01\x01\x01\x00H\...'
~~~



~~~python
>>> requests.get("https://randomuser.me/api/").json()
{'results': [{'gender': 'male', 'name':
{'title': 'Mr', 'first': 'Silvijn', 'last': 'Van Bekkum'},
'location': {'street': {'number': 2480, 'name': 'Hooijengastrjitte'},
'city': 'Terherne', 'state': 'Drenthe',
'country': 'Netherlands', 'postcode': 59904...}
~~~

~~~python
>>> requests.get("https://randomuser.me/api/?gender=female").json()
{'results': [{'gender': 'female', 'name':
{'title': 'Mrs', 'first': 'Marjoleine', 'last': 'Van Huffelen'},
'location': {'street': {'number': 8993, 'name': 'De Teebus'},
'city': 'West-Terschelling', 'state': 'Limburg',
'country': 'Netherlands', 'postcode': 24241...}
~~~

~~~python
>>> requests.get("https://randomuser.me/api/?gender=female&nat=de").json()
{'results': [{'gender': 'female', 'name':
{'title': 'Ms', 'first': 'Marita', 'last': 'Hertwig'},
'location': {'street': {'number': 1430, 'name': 'Waldstraße'},
'city': 'Velden', 'state': 'Rheinland-Pfalz',
'country': 'Germany', 'postcode': 30737...}
~~~


~~~python
>>> query_params = {"gender": "female", "nat": "de"}
>>> requests.get("https://randomuser.me/api/", params=query_params).json()
{'results': [{'gender': 'female', 'name':
{'title': 'Ms', 'first': 'Janet', 'last': 'Weyer'},
'location': {'street': {'number': 2582, 'name': 'Meisenweg'},
'city': 'Garding', 'state': 'Mecklenburg-Vorpommern',
'country': 'Germany', 'postcode': 56953...}
~~~~


https://608ffd813847340017020927.mockapi.io/users/48



~~~python
@app.route('/data')
def data():
    # here we want to get the value of user (i.e. ?user=some-value)
    user = request.args.get('user')
~~~

create, read, update, delete

CREATE:
    POST http://dog/breedz/ {"Ras":"Beagle","Kleur":"witbruin"}
    {"id"= 1,"Ras":"Beagle","Kleur":"witbruin"}

READ:
    GET http://dog/breedz/1
    {"id"= 1,"Ras":"Beagle","Kleur":"witbruin"}

UPDATE:
    PUT http://dog/breedz/1
    {"Ras":"Beagle","Kleur":"witbruin met stippels"}

READ
    GET http://dog/breedz/1
    {"id"= 1,"Ras":"Beagle","Kleur":"witbruin met stippels"}

DELETE
    DELETE http://dog/breedz/1

READ
    GET http://dog/breedz/1
404

requests.post("http://dog/breed/", '{"id"= 1,"Ras":"Beagle","Kleur":"witbruin"}')


* POST => create
* GET => read
  
