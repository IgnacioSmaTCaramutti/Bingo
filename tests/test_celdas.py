from src.bingo import carton
from src.bingo import columna

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
