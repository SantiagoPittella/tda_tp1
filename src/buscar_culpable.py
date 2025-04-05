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

# El algoritmo busca el culpable de manera greedy ya que su optimo local es el ti + ei mas bajo,
# es decir el tiempo de "finalizacion" de cada intervalo donde hubo actividad sospechosa.
# Su complejidad es O(nlogn) ya que iteramos hasta vaciar un heap de n elementos, en cada iteracion desencolamos
# del heap (operacion que es O(logn)), por tanto la complejidad es O(nlogn)
# El algoritmo es óptimo ya que al ordenar por el final de cada intervalo, dejamos la mayor cantidad de lugar para los siguientes intervalos
# Los casos de prueba proveidos por la catedra dan el resultado correcto.

def buscar_culpable(t, s):
    coincidencias = []
    heap = [(ti[0] + ti[1], ti) for ti in t]
    heapq.heapify(heap)
    i = 0
    dqed = []
    while heap:
        ti = heapq.heappop(heap)
        if ti[1][0] - ti[1][1] <= s[i] <= ti[1][0] + ti[1][1]:
            coincidencias.append((s[i], ti[1]))
            i += 1
            for elem in dqed:
                heapq.heappush(heap, elem)
            dqed = []
            continue
        dqed.append(ti)
    return len(coincidencias) == len(s), coincidencias if len(coincidencias) == len(s) else None
