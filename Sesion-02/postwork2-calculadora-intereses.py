
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
            #pago_mayor_deuda(deuda_validar, -1)
            return pago_mayor_deuda(deuda_validar, -1)
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
def captura_nueva_deuda ( tarjeta_dict, recorre = 0  ):
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
    print("")
    print("")
    print("")

# 4. Imprimir tarjetas #Usuario modulo
def imprimir_tarjetas(lista_tarjetas):
    #recorrer la lista de tarjetas 
    for diccionario_tarjeta in lista_tarjetas:
        #recorrer e imprimir la informacion de cada tarjeta -- diccionario
        generar_reporte(diccionario_tarjeta)



# 5. Pago recurrente
def pago_recurrente(tarjeta_dict):

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


# Preparar programa opcion para calcular un pago recurrente o incluir nueva tarjeta
print('-'*50)
print('-'*15 , " Bienvenido a su banco ", '-'*15)
print(' '*5 , " Por favor digite el número de la acción que desea realizar", ' '*5)
print(' '*5 , " 1. Incluir nueva tarjeta", ' '*5)
print(' '*5 , " 2. Calcular proyección de tarjeta", ' '*5)
print(' '*5, " 3. Captutar varias tarjetas", ' '*5)
print('-'*50)

def main():
    #Capturar la accion
    opcion = int( input('Digite la acción: ') ) 
    lista_tarjetas = []

    if opcion == 1:
        tarjeta_nueva = crea_tarjeta()
        #tarjeta_nueva = captura_nueva_deuda(tarjeta_nueva)
        tarjeta_calculada = captura_nueva_deuda(tarjeta_nueva)
        generar_reporte(tarjeta_calculada)

    elif opcion == 2:
        tarjeta_nueva = crea_tarjeta()
        #tarjeta_nueva = captura_nueva_deuda(tarjeta_nueva)
        tarjeta_recurrente = captura_nueva_deuda(tarjeta_nueva)
        print("2. ", tarjeta_recurrente)
        #Pasar a cálculo de proyección
        pago_recurrente(tarjeta_recurrente)
    elif opcion == 3:
        while opcion == 3:
            tarjeta_varias = crea_tarjeta()
            tarjeta_a_lista = captura_nueva_deuda(tarjeta_varias)
            #print(tarjeta_a_lista)
            lista_tarjetas.append(tarjeta_a_lista)
            #print( "lista tarjeta: ", lista_tarjetas)
            print("")
            adicion_tarjeta = input("¿Desea agregar una nueva tarjeta? (Y/N): ")
            if adicion_tarjeta == 'N':
                opcion = -1
            elif adicion_tarjeta != 'Y':
                opcion = -1
        imprimir_tarjetas(lista_tarjetas)
    else:
        print(' ')
        print('No contamos con la opcion seleccionada, regrese pronto')
        print(' ')


main()
# Llamada para incluir nueva tarjeta

