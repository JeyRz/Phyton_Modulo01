from tarjeta.usuario import Usuario


usuario1 = Usuario('Jeimy')
usuario1.importar_de_csv()

usuario2 = Usuario('Ricardo')
usuario2.importar_de_csv()

usuario3 = Usuario('Anna')
usuario3.importar_de_csv()

base_de_usuarios = [usuario1,usuario2,usuario3]