from rich.console import Console # type: ignore
from rich.table import Table # type: ignore
from rich.panel import Panel # type: ignore
from rich.box import HEAVY# type: ignore
from funciones.utils import paginar_tabla

def buscar_pais():
    console = Console()
    encontrado = []
    while True:
        console.clear()
        try:
            console.print()
            console.rule("[bold yellow]Búsqueda de Países[/bold yellow]")
            busqueda = console.input(
                "\n:mag: Ingrese el [yellow][underline]nombre[/underline][/yellow] del país a buscar "
                "o escriba [yellow]'exit'[/yellow] para volver al menu anterior\n"
                ).strip()
     
            if not busqueda:
                raise ValueError("El nombre no puede estar vacío.")
        
             # validacion de que sean solo letras y espacios
            if not all(palabra.isalpha() for palabra in busqueda.split()):
                raise ValueError("El nombre solo puede contener letras y espacios.")
            
            busqueda = busqueda.replace(" ","").lower()  # le quito los espacios y lo pongo en minus al input para despues buscarlo en el csv
            if busqueda == "exit": 
                console.clear()
                return
            break  # si esta todo bien salgo del while
        except ValueError as e: 
            console.clear()
            console.print("\n",Panel(f"[underline]ERROR:[/underline] {e}",style="bold red",box=HEAVY,  title=":x: ERROR!"))
            console.input("\nPresione Enter para continuar..")


    with open("data/paises.csv", "r")as archivo:
        encabezado = archivo.readline().strip().split(",")
        lineas = archivo.readlines()

        for i in lineas:
            fila = i.strip().split(",")
            if busqueda in fila[0].replace(" ","").lower(): #al csv tambien le quito los espacios y lo pongo en minus para verificar si existe
                fila[2] = fila[2] + " km2"
                encontrado.append(fila)  #me llevo todo el pais con sus datos para despues mostrarlos       

    if encontrado:
        paginar_tabla(encontrado, encabezado, titulo="🌎 Países")
    else:
        console.clear()      
        console.print("\n", Panel( ":x: No se encontro ningun pais 😥", style="bold red"))
        console.input("\nPresione Enter para continuar..")