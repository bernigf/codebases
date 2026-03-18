"""
Limitador de Tasa (Rate Limiter)
Contexto: Evitar que un usuario sature la API de órdenes de compra.
"""

import time

class RateLimiter:
    """
    Implementación de un Fixed Window Rate Limiter.
    En un entorno real, esto usaría Redis para ser distribuido.
    """
    def __init__(self, max_requests: int, window_seconds: int):
        self.max_requests = max_requests
        self.window_seconds = window_seconds
        self.hits = {}

    def is_allowed(self, user_id: str) -> bool:

        current_time = int(time.time())

        # Definimos la ventana actual (ej: cada 60 seg)
        # Calculamos la clave de la ventana de tiempo actual ("window_key").
        # Utilizamos la división entera para agrupar los segundos UNIX actuales en intervalos fijos
        # definidos por 'self.window_seconds'. Por ejemplo, si window_seconds=60, todos los requests recibidos 
        # entre 12:00:00 y 12:00:59 pertenecerán a la misma ventana (tendrán el mismo window_key).
        # Esto permite mitigar ataques o altas frecuencias de solicitudes agrupándolas y limitándolas por ventana,
        # en vez de llevar un registro individualizado por segundo.
        # Ejemplo:
        #   - current_time = 1722420397 (UNIX timestamp)
        #   - window_seconds = 60
        #   - window_key = 1722420397 // 60 = 28707006
        #   Cualquier llamada hecha entre 1722420360 y 1722420419 (inclusive) tendrá el mismo window_key.
        window_key = current_time // self.window_seconds
        identifier = f"{user_id}:{window_key}"

        # Aquí usamos un diccionario `self.hits` para llevar el conteo de solicitudes por usuario y ventana temporal:
        # - La clave `identifier` tiene el formato "<user_id>:<window_key>", agrupando los requests del mismo usuario en la misma ventana.
        # - `self.hits.get(identifier, 0)` devuelve el número de requests registrados hasta ahora para esa clave, retornando 0 si es la primera vez.
        # - Sumamos 1 para reflejar la nueva solicitud entrante.
        # - El valor resultante se almacena de vuelta bajo la misma clave.
        # Ejemplo práctico:
        #   Si es la primera petición del usuario en esta ventana, self.hits[identifier] pasará de no existir a ser 1.
        #   Si ya hubo 3 requests previas en esta ventana, self.hits[identifier] pasará de 3 a 4.
        # Así, este contador nos permite saber si el usuario ha superado el límite configurado en la ventana actual a continuación.
        self.hits[identifier] = self.hits.get(identifier, 0) + 1

        # Si supera el máximo, bloqueamos
        if self.hits[identifier] > self.max_requests:
            return False
        return True

# Ejemplo de uso
limiter = RateLimiter(max_requests=5, window_seconds=10)
user = "user_123"
for i in range(7):
    allowed = limiter.is_allowed(user)
    print(f"Request {i+1}: {'Allowed' if allowed else 'Blocked'}")
    