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
