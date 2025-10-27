from rich.console import Console # type: ignore
from rich.table import Table # type: ignore
from rich.panel import Panel # type: ignore
from rich.box import HEAVY# type: ignore
from funciones.utils import paginar_tabla

def filtrar_poblacion():
    console = Console()

    while True:  #Validacion del rango minimo
        console.clear()
        try:
            console.print()
            console.rule("[bold yellow]Filtrar por rango de Población[/bold yellow]")
            pob_min = console.input("Ingrese población [underline]Mínima[/underline] → ")

            if " " in pob_min:
                raise ValueError("No se permiten espacios")

            if not pob_min.isdigit():
                raise ValueError("Solo se permiten valores numéricos enteros y positivos")

            pob_min = int(pob_min)

            if pob_min < 0:
                raise ValueError("La población mínima debe ser positiva")

            break #si esta todo bien salgo del while
        except ValueError as e:
            console.clear()
            console.print("\n",Panel(f"[underline]ERROR:[/underline] {e}",style="bold red",box=HEAVY,  title=":x: ERROR!"))
            console.input("Presione Enter para continuar..")  

    while True: # Validacion del rango máximo
        try:
            pob_max = console.input("Ingrese población [underline]Máxima[/underline] → ")

            if " " in pob_max:
                raise ValueError("No se permiten espacios")

            if not pob_max.isdigit():
                raise ValueError("Solo se permiten valores numéricos enteros y positivos")

            pob_max = int(pob_max)

            if pob_max <= pob_min:
                raise ValueError("La población máxima debe ser mayor a la poblacion mínima")

            break#si ta todo bien salgo
        except ValueError as e:
            console.clear()
            console.print("\n",Panel(f"[underline]ERROR:[/underline] {e}",style="bold red",box=HEAVY,  title=":x: ERROR!"))
            console.input("Presione Enter para continuar..")    

    with open("data/paises.csv", "r")as archivo:
        encabezado = archivo.readline().strip().split(",")
        lineas = archivo.readlines()
        filtrados = [] #me guardo los filtrados aca 
        
        for i in lineas:
            fila = i.strip().split(",")
            fila[2] = fila[2] + " km2"
            #paises.append(dict(zip(encabezado,fila)))
            if int(fila[1]) >= pob_min and int(fila[1]) <= pob_max:
                filtrados.append(fila)     

        if filtrados:
            paginar_tabla(filtrados,encabezado, titulo= f"Países con rango de poblacion entre {pob_min}-{pob_max}")
        else:
            console.print("No se encontro ningun pais con ese rango de poblacion.", style="bold underline red")
            console.input("Presione Enter para continuar..")
