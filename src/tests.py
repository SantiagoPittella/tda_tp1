from src.buscar_culpable import buscar_culpable
from src.helpers import DIRECTORIO_PRUEBAS, coincide_con_esperado, parsear_archivo

def pruebas_catedra():
    import os

    archivos = os.listdir(DIRECTORIO_PRUEBAS)

    for archivo in archivos:
        t, s = parsear_archivo(DIRECTORIO_PRUEBAS + archivo)
        (es_culpable, pruebas) = buscar_culpable(t, s)
        print("Archivo: {}".format(archivo))
        print("Es culpable? {}", es_culpable)
        print("Pruebas esperadas coinciden? {}".format(coincide_con_esperado(pruebas, archivo)))

def pruebas_generadas():
    import os
    from src.test_generator import DIRECTORIO_DE_EJEMPLOS_GENERADOS

    archivos = os.listdir(DIRECTORIO_DE_EJEMPLOS_GENERADOS)

    for archivo in archivos:
        t, s = parsear_archivo(DIRECTORIO_DE_EJEMPLOS_GENERADOS + archivo)
        (es_culpable, _) = buscar_culpable(t, s)
        print("Archivo: {}".format(archivo))
        print("Es culpable? {}", es_culpable)
