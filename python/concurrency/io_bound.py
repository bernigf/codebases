""""
Asyncio: Manejo de Conexiones (I/O Bound)
En frameworks modernos como FastAPI, no bloqueas el hilo principal mientras esperas una respuesta de la base de datos o de una API externa.
"""

import asyncio
import random

async def consultar_precio(ticker):
    print(f"Consultando {ticker}...")
    # Simulamos una espera de red (I/O) de 1 segundo
    await asyncio.sleep(1) 
    return {ticker: round(random.random() * 100, 2)}

async def main():
    # Lanzamos todas las consultas concurrentemente
    tickers = ['AAPL', 'GOOGL', 'TSLA', 'MSFT']
    
    # Usamos 'asyncio.gather' para ejecutar múltiples corutinas de manera concurrente.
    # Aquí, construimos una "generator expression" (consultar_precio(t) for t in tickers) que,
    # para cada ticker en nuestra lista 'tickers', crea una corutina que simula una consulta.
    # El operador '*' desempaca la expresión generadora, pasando cada corutina como argumento
    # individual a 'asyncio.gather'. De esta forma, 'gather' las inicia todas al mismo tiempo
    # y aguarda a que todas terminen su ejecución, devolviendo una lista con sus resultados.
    # Usamos 'await' para esperar el resultado final antes de continuar.
    resultados = await asyncio.gather(*(consultar_precio(t) for t in tickers))

    print(f"Resultados: {resultados}")

# El Event Loop gestiona todo en UN solo hilo
asyncio.run(main())
