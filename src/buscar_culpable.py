"""
Trabajamos para la mafia de los amigos Amarilla Pérez y el Gringo Hinz. En estos momentos hay un
problema: alguien les está robando dinero. No saben bien cómo, no saben exactamente cuándo, y por
supuesto que no saben quién. Evidentemente quien lo está haciendo es muy hábil (probablemente haya
aprendido de sus mentores).

La única información con la que contamos son n transacciones sospechosas, de las que tenemos un
timestamp aproximado. Es decir, tenemos n tiempos ti, con un posible error ei. Por lo tanto,
sabemos que dichas transacciones fueron realizadas en el intervalo [ti-ei;ti+ei].

Por medio de métodos de los cuales es mejor no estar al tanto, un interrogado dio el nombre de
alguien que podría ser la rata. El Gringo nos pidió revisar las transacciones realizadas por dicha
persona… en efecto, eran nn transacciones. Pero falta saber si, en efecto, condicen con los
timestamps aproximados que habíamos obtenido previamente.

El Gringo nos dio la orden de implementar un algoritmo que determine si, en efecto, las
transacciones coinciden. Amarilla Perez nos sugirió que nos apuremos, si es que no queremos ser
nosotros los siguientes sospechosos…

Hacer un análisis del problema, y proponer un algoritmo greedy que obtenga la solución al problema
planteado: Dados los n valores de los timestamps aproximados ti y sus correspondientes errores
ei, así como los timestamps de las n operaciones si del sospechoso (pueden asumir que estos
últimos vienen ordenados), indicar si el sospechoso es en efecto la rata y, si lo es, mostrar cuál
timestamp coincide con cuál timestamp aproximado y error. Es importante notar que los intervalos de
los timestamps aproximados pueden solaparse parcial o totalmente.
"""

import heapq

def buscar_culpable(t, s):
    return None
