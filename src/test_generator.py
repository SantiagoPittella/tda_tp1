import random
import os

DIRECTORIO_DE_EJEMPLOS_GENERADOS = "ejemplos_generados/"

def generar_caso_de_prueba(n, es_valido):
    """
    Genera un caso de prueba para buscar_culpable/2
    
    Args:
        n: Numero de timestamps a generar 
        es_valido: Si es True, genera un caso de prueba valido donde todos los timestamps pueden ser encontrados
                   Si es False, genera un caso de prueba invalido donde al menos un timestamp no puede ser encontrado
 
    Returns:
        Un tupla que contiene:
        - Lista de tuplas (timestamp, error)
        - Lista de timestamps del sospechoso
    """
    # Generar timestamps base
    timestamps_base = sorted([random.randint(0, 1000) for _ in range(n)])
    
    # Generar errores que sean suficientemente grandes para permitir superposiciones
    errores = [random.randint(5, 20) for _ in range(n)]
    
    # Generar timestamps del sospechoso
    if es_valido:
        # Para casos validos, asegurar que cada timestamp del sospechoso caiga dentro de al menos uno de los intervalos
        timestamps_sospechosos = []
        for i in range(n):
            # Elegir un timestamp aleatorio dentro del intervalo [t-e, t+e]
            t, e = timestamps_base[i], errores[i]
            timestamps_sospechosos.append(random.randint(t - e, t + e))
    else:
        # Para casos invalidos, asegurar que al menos un timestamp caiga fuera de todos los intervalos
        timestamps_sospechosos = []
        for i in range(n):
            if i == n-1:  # Hacer el último timestamp invalido
                # Elegir un timestamp que esté definitivamente fuera de todos los intervalos
                max_interval_end = max(t + e for t, e in zip(timestamps_base, errores))
                timestamps_sospechosos.append(max_interval_end + random.randint(1, 10))
            else:
                # Elegir un timestamp valido para otras posiciones
                t, e = timestamps_base[i], errores[i]
                timestamps_sospechosos.append(random.randint(t - e, t + e))
    
    # Ordenar timestamps del sospechoso
    timestamps_sospechosos.sort()
    
    # Crear la lista de tuplas (timestamp, error)
    timestamp_tuples = list(zip(timestamps_base, errores))
    
    return timestamp_tuples, timestamps_sospechosos

def guardar_caso_de_prueba(t, s, n, es_valido, directorio_de_resultados, random_value=None):
    """
    Guarda un caso de prueba en un archivo
    
    Args:
        t: Lista de tuplas (timestamp, error)
        s: Lista de timestamps del sospechoso
        n: Numero de timestamps
        es_valido: Si el caso de prueba es valido
        directorio_de_resultados: Directorio para guardar el archivo
        random_value: Valor aleatorio para el nombre del archivo (opcional)
    """
    # Crear directorio de salida si no existe
    os.makedirs(directorio_de_resultados, exist_ok=True)
    
    # Crear nombre de archivo
    sufijo = "es" if es_valido else "no-es"
    if random_value is None:
        random_value = random.randint(1000, 9999)
    nombre_archivo = f"{n}-{sufijo}-{random_value}.txt"
    ruta_archivo = os.path.join(directorio_de_resultados, nombre_archivo)
    
    # Escribir en el archivo
    with open(ruta_archivo, 'w') as f:
        # Escribir encabezado
        f.write("# Primero viene la cantidad (n) de timestamps para ambos, luego n líneas que son un timestamp aproximado cada uno separado por una coma (',') del error, y luego n lineas de las transacciones del sospechoso\n")
        
        # Escribir n
        f.write(f"{n}\n")
        
        # Escribir timestamps con errores
        for timestamp, error in t:
            f.write(f"{timestamp},{error}\n")
        
        # Escribir timestamps del sospechoso
        for timestamp in s:
            f.write(f"{timestamp}\n")

def generar_y_guardar_casos(n_values, casos_por_n, directorio_de_resultados):
    """
    Genera y guarda casos de prueba para diferentes valores de n
    
    Args:
        n_values: Lista de valores de n para generar casos de prueba
        casos_por_n: Numero de casos a generar para cada valor de n
        directorio_de_resultados: Directorio para guardar los archivos
    """
    for n in n_values:
        for i in range(casos_por_n):
            # Generar caso de prueba valido
            t_valid, s_valid = generar_caso_de_prueba(n, es_valido=True)
            guardar_caso_de_prueba(t_valid, s_valid, n, es_valido=True, 
                                 directorio_de_resultados=directorio_de_resultados,
                                 random_value=i)
            
            # Generar caso de prueba invalido
            t_invalid, s_invalid = generar_caso_de_prueba(n, es_valido=False)
            guardar_caso_de_prueba(t_invalid, s_invalid, n, es_valido=False, 
                                 directorio_de_resultados=directorio_de_resultados,
                                 random_value=i)

if __name__ == "__main__":
    # Generar casos de prueba para diferentes valores de n
    n_values = [5, 10, 50, 100, 500, 1000, 5000]
    casos_por_n = 3  # Generar 3 casos de prueba para cada valor de n
    generar_y_guardar_casos(n_values, casos_por_n, DIRECTORIO_DE_EJEMPLOS_GENERADOS)
