from rich.console import Console # type: ignore
from rich.table import Table # type: ignore
from rich.panel import Panel # type: ignore
from rich.box import HEAVY# type: ignore
from funciones.utils import paginar_tabla

def filtrar_superficie():
    console = Console()

    while True:  #Validacion del rango minimo
        console.clear()
        try:
            console.print()
            console.rule("[bold yellow]Filtrar por rango de Superficie[/bold yellow]")
            sup_min = console.input("Ingrese superficie (km2) [underline]Mínima[/underline] → ")

            if " " in sup_min:
                raise ValueError("No se permiten espacios")

            if not sup_min.isdigit():
                raise ValueError("Solo se permiten valores numéricos enteros y positivos")

            sup_min = int(sup_min)

            if sup_min < 0:
                raise ValueError("La superficie mínima debe ser positiva")

            break #si esta todo bien salgo del while
        except ValueError as e:
            console.clear()
            console.print("\n",Panel(f"[underline]ERROR:[/underline] {e}",style="bold red",box=HEAVY,  title=":x: ERROR!"))
            console.input("Presione Enter para continuar..")

    while True: # Validacion del rango máximo
        try:
            sup_max = console.input("Ingrese superficie (km2) [underline]Máxima[/underline] → ")

            if " " in sup_max:
                raise ValueError("No se permiten espacios")

            if not sup_max.isdigit():
                raise ValueError("Solo se permiten valores numéricos enteros y positivos")

            sup_max = int(sup_max)

            if sup_max <= sup_min:
                raise ValueError("La superficie máxima debe ser mayor a la superficie mínima")

            break#si ta todo bien salgo
        except ValueError as e:
            console.clear()
            console.print("\n",Panel(f"[underline]ERROR:[/underline] {e}",style="bold red",box=HEAVY,  title=":x: ERROR!"))
            console.input("Presione Enter para continuar..")

    with open("data/paises.csv", "r")as archivo:
        encabezado = archivo.readline().strip().split(",")
        lineas = archivo.readlines()
        filtrados = []
        
        for i in lineas:
            fila = i.strip().split(",")
            #paises.append(dict(zip(encabezado,fila)))
            if int(fila[2]) >= sup_min and int(fila[2]) <= sup_max:
                fila[2] = fila[2] + " km2"
                filtrados.append(fila)

        if filtrados:
            paginar_tabla(filtrados,encabezado, titulo= f"Países con rango de superficie entre {sup_min}-{sup_max}")
   
        else:
            console.print("No se encontro ningun pais con ese rango de superficie.", style="bold underline red")
            console.input("Presione Enter para continuar..")
