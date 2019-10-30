USE lab_mysql;
CREATE TABLE autos (nombre VARCHAR(20), numero_identificacion int, marca VARCHAR(20), modelo VARCHAR(20), año DATE, color VARCHAR(20), precio INT, fecha_venta DATE, cliente VARCHAR(50), vendedor VARCHAR(50));
CREATE TABLE vendedores (nombre VARCHAR(50),  fecha_nacimiento DATE, coches_vendidos INT, ganancias BIGINT, numero_id INT, fechas_ventas DATE);
CREATE TABLE clientes (nombre VARCHAR(50), telefono bigint, correo VARCHAR(30), direccion TEXT,  coche_comprado varchar(20),  vendedor_atend varchar(50), fecha_nacimiento DATE, fecha_compra DATE);
CREATE TABLE ventas (coches_vendidos VARCHAR(20), clientes VARCHAR(50), vendedores VARCHAR(50), fechas DATE, precio int, ganancia int);