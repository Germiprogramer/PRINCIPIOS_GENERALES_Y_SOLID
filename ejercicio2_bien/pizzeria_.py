import tkinter as tk
import csv
from Cliente import Cliente  # Asegúrate de importar la clase Cliente desde el archivo correspondiente

class PizzeriaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Pizzería")

        self.label_usuario = tk.Label(root, text="Usuario:")
        self.label_usuario.pack()
        self.entry_usuario = tk.Entry(root)
        self.entry_usuario.pack()

        self.label_contrasenia = tk.Label(root, text="Contraseña:")
        self.label_contrasenia.pack()
        self.entry_contrasenia = tk.Entry(root, show="*")
        self.entry_contrasenia.pack()

        self.login_button = tk.Button(root, text="Iniciar Sesión", command=self.login)
        self.login_button.pack()

        self.label_pedido = tk.Label(root, text="Realiza tu pedido:")
        self.label_pedido.pack()
        self.entry_pedido = tk.Entry(root)
        self.entry_pedido.pack()

        self.pedido_button = tk.Button(root, text="Realizar Pedido", command=self.realizar_pedido)
        self.pedido_button.pack()

        self.resultado_label = tk.Label(root, text="")
        self.resultado_label.pack()

        # Cargar datos de clientes desde el archivo CSV
        self.clientes = self.cargar_clientes("ejercicio2_bien/clientes.csv")

    def cargar_clientes(self, archivo):
        clientes = []
        with open(archivo, "r") as file:
            reader = csv.DictReader(file, delimiter=';')
            for row in reader:
                cliente = Cliente(row['usuario'],row['nombre'], row['apellido'], row['direccion'], row['telefono'], row['email'],
                                  row['contrasenia'], row['n_pedidos'], row['dinero'])
                clientes.append(cliente)
        return clientes

    def login(self):
        usuario = self.entry_usuario.get()
        contrasenia = self.entry_contrasenia.get()
        for cliente in self.clientes:
            if cliente.usuario == usuario and cliente.contrasenia == contrasenia:
                self.resultado_label.config(text=f"Bienvenido, {usuario}!")
                return
        self.resultado_label.config(text="Usuario o contraseña incorrectos.")

    def realizar_pedido(self):
        cliente = self.entry_usuario.get()
        pedido = self.entry_pedido.get()
        with open("ejercicio2_bien/pedidos.csv", "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([cliente, pedido])
        self.resultado_label.config(text=f"Pedido de {cliente}: {pedido} realizado con éxito!")

if __name__ == "__main__":
    root = tk.Tk()
    app = PizzeriaApp(root)
    root.mainloop()

