class Usuario:
    def __init__(self, nombre, apellido, direccion, telefono, email, password, n_pedidos, dinero):
        self.nombre = nombre
        self.apellido = apellido
        self.direccion = direccion
        self.telefono = telefono
        self.email = email
        self.password = password
        self.n_pedidos = n_pedidos
        self.dinero = dinero
       


    def __str__(self):
        return f"({self.dni}) {self.nombre} {self.apellido} - Dinero: {self.dinero}"

    def to_dict(self):
        return {'dni': self.dni, 'nombre': self.nombre, 'apellido': self.apellido, 'dinero': self.dinero}
    


