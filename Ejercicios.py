import math

def promedio_std(lista):
    n = len(lista)
    if n<1:
        return None
    x = sum(lista) / n
    suma_cuadrados_diferencias = sum((z-x)**2 for z in lista)
    y = math.sqrt(suma_cuadrados_diferencias / n)

    return x,y

print(promedio_std([0,0,2,5,8,1,2,1,2,6,]))



def color_frecuente (lista):
    prioridad_colores = ['azul','rojo','verde','amarillo']

    conteo_colores = {}
    for color in lista:
        conteo_colores[color] = conteo_colores.get(color,0)+1

    max_frecuencia = max(conteo_colores.values())

    colores_max_frecuencia = [color for color,frecuencia in conteo_colores.items() if frecuencia == max_frecuencia]

    for color in prioridad_colores:
        if color in colores_max_frecuencia:
            return color,max_frecuencia
      
liista = ['azul', 'rojo', 'verde', 'verde', 'verde', 
          'rojo', 'verde', 'verde', 'azul', 'amarillo', 
          'azul', 'azul', 'verde', 'verde', 'verde', 'amarillo',
          'amarillo']
liiista = ['rojo', 'rojo', 'azul', 'azul']
print(color_frecuente(liista))
print(color_frecuente(liiista))

tablero = [[' ', 'X', ' ', 'X'],['X', ' ', ' ', ' '],[' ', 'X', 'X', ' '],['X', ' ', ' ', 'X']]

def buscaminas (tablero,i,j):
    filas = len(tablero)
    columnas = len(tablero[0])
    bombas_alrededor = 0

    for x in range (max (0, i-1) , min(filas,i+2)):
        for y in range (max (0, j-1), min(columnas, j+2)):
            if (x,y) != (i,j) and tablero [x][y] == 'X':
                bombas_alrededor+=1
    return bombas_alrededor

print(buscaminas(tablero,5,5))
