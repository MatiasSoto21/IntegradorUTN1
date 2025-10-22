from rich.console import Console # type: ignore
from rich.table import Table # type: ignore

def filtrar_superficie():
    console = Console()

    while True:  #Validacion del rango minimo
        try:
            sup_min = input("Ingrese superficie mínima: ")

            if " " in sup_min:
                raise ValueError("ERROR: No se permiten espacios")

            if not sup_min.isdigit():
                raise ValueError("ERROR: Solo se permiten valores numéricos enteros y positivos")

            sup_min = int(sup_min)

            if sup_min < 0:
                raise ValueError("ERROR: La superficie mínima debe ser positiva")

            break #si esta todo bien salgo del while
        except ValueError as e:
            console.print(f"[red]{e}")

    while True: # Validacion del rango máximo
        try:
            sup_max = input("Ingrese superficie máxima: ")

            if " " in sup_max:
                raise ValueError("ERROR: No se permiten espacios")

            if not sup_max.isdigit():
                raise ValueError("ERROR: Solo se permiten valores numéricos enteros y positivos")

            sup_max = int(sup_max)

            if sup_max <= sup_min:
                raise ValueError("ERROR: La superficie máxima debe ser mayor a la superficie mínima")

            break#si ta todo bien salgo
        except ValueError as e:
            console.print(f"[red]{e}")

    table = Table(title= f"Países con rango de superficie entre: {sup_min} km2 y {sup_max} km2 :earth_americas:", style="bold")

    with open("data/paises.csv", "r")as archivo:
        paises = []
        encabezado = archivo.readline().strip().split(",")
        table.add_column(encabezado[0].capitalize(), style="cyan")
        table.add_column(encabezado[1].capitalize(), style="magenta")
        table.add_column(encabezado[2].capitalize(), style="green")
        table.add_column(encabezado[3].capitalize(), style="blue")

        lineas = archivo.readlines()
        
        for i in lineas:
            fila = i.strip().split(",")
            paises.append(dict(zip(encabezado,fila)))

        filtrados = [] #me guardo los filtrados aca 
        for i in paises:
            if int(i["superficie"]) >= sup_min and int(i["superficie"]) <= sup_max:
                filtrados.append([i['nombre'], i['poblacion'], i['superficie']+" km2", i['continente']])
                


        if filtrados:
            for i in filtrados:
                table.add_row(*i)
               
            console.print("\n",table)    
        else: console.print("No se encontro ningun pais con ese rango de superficie.", style="bold underline red")   