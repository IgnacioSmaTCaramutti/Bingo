from src.bingo import carton
from src.bingo import columna
from src.bingo import validar_quince_numeros
from src.bingo import validar_no_menor_a_quince
from src.bingo import validar_no_mayor_a_quince
from src.bingo import validar_no_columnas_vacias

def test_columnas(): #Verifica que no haya filas vacias
	test_carton = carton()
	contador = 0
	bandera = 0
	while contador < 9: #revisa las 9 columnas
		if ((columna(test_carton, contador)) == (0, 0, 0)): #en caso de haber una columna vacia
			bandera = 1#bandera
			break

		contador += 1

	assert bandera == 0;
        

def test_filas():#verifica que no haya filas vacias
	carton_filas= carton()
	contador = 0
	bandera = 0
	while contador < 3:#revisa las tres filas
		if ((carton_filas[contador]) == (0,0,0,0,0,0,0,0,0)):#si hay una fila vacia
			bandera = 1#pone una bandera
			break

		contador += 1

	assert bandera == 0

def test_contar_celdas_ocupadas():
    mi_carton = (
            (1,0,1,0,0,1,0,1,1),
            (1,1,0,1,1,0,1,0,1),
            (1,0,0,0,1,0,0,1,1),
   )
    assert validar_quince_numeros(mi_carton) == True

def test_celdas_menor_15():
    mi_carton = carton()
    contador = 0
    for fila in mi_carton:
        for celda in fila:
            contador = contador + celda
    assert contador >= 15

def test_celdas_mayor_15():
    mi_carton = carton()
    contador = 0
    for fila in mi_carton:
        for celda in fila:
            contador = contador + celda
    assert contador <= 15
