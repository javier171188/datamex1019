#use publications;

#Challenge 1.
# Step 1
select tituloautor.title_id as TITLE_ID, au_id as AUTHOR_ID, 
titulos.price * ventas.qty * titulos.royalty / 100 * tituloautor.royaltyper / 100 as sales_royalty
 from  titleauthor as tituloautor
inner join titles as titulos
on tituloautor.title_id = titulos.title_id
inner join sales as ventas
on  ventas.title_id=tituloautor.title_id;	

#Step 2
create temporary table publications.stp2
select tituloautor.title_id as TITLE_ID, au_id as AUTHOR_ID, 
titulos.price * ventas.qty * titulos.royalty / 100 * tituloautor.royaltyper / 100 as sales_royalty
 from  titleauthor as tituloautor
inner join titles as titulos
on tituloautor.title_id = titulos.title_id
inner join sales as ventas
on  ventas.title_id=tituloautor.title_id;	

select TITLE_ID, AUTHOR_ID, sum(sales_royalty) as ag_royalty from
stp2 group by AUTHOR_ID, TITLE_ID;

#step 3
select TITLE_ID, AUTHOR_ID, sum(sales_royalty) as ag_royalty from
stp2 group by AUTHOR_ID, TITLE_ID 
order by ag_royalty desc limit 3;

#Challenge 2
select TITLE_ID, AUTHOR_ID, sum(sales_royalty) as ag_royalty from
(select tituloautor.title_id as TITLE_ID, au_id as AUTHOR_ID, 
titulos.price * ventas.qty * titulos.royalty / 100 * tituloautor.royaltyper / 100 as sales_royalty
 from  titleauthor as tituloautor
inner join titles as titulos
on tituloautor.title_id = titulos.title_id
inner join sales as ventas
on  ventas.title_id=tituloautor.title_id) as gr
group by AUTHOR_ID, TITLE_ID 
order by ag_royalty desc limit 3;	


#Challenge 3
CREATE TABLE publications.most_profiting_authors
select TITLE_ID, sum(sales_royalty) as profits from
stp2 group by AUTHOR_ID, TITLE_ID 
order by profits desc;





