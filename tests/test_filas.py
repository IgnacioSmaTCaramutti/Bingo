from src.bingo import carton
from src.bingo import validar_no_filas_vacias

def test_filas_vacias():
    mi_carton = (
       (0,0,0,0,0,0,0,0,1),
       (0,0,0,0,0,0,1,0,0),
       (0,0,0,0,0,0,0,0,1),
   )
    assert validar_no_filas_vacias(mi_carton) == True
