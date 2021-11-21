
def multiples_reportes(lista_tarjetas):
    """ 
    Permite recorrer una lista de tarjetas e imprimirlas en el reporte
    """
    #recorrer la lista de tarjetas 
    for diccionario_tarjeta in lista_tarjetas:
        #recorrer e imprimir la informacion de cada tarjeta -- diccionario
        generar_reporte(diccionario_tarjeta)

def generar_reporte(tarjeta_dict):
    """
    Recibe una tarjeta y la imprime en el formato adecuado 
    """
    print('-'*60)
    print('-'*15 , " Resumen de la tajeta de crédito ", '-'*15)
    print('-'*60)
    print('{:>30} {:>20}'.format('Tarjeta a nombre de:', tarjeta_dict['Nombre'] ) )
    print('{:>30} {:>20}%'.format('Tasa de interés anual:', tarjeta_dict['Tasa'] ) )
    print('-'*60)
    print('{:>30} {:>20}'.format('Deuda actual:', tarjeta_dict['Deuda']) )
    print('{:>30} {:>20}'.format('Monto del pago:', tarjeta_dict['Pago']) )
    print('-'*60)
    print('{:>30} {:>20}'.format('Deuda después del pago:', tarjeta_dict['Deuda'] - tarjeta_dict['Pago']) )
    print('{:>30} {:>20}'.format('Intereses del mes:', tarjeta_dict['T_mensual']) )
    print('-'*60)
    print('{:>30} {:>20.2f}'.format('Deuda recalculada:', tarjeta_dict['T_recalculada']) )
    print('{:>30} {:>20}'.format('Nuevos cargos:', tarjeta_dict['N_cargos']) )
    print('-'*60)
    print('{:>30} {:>20}'.format('Nueva deuda del mes:', tarjeta_dict['N_deuda']) )
    print("")
    print("")
    print("")

def imprimir_tarjetas(lista_tarjetas):
    """
    Permite recorrer una lista de tarjetas e imprimirlas
    """
    #recorrer la lista de tarjetas 
    for diccionario_tarjeta in lista_tarjetas:
        #recorrer e imprimir la informacion de cada tarjeta -- diccionario
        generar_reporte(diccionario_tarjeta)