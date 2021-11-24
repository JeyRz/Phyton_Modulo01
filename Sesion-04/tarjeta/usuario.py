from tarjeta.tarjeta import Tarjeta

class Usuario():
    def  __init__(self, nombre):
        self.nombre = nombre
        self.tarjetas = []
    
    def __del__(self):
        print("Objeto de clase Usuario destruido")

    def __str__(self):
        return "Objeto de clase Usuario"

    def multiples_reportes(self, lista_tarjetas):
        """ 
        Permite recorrer una lista de tarjetas e imprimirlas en el reporte
        """
        #recorrer la lista de tarjetas 
        for diccionario_tarjeta in lista_tarjetas:
            #recorrer e imprimir la informacion de cada tarjeta -- diccionario
            self.generar_reporte(diccionario_tarjeta)

    def imprimir_tarjetas(self):
        """
        Permite recorrer una lista de tarjetas e imprimirlas
        """
        #print("tarjetas de usuario", self.tarjetas)
        #recorrer la lista de tarjetas 
        for tarjeta in self.tarjetas:
            #recorrer e imprimir la informacion de cada tarjeta -- diccionario
            tarjeta.generar_reporte()
    
    def agregar_tarjeta (self, tarjeta):
        self.tarjetas.append(tarjeta)
    
    def borrarTarjeta (self, nombre):
        for tarjeta in self.tarjetas:
            if tarjeta.getNombre() == nombre:
                self.tarjetas.remove(tarjeta)
                break
    
    def buscarTarjeta(self, nombre):
        for tarjeta in self.tarjetas:
            if tarjeta.getNombre() == nombre:
                #tarjeta.generar_reporte()
                return tarjeta
                break