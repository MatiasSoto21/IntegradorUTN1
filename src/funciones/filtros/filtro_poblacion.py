from rich.console import Console # type: ignore
from rich.table import Table # type: ignore

def filtrar_poblacion():
    console = Console()

    while True:  #Validacion del rango minimo
        try:
            pob_min = input("Ingrese población mínima: ")

            if " " in pob_min:
                raise ValueError("ERROR: No se permiten espacios")

            if not pob_min.isdigit():
                raise ValueError("ERROR: Solo se permiten valores numéricos enteros y positivos")

            pob_min = int(pob_min)

            if pob_min < 0:
                raise ValueError("ERROR: La población mínima debe ser positiva")

            break #si esta todo bien salgo del while
        except ValueError as e:
            console.print(f"[red]{e}")

    while True: # Validacion del rango máximo
        try:
            pob_max = input("Ingrese población máxima: ")

            if " " in pob_max:
                raise ValueError("ERROR: No se permiten espacios")

            if not pob_max.isdigit():
                raise ValueError("ERROR: Solo se permiten valores numéricos enteros y positivos")

            pob_max = int(pob_max)

            if pob_max <= pob_min:
                raise ValueError("ERROR: La población máxima debe ser mayor a la poblacion mínima")

            break#si ta todo bien salgo
        except ValueError as e:
            console.print(f"[red]{e}")

    table = Table(title= f"Países con rango de poblacion entre: {pob_min} y {pob_max} :earth_americas:", style="bold")

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
            fila[2] = fila[2] + " km2"
            paises.append(dict(zip(encabezado,fila)))

        filtrados = [] #me guardo los filtrados aca 
        for i in paises:
            if int(i["poblacion"]) >= pob_min and int(i["poblacion"]) <= pob_max:
                filtrados.append([i['nombre'], i['poblacion'], i['superficie'], i['continente']])
                


        if filtrados:
            for i in filtrados:
                table.add_row(*i)
               
            console.print("\n",table)    
        else: console.print("No se encontro ningun pais con ese rango de poblacion.", style="bold underline red")            