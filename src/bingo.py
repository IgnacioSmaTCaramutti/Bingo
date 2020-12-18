#Los 0 representan celdas vacias en el carton.
#Los 1 representan celdas ocupadas en el carton.
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

def validar_quince_numeros(carton):
    celdas_vacias = 0
    for fila in carton:
        for celda in fila:
            if celda == 0:
                celdas_vacias =  celdas_vacias + 1
    return celdas_vacias == 12

def validar_no_menor_a_quince(carton):
    celdas_vacias = 0
    for fila in carton:
        for celda in fila:
            if celda == 0:
                celdas_vacias = celdas_vacias + 1
    return celdas_vacias <= 12

def validar_no_mayor_a_quince(carton):
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

#Valida que ninguna de las filas del carton esten absolutamente vacias
def validar_no_filas_vacias(carton):
    filas_no_vacias = 0
    for x in range(0,3):
        celdas_ocupadas = 0
        for y in range(0,9):
            celdas_ocupadas += carton[x][y]
        if celdas_ocupadas > 0:
            filas_no_vacias = filas_no_vacias + 1
    return filas_no_vacias == 3

#Valida que los numeros del carton esten comprendidos entre 1 y 90
def validar_uno_a_noventa(carton):
    casillas_validas = 0
    for fila in range(0,3):
        for columna in range(0,9):
          celda = carton[fila][columna]
          if celda >= 0 and celda <=90:
              casillas_validas = casillas_validas + 1
    return casillas_validas == 27
