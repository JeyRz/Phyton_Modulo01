import tarjeta
from tarjeta.tarjetaDB import TarjetaBD
import os


class Usuario():
    def  __init__(self, nombre):
        self.nombre = nombre
        self.tarjetas = []
         # Creación de la base de datos
        #DB = "test.sqlite3"
        self.tabla_db = TarjetaBD()
        self.tabla_db.crear_tabla()
        #print("Tabla creada!")
    
    def __del__(self):
        self.tabla_db.cerrar()
        if os.path.exists("test.sqlite3"):
            os.remove("test.sqlite3")
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
        #for tarjeta in self.tarjetas:
            #recorrer e imprimir la informacion de cada tarjeta -- diccionario
         #   tarjeta.generar_reporte()
        print('-'*120)
        print('{:>20} {:>10} {:10} {:10} {:10} {:10} {:10} {:10}'.\
            format("Nombre","Tasa (%)","Deduda","Pago","Nuevos_cargos",\
            "Deuda_recal", "Tasa_Men", "Nueva_Deuda"))
        print('-'*120)
        for reg in self.tabla_db.listar_todo():
            print( "{:>20} {:>10} {:10} {:10} {:10} {:10} {:10} {:10}".format(*reg) )
        print('-'*120)
        print("")
    
    def agregar_tarjeta (self, tarjeta):
        """ 
        Agregar una tarjeta a la base de datos de Tarjeta
        """
        #self.tarjetas.append(tarjeta)
        # Insertar tarjeta en la BD Tarjeta
        #print("tupla: ", tarjeta.getTuplaTarjetas())
        #tarjeta: Tarjeta
        #print("tupla: ", tarjeta.tupla_tarjeta())
        self.tabla_db.insertar(tarjeta.tupla_tarjeta())
        print("tajeta insertada")
    
    def borrarTarjeta (self, nombre):
        """ Realiza la búsqueda de una tarjeta por su nombre 
            y la elimina de la lista """
        #for tarjeta in self.tarjetas:
        #    if tarjeta.getNombre() == nombre:
        #        self.tarjetas.remove(tarjeta)
        #        break
        self.tabla_db.borrar(nombre)
        print("Su tarjeta ha sido eliminada")
    
    def buscarTarjeta(self, nombre):
        """ Realiza la busqueda de una tarjeta por su nombre """
        for reg in self.tabla_db.listar_todo():
            #print("reg", reg) #tupla
            if reg[0] == nombre:
                return reg
                break

        #for tarjeta in self.tarjetas:
        #    if tarjeta.getNombre() == nombre:
        #        #tarjeta.generar_reporte()
        #        return tarjeta
        #        break
    
    def getTuplaTarjetas(self):
        """
        Permite obtener en formato tupla la lista de tarjetas
        """
        tupla_tarjetas = []

        #tupla_tarjetas: list = [tupla_tarjetas.append(i.tupla_tarjeta()) for i in self.tarjetas]
        for tarjeta in self.tarjetas:
            tupla_tarjetas.append(tarjeta.tupla_tarjeta())  
        return tupla_tarjetas
        