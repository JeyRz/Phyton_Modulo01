from tarjeta.tarjetaDB import TarjetaBD
from tarjeta.tarjeta import Tarjeta
import os
import json
import csv

# Definición de constantes
NOMBRE_JSON = "tarjetas.json"
#NOMBRE_CSV = "tarjetas.csv"
NOMBRE_TXT = "log_usuario.txt"


class Usuario():
    def  __init__(self, nombre):
        self.nombre = nombre
        self.tarjetas = []
        self.tabla_db = TarjetaBD()
        self.__log_de_usuario(f"Se crea el usuario {nombre} ")
        self.tabla_db.crear_tabla()
        self.__log_de_usuario(f"Se crea la tabla Tarjeta en una base de datos qlite3 ")
        self.__NOMBRE_CSV = 'tarjetas_'+nombre+'.csv'
        #print("Tabla creada!")
    
    def __del__(self):
        self.tabla_db.cerrar()
        self.__log_de_usuario(f"Se cierra la conexión a la base de datos ")
        if os.path.exists("test.sqlite3"):
            os.remove("test.sqlite3")
        self.__log_de_usuario(f"Se elimina la base de datos")
        

    def __str__(self):
        """ Devuelve la clase usuario en texto"""
        return(self.nombre, self.tarjetas)
    
    def getTarjetas(self):
        return self.tarjetas
    
    def getNombreU(self):
        """ Devuelve el nombre del usuario """
        return(self.nombre)
    
    def numTarjetas(self):
        """ Obtiene la cantidad de tarjetas cargadas """
        return(str(len(self.tarjetas)))

    def multiples_reportes(self, lista_tarjetas):
        """ 
        Permite recorrer una lista de tarjetas e imprimirlas en el reporte
        """
        #recorrer la lista de tarjetas 
        for diccionario_tarjeta in lista_tarjetas:
            #recorrer e imprimir la informacion de cada tarjeta -- diccionario
            self.generar_reporte(diccionario_tarjeta)
        self.__log_de_usuario(f"El usuario imprime las tarjetas de una lista")

    def imprimir_tarjetas(self):
        """
        Permite recorrer una lista de tarjetas de la BD e imprimirlas
        """
        self.__log_de_usuario(f"El usuario imprime las tarjetas de la BD")
        self.__log_de_usuario('-'*120)
        print('-'*120)
        print('{:>20} {:>10} {:10} {:10} {:10} {:10} {:10} {:10}'.\
            format("Nombre","Tasa (%)","Deduda","Pago","Nuevos_cargos",\
            "Deuda_recal", "Tasa_Men", "Nueva_Deuda"))
        self.__log_de_usuario('{:>20} {:>10} {:10} {:10} {:10} {:10} {:10} {:10}'.\
            format("Nombre","Tasa (%)","Deduda","Pago","Nuevos_cargos",\
            "Deuda_recal", "Tasa_Men", "Nueva_Deuda"))
        print('-'*120)
        self.__log_de_usuario('-'*120)
        for reg in self.tabla_db.listar_todo():
            print( "{:>20} {:>10} {:10} {:10} {:10} {:10} {:10} {:10}".format(*reg) )
            self.__log_de_usuario("{:>20} {:>10} {:10} {:10} {:10} {:10} {:10} {:10}".format(*reg))
        print('-'*120)
        self.__log_de_usuario('-'*120)
        print("")

    
    def agregar_tarjeta (self, tarjeta):
        """ 
        Agregar una tarjeta a la base de datos de Tarjeta
        """
        self.tabla_db.insertar(tarjeta.tupla_tarjeta())
        self.__log_de_usuario("El usuario ha insertado una tarjeta a la BD")
        self.__log_de_usuario(tarjeta.texto_tarjeta())
        print("¡Tajeta insertada!")
    
    def borrarTarjeta (self, nombre):
        """ Realiza la búsqueda de una tarjeta por su nombre 
            y la elimina de la lista o borra todas las tarjetas si el nombre es 'Todas' """
        self.tabla_db.borrar(nombre)
        self.__log_de_usuario(f"El usuario ha borrado la(s) tarjeta(s) {nombre}")
        print("¡Su tarjeta(s) ha(n) sido eliminada(s)!")
    
    def buscarTarjeta(self, nombre):
        """ Realiza la busqueda de una tarjeta por su nombre """
        for reg in self.tabla_db.listar_todo():
            #print("reg", reg) #tupla
            if reg[0] == nombre:
                return reg
                break
        self.__log_de_usuario(f"El usuario busca la tarjeta {nombre}")
    
    def getTuplaTarjetas(self):
        """
        Permite obtener en formato tupla la lista de tarjetas
        """
        tupla_tarjetas = []

        #tupla_tarjetas: list = [tupla_tarjetas.append(i.tupla_tarjeta()) for i in self.tarjetas]
        for tarjeta in self.tarjetas:
            tupla_tarjetas.append(tarjeta.tupla_tarjeta())  
        return tupla_tarjetas
    

    def exportar_tarjetas_json(self):
        """ Exporta la lista de tarjetas guardas en la base de datos a formato JSON """
        datos = self.tabla_db.listar_todo()
        #print("datos: ", datos)
        lista_tarjetas = []
        tarjeta_aux = Tarjeta(1)
        [lista_tarjetas.append(tarjeta_aux.tupla_to_dict(tarj)) for tarj in datos]
        #print("lista tarjetas: ", lista_tarjetas)
        with open(NOMBRE_JSON, "w") as arch_txt:
            #for dic in lista_tarjetas:
            json.dump(lista_tarjetas, arch_txt, indent=4)
        print("¡Las tarjetas han sido exportados de forma correcta!")
        self.__log_de_usuario(f"El usuario exporto tarjetas al archivo {NOMBRE_JSON}")
        print("")
    
    def importar_de_json(self):
        """ Importa la lista de tarjetas desde un archivo en formato JSON """
        with open(NOMBRE_JSON) as arch_txt:
            datos = json.load(arch_txt)
        #print("datos json:", datos)
        #tarjetas = []
        for t in datos:  # p es de tipo dict
            tarjeta_aux = Tarjeta(1)
            tarjeta_aux.crearTarjeta(t)
            self.tarjetas.append(tarjeta_aux)
        print("Tarjetas importadas")
        self.__log_de_usuario(f"El usuario importó tarjetas del archivo {NOMBRE_JSON}")
    
    def guardarTarjetasDB(self):
        """ De una lista de tarjetas guardar a BD """
        [self.agregar_tarjeta(t) for t in self.tarjetas]
        self.__log_de_usuario(f"El usuario guardó tarjetas en la BD Tarjetas")
        print("¡Tarjetas guardadas en BD!")


    def guarda_tarjeta_csv(self): # ruta al archivo donde voy a a guardar los resulados
        """
        Guarda los elementos de lista en el archivo en ruta en formato 
        csv
        """
        tupla_titulo = ("Nombre","Tasa (%)","Deduda","Pago","Nuevos_cargos",\
            "Deuda_recal", "Tasa_Men", "Nueva_Deuda")
        # Obtener de BD
        datos = self.tabla_db.listar_todo() #Lista de tuplas
        #print("datos: ", datos)
        with open(self.__NOMBRE_CSV, "w", newline="", encoding="utf-8" ) as arch_texto: 
            escritor_csv = csv.writer(arch_texto, delimiter = ";")
            escritor_csv.writerow(tupla_titulo)
            for elemento in datos: #lista -> [Archivo, Carpeta(), ...]

                escritor_csv.writerow( elemento ) # PAsar en lista
        print(" Tarjetas exportadas a CSV ")
        self.__log_de_usuario(f"El usuario exporto tarjetas al archivo {self.__NOMBRE_CSV}")

    def importar_de_csv(self):
        """ Importa la lista de tarjetas desde un archivo en formato JSON """
        registro = 0
        with open(self.__NOMBRE_CSV, 'r', encoding='utf-8') as arch_txt:
            datos = csv.reader(arch_txt, delimiter=';')
            #print("datos csv:", datos)

            for row in datos:
                if registro == 0:
                    registro += 1
                else:
                    tarjeta = Tarjeta(1)
                    tarjeta.crearTarjetaTupla(row)
                    self.tarjetas.append(tarjeta)
        print("Tarjetas importadas desde archivo CSV")
        self.__log_de_usuario(f"El usuario importó tarjetas del archivo {self.__NOMBRE_CSV}")

    def __log_de_usuario(self, texto): # ruta al archivo donde voy a a guardar los resulados
        """
        Guarda los elementos de lista en el archivo en ruta en formato 
        texto plano
        """
        with open(NOMBRE_TXT, "a", encoding="utf-8" ) as arch_texto: 
            arch_texto.write( texto + "\n")

    def get_reportes_html(self):
        texto = "Reporte del usuario:      {}<br>".format(self.nombre)
        for t in self.tarjetas:
            texto = texto + t.get_reporte_html()
        return texto

