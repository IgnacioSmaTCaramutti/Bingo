import math
import random

def carton():
	mi_carton = (
                (1,0,1,1,1,0,1,0,1),
		(0,1,0,1,0,1,1,1,1),
		(0,1,0,0,1,0,0,1,0)
	)
	return mi_carton

def columna(carton, nmro_columna):
	return(
		carton[0][nmro_columna],
		carton[1][nmro_columna],
		carton[2][nmro_columna]
                )

def validar_cantidad_numeros(carton):
    celdas_vacias = 0
    for fila in carton:
        for celda in fila:
            if celda == 0:
                celdas_vacias =  celdas_vacias + 1
    return celdas_vacias == 12

def validar_no_menor(carton):
    celdas_vacias = 0
    for fila in carton:
        for celda in fila:
            if celda == 0:
                celdas_vacias = celdas_vacias + 1
    return celdas_vacias <= 12

def validar_no_mayor(carton):
    celdas_vacias = 0
    for fila in carton:
        for celda in fila:
            if celda == 0:
                celdas_vacias = celdas_vacias + 1
    return celdas_vacias >= 12

def validar_no_columnas_vacias(carton):
    columnas_no_vacias = 0
    for x in range(0,9):
        if carton[0][x]+carton[1][x]+carton[2][x] > 0:
            columnas_no_vacias = columnas_no_vacias + 1
    return columnas_no_vacias == 9


def validar_no_filas_vacias(carton):
    filas_no_vacias = 0
    for x in range(0,3):
        celdas_ocupadas = 0
        for y in range(0,9):
            celdas_ocupadas += carton[x][y]
        if celdas_ocupadas > 0:
            filas_no_vacias = filas_no_vacias + 1
    return filas_no_vacias == 3


def validar_rango(carton):
    casillas_validas = 0
    for fila in range(0,3):
        for columna in range(0,9):
          celda = carton[fila][columna]
          if celda >= 0 and celda <=90:
              casillas_validas = casillas_validas + 1
    return casillas_validas == 27

def validar_numeros_filas(carton):
    celdas_validas = 0
    for columna in range(0,3):
        celda_anterior = -1
        for fila in range(0,9):
            celda = carton[columna][fila]
            if celda > celda_anterior and celda != 0:
                celdas_validas = celdas_validas + 1
            if celda != 0:
                celda_anterior = celda
    return celdas_validas == 15

def validar_numeros_columnas(carton):
    celdas_validas = 0
    for fila in range (0,9):
        celda_anterior = -1
        for columna in range(0,3):
                celda = carton[columna][fila]
                if celda > celda_anterior and celda != 0:
                    celdas_validas = celdas_validas + 1
                if celda != 0:
                    celda_anterior = celda
    return celdas_validas

def validar_repetidos(carton):
    repetidos = True
    elementos_carton = []
    for columna in range(0,3):
        for fila in range(0,9):
            celda = carton[columna][fila]
            if celda != 0:
                elementos_carton.append(celda)
    for columna in range (0,3):
        for fila in range(0,9):
            celda = carton[columna][fila]
            if celda != 0:
                if elementos_carton.count(celda) != 1:
                    repetidos = False
    return repetidos

def validar_cantidad_celdas_por_fila_ocupadas(carton):
    bool_valido = True
    contador = 5
    for x in range(0,3):
        if contador != 5:
            bool_valido = False
        contador = 0
        for y in range(0,9):
            if carton[x][y]!= 0:
                contador = contador + 1
    return bool_valido


def validar_tamanio_carton(carton):
    bool_valido = True
    if len(carton) != 3:
        bool_valido = False
    else:
        for x in range(0,3):
            if len(carton[x]) != 9:
                bool_valido = False
    return bool_valido

def validar_columnas_ocupadas(carton):
    bool_valido = True
    for x in range(0,9):
        if (carton[0][x] == 0) and (carton[1][x] == 0) and (carton[2][x] == 0):
            bool_valido = False
    return bool_valido


