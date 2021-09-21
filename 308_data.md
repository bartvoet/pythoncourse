## Dataformaten

Om data uit te wisselen 

### xml

~~~xml
<sensor_meassurement>
    <sensor>10</sensor>
    <value>10</value>
</sensor_meassurement>
~~~

~~~xml
<sensor_meassurement sensor="5">
    <location>
        <street>Goreweg</street>
        <number>70</number>
    </location>
    <value>10</value>
</sensor_meassurement>
~~~

### json

~~~json
{
    "location" : {
        "street" : "Goreweg",
        "number" : 70
    },
    "sensor" : 5,
    "value" : 10
}
~~~

### csv

Een heel simpel format, dit wordt gebruikt

~~~csv
70,5,Goreweg,70
~~~
