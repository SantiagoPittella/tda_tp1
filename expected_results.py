"""
Dado un resultado en formato [(s_1, (t_1, e_1)), ..., (s_i, (t_i, e_i)] para casos donde el sospechoso
es culpable, o None cuando no lo es, creamos lineas compatibles con el mismo formato dado en el
archivo [Resultados Esperados.txt] con el fin de comprobar si el resultado es el esperado.
"""

def serializar_pruebas(resultado):
    if not resultado:
        return "No es el sospechoso correcto"
    
    serializado = ""
    for (s_i, (t_i, e_i)) in resultado:
        serializado += "{} --> {} ± {}\n".format(s_i, t_i, e_i) 

    return serializado + "\n"

