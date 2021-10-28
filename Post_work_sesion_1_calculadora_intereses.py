#Solicitar entradas para los diferentes datos

nombre_tarjeta = input("Digite el nombre de la tarjeta: ")
tasa_de_interes = float(input("Digite la tasa de interés (%) : ") )
deuda = float(input("Digite el monto de su deuda: ") )
pago_a_realizar = float(input("Digite el pago que desea realizar: ") )
nuevos_cargos = float(input("Digite nuevos gastos de la tarjeta en caso que tenga: ") )

print("Resumen de la tajeta de crédito")
print("_______________________________")
print('{:>30} {:>20}'.format('Tarjeta a nombre de:',nombre_tarjeta) )
print('{:>30} {:>20}%'.format('Tasa de interés anual:',tasa_de_interes) )
print("_______________________________")
print('{:>30} {:>20}'.format('Deuda actual:',deuda) )
print('{:>30} {:>20}'.format('Pago a realizar:',pago_a_realizar) )
print("_______________________________")


# Cálculo de la calculadora
if pago_a_realizar<deuda:
    
    tasa_mensual = tasa_de_interes / 12
    interes_mensual = (tasa_mensual / 100) * (deuda - pago_a_realizar)
    
    deuda_recalculada = (deuda - pago_a_realizar) * (1 + interes_mensual)
    deuda_recalculada2 = (deuda - pago_a_realizar) + interes_mensual
    nueva_deuda = deuda_recalculada2 + nuevos_cargos

    print('{:>30} {:>20}'.format('Deuda después del pago:',deuda - pago_a_realizar) )
    print('{:>30} {:>20}'.format('Intereses del mes:',interes_mensual) )

    print("_______________________________")

    print('{:>30} {:>20.2f}'.format('Próximo pago mensual:',deuda_recalculada2) )
    print('{:>30} {:>20}'.format('Nuevos cargos:',nuevos_cargos) )

    print("_______________________________")
    print('{:>30} {:>20.2f}'.format('Deuda a la fecha:',nueva_deuda) )
    
else:
    print(" El pago a realizar no puede ser superior a la deuda")