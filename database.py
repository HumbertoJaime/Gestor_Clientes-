class Cliente:
    def __init__(self, dni, nombre, apellidoPaterno, apellidoMaterno):
        self.dni =  dni 
        self.nombre = nombre
        self.apellidoPaterno = apellidoPaterno
        self.apellidoMaterno = apellidoMaterno

    def __str__(self) -> str:
        return f"({self.dni}) {self.nombre} {self.apellidoPaterno} {self.apellidoMaterno}"

class Clientes:
    lista = []

    @staticmethod
    def buscar(dni):
        for cliente in Clientes.lista:
            if cliente.dni == dni:
                return cliente

    
    @staticmethod
    def crear(dni, nombre, apellidoPaterno, apellidoMaterno):
        cliente = Cliente(dni, nombre, apellidoPaterno, apellidoMaterno)
        Clientes.listas.append(cliente)
        return cliente

    @staticmethod
    def modificar(dni, nombre, apellidoPaterno, apellidoMaterno):
        for indice,cliente in enumerate(Clientes.lista):
            if cliente.dni == dni:
                Clientes.lista[indice].nombre = nombre
                Clientes.lista[indice].apellidoPaterno = apellidoPaterno
                Clientes.lista[indice].apellidoMaterno = apellidoMaterno
                return cliente
    @staticmethod
    def borrar(dni):
        for indice,cliente in enumerate(Clientes.lista):
            if cliente.dni == dni:
                return Clientes.lista.pop(indice)
                
            