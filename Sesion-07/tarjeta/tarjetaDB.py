import sqlite3
#import os

class TarjetaBD ():
    __nombre_tabla = "Tarjeta"
    __tabla_tarjeta = (
        "Nombre VARCHAR(500)",
        "Tasa REAL",  
        "Deuda REAL",
        "Pago REAL",
        "Nuevos_cargos REAL",
        "Tarjeta_recalculada REAL",
        "Tasa_mensual REAL",
        "Nueva_deuda REAL"
    )
    DB = "test.sqlite3"

    def __init__(self):
        """ Construir la clase conexión """
        self.ruta = self.DB
        self.conn = sqlite3.connect(self.DB) #conexión a la bd
        self.cur = self.conn.cursor() #variable que permite interactuar con la bd que nos conectamos

    def __del__(self):
        #archivos_db.cerrar()
        #if os.path.exists(DB):
        #    os.remove(DB)
        print("Objeto de clase TarjetaDB destruido")

    def getTablaTarjeta(self):
        """ Permite obtener la estructura para
            la creación de la tabla tarjeta
        """
        return self.__tabla_tarjeta

    def getNombreTabla(self):
        """ Permite obtener el nombre de la tabla a crear"""
        return self.__nombre_tabla
    
    
    def cerrar(self):
        """ Cierra la conexión a la BD """
        self.cur.close()
        self.conn.close()

    def crear_tabla(self):
        """ Crea tabla con campos en la BD """
        campos_texto = ",".join(self.__tabla_tarjeta)
        sql = f" CREATE TABLE IF NOT EXISTS {self.__nombre_tabla} ({campos_texto})"
        self.cur.execute(sql)
    
    def borrar(self, nombre):
        """ Elimina un registro determinado de la tabla """
        if nombre == 'Todas':
            sql = f"DELETE FROM {self.__nombre_tabla}'"
        else:
            sql = f"DELETE FROM {self.__nombre_tabla} WHERE Nombre = '{nombre}'"

        self.cur.execute(sql)
        self.conn.commit()

    def insertar(self, registros):
        """ Insertar registros en tabla """
        
        #print("registros: ", registros)
        signos: list = [ "?" for t in registros ] # listas de compresión 
        signos: str = ",".join(signos)
        #print("signos:", signos)

        sql = f"INSERT INTO {self.__nombre_tabla} VALUES ({signos})"

        self.cur.execute(sql, registros)
        #self.cur.execute(sql, reg)
        self.conn.commit()

        

    def listar_todo(self):
        """ Regresa la lista de todos los registros en tabla """
        sql = f"SELECT * FROM {self.__nombre_tabla}"
        self.cur.execute(sql)
        datos = self.cur.fetchall()
        #print(datos)
        return datos