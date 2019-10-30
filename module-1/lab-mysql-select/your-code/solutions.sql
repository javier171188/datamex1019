select tabids.au_id as AUTHOR_ID,
au_fname as FIRST_NAME,
au_lname as LAST_NAME,
titulos.title, publications.pub_name as PUBLISHER
from (publications.authors  autores
inner join publications.titleauthor tabids
on  autores.au_id = tabids.au_id)
left join publications.titles as titulos
on tabids.title_id = titulos.title_id
left join publications.publishers as publications
on titulos.pub_id = publications.pub_id;
 
 
 create temporary table publications.ch1
 select tabids.au_id as AUTHOR_ID,
au_fname as FIRST_NAME,	
au_lname as LAST_NAME,
titulos.title, publications.pub_name as PUBLISHER
from (publications.authors  autores
inner join publications.titleauthor tabids
on  autores.au_id = tabids.au_id)
left join publications.titles as titulos
on tabids.title_id = titulos.title_id
left join publications.publishers as publications
on titulos.pub_id = publications.pub_id;


select AUTHOR_ID,
FIRST_NAME,	
 LAST_NAME,
title as TITLE, PUBLISHER, count(title) as TITLE_COUNT
from publications.ch1
group by PUBLISHER, AUTHOR_ID;

create temporary table publications.ch2b
select AUTHOR_ID,
FIRST_NAME,	
 LAST_NAME,
title as TITLE, PUBLISHER, count(title) as TITLE_COUNT
from publications.ch1
group by PUBLISHER, AUTHOR_ID;

select AUTHOR_ID, LAST_NAME, FIRST_NAME,
sum(TITLE_COUNT) as TOTAL
from publications.ch2b
group by AUTHOR_ID
order by Total desc limit 3;

create temporary table publications.ch3
select AUTHOR_ID, LAST_NAME, FIRST_NAME,
sum(TITLE_COUNT) as TOTAL
from publications.ch2b
group by AUTHOR_ID
order by Total desc limit 3;

select AUTHOR_ID, LAST_NAME, FIRST_NAME,
sum(TITLE_COUNT) as TOTAL
from publications.ch2b
group by AUTHOR_ID
order by Total desc;