#Challenge 1
use publications
select autores.au_id as AUTHOR_ID, au_lname as AUTHOR_LAST_NAME, au_fname as FIRST_NAME,
titulos.title as TITLE, editoriales.pub_name as PUBLISHER
from  authors as autores 
inner join titleauthor as tituloautor
on autores.au_id=tituloautor.au_id
inner join titles as titulos
on titulos.title_id = tituloautor.title_id
inner join publishers as editoriales
on editoriales.pub_id= titulos.pub_id;

#Challenge 2
create temporary table publications.cha2
select autores.au_id as AUTHOR_ID, au_lname as AUTHOR_LAST_NAME, au_fname as FIRST_NAME,
titulos.title as TITLE, editoriales.pub_name as PUBLISHER
from  authors as autores 
inner join titleauthor as tituloautor
on autores.au_id=tituloautor.au_id
inner join titles as titulos
on titulos.title_id = tituloautor.title_id
inner join publishers as editoriales
on editoriales.pub_id= titulos.pub_id;


select *, count(*)
from cha2
group by AUTHOR_ID, PUBLISHER;

#Challenge 3
select AUTHOR_ID, AUTHOR_LAST_NAME, FIRST_NAME, count(*) as TOTAL
from cha2
group by AUTHOR_ID
order by TOTAL DESC limit 3;

#CHALLENGE 4
select AUTHOR_ID, AUTHOR_LAST_NAME, FIRST_NAME, count(*) as TOTAL
from cha2
group by AUTHOR_ID
order by TOTAL DESC;
