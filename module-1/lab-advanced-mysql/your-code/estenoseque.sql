use publications;
select * from sales;
	
select tabids.au_id as AUTHOR_ID,
tabids.title_id as TITLE_ID,
titulos.price
from (publications.authors  autores
inner join publications.titleauthor tabids
on  autores.au_id = tabids.au_id)
left join publications.titles as titulos
on tabids.title_id = titulos.title_id
left join publications.publishers as publications
on titulos.pub_id = publications.pub_id;







select tabids.au_id, tabids.title_id, titulos.price, titulos.royalty, tabids.royaltyper
from (publications.authors  autores
inner join publications.titleauthor tabids
on  autores.au_id = tabids.au_id)
left join publications.titles as titulos
on tabids.title_id = titulos.title_id
left join publications.publishers as publications
on titulos.pub_id = publications.pub_id;

create temporary table publications.sinqty
select tabids.au_id, tabids.title_id, titulos.price, titulos.royalty, tabids.royaltyper
from (publications.authors  autores
inner join publications.titleauthor tabids
on  autores.au_id = tabids.au_id)
left join publications.titles as titulos
on tabids.title_id = titulos.title_id
left join publications.publishers as publications
on titulos.pub_id = publications.pub_id;

select * from sinqty;


select au_id, ventas.title_id, ventas.qty, price, royalty, royaltyper
from publications.sinqty as temporal
left join publications.sales as ventas
on temporal.title_id=ventas.title_id;

create temporary table publications.tab1
select au_id, ventas.title_id, ventas.qty, price, royalty, royaltyper
from publications.sinqty as temporal
left join publications.sales as ventas
on temporal.title_id=ventas.title_id;

select title_id, au_id, (price * qty * royalty / 100 * royaltyper / 100) as sales_royalty
from tab1;

create temporary table publications.tab2
select title_id, au_id, (price * qty * royalty / 100 * royaltyper / 100) as sales_royalty
from tab1;

select title_id, au_id, sum(distinct(sales_royalty)),  as total_sales_royalty
from tab2
group by au_id, title_id

select tabids.au_id, tabids.title_id, titulos.price, titulos.royalty, tabids.royaltyper, titulos.advance
from (publications.authors  autores
inner join publications.titleauthor tabids
on  autores.au_id = tabids.au_id)
left join publications.titles as titulos
on tabids.title_id = titulos.title_id
left join publications.publishers as publications
on titulos.pub_id = publications.pub_id;

create temporary table publications.tab5
select tabids.au_id, tabids.title_id, titulos.price, titulos.royalty, tabids.royaltyper, titulos.advance
from (publications.authors  autores
inner join publications.titleauthor tabids
on  autores.au_id = tabids.au_id)
left join publications.titles as titulos
on tabids.title_id = titulos.title_id
left join publications.publishers as publications
on titulos.pub_id = publications.pub_id;

select tabids.au_id, tabids.title_id, titulos.price, titulos.royalty, tabids.royaltyper, titulos.advance
from (publications.authors  autores	
inner join publications.titleauthor tabids
on  autores.au_id = tabids.au_id)
left join publications.titles as titulos
on tabids.title_id = titulos.title_id
left join publications.publishers as publications
on titulos.pub_id = publications.pub_id;

#challenge  3
select au_id, advance*royaltyper/100 as profits from tab5;