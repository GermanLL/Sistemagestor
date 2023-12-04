from Conexion import Conexion
con = Conexion()
con.conectar()
cur = con.c()
print("Bienvenido, por favor ingrese su nombre y su contraseña...")
nom = input("Usuario...")
pas = input("Password...")
query = "SELECT * FROM usuario WHERE nombreusuario = '"+nom+"' AND passusuario = '"+pas+"'"
cur.execute(query)
r = cur.fetchall() #Lista de resultados
while(len(r) == 0):
    print("El usuario NO existe, ingrese nuevamente...")
    nom = input("Usuario...")
    pas = input("Password...")
    query = "SELECT * FROM usuario WHERE nombreusuario = '"+nom+"' AND passusuario = '"+pas+"'"
    cur.execute(query)
    r = cur.fetchall()
for registro in r:
    idUs = registro[0]
print("Bienvenido, identificado correctamente...")
print("1 - Ver lista de productos\n2 - Crear nuevo producto\n3 - Registrar nuevo pedido\n4 - Ver pedidos")
opc = int(input("Ingrese su selección ó -1 para salir"))
while(opc != -1):
    if opc == 1:
        q = "SELECT * FROM producto"
        cur.execute(q)
        resultado = cur.fetchall()
        for res in resultado:
            print(res)
    elif opc == 2:
        n = input("Nombre del nuevo producto")
        d = input("Descripción del nuevo producto")
        p = int(input("Precio del nuevo producto"))
        s = int(input("Stock del nuevo producto"))
        tupla = (n,d,p,s)
        sentencia = "INSERT INTO producto (nombre, descripcion, precio, stock) VALUES (%s,%s,%s,%s)"
        recs = [tupla]
        cur.executemany(sentencia, recs)
        con.grabar()
    elif opc == 3:
        f = input("Ingrese fecha del pedido (dd/mm/yyyy)")
        idU = idUs #ID del usuario, identificado más arriba
        total = 0
        entregado = 'false'
        tupla = (f, idU, total, entregado)
        sentencia = "INSERT INTO pedido (fecha, idautor, total, entregado) VALUES (%s,%s,%s,%s)"
        recs = [tupla]
        cur.executemany(sentencia, recs)
        con.grabar()
        q = "SELECT idpedido FROM pedido ORDER BY idpedido DESC LIMIT 1"
        cur.execute(q)
        resultado = cur.fetchone()
        idPedido = resultado[0]
        print(" ---- Ingrese los productos que estarán en el pedido (-1 para dejar de cargar) ----")
        q = "SELECT * FROM producto"
        cur.execute(q)
        resultado = cur.fetchall()
        for res in resultado:
            print(res)
        idACargar = int(input("Ingrese el ID que desea cargar (-1 para cerrar)"))
        if idACargar != -1:
            cantidad = int(input("Ingrese la cantidad que desea cargar"))
        while(idACargar != -1):
            tupla = (idPedido, idACargar, cantidad)
            sentencia = "INSERT INTO productopedido (idpedido, idproducto, cantidad) VALUES (%s,%s,%s)"
            recs = [tupla]
            cur.executemany(sentencia, recs)
            con.grabar()
            idACargar = int(input("Ingrese el ID que desea cargar (-1 para cerrar)"))

    elif opc == 4:
        q = "SELECT fecha, entregado, nombreusuario FROM pedido INNER JOIN usuario ON pedido.idautor = usuario.id"
        qDos = "select nombre from productopedido inner join producto on productopedido.idproducto = producto.id inner join pedido on pedido.idpedido = productopedido.idpedido"
        cur.execute(q)
        resultado = cur.fetchall()
        cur.execute(qDos)
        productos = cur.fetchall()
        for res in resultado:
            print("----------------------")
            print("Fecha: ", res[0])
            print("Entregado: ", res[1])
            print("Usuario que lo realizó:", res[2])
            print("Lista de productos pedidos:")
            for prod in productos:
                print(prod)
            print("-----  -----------------")     

    else:
        print("Opción inválida")
    print("1 - Ver lista de productos\n2 - Crear nuevo producto\n3 - Registrar nuevo pedido\n4 - Ver pedidos")
    opc = int(input("Ingrese su selección ó -1 para salir"))


con.desconectar()