import sqlite3
#-----------------------------funciones-----------------------------------------------------------
def TUPLAaVARIABLE(tpl):
    lista = list(map(list,tpl))
    for i in range(1):
        for j in range(1):
            variable = lista[i][j]
    return variable

#-----------------------------funciones con base de datos-----------------------------------------------------------
def agregar(codigo,nombre,cantidad):
    conexion = sqlite3.connect("basecompras.db")
    cursor = conexion.cursor()
    prduc = (codigo,nombre,cantidad)
    cursor.execute("INSERT INTO productos VALUES (?,?,?)",prduc)
    conexion.commit()  
    conexion.close()
    

def MOSTRAR():
    conexion = sqlite3.connect("basecompras.db")
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM productos")
    todos = cursor.fetchall()
    print("codigo,producto,cantidad")
    for i in todos:
        print(i)
    print("\n")
    conexion.close()
    
def ESPECIFICO():
    codi = int(input("ingrese el codigo del pruducto: "))
    conexion = sqlite3.connect("basecompras.db")
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM productos WHERE codigo = ?",[codi])
    todos = cursor.fetchall()
    print("codigo,producto,cantidad")
    for i in todos:
        print(i)
    print("\n")
    conexion.close()
    

def modificar(codigo,cantidad):
    conexion = sqlite3.connect("basecompras.db")
    cursor = conexion.cursor()
    sql = "UPDATE productos SET cantidad =? WHERE codigo= ?"
    act = cantidad,codigo
    cursor.execute(sql,act)
    conexion.commit()  
    conexion.close()
    print("se cambio con exito\n")
    
    
    
def CANTIDADDB(co):
    conexion = sqlite3.connect("basecompras.db")
    cursor = conexion.cursor()
    cursor.execute("SELECT cantidad FROM productos WHERE codigo = ? ",[co])
    todos = cursor.fetchall()
    conexion.commit()  
    conexion.close()
    cantidad = TUPLAaVARIABLE(todos)
    return cantidad


def NOMBREDB(co):
    conexion = sqlite3.connect("basecompras.db")
    cursor = conexion.cursor()
    cursor.execute("SELECT nombre FROM productos WHERE codigo = ? ",[co])
    todos = cursor.fetchall()
    conexion.commit()  
    conexion.close()
    nombre = TUPLAaVARIABLE(todos)
    return nombre

def COMPRA():
    MOSTRAR()
    codigo = int(input("ingrese el codigo del pruducto: "))
    cantidad= int(input("ingrese la cantidad del producto la cual desea comprar"))
    nombre = NOMBREDB(codigo)
    print("usted desea hacer una compra de ",cantidad,nombre,"? Y/N")
    op = input()
    if op == "Y" or op =="y":
        cantidadM = CANTIDADDB(codigo)
        cantidad = cantidadM - cantidad
        modificar(codigo,cantidad)
    else:
        print("volver")


def REPONER():
    codigo =int(input("ingrese el codigo del prducto"))
    cantidad= int(input("ingrese la cantidad del producto que haya ingresado"))
    cantidadM = CANTIDADDB(codigo)
    cantidad = cantidad + cantidadM
    modificar(codigo,cantidad)


#-----------------------programa principal-------------------------------------
programa = True
while programa:
    opcion = int(input("elija la opcion\n1 agregar producto \n2 buscar stock del producto \n3 venta\n4 reposicion stock\n5 para salir\n"))
    if opcion == 5:
        programa = False
    elif opcion == 1:
        codigo = int(input("Cual es el codigo del producto: "))
        nombre = input("nombre del porducto: ")
        cantidad = int(input("cantidad del pruducto: "))
        agregar(codigo,nombre,cantidad)
    elif opcion == 2:
        op = int(input("ingresar 1 para buscar un producto especifico o 2 para toda la lista\n"))
        if op == 1:
            ESPECIFICO()
        else:
            MOSTRAR()
    elif opcion == 3:
        COMPRA()
    elif opcion == 4:
        REPONER()
