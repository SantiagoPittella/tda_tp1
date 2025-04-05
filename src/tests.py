from src.buscar_culpable import buscar_culpable
from src.helpers import DIRECTORIO_PRUEBAS, coincide_con_esperado, parsear_archivo

def pruebas_catedra():
    import os

    archivos = os.listdir(DIRECTORIO_PRUEBAS)

    for archivo in archivos:
        t, s = parsear_archivo(DIRECTORIO_PRUEBAS + archivo)
        pruebas = buscar_culpable(t, s)
        print("Archivo: {}".format(archivo))
        print("Pruebas esperadas coinciden? {}".format(coincide_con_esperado(pruebas, archivo)))
