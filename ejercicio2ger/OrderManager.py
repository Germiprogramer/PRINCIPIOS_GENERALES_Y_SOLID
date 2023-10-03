from DataBaseManager import DatabaseManager
from Authenticator import Authenticator
from PaymentProcessor import PaymentProcessor
import csv

class OrderManager(DatabaseManager, Authenticator, PaymentProcessor):
    def __init__(self, database_manager, authenticator, payment_processor):
        self.database_manager = database_manager
        self.authenticator = authenticator
        self.payment_processor = payment_processor

def guardar_pedidos(pedidos):
    with open(pedidos.csv, mode='w', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        # Escribir la cabecera del archivo CSV
        writer.writerow(["Cliente", "Tipo de Pizza", "Tamaño", "Ingredientes", "Total"])

        # Escribir los pedidos en el archivo CSV
        for pedido in pedidos:
            writer.writerow([pedido.cliente, pedido.tipo_pizza, pedido.tamano,
                             ', '.join(pedido.ingredientes), pedido.total])

    print(f"Los pedidos han sido guardados en {pedidos.csv}")
