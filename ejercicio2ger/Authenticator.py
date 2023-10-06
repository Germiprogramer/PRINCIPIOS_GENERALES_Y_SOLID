from ejercicio2_bien.Cliente import Usuario
import csv 

class Authenticator:
    # Método estático para leer datos desde un archivo CSV y retornar una lista de usuarios
    def __init__(self, user_database):
        self.user_database = user_database


    @staticmethod
    def read_data(self):
        users = []  
        try:
            # Abrimos el archivo CSV en modo lectura y configuramos el delimitador como ";"
            with open(self.user_database, newline="\n") as file:
                reader = csv.reader(file, delimiter=";")
                # Iteramos sobre las filas del archivo CSV y creamos objetos Usuario con los datos
                for dni, nombre, apellido, dinero in reader:
                    user = Usuario(dni, nombre, apellido, dinero)
                    users.append(user)  
        # Manejo de errores
        except FileNotFoundError:
            print(f"El archivo {self.user_database} no fue encontrado.")  
            print(f"Ocurrió un error: {FileNotFoundError}")  
        return users  
    
    @staticmethod
    def write_data(file_path, users):
        # Abrimos el archivo CSV en modo escritura y configuramos el delimitador como ";"
        with open(file_path, "w", newline="\n") as file:
            writer = csv.writer(file, delimiter=";")
            # Iteramos sobre la lista de usuarios y escribimos sus datos en el archivo CSV
            for user in users:
                writer.writerow((user.dni, user.nombre, user.apellido, user.dinero))
