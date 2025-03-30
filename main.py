from expected_results import serializar_pruebas
from tp1 import buscar_culpable2


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
        return res_esperados.read() == serializar_pruebas(pruebas)

def pruebas_catedra():
    import os

    archivos = os.listdir(DIRECTORIO_PRUEBAS)

    for archivo in archivos:
        t, s = parsear_archivo(DIRECTORIO_PRUEBAS + archivo)
        (es_culpable, pruebas) = buscar_culpable2(t, s)
        print("Archivo: {}".format(archivo))
        print("Es culpable: {}".format(es_culpable))
        print("Pruebas esperadas coinciden? {}".format(coincide_con_esperado(pruebas, archivo)))

if __name__ == "__main__":
    pruebas_catedra()
