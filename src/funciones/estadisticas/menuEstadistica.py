from .mayorYmenorPoblacion import estadistica_poblacion
from .promedioPoblacion import estadistica_poblacionContinente



def menuEstadistica():
    while True:
            print("\n" + "="*50)
            print("🌎 Seleccione la estadistica que quiere consultar")
            print("="*50)
            print("1) País con Mayor y Menor Población")
            print("2) Promedio de Poblacion de algun continente")
            print("3) Promedio de Superficie")
            print("4) Cantidad de países por continente")
            print("5) Regresar al menú principal")
            print("="*50)
            opcion=input("Elija una opcion del 1 al 3: ")
            if opcion == "1":
                estadistica_poblacion()
            elif opcion == "2":
                estadistica_poblacionContinente()
            elif opcion == "3":
                pass
            elif opcion == "4":
                pass    
            elif opcion == "5":
                break
            else:
                print("Error, Intente Nuevamente con: 1, 2, 3, 4 ó 5")