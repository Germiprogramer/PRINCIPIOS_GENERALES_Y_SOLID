class Pedido:
    def __init__(self, cliente, tipo_pizza, tamano, ingredientes, total):
        self.cliente = cliente
        self.tipo_pizza = tipo_pizza
        self.tamano = tamano
        self.ingredientes = ingredientes
        self.total = total

    def mostrar_pedido(self):
        print(f"Cliente: {self.cliente}")
        print(f"Tipo de pizza: {self.tipo_pizza}")
        print(f"Tamaño: {self.tamano}")
        print(f"Ingredientes: {', '.join(self.ingredientes)}")
        print(f"Total a pagar: {self.total} USD")
