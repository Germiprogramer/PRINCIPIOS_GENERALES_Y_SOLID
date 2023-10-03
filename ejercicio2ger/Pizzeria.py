from rx.subject import Subject
import random
from Pedido import Pedido

# Clase Pizzeria como observado
class Pizzeria:
    def __init__(self):
        
        self.subject = Subject()

    

    def generar_pedido(self):
        cliente = f"Cliente{random.randint(1, 100)}"
        tipo_pizza = random.choice(["Margarita", "Pepperoni", "Vegetariana"])
        tamano = random.choice(["Pequeña", "Mediana", "Grande"])
        ingredientes = random.sample(["tomate", "mozzarella", "pepperoni", "champiñones", "cebolla"], random.randint(1, 3))
        total = random.uniform(5, 20)
        pedido = Pedido(cliente, tipo_pizza, tamano, ingredientes, total)
        self.subject.on_next(pedido)  # Notificar a los observadores sobre el nuevo pedido

# Clase Pedido (similar a la definición anterior)

# Bloque principal de ejecución
if __name__ == "__main__":
    # Crear observadores (clientes)
    

    # Crear la pizzería como observado
    pizzeria = Pizzeria()
    
    # Generar y procesar los pedidos
    num_pedidos = 5
    for _ in range(num_pedidos):
        pizzeria.generar_pedido()
