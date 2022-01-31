import random
import pandas as pd
def Relleno(f,c,matriz):
    nombres = ["Lucas","mariano","Juan","Matias","ignacio","Tobias","Pablo"]
    apellido = ["Lopez","Garcia","Morales","Sandobal","Gonzales","Montero","Vera"]
    productos = ["Clavos","Maritillos","Metro","Cierra","Destornilladores","Pinzas","Guantes","Taladro","Solador","Cepillo","Pulidora","Alambre"]
    precioUnidad = [1,15,10,12,8,9,13,20,50,5,30,5]
    p = len(productos)
    p = p - 1
    
    for i in range(f):
        for j in range(c):
            #nombre
            n = random.randint(0,6)
            matriz[i][1] = nombres[n]
            #apellido
            n = random.randint(0,6)
            matriz[i][2] = apellido[n]
            #producto
            n = random.randint(0,p)
            matriz[i][3] = productos[n]
            #cantidad
            c = random.randint(1,100)
            matriz[i][4] = c
            #precio
            h = precioUnidad[n]*c
            matriz[i][5] = h
    return matriz
                


def Dni(f,c,matriz):
    datos = {}
    
    for i in range(f):
        c1 = matriz[i][1]
        c2 = matriz[i][2]
        c1 = c1+c2
        valores = datos.keys()
        if c1 in valores:
            ag = datos[c1]
            matriz[i][0] = ag
                
            
        else:
            ag = random.randint(2000000,5000000)
            matriz[i][0] = ag
            datos.update({c1:ag})
    
    
    return matriz

def Data(matriz):
    data = pd.DataFrame(matriz,columns=['DNI','Nombre','apellido','producto','cantidad','precio total'])
    return data


###############################################################################################################################


f= 200
c= 6
matriz = [[0]*c for i in range(f)]

matriz1 = Relleno(f,c,matriz)
matriz2 = Dni(f,c,matriz1)

matrizData = Data(matriz2)



matrizData.to_csv('ventas1.csv',index=False)


