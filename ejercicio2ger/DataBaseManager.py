from Authenticator import Authenticator
from ejercicio2_bien.Cliente import Usuario
import csv
import config

# Clase encargada de manejar las operaciones de la base de datos de usuarios
class DataBaseManager:
    # Constructor de la clase, recibe una cadena de conexión y carga los usuarios desde el archivo CSV
    def __init__(self, connection_string):
        self.connection_string = connection_string 
        self.lista = Authenticator.read_data(config.DATABASE_PATH)  # Cargamos los usuarios desde el archivo CSV
    
    # Método para buscar un usuario por su número de identificación (DNI)
    def buscar(self, dni):
        for user in self.lista:
            if user.dni == dni:
                return user 
        return None  
    
    # Método para crear un nuevo usuario y agregarlo a la lista de usuarios
    def crear(self, dni, nombre, apellido, dinero):
        user = Usuario(dni, nombre, apellido, dinero)  
        self.lista.append(user)  
        self.guardar() 
        return user  
    
    # Método para modificar los datos de un usuario existente
    def modificar(self, dni, nombre, apellido, dinero):
        for user in self.lista:
            if user.dni == dni:
                user.nombre = nombre 
                user.apellido = apellido 
                user.dinero = dinero
                self.guardar()  # Llamamos al método guardar para escribir los cambios en el archivo CSV
                return user  
        return None  
    
    # Método para borrar un usuario por su número de identificación (DNI)
    def borrar(self, dni):
        for user in self.lista:
            if user.dni == dni:
                self.lista.remove(user)  
                self.guardar()  
                return user  
        return None  
    
    # Método para guardar los cambios en la lista de usuarios al archivo CSV
    def guardar(self):
        Authenticator.write_data(config.DATABASE_PATH, self.lista)  

# Bloque principal de ejecución del programa
if __name__ == "__main__":
    # Creamos una instancia de DataBaseManager con la cadena de conexión desde config
    manager = DataBaseManager(config.connection_string)
    
    # Ejemplos de uso de las operaciones del DataBaseManager
    # manager.crear("123", "Alice", "Johnson")
    # usuario = manager.buscar("123")
    # manager.modificar("123", "Alice", "Smith")
    # usuario_modificado = manager.buscar("123")
    # manager.borrar("123")


class ClienteDataBaseManager:
    def __init__(self, csv_path):
        self.csv_path = csv_path

    def buscar(self, dni):
        with open(self.csv_path, 'r', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row['dni'] == dni:
                    return row
        return None

    def crear(self, dni, nombre, apellido, dinero):
        with open(self.csv_path, 'a', newline='') as csvfile:
            fieldnames = ['dni', 'nombre', 'apellido', 'dinero']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writerow({'dni': dni, 'nombre': nombre, 'apellido': apellido, 'dinero': dinero})

    # Implementa los métodos modificar y borrar según sea necesario

    def cerrar_conexion(self):
        pass  # No es necesario cerrar un archivo CSV

class PedidoDataBaseManager:
    def __init__(self, csv_path):
        self.csv_path = csv_path

    def guardar_pedido(self, pedido):
        with open(self.csv_path, 'a', newline='') as csvfile:
            fieldnames = ['cliente', 'tipo_pizza', 'tamano', 'ingredientes', 'total']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writerow({'cliente': pedido.cliente,
                             'tipo_pizza': pedido.tipo_pizza,
                             'tamano': pedido.tamano,
                             'ingredientes': ', '.join(pedido.ingredientes),
                             'total': pedido.total})

    def cerrar_conexion(self):
        pass  # No es necesario cerrar un archivo CSV

if __name__ == "__main__":
    # Crear instancias de los manejadores de bases de datos para clientes y pedidos
    cliente_db_manager = ClienteDataBaseManager('clientes.csv')
    pedido_db_manager = PedidoDataBaseManager('pedidos.csv')

    # Ejemplo de creación de un cliente
    cliente_db_manager.crear("123", "Alice", "Johnson", 100)

    # Pizzería y Cliente (clases Pizzeria y Cliente del código anterior)

    # Generar y procesar los pedidos concurrentemente
    with concurrent.futures.ThreadPoolExecutor() as executor:
        for _ in range(num_pedidos):
            pedido = pizzeria.generar_pedido()
            executor.submit(Usuario.realizar_pedido, pedido)  # Simular la realización del pedido por el cliente
            pedido_db_manager.guardar_pedido(pedido)  # Guardar el pedido en el archivo CSV de pedidos

    # No es necesario cerrar conexiones con archivos CSV
