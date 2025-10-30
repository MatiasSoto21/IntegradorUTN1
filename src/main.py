from funciones.getpaises.paises import get_paises
from funciones.buscar.buscar import buscar_pais
from funciones.filtros.filtro_continente import filtrar_continente
from funciones.filtros.filtro_poblacion import filtrar_poblacion
from funciones.filtros.filtro_superficie import filtrar_superficie
from funciones.ordenamientos.ordenar_nombre import ordenar_nombre
from funciones.ordenamientos.ordenar_poblacion import ordenar_poblacion
from funciones.ordenamientos.ordenar_superficie import ordenar_superficie
from funciones.estadisticas.menu_estadistica import menu_estadistica
from funciones.utils import asegurar_archivo
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
[bold][underline][green]Bienvenido a la app de Paises![/green][/bold][/underline]

[yellow]Elija la opcion deseada[/yellow]
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
            asegurar_archivo(console)
            buscar_pais()        
        elif respuesta == "2":
            asegurar_archivo(console)
            filtrar_continente()
        elif respuesta == "3":
            asegurar_archivo(console)
            filtrar_poblacion()
        elif respuesta == "4":
            asegurar_archivo(console)
            filtrar_superficie()
        elif respuesta == "5":
            asegurar_archivo(console)
            ordenar_nombre()
        elif respuesta == "6":
            asegurar_archivo(console)
            ordenar_poblacion()
        elif respuesta == "7":
            asegurar_archivo(console)
            ordenar_superficie()
        elif respuesta == "8":
            asegurar_archivo(console)
            menu_estadistica()
        elif respuesta == "9":
            bandera = False
            console.print("[green][bold]GRACIAS POR USAR LA APP, ADIOS")
        else:
            console.clear() 
            console.print("\n",Panel("[red]ERROR: Porfavor seleccione algunas de las opciones (1-8)", title="ERROR", style="bold red"))
            console.input("Presione Enter para continuar..")
if __name__ == "__main__":
    main()        
