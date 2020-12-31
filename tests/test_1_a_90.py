from src.bingo import carton
from src.bingo import validar_rango

def test_uno_a_noventa():
    mi_carton = (
       (0,5,0,0,0,0,0,0,1),
       (0,0,0,90,0,2,0,0,0),
       (0,0,6,0,0,0,0,0,76),
   )
    assert validar_rango(mi_carton) == True 