def validar_columnas_con_una_celda_ocupada(carton):
    bool_valido = True
    contador_columnas = 0
    for y in range (0,9):
        contador = 0
        for x in range(0,3):
            if carton[x][y] != 0:
                contador = contador + 1
        if contador == 1:
            contador_columnas = contador_columnas + 1
    if contador_columnas != 3:
        bool_valido = False
    return bool_valido

def validar_celdas_vacias_consecutivas(carton):
    bool_valido = True
    for x in range (0,3):
        for y in range (0,7):
            if (carton[x][y] == 0) and (carton[x][y+1] == 0) and (carton[x][y+2] == 0):
                bool_valido = False
    return bool_valido

def validar_celdas_ocupadas_consecutivas(carton):
    bool_valido = True
    for x in range (0,3):
        for y in range (0,7):
            if (carton[x][y] != 0) and (carton[x][y+1] != 0) and (carton[x][y+2] != 0):
                bool_valido = False
    return bool_valido

def intentoCarton():
    contador = 0
    carton = (
        [0,0,0],
        [0,0,0],
        [0,0,0],
        [0,0,0],
        [0,0,0],
        [0,0,0],
        [0,0,0],
        [0,0,0],
        [0,0,0]
    )
    numerosCarton = 0

    while numerosCarton < 15:
        contador += 1
        if contador == 50:
            return intentoCarton()
        numero = random.randint(1, 90)

        columna = math.floor(numero / 10)
        if columna == 9:
            columna = 8
        huecos = 0
        for i in range(0,3): 
            if carton[columna][i] == 0:
                huecos += 1
            if carton[columna][i] == numero:
                huecos = 0
                break
        if huecos < 2:
            continue

        fila = 0
        for j in range(0,3):
            huecos = 0
            for i in range(0,9):
                if carton[i][fila] == 0:
                    huecos += 1

            if huecos < 5 or carton[columna][fila] != 0:
                fila += 1
            else:
                break
        if fila == 3:
            continue

        carton[columna][fila] = numero
        numerosCarton += 1
        contador = 0
    for x in range(0,9):
        huecos = 0
        for y in range (0,3):
            if carton[x][y] == 0:
                huecos += 1
        if huecos == 3:
            return intentoCarton()

    return carton

def imprimirCarton(carton):
    print("\n")
    for fila in range(0,3):
        for columna in range(0,9):
            print(carton[fila][columna], end == ' ')
        print("\n")
    print("\n")

#Se encarga de transformar el carton que pasa intentoCarton a uno que pueda interpretarse por las funciones que ya creamos antes
def transformar_carton(carton):
    carton_interpretable= (
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0]
    )
    for x in range (0,3):
        for y in range (0,9):
            carton_interpretable[x][y] = carton[y][x]
    return carton_interpretable

#Corre todos los tests en el carton que se le pase y devuelve True si pasa todos ellos de forma satisfactoria
def tests_carton(carton_transformado):
    if (validar_cantidad_numeros(carton_transformado) != True) or ((validar_no_menor(carton_transformado) != True) or (validar_no_mayor(carton_transformado) != True) or (validar_no_columnas_vacias(carton_transformado) != True) or (validar_no_filas_vacias(carton_transformado) != True) or (validar_rango(carton_transformado) != True) or (validar_numeros_filas(carton_transformado) != True) or (validar_numeros_columnas(carton_transformado) != 15) or (validar_repetidos(carton_transformado) != True) or (validar_cantidad_celdas_por_fila_ocupadas(carton_transformado) != True) or (validar_tamanio_carton(carton_transformado) != True) or (validar_columnas_ocupadas(carton_transformado) != True) or (validar_columnas_con_una_celda_ocupada(carton_transformado) != True) or (validar_celdas_vacias_consecutivas(carton_transformado) != True) or (validar_celdas_ocupadas_consecutivas(carton_transformado) != True):
        return False
    else:
        return True

#Transforma cada carton generado para luego testearlo, hasta encontrar uno que cumpla con todos los criterios y devolverlo
def carton_definitivo():
    while True:
        carton_original = intentoCarton()
        carton_transformado = transformar_carton(carton_original)
        if tests_carton(carton_transformado) == True:
            break
    return carton_transformado

def main():
    imprimirCarton(carton_definitivo())

if __name__ == '__main__':
    main()
