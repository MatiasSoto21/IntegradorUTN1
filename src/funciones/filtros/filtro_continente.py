from rich.console import Console # type: ignore
from rich.table import Table # type: ignore
from rich.panel import Panel # type: ignore
from rich.box import HEAVY# type: ignore
from funciones.utils import paginar_tabla

def filtrar_continente():
    console = Console()
    while True:
        console.clear()
        try:
            console.print()
            console.rule("[bold yellow]Filtro de Paises[/bold yellow]")
            filtro = console.input("""
            [bold][underline] Seleccione el filtro a aplicar: [/bold][/underline]
            1) Mostrar países de África
            2) Mostrar países de América del Norte
            3) Mostrar países de América del Sur
            4) Mostrar países de Asia
            5) Mostrar países de Oceania
            6) Mostrar países de Europa  
            7) Mostrar países de Antartida
            8) Volver al Menú anterior                                       
            """)

            if filtro not in ("1","2","3","4","5","6","7","8"):
                raise ValueError("Porfavor seleccione algunas de las opciones (1-8)")
            break
        except ValueError as e:
            console.clear()
            console.print("\n",Panel(f"[underline]ERROR:[/underline] {e}",style="bold red",box=HEAVY,  title=":x: ERROR!"))
            console.input("Presione Enter para continuar..")    

    if filtro == "1":
        filtro = "Africa"  
    elif filtro == "2":
        filtro = "North America"
    elif filtro == "3":
        filtro = "South America"  
    elif filtro == "4":
        filtro = "Asia"    
    elif filtro == "5":
        filtro = "Oceania"      
    elif filtro == "6":
        filtro = "Europe"  
    elif filtro == "7":
        filtro = "Antarctica"
    elif filtro =="8":
        return            

    with open("data/paises.csv", "r")as archivo:
        encabezado = archivo.readline().strip().split(",")
        lineas = archivo.readlines()
        filtrados = []

        for i in lineas:
            fila = i.strip().split(",")

            if any(filtro in elemento for elemento in fila):
                fila[2] = fila[2] + " km2" #le agrego el km2 para que se muestre en la tabla sino, se muestra solo el numero sin km2
                filtrados.append(fila)

    if filtrados:
        paginar_tabla(filtrados,encabezado, titulo= f"Países de {filtro}")
    else:
        return print("No se encontraron paises para el filtro")