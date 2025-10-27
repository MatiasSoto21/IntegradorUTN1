from funciones.getpaises.paises import get_paises
from funciones.buscar.buscar import buscar_pais
from funciones.filtros.filtro_continente import filtrar_continente
from funciones.filtros.filtro_poblacion import filtrar_poblacion
from funciones.filtros.filtro_superficie import filtrar_superficie
from funciones.ordenamientos.ordenar_nombre import ordenar_nombre
from funciones.ordenamientos.ordenar_poblacion import ordenar_poblacion
from funciones.ordenamientos.ordenar_superficie import ordenar_superficie
from funciones.estadisticas.menuEstadistica import menuEstadistica

from rich.console import Console # type: ignore
from rich.panel import Panel # type: ignore
import os

def main():
    bandera: bool = True
    console = Console()

    while bandera:
        console.clear() #Se limpia la consola cada vez que se imprime el menu
        console.print()
        console.rule("[bold yellow]MENU PRINCIPAL[/bold yellow]")
        if not os.path.exists("data/paises.csv"): #verifico si ya se hizo el request de la api
            get_paises()   
            
        respuesta = console.input("""
            [bold][underline]Bienvenido a la app de Paises![/bold][/underline]

            Elija la opcion deseada
            ---------------------------------------------------
            1) Buscar Pais
            2) Filtrar paises por continente
            3) Filtrar por rango de poblacion
            4) Filtrar por rango de superficie
            5) Ordenar paises por Nombre
            6) Ordenar paises por Poblacion                 
            7) Ordenar paises por Superficie                 
            8) Mostrar estadisticas                                                       
            9) SALIR
    """)

        if respuesta == "1":
            buscar_pais()        
        elif respuesta == "2":
            filtrar_continente()
        elif respuesta == "3":
            filtrar_poblacion()
        elif respuesta == "4":
            filtrar_superficie()
        elif respuesta == "5":
            while True:
                    print("""
                --------- Paises Ordenados --------- 
                1) Ordenados de la A-Z (Ascendente)
                2) Ordenados de la Z-A (Descendente)
                """)
                    opcion:str=input("Elija un opcion (1-2): ")
                    if opcion == "1":
                        paises_ordenados = ordenar_nombre(orden="A-Z")

                        console.print("\n[bold green]=== Países Ordenados A-Z ===[/bold green]")
                        for i, pais in enumerate(paises_ordenados, 1):
                            console.print(f"{i}. {pais}")
                        break
                    elif opcion=="2":
                        paises_ordenados = ordenar_nombre(orden="Z-A")

                        console.print("\n[bold green]=== Países Ordenados Z-A ===[/bold green]")
                        for i, pais in enumerate(paises_ordenados, 1):
                            console.print(f"{i}. {pais}")
                        break
                    else:
                        print("Error: Intente nuevamente")

        elif respuesta == "6":
            ordenar_poblacion()
        elif respuesta == "7":
            ordenar_superficie()
        elif respuesta == "8":
            menuEstadistica()
        elif respuesta == "9":
            bandera = False
            print("ADIOS")
        else:
            console.clear() 
            console.print("\n",Panel("[red]ERROR: Porfavor seleccione algunas de las opciones (1-8)", title="ERROR", style="bold red"))
            console.input("Presione Enter para continuar..")
if __name__ == "__main__":
    main()        
