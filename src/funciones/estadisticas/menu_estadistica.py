from .mayor_menor_poblacion import estadistica_poblacion
from .promedio_poblacion import estadistica_poblacionContinente
from .promedio_superficie import estadistica_superficie
from .cantidad_continente_pais import estadistica_pais
from rich.console import Console # type: ignore


def menu_estadistica():
    while True:
            console = Console()
            console.clear()
            console.print("[yellow]\n" + "="*50)
            console.print("🌎 Seleccione la estadistica que quiere consultar")
            console.print("[yellow]="*50)
            console.print("1) País con Mayor y Menor Población")
            console.print("2) Promedio de Poblacion de algun continente")
            console.print("3) Promedio de Superficie")
            console.print("4) Cantidad de países por continente")
            console.print("5) Regresar al menú principal")
            console.print("[yellow]="*50)
            opcion=input("Elija una opcion del 1 al 5: ")
            if opcion == "1":
                estadistica_poblacion()
            elif opcion == "2":
                estadistica_poblacionContinente()
            elif opcion == "3":
                estadistica_superficie()
            elif opcion == "4":
                estadistica_pais()
            elif opcion == "5":
                break
            else:
                print("Error, Intente Nuevamente con: 1, 2, 3, 4 ó 5")