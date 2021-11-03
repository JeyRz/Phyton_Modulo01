
#Creacion de variables
nombre_tarjeta = ''
tasa_de_interes = 0
deuda = 0
pago_a_realizar = -1


#Validar deuda y pago
def pago_mayor_deuda( deuda_validar, ciclo = -1):

    if ciclo == -1:
        pago_a_realizar = float(input("Digite el pago que desea realizar: ") )
        if pago_a_realizar > deuda_validar:
            print( "El pago a realizar no puede ser superior a la deuda" )
            pago_mayor_deuda(deuda_validar, -1)
        else:
            return pago_a_realizar

    


# 1. Funcion crear tarjeta
def crea_tarjeta():

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


# 2. Captura nueva deuda
def captura_nueva_deuda (tarjeta_dict, lista_tarjetas, recorre = 0  ):
    #Calculos de la tarjeta
    tasa_mensual = tarjeta_dict['Tasa'] / 12
    interes_mensual = (tasa_mensual / 100) * (tarjeta_dict['Deuda'] - tarjeta_dict['Pago'])
    
    deuda_recalculada2 = ( tarjeta_dict['Deuda'] - tarjeta_dict['Pago'] ) + interes_mensual
    nueva_deuda = deuda_recalculada2 + tarjeta_dict['N_cargos']

    print("pasa punto", lista_tarjetas, recorre)
    #Agregar nuevo campo al diccionario de tarjeta o reemplazarlo para calcular pago recurrente
    if recorre == 0:
        tarjeta_dict.setdefault('T_recalculada',deuda_recalculada2)
        tarjeta_dict.setdefault('T_mensual',tasa_mensual)
        tarjeta_dict.setdefault('N_deuda', nueva_deuda)
        #Adicionar a una lista de tarjetas
        #lista_tarjetas = []
        lista_tarjetas.append(tarjeta_dict) 
    else:
        tarjeta_aux = {}
        tarjeta_aux.clear()
        tarjeta_aux = tarjeta_dict.copy()
        tarjeta_aux['Deuda'] = tarjeta_aux['N_deuda']
        tarjeta_aux['T_recalculada'] = deuda_recalculada2
        tarjeta_aux['T_mensual']= tasa_mensual
        tarjeta_aux['N_deuda'] = nueva_deuda

        lista_tarjetas.append(tarjeta_aux) 
        """
        tarjeta_dict['Deuda'] = tarjeta_dict['N_deuda']
        tarjeta_dict['T_recalculada'] = deuda_recalculada2
        tarjeta_dict['T_mensual']=tasa_mensual
        tarjeta_dict['N_deuda'] = nueva_deuda
        """
        

    return lista_tarjetas

# 3. Generar reporte
def generar_reporte(tarjeta_dict):
    print('-'*50)
    print('-'*15 , " Resumen de la tajeta de crédito ", '-'*15)
    print('-'*50)
    print('{:>30} {:>20}'.format('Tarjeta a nombre de:', tarjeta_dict['Nombre'] ) )
    print('{:>30} {:>20}%'.format('Tasa de interés anual:', tarjeta_dict['Tasa'] ) )
    print('-'*50)
    print('{:>30} {:>20}'.format('Deuda actual:', tarjeta_dict['Deuda']) )
    print('{:>30} {:>20}'.format('Monto del pago:', tarjeta_dict['Pago']) )
    print('-'*50)
    print('{:>30} {:>20}'.format('Deuda después del pago:', tarjeta_dict['Deuda'] - tarjeta_dict['Pago']) )
    print('{:>30} {:>20}'.format('Intereses del mes:', tarjeta_dict['T_mensual']) )
    print('-'*50)
    print('{:>30} {:>20.2f}'.format('Deuda recalculada:', tarjeta_dict['T_recalculada']) )
    print('{:>30} {:>20}'.format('Nuevos cargos:', tarjeta_dict['N_cargos']) )
    print('-'*50)
    print('{:>30} {:>20}'.format('Nueva deuda del mes:', tarjeta_dict['N_deuda']) )

# 4. Imprimir tarjetas
def imprimir_tarjetas(lista_tarjetas):
    #recorrer la lista de tarjetas 
    for diccionario_tarjeta in lista_tarjetas:
        #recorrer e imprimir la informacion de cada tarjeta -- diccionario
        for key in diccionario_tarjeta:
            generar_reporte(diccionario_tarjeta)



# 5. Pago recurrente
def pago_recurrente(tarjeta_dict, lista_pago_recurrente):

    if  tarjeta_dict['Pago'] < tarjeta_dict['Deuda'] :
        #adicionar a la lista
        lista_pago_recurrente.append(tarjeta_dict)
        # generar nueva tarjeta con la nueva deuda

        lista_pago_recurrente = captura_nueva_deuda(tarjeta_dict, lista_pago_recurrente, 1)
        tarjeta_aux = {}
        tarjeta_aux = lista_pago_recurrente[len(lista_pago_recurrente)-1].copy()
        pago_recurrente(tarjeta_aux, lista_pago_recurrente )
        #print("otro punto")

    else :
        #Igualo el pago con la deuda
        tarjeta_dict['Pago'] = tarjeta_dict['N_deuda']
        lista_pago_recurrente.append(tarjeta_dict)
    
    imprimir_tarjetas (lista_pago_recurrente)



# Preparar programa opcion para calcular un pago recurrente o incluir nueva tarjeta
print('-'*50)
print('-'*15 , " Bienvenido a su banco ", '-'*15)
print(' '*5 , " Por favor digite el número de la acción que desea realizar", ' '*5)
print(' '*5 , " 1. Incluir nueva tarjeta", ' '*5)
print(' '*5 , " 2. Calcular proyección de tarjeta", ' '*5)
print('-'*50)

def main():
    #Capturar la accion
    opcion = int( input('Digite la acción: ') ) 
    lista_tarjetas = []

    if opcion == 1:
        tarjeta_nueva = crea_tarjeta()
        #tarjeta_nueva = captura_nueva_deuda(tarjeta_nueva)
        lista_tarjeta = captura_nueva_deuda(tarjeta_nueva, lista_tarjetas)
        generar_reporte(lista_tarjeta[-1])

    elif opcion == 2:
        tarjeta_nueva = crea_tarjeta()
        #tarjeta_nueva = captura_nueva_deuda(tarjeta_nueva)
        lista_tarjeta = captura_nueva_deuda(tarjeta_nueva, lista_tarjetas)
        #lista del pago recurrente
        lista_pago_recurrente = []
        #print('prueba tarjeta',lista_tarjeta[-1])
        pago_recurrente(lista_tarjeta[-1], lista_pago_recurrente)

    else:
        print(' ')
        print('No contamos con la opcion seleccionada, regrese pronto')
        print(' ')


main()
# Llamada para incluir nueva tarjeta

