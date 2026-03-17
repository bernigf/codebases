"""
Multiprocessing: Cálculo Pesado (CPU Bound)

Si intentas procesar datos pesados con threading o asyncio,
el GIL hará que los núcleos de tu procesador se turnen,
tardando lo mismo que si fuera secuencial.

Con multiprocessing, creas copias del intérprete en distintos núcleos.
"""

import time
import os

from multiprocessing import Pool

def calcular_pesado(core):
    # Simulación de espera cargando intensamente la CPU
    long_calculation = sum(i * i for i in range(10**7))
    return (core, long_calculation)

if __name__ == "__main__":

    # Simulamos 8 núcleos
    # cores = [1, 2, 3, 4, 5, 6, 7, 8]
    # Otra opcion: usar todos los núcleos disponibles
    cores = [x for x in range(os.cpu_count())]

    print(f"Núcleos disponibles: {len(cores)}")
    
    start = time.time()
    
    # Creamos un pool de procesos (uno por cada núcleo disponible)
    with Pool() as p:        
        # Utilizamos el método 'map' del pool de procesos para aplicar la función 'calcular_pesado'
        # a cada elemento de la lista 'cores'. 
        # Esto significa que Python creará un proceso independiente (en otro núcleo, si está disponible)
        # para cada elemento, ejecutando 'calcular_pesado(n)' para cada 'n' de 'cores'.
        # La función 'map' se comporta de manera similar a la función incorporada 'map', pero distribuye
        # el trabajo entre múltiples procesos, permitiendo el procesamiento en paralelo y,
        # por ende, sacando provecho de sistemas multinúcleo y evitando el GIL. 
        # Al final, 'map' recogerá los valores retornados por cada llamada a 'calcular_pesado'
        # y los devolverá juntos en una lista, preservando el orden de entrada.
        resultado = p.map(calcular_pesado, cores)
    
    print(f"Tiempo total: {time.time() - start:.2f} segundos")
    print(f"Resultado: {resultado}")
    