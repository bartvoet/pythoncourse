
~~~sql
create table BasketItem
(
itemId integer  primary key,
itemDescription varchar,
price integer,
quantity integer
);
~~~

~~~sql
insert into BasketItem(itemDescription,price,quantity) values("gsm",500,2);
~~~

~~~sql
drop table BasketItem;
~~~


~~~sql
create table if not exists BasketItem 
(
itemId integer  primary key,
itemDescription varchar,
price integer,
quantity integer
);

insert into BasketItem(itemDescription,price,quantity) values("gsm",500,2);
insert into BasketItem(itemDescription,price,quantity) values("test",500,2);
select * from BasketItem;
~~~
Data pesisteren opslagen



Relationele data => data linken aan elkaar

ide

unit testing
overerving
1 database voor demo op basis van basket oefening
1 interactieve database-oefening als oefening op sensoren
1 echte oefening als labo-oefening