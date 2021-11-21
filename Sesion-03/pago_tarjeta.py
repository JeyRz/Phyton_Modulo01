from tarjeta.tarjeta import crea_tarjeta, captura_nueva_deuda, pago_recurrente, pago_recurrente_dif_pagos
from tarjeta.usuario import generar_reporte, imprimir_tarjetas

def main():
    """
    Permite capturar la acción correspondiente para el usuario
    """
    print('-'*50)
    print('-'*15 , " Bienvenido a su banco ", '-'*15)
    print(' '*5 , " Por favor digite el número de la acción que desea realizar", ' '*5)
    print(' '*5 , " 1. Incluir nueva tarjeta", ' '*5)
    print(' '*5 , " 2. Calcular proyección de tarjeta", ' '*5)
    print(' '*5, " 3. Captutar varias tarjetas", ' '*5)
    print(' '*5, " 4. Proyectar tarjeta con múltiples pagos ", ' '*5)
    print('-'*60)

    opcion = int( input('Digite la acción: ') ) 
    lista_tarjetas = []

    if opcion == 1:
        tarjeta_nueva = crea_tarjeta()
        #tarjeta_nueva = captura_nueva_deuda(tarjeta_nueva)
        tarjeta_calculada = captura_nueva_deuda(tarjeta_nueva)
        generar_reporte(tarjeta_calculada)

    elif opcion == 2:
        tarjeta_nueva = crea_tarjeta()
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

    elif opcion == 4:
        tarjeta_pago_variable = crea_tarjeta()
        tarjeta_pago_var_comp = captura_nueva_deuda(tarjeta_pago_variable)
        # Proyección tarjeta con pagos variables
        #print(tarjeta_pago_var_comp)
        pago_recurrente_dif_pagos(tarjeta_pago_var_comp)

    else:
        print(' ')
        print('No contamos con la opcion seleccionada, regrese pronto')
        print(' ')


main()
# Llamada para incluir nueva tarjeta
