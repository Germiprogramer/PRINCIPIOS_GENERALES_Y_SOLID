import tkinter as tk
import csv

class PizzeriaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Pizzería")

        self.label_usuario = tk.Label(root, text="Usuario:")
        self.label_usuario.pack()
        self.entry_usuario = tk.Entry(root)
        self.entry_usuario.pack()

        self.label_contraseña = tk.Label(root, text="Contraseña:")
        self.label_contraseña.pack()
        self.entry_contraseña = tk.Entry(root, show="*")
        self.entry_contraseña.pack()

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

        # Cargar datos de clientes y pedidos desde los archivos CSV
        self.clientes = self.cargar_csv("ejercicio2_bien/clientes.csv")
        self.pedidos = self.cargar_csv("ejercicio2_bien/pedidos.csv")

    def cargar_csv(self, archivo):
        with open(archivo, "r") as file:
            reader = csv.DictReader(file)
            data = [row for row in reader]
        return data

    def login(self):
        usuario = self.entry_usuario.get()
        contraseña = self.entry_contraseña.get()
        for cliente in self.clientes:
            if cliente["nombre"] == usuario and cliente["contraseña"] == contraseña:
                self.resultado_label.config(text=f"Bienvenido, {usuario}!")
                return
        self.resultado_label.config(text="Usuario o contraseña incorrectos.")

    def realizar_pedido(self):
        cliente = self.entry_usuario.get()
        pedido = self.entry_pedido.get()
        with open("pedidos.csv", "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([cliente, pedido])
        self.resultado_label.config(text=f"Pedido de {cliente}: {pedido} realizado con éxito!")

if __name__ == "__main__":
    root = tk.Tk()
    app = PizzeriaApp(root)
    root.mainloop()
