from src.bingo import carton
from src.bingo import validar_numeros_filas
from src.bingo import validar_numeros_columnas

def test_avance_filas():
    mi_carton = (
       (1,0,3,0,0,15,0,0,30),
       (4,5,0,8,77,0,78,0,79),
       (45,55,65,0,0,75,80,0,0),
   )
    assert validar_numeros_filas(mi_carton) == True

def test_avance_columnas():
    mi_carton = (
       (60,0,3,0,0,17,0,1,39),
       (70,20,0,38,8,0,22,0,0),
       (80,30,25,0,70,0,90,0,0),
   )
    assert validar_numeros_columnas(mi_carton) == 15
