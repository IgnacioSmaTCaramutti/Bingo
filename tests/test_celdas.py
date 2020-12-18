from src.bingo import carton
from src.bingo import columna

def test_columnas():
	test_carton = carton()
	contador = 0
	bandera_test = 0
	while contador < 9:
		if ((columna(test_carton, contador)) == (0, 0, 0)):
			bandera_test = 1
			break

		contador += 1

	assert bandera_test == 0;
