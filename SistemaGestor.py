def generarDiccionario():
    codigos = [143,568,991,321]
    nombresPrecios = [("Disco rígido SSD",5000), ("Mouse inalámbrico",800), ("Teclado bluetooth",1000), ("Memoria 8GB",5000)]
    datos = dict(zip(codigos, nombresPrecios))
    return datos
def verProductosDisponibles(dicProd):
    cods = list(dicProd.keys()) 
    print("Lista de códigos disponibles para agregar:")
    for i in range(len(cods)) :
        print(cods[i], " | ",dicProd[cods[i]])
def validarCodigo(dicProd, codIngresado):
    cods = list(dicProd.keys())
    if codIngresado in cods:
        return True
    else:
        return False
def agregarProducto(dicProds, codProd, nomProd, precProd):
    datos = dicProds
    tuplaInfo = (nomProd, precProd)
    datos[codProd] = tuplaInfo
    return datos
def agregarAPedido(listaPedidos, tuplaProd):
    lista = listaPedidos
    lista.append(tuplaProd)
    return lista
def verPedido(listaPedidos):
    suma = 0
    for elemento in listaPedidos:
        suma = suma+elemento[1]

        print("Nombre del producto: ", elemento[0], " | Precio: ", elemento[1])
    print("Total del pedido ---- ", suma)

pedido = [] 
print(" ---- Programa gestor de pedidos ---- ")
nombre = input("Por favor, ingrese su nombre...")
print("Estimado " , nombre , " a continuación confeccionaremos su lista de pedidos.")
codigo = -2
datos = generarDiccionario()
while(codigo!=-1) :
    verProductosDisponibles(datos)
    codigo = int(input("¿Qué código desea agregar al pedido? (Ingrese -1 para finalizar)"))
    if(codigo!=-1):
        if(validarCodigo(datos, codigo) == False):
            print("Código ingresado inexistente, por favor elija otro...")
            agregar = input("¿Quiere crear un nuevo producto con el código agregado(S/N)?")
            if(agregar.upper() == "S"):
                nombreProd = input("Ingrese nombre del nuevo producto...")
                precProd = float(input("Ingrese precio del nuevo producto..."))
                datos = agregarProducto(datos, codigo, nombreProd, precProd)
        else:    
            datosAInsertar = datos.get(codigo)
            pedido = agregarAPedido(pedido, datosAInsertar)
            print("Producto cargado con éxito")
   
    print("----------------------------------------")

print("Tu pedido consiste de: ")
verPedido(pedido)