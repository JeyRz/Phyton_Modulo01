from tarjeta.tarjeta import Tarjeta
from tarjeta.tarjeta_de_servicios import Tarjeta_de_servicios
from tarjeta.usuario import Usuario
import pytest



tarjeta1 = None
tarjeta2 = None

def setup_module(module):
    global tarjeta1 
    global tarjeta2

    tarjeta1 = Tarjeta(1)
    tupla_tarjeta = ('Visa', 2.0, 5000.0, 200.0, 50.0, 4850.0, 0.2, 4872.0 )
    tarjeta1.crearTarjetaTupla(tupla_tarjeta)

    tarjeta2 = Tarjeta_de_servicios(1)
    tupla_tarjeta2 = ('Rappi', 2.0, 7000.0, 7000.0, 0.0, 50.0, 0.2, 52.0 )
    tarjeta2.crearTarjetaTupla(tupla_tarjeta2)

def test_tarjeta():
    assert type(tarjeta1) == Tarjeta
    assert tarjeta1.getNombre() == 'Visa'
    assert tarjeta1.getTasa() == 2.0
    assert tarjeta1.getDeudaActual() == 5000.0
    assert tarjeta1.getPago() == 200.0
    assert tarjeta1.getNuevosCargos() == 50.0
    assert tarjeta1.getDeudaRecalculada() == 4850.0
    assert tarjeta1.getTasaMensual() == 0.2
    assert tarjeta1.getNuevaDeduda() == 4872.0
    assert tarjeta1.obtener_diccionario() == {'Nombre': 'Visa', 'Tasa': 2.0, 'Deuda': 5000.0, \
                'Pago': 200.0, 'N_cargos': 50.0, 'T_recalculada':4850.0, 'T_mensual': 0.2, \
                'N_deuda':4872.0}
    assert type(tarjeta1.crearTarjetaTupla(('Visa', 2.0, 5000.0, 200.0, 50.0, 4850.0, 0.2, 4872.0 ))) == Tarjeta
    assert tarjeta1.texto_tarjeta() == 'Visa,2.0,5000.0,200.0,50.0,4850.0,0.2,4872.0'
    assert tarjeta1.tupla_tarjeta() == ('Visa', 2.0, 5000.0, 200.0, 50.0, 4850.0, 0.2, 4872.0 )

def test_tarjeta_servicio():
    assert type(tarjeta2) == Tarjeta_de_servicios
    assert tarjeta2.getNombre() == 'Rappi'
    assert tarjeta2.getTasa() == 2.0
    assert tarjeta2.getDeudaActual() == 7000.0
    assert tarjeta2.getPago() == 7000.0
    assert tarjeta2.getDeudaActual() == tarjeta2.getPago()
    assert tarjeta2.getNuevosCargos() == 0.0
    assert tarjeta2.getDeudaRecalculada() == 50.0
    assert tarjeta2.getTasaMensual() == 0.2
    assert tarjeta2.getNuevaDeduda() == 52.0
    assert tarjeta2.obtener_diccionario() == {'Nombre': 'Rappi', 'Tasa': 2.0, 'Deuda': 7000.0, \
                'Pago': 7000.0, 'N_cargos': 0.0, 'T_recalculada':50.0, 'T_mensual': 0.2, \
                'N_deuda':52.0}
    assert type(tarjeta2.crearTarjetaTupla(('Rappi', 2.0, 7000.0, 7000.0, 0.0, 50.0, 0.2, 52.0))) == Tarjeta_de_servicios
    assert tarjeta2.texto_tarjeta() == 'Rappi,2.0,7000.0,7000.0,0.0,50.0,0.2,52.0'
    assert tarjeta2.tupla_tarjeta() == ('Rappi', 2.0, 7000.0, 7000.0, 0.0, 50.0, 0.2, 52.0)
    










"""

@pytest.mark.parametrize("lista, resultado", 
    [
        ([1,2,3,4,5], [1,2,3,4,5]),
        ([1,1,1,1,1], [1]),
        ([1,1,2,3,4,4,5], [1,2,3,4,5]),
        ([5,3,2,1,4,4], [1,2,3,4,5])
    ]
    )
def test_procesa(lista, resultado):
    """ 'Batería de pruebas para procesa()' """
    assert type( listas.procesa([1]) ) == Tarjeta
    assert listas.procesa(lista) == resultado

"""