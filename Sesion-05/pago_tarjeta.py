from tarjeta.tarjeta import Tarjeta
from tarjeta.tarjeta_de_servicios import Tarjeta_de_servicios
from tarjeta.usuario import Usuario

def main():
    """
    Permite capturar la acción correspondiente para el usuario
    """
    print('-'*50)
    print('-'*15 , " Bienvenido a su banco ", '-'*15)
    nombre_usuario = input ("Por favor digite su nombre: ")
    print("")
    usuario = Usuario(nombre_usuario)    
    
    ciclo = True
    try:
        while ciclo == True:
        
            print(' '*5 , " Por favor digite el número de la acción que desea realizar", ' '*5)
            print(' '*5 , " 1. Incluir nueva tarjeta", ' '*5)
            print(' '*5 , " 2. Incluir nueva tarjeta de servicios", ' '*5)
            print(' '*5 , " 3. Calcular proyección de tarjeta", ' '*5)
            print(' '*5 , " 4. Proyectar tarjeta con múltiples pagos ", ' '*5)
            print(' '*5 , " 5. Borrar tarjeta ", ' '*5)
            print(' '*5 , " 6. Imprimir tarjetas ", ' '*5)
            print(' '*5 , " 7. Salir ", ' '*5)
            print('-'*60)

            opcion = int( input('Digite la acción: ') ) 
            print("")

            if opcion == 1:
                opcionw = 1
                while opcionw == 1:
                    tarjeta_nueva = Tarjeta()
                    usuario.agregar_tarjeta(tarjeta_nueva)

                    print("")
                    adicion_tarjeta = input("¿Desea agregar una nueva tarjeta? (Y/N): ")
                    print("")
                    if adicion_tarjeta == 'N':
                        opcionw = -1
                    elif adicion_tarjeta != 'Y':
                        opcionw = -1
                    #usuario.imprimir_tarjetas()

                    
            elif opcion == 2:
                opcionw = 1
                while opcionw == 1:

                    tarjeta_servicio = Tarjeta_de_servicios()
                    usuario.agregar_tarjeta(tarjeta_servicio)

                    print("")
                    adicion_tarjeta = input("¿Desea agregar una nueva tarjeta de servicios? (Y/N): ")
                    print("")
                    if adicion_tarjeta == 'N':
                        opcionw = -1
                    elif adicion_tarjeta != 'Y':
                        opcionw = -1

                #usuario.imprimir_tarjetas()


            elif opcion == 3:
                #Pasar a cálculo de proyección
                print("")
                nombre_tarjeta_rec = input("Digite el nombre de la tarjeta que de sea conocer la proyección: ")
                tupla_tarjeta = usuario.buscarTarjeta(nombre_tarjeta_rec) #Tupla
                #print("tupla tar:", tupla_tarjeta)
                tarjeta = Tarjeta(1)
                tarjeta = tarjeta.crearTarjetaTupla(tupla_tarjeta)
                #print("tarjeta: ",tarjeta)
                tarjeta.pago_recurrente()
                #lista_tarjeta_pryectada = tarjeta.getProyeccion()
                #tarjeta.crearTarjeta(lista_tarjeta_pryectada[0])
                tarjeta.borrar_proyeccion()

                    

            elif opcion == 4:
                print("")
                nombre_tarjeta_rec = input("Digite el nombre de la tarjeta que de sea conocer la proyección con diferentes pagos: ")
                tarjeta_rec = usuario.buscarTarjeta(nombre_tarjeta_rec)
                tarjeta = Tarjeta(1)
                tarjeta = tarjeta.crearTarjetaTupla(tarjeta_rec)

                tarjeta.pago_recurrente_dif_pagos()
                #lista_tarj_pagos = tarjeta.getProyeccion()
                #tarjeta.crearTarjeta(lista_tarj_pagos[0])
                tarjeta.borrar_proyeccion()
                    # Proyección tarjeta con pagos variables
                    #print(tarjeta_pago_var_comp)
                    

            elif opcion == 5:
                print("")
                tarjeta_borrar = input("Digite el nombre de la tarjeta que desea eliminar: ")
                #tarjeta_b = usuario.buscarTarjeta(tarjeta_borrar)
                usuario.borrarTarjeta(tarjeta_borrar)
                #tarjeta_b.generar_reporte()
                print("Sus nuevas tarjetas son: ")
                usuario.imprimir_tarjetas()
                #if resp == 'Y':
                #    usuario.borrarTarjeta(tarjeta_borrar)

            elif opcion == 6:
                print("")
                usuario.imprimir_tarjetas()
                    
            elif opcion == 7:
                print("")
                print("¡Regrese pronto!")
                ciclo = False

            else:
                print(' ')
                print('No contamos con la opcion seleccionada, digite una opción válida')
                print(' ')
    except:
        print("¡Opción no válida!")


main()
# Llamada para incluir nueva tarjeta
