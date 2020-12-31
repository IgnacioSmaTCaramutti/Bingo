
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
#No pueden haber columnas vacìas
def validar_no_columnas_vacias(carton):
    columnas_no_vacias = 0
    for x in range(0,9):
        if carton[0][x]+carton[1][x]+carton[2][x] > 0:
            columnas_no_vacias = columnas_no_vacias + 1
    return columnas_no_vacias == 9

#Las filas no pueden estar absolutamente vacìas
def validar_no_filas_vacias(carton):
    filas_no_vacias = 0
    for x in range(0,3):
        celdas_ocupadas = 0
        for y in range(0,9):
            celdas_ocupadas += carton[x][y]
        if celdas_ocupadas > 0:
            filas_no_vacias = filas_no_vacias + 1
    return filas_no_vacias == 3

#Los numeros deben estar comprendidos entre 1 y 90 (inclusive)
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
