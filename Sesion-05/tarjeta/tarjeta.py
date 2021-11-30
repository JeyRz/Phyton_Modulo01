from copy import copy, deepcopy

class Tarjeta():
    __nombre: str
    __tasa: float
    __deuda: float 
    __pago: float
    __nuevosCargos: float
    __tarjetaRecalculada: float
    __tasaMensual: float
    __nuevaDeduda: float
    __proyeccion : list

    def __init__(self, paso = 0):
        if paso == 0:
            pretarjeta = self.crea_tarjeta()
            tarjeta = self.captura_nueva_deuda(pretarjeta)
            #print(tarjeta)
            """ Atributos de la tarjeta"""
            self.__nombre = tarjeta['Nombre']
            self.__tasa = tarjeta['Tasa']
            self.__deuda = tarjeta['Deuda']
            self.__pago = tarjeta['Pago']
            self.__nuevosCargos = tarjeta['N_cargos']
            self.__tarjetaRecalculada = tarjeta['T_recalculada']
            self.__tasaMensual = tarjeta['T_mensual']
            self.__nuevaDeduda = tarjeta['N_deuda']
        self.__proyeccion = []
        print("Objeto de clase Tarjeta creado")
    
    def crearTarjeta(self, dicTarjeta):
        """ Crea un objeto tarjeta a partir de un diccionario """
        self.__nombre = dicTarjeta['Nombre']
        self.__tasa = dicTarjeta['Tasa']
        self.__deuda = dicTarjeta['Deuda']
        self.__pago = dicTarjeta['Pago']
        self.__nuevosCargos = dicTarjeta['N_cargos']
        self.__tarjetaRecalculada = dicTarjeta['T_recalculada']
        self.__tasaMensual = dicTarjeta['T_mensual']
        self.__nuevaDeduda = dicTarjeta['N_deuda']
        #return self
    
    def crearTarjetaTupla(self, tuplaTarj):
        """ Crea un objeto tarjeta a partir de un diccionario """
        print("tupla recibida: ", tuplaTarj)
        self.__nombre = tuplaTarj[0]
        self.__tasa = tuplaTarj[1]
        self.__deuda = tuplaTarj[2]
        self.__pago = tuplaTarj[3]
        self.__nuevosCargos = tuplaTarj[4]
        self.__tarjetaRecalculada = tuplaTarj[5]
        self.__tasaMensual = tuplaTarj[6]
        self.__nuevaDeduda = tuplaTarj[7]
        return self
        
    def borrar_proyeccion(self):
        """ Borra la lista de una tarjeta proyectada """
        [self.__proyeccion.remove(i) for i in self.__proyeccion]

    def __del__(self):
        print("Objeto de clase Tarjeta destruido")

    def __str__(self):
        return "Objeto de clase Tarjeta"

    def __deepcopy__(self, memo): # memo is a dict of id's to copies
        id_self = id(self)        # memoization avoids unnecesary recursion
        _copy = memo.get(id_self)
        if _copy is None:
            _copy = type(self)(
                deepcopy(self.__nombre, memo), 
                deepcopy(self.__tasa, memo),
                deepcopy(self.__deuda, memo),
                deepcopy(self.__pago, memo),
                deepcopy(self.__nuevosCargos, memo),
                deepcopy(self.__tarjetaRecalculada, memo),
                deepcopy(self.__tasaMensual, memo),
                deepcopy(self.__nuevaDeduda, memo)
                )
            memo[id_self] = _copy 
        return _copy
    
    def obtener_diccionario(self):
        """ Crea un diccionario a partir de un objeto tarjeta """
        diccionario_tarjeta = {'Nombre': self.__nombre, 'Tasa':self.__tasa, 'Deuda': self.__deuda, \
            'Pago': self.__pago, 'N_cargos': self.__nuevosCargos, 'T_recalculada':self.__tarjetaRecalculada, \
            'T_mensual': self.__tasaMensual, 'N_deuda' : self.__nuevaDeduda }    
        return diccionario_tarjeta
    
    def texto_tarjeta(self):
        "Crea la tarjeta en formato texto para insertar a la BD"
        campos_texto = self.__nombre + ","+ str(self.__tasa)+  ","+ str(self.__deuda) +  ","+ str(self.__pago) \
                        +","+ str(self.__nuevosCargos)+","+str(self.__tarjetaRecalculada)+","+str(self.__tasaMensual) \
                        +","+str(self.__nuevaDeduda)
        #print("tarjeta texto:", campos_texto)
        return campos_texto
    
    def tupla_tarjeta(self):
        "Crea la tarjeta en formato texto para insertar a la BD"
        tupla_tarjeta = (self.__nombre, self.__tasa,self.__deuda,self.__pago,
                        self.__nuevosCargos,self.__tarjetaRecalculada,self.__tasaMensual,
                        self.__nuevaDeduda)
        #print("tarjeta texto:", campos_texto)
        return tupla_tarjeta
        
    
    def getProyeccion(self):
        """ Obtiene una lista de la proyección de una tarjeta """
        return self.__proyeccion
    
    def getTarjeta(self):
        return self.__tarjeta
    
    def getDeudaActual(self):
        return self.__deuda
    
    def getNombre(self):
        return self.__nombre
    
    def getTasa(self):
        return self.__tasa
    
    def getPago(self):
        return self.__pago
    
    def getDeudaRecalculada(self):
        return self.__tarjetaRecalculada
    
    def getNuevaDeduda(self):
        return self.__nuevaDeduda
    
    def getTasaMensual (self):
        return self.__tasaMensual
    
    def getNuevosCargos (self):
        return self.__nuevosCargos

    def setDeudaActual(self, deuda):
        self.__deuda = round(deuda,1)
    
    def setNombre (self, nombre):
        self.__nombre =  nombre
    
    def setTasa (self, tasa):
        self.__tasa = tasa
    
    def setPago (self, pago):
        self.__pago = pago
    
    def setDeudaRecalculada (self, t_recalculada):
        self.__tarjetaRecalculada = round(t_recalculada,1)
    
    def setNuevaDeuda (self, n_deuda):
        self.__nuevaDeduda = round(n_deuda,1)

    def setTasaMensual (self, tMensual):
        self.__tasaMensual = round(tMensual,1)
    
    def setNuevosCargos (self, nuevosCargos):
        self.__nuevosCargos = nuevosCargos
 
    def pago_mayor_deuda(slef, deuda_validar):
        """
        Valida si el pago a realizar no es superior a la nueva deuda,
        en caso de que sea mayor solicita un valor váldio
        """
        ciclo = True
        while ciclo == True:
            pago_a_realizar = float(input("Digite el pago que desea realizar: ") )
            if pago_a_realizar > deuda_validar:
                print( "El pago a realizar no puede ser superior a la deuda" )
                #pago_mayor_deuda(deuda_validar, -1)
                #return super.pago_mayor_deuda( deuda_validar, -1)
            else:
                ciclo = False
                return pago_a_realizar

    def crea_tarjeta(self):
        """
        Captura del usuario la nueva tarjeta y calcula la nueva deuda
        """
        try:
            nombre_tarjeta = input("Digite el nombre de la tarjeta: ")
            tasa_de_interes = float(input("Digite la tasa de interés (%) : ") )
            deuda = float(input("Digite el monto de su deuda: ") )

            #Se solicita el pago hasta que sea menor que la deuda
            pago_a_realizar = self.pago_mayor_deuda (deuda)
            #print("Pago", pago_a_realizar)
            
            #Solicitar demás datos
            nuevos_cargos = float(input("Digite nuevos gastos de la tarjeta en caso que tenga: ") )
            diccionario_tarjeta = {'Nombre': nombre_tarjeta, 'Tasa': tasa_de_interes, 'Deuda':deuda, 'Pago': pago_a_realizar,\
            'N_cargos':nuevos_cargos}
            #print('prueba: ',diccionario_tarjeta)
            return diccionario_tarjeta
        except:
            print("Ingreso de datos inválidos.")

    def captura_nueva_deuda (slef, tarjeta_dict, recorre = 0  ):
        """ Permite calcular los intereses mensuales y recalcular una nueva deuda para una tarjeta
            según su monto nuevos cargos y el pago realizado, así como establecer nuevas deudas para una proyección mensual
        """
        try:
            #Calculos de la tarjeta
            tasa_mensual = round(tarjeta_dict['Tasa'] / 12,1)
            interes_mensual = round((tasa_mensual / 100) * (tarjeta_dict['Deuda'] - tarjeta_dict['Pago']),1)
            
            deuda_recalculada2 = ( tarjeta_dict['Deuda'] - tarjeta_dict['Pago'] ) + interes_mensual
            nueva_deuda = deuda_recalculada2 + tarjeta_dict['N_cargos']

            #Agregar nuevo campo al diccionario de tarjeta o reemplazarlo para calcular pago recurrente
            if recorre == 0:
                tarjeta_dict.setdefault('T_recalculada', deuda_recalculada2)
                tarjeta_dict.setdefault('T_mensual', tasa_mensual)
                tarjeta_dict.setdefault('N_deuda', nueva_deuda)

            elif recorre == 2:
                # calcular deuda e imprimir
                tarjeta_dict['T_recalculada'] = deuda_recalculada2
                tarjeta_dict['T_mensual']= tasa_mensual
                tarjeta_dict['N_deuda'] = nueva_deuda
            return tarjeta_dict
        except:
            print("Ingreso de datos inválidos")

    def captura_nueva_deuda_propia (self ):
        """ Permite calcular los intereses mensuales y recalcular una nueva deuda para una tarjeta
            que ya ha sido guardada para un usaurio para la funcion pago recurrente
        """
        interes_mensual = round((self.getTasaMensual() / 100) * (self.getDeudaActual() - self.getPago()),1)
        
        deuda_recalculada2 = ( self.getDeudaActual() - self.getPago() ) + interes_mensual
        nueva_deuda = deuda_recalculada2 + self.getNuevosCargos()
        #print("Punto nrecalc:", deuda_recalculada2)
        #Agregar nuevo campo al diccionario de tarjeta o reemplazarlo para calcular pago recurrente
            # calcular deuda e imprimir
        self.setDeudaRecalculada(deuda_recalculada2) 
        self.setNuevaDeuda(nueva_deuda)

    
    def generar_reporte(self):
        """
        Recibe una tarjeta y la imprime en el formato adecuado 
        """
        print('-'*60)
        print('-'*15 , " Resumen de la tajeta de crédito ", '-'*15)
        print('-'*60)
        print('{:>30} {:>20}'.format('Tarjeta a nombre de:', self.__nombre ) )
        print('{:>30} {:>20}%'.format('Tasa de interés anual:', self.__tasa ) )
        print('-'*60)
        print('{:>30} {:>20}'.format('Deuda actual:', self.__deuda ) )
        print('{:>30} {:>20}'.format('Monto del pago:', self.__pago ) )
        print('-'*60)
        print('{:>30} {:>20}'.format('Deuda después del pago:', self.__deuda - self.__pago ) )
        print('{:>30} {:>20}'.format('Intereses del mes:', self.__tasaMensual ) )
        print('-'*60)
        print('{:>30} {:>20.2f}'.format('Deuda recalculada:', self.__tarjetaRecalculada ) )
        print('{:>30} {:>20}'.format('Nuevos cargos:', self.__nuevosCargos ) )
        print('-'*60)
        print('{:>30} {:>20}'.format('Nueva deuda del mes:', self.__nuevaDeduda ) )
        print("")
        print("")
        print("")


    def pago_recurrente(self):
        """ Permite recibir una tarjeta y proyectar los pagos de distintos meses con un mismo pago hasta 
            que su deuda sea 0
        """
        print("tarjeta: ", self.__str__)
        while self.getPago() < self.getDeudaActual():
            #crea diccionarios y los guarda en una lista pra su proyeccion
            dicc_tarjetas = self.obtener_diccionario()
            self.__proyeccion.append(dicc_tarjetas)

            self.generar_reporte()
            self.setDeudaActual(self.getNuevaDeduda() ) 
            self.setNuevosCargos(0)
            # Calcular nueva deuda con el mismo pago
            self.captura_nueva_deuda_propia()

        
        if self.getNuevaDeduda() <= self.getPago():
            self.setPago(self.getDeudaActual())
            self.setTasaMensual(0)
            self.setDeudaRecalculada(0)
            self.setNuevaDeuda(0)

            self.generar_reporte()
            #crea diccionarios y los pone en la lista
            dicc_tarjetas = self.obtener_diccionario()
            self.__proyeccion.append(dicc_tarjetas)
    
    def pago_recurrente_dif_pagos(self):
        """
        Mediante una tarjeta permite calcular un pago recurrente diferente
        hasta cancelar la totalidad de la deuda.
        """

        while self.getPago() < self.getDeudaActual():

            self.generar_reporte()

            dicc_tarjetas = self.obtener_diccionario()
            self.__proyeccion.append(dicc_tarjetas)


            self.setDeudaActual ( self.getNuevaDeduda() )
            # Capturar nuevo pago
            nuevo_pago = self.pago_mayor_deuda (self.getDeudaActual() )
            self.setPago(nuevo_pago)
            self.setNuevosCargos(0)
            self.captura_nueva_deuda_propia()
        
        if self.getNuevaDeduda() <= 0:

            self.setPago(self.getDeudaActual() )
            self.setTasaMensual(0)
            self.setDeudaRecalculada(0)
            self.setNuevaDeuda(0)
            self.generar_reporte()

            dicc_tarjetas = self.obtener_diccionario()
            self.__proyeccion.append(dicc_tarjetas)


