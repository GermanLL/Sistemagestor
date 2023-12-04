SELECT nombre,cantidad FROM productopedido INNER JOIN producto ON productopedido.idproducto = producto.id WHERE idpedido = 2;

select nombreusuario from pedido inner join usuario on pedido.idautor = usuario.id where idpedido = 2;

select nombre from productopedido inner join producto on productopedido.idproducto = producto.id inner join pedido on pedido.idpedido = productopedido.idpedido where entregado = false;

update pedido set entregado = true where idpedido = 2;

SELECT * FROM producto ORDER BY precio desc;

SELECT * FROM producto GROUP BY id;

select sum(precio) from producto;

select min(precio) from producto;