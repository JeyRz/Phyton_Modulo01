from tarjeta.usuario import generar_reporte

#Validar deuda y pago
def pago_mayor_deuda( deuda_validar, ciclo = -1):
    """
    Valida si el pago a realizar no es superior a la nueva deuda,
    en caso de que sea mayor solicita un valor váldio
    """
    if ciclo == -1:
        pago_a_realizar = float(input("Digite el pago que desea realizar: ") )
        if pago_a_realizar > deuda_validar:
            print( "El pago a realizar no puede ser superior a la deuda" )
            #pago_mayor_deuda(deuda_validar, -1)
            return pago_mayor_deuda(deuda_validar, -1)
        else:
            return pago_a_realizar

def crea_tarjeta():
    """
    Captura del usuario la nuva tarjeta y calcula la nueva deuda
    """

    nombre_tarjeta = input("Digite el nombre de la tarjeta: ")
    tasa_de_interes = float(input("Digite la tasa de interés (%) : ") )
    deuda = float(input("Digite el monto de su deuda: ") )

    #Se solicita el pago hasta que sea menor que la deuda
    pago_a_realizar = pago_mayor_deuda (deuda)
    #print("Pago", pago_a_realizar)
    
    #Solicitar demás datos
    nuevos_cargos = float(input("Digite nuevos gastos de la tarjeta en caso que tenga: ") )
    diccionario_tarjeta = {'Nombre': nombre_tarjeta, 'Tasa': tasa_de_interes, 'Deuda':deuda, 'Pago': pago_a_realizar,\
    'N_cargos':nuevos_cargos}
    #print('prueba: ',diccionario_tarjeta)
    return diccionario_tarjeta

def captura_nueva_deuda ( tarjeta_dict, recorre = 0  ):
    """ Permite calcular los intereses mensuales y recalcular una nueva deuda para una tarjeta
        según su monto nuevos cargos y el pago realizado, así como establecer nuevas deudas para una proyección mensual
    """
    #Calculos de la tarjeta
    tasa_mensual = tarjeta_dict['Tasa'] / 12
    interes_mensual = (tasa_mensual / 100) * (tarjeta_dict['Deuda'] - tarjeta_dict['Pago'])
    
    deuda_recalculada2 = ( tarjeta_dict['Deuda'] - tarjeta_dict['Pago'] ) + interes_mensual
    nueva_deuda = deuda_recalculada2 + tarjeta_dict['N_cargos']

    #print("pasa punto", tarjeta_dict)
    #Agregar nuevo campo al diccionario de tarjeta o reemplazarlo para calcular pago recurrente
    if recorre == 0:
        tarjeta_dict.setdefault('T_recalculada',deuda_recalculada2)
        tarjeta_dict.setdefault('T_mensual',tasa_mensual)
        tarjeta_dict.setdefault('N_deuda', nueva_deuda)

    elif recorre == 2:
        # calcular deuda e imprimir
        #print("pasa")
        tarjeta_dict['T_recalculada'] = deuda_recalculada2
        tarjeta_dict['T_mensual']= tasa_mensual
        tarjeta_dict['N_deuda'] = nueva_deuda

    return tarjeta_dict


def pago_recurrente(tarjeta_dict):
    """ Permite recibir una tarjeta y proyectar los pagos de distintos meses con un mismo pago hasta 
        que su deuda sea 0
    """

    print("pago tarjeta", tarjeta_dict)

    while tarjeta_dict['Pago'] < tarjeta_dict['Deuda']:

        generar_reporte(tarjeta_dict)
        
        # Nueva deuda igual a la deuda
        tarjeta_dict['Deuda'] = tarjeta_dict['N_deuda']
        tarjeta_dict['N_cargos'] = 0
        # Calcular nueva deuda con el mismo pago
        tarjet_dict = captura_nueva_deuda(tarjeta_dict, 2)
    
    if tarjet_dict['N_deuda'] != 0:
        #tarjet_dict['Deuda'] = tarjet_dict['N_deuda']
        tarjet_dict['Pago'] = tarjet_dict['Deuda']
        tarjet_dict['T_mensual'] = 0
        tarjeta_dict['T_recalculada'] = 0
        tarjeta_dict['N_deuda'] = 0
        generar_reporte(tarjeta_dict)

def pago_recurrente(tarjeta_dict):
    """
    Mediante una tarjeta permite calcular un pago recurrente hasta 
    cancelar la totalidad de la deuda
    """
    #print("pago tarjeta", tarjeta_dict)

    while tarjeta_dict['Pago'] < tarjeta_dict['Deuda']:

        generar_reporte(tarjeta_dict)
        
        # Nueva deuda igual a la deuda
        tarjeta_dict['Deuda'] = tarjeta_dict['N_deuda']
        tarjeta_dict['N_cargos'] = 0
        # Calcular nueva deuda con el mismo pago
        tarjet_dict = captura_nueva_deuda(tarjeta_dict, 2)
    
    if tarjet_dict['N_deuda'] != 0:
        #tarjet_dict['Deuda'] = tarjet_dict['N_deuda']
        tarjet_dict['Pago'] = tarjet_dict['Deuda']
        tarjet_dict['T_mensual'] = 0
        tarjeta_dict['T_recalculada'] = 0
        tarjeta_dict['N_deuda'] = 0
        generar_reporte(tarjeta_dict)

def pago_recurrente_dif_pagos(tarjeta_recibida):
    """
    Mediante una tarjeta permite calcular un pago recurrente diferente
    hasta cancelar la totalidad de la deuda.
    """

    while tarjeta_recibida['Pago'] < tarjeta_recibida['Deuda']:

        generar_reporte(tarjeta_recibida)
        #print(tarjeta_recibida)
        tarjeta_recibida['Deuda'] = tarjeta_recibida['N_deuda']
        # Capturar nuevo pago
        nuevo_pago = pago_mayor_deuda (tarjeta_recibida['Deuda'])
        tarjeta_recibida['Pago'] = nuevo_pago
        tarjeta_recibida['N_cargos'] = 0
        tarjeta_recibida = captura_nueva_deuda(tarjeta_recibida, 2)
    
    if tarjeta_recibida['N_deuda'] != 0:
        tarjeta_recibida['Pago'] = tarjeta_recibida['Deuda']
        tarjeta_recibida['T_mensual'] = 0
        tarjeta_recibida['T_recalculada'] = 0
        tarjeta_recibida['N_deuda'] = 0
        generar_reporte(tarjeta_recibida)

