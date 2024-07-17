from Departamentos import departamentos_municipios
from ClaseLogin import Login
from InspeccionarDept import InspeccionarDept
from ClaseDNI import DNI
from ClaseRF import ReconocimientoFacial
from ClaseFigura import Figura
'''
    ALUMNOS:
    - ILIANA LICETH ZUNIGA ENAMORADO
    - DIANY LIZBETH ENAMORADO FERNANDEZ
    - ANDERSON JAIR GARCIA MENJIVAR
    - TOMY JOSE MONTUFAR ZUNIGA
    - ANROLD STANLY FORD MADRID
'''

def main():

    usuario_correcto = "Iliana"
    intentos = 3
    reconocimiento_facial = ReconocimientoFacial("Empleados")

    # Acceder al programa
    login = Login(usuario_correcto, intentos, reconocimiento_facial)
    while True:
        if login.autenticar():
            break
        elif login.intentos == 0:
            print("Ha excedido el número de intentos permitidos.")
            exit()

    # Menu principal
    while True:
        print("Bienvenido al programa")
        print("1. Inspeccionar departamentos y municipios.")
        print("2. Ingresar su cedula.")
        print("3. Calcular Area y Volumen.")
        print("4. Salir.")
        selec = input("Elija una opcion: ")

        # Inspeccionar departamentos y municipios
        if selec == '1':
            inspeccion = InspeccionarDept()
        # Ingresar su cedula
        elif selec == '2':
            dni = DNI()
            dni.validar_dni()

        elif selec == '3':
            print("Calcular Área y Volumen.")
            radio = input("Ingrese el radio: ")
            area_esfera= Figura.Calcular_AreaEsfera(radio)
            area_circulo = Figura.Calcular_AreaCirculo(radio)
            volumen= Figura.Calcular_Volumen(radio)
            print(f"Área de la esfera: {area_esfera}")
            print(f"Área del círculo: {area_circulo}")
            print(f"Volumen de la esfera: {volumen}")
        # Salir
        elif selec == '4':
            print("Programa finalizado.")
            exit()
        else:
            print("Opcion no valida, intente de nuevo.")
            input("Presione Enter para continuar...")

if __name__ == "__main__":
    main()