DIRECTORIO_PRUEBAS = "ejemplos/"
DIRECTORIO_RES_ESPERADOS = "resultados_esperados/"

def parsear_archivo(archivo):
    # Descarto primer linea (comentario)
    # Segunda linea me da el largo de t y s, llamemoslo N.
    # Itero N veces creando los t.
    # Itero N veces creando los s.
    with open(archivo) as archivo:
        lineas = archivo.readlines()
        n = int(lineas[1])
        t = []
        s = []
        for i in range(n):
            ti = lineas[2 + i]
            [ti, ei] = ti.split(",")
            t.append((int(ti), int(ei)))
            s.append(int(lineas[2 + n + i]))
        return t, s

def coincide_con_esperado(pruebas, archivo):
    with open(DIRECTORIO_RES_ESPERADOS + archivo) as res_esperados:
        return res_esperados.read().rstrip() == serializar_pruebas(pruebas)

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

    return serializado

