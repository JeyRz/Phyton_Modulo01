from tarjeta.tarjeta import Tarjeta

class Tarjeta_de_servicios(Tarjeta):
    

    def pago_mayor_deuda(slef, deuda_validar):
        """
        Valida si el pago a realizar es igual al monto de la deuda
        """
        ciclo = True
        while ciclo == True:
            pago_a_realizar = float(input("Digite el pago que desea realizar: ") )
            if pago_a_realizar != deuda_validar:
                print( "El pago debe ser igual monto de la deuda" )
            else:
                ciclo = False
                return pago_a_realizar

#print(Tarjeta_de_servicios.__base__)
#print(tarjeta.Tarjeta.__subclasses__())