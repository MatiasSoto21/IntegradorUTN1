from rich.console import Console # type: ignore
from rich.table import Table # type: ignore


def buscar_pais():
    console = Console()
    table = Table(title= "Países :earth_americas:", style="bold")
    encontrado = []

    while True:
        try:
            busqueda = console.input("Ingresa el nombre del país a buscar: :mag: \n").strip()
        
            if not busqueda:
                raise ValueError("El nombre no puede estar vacío")
        
             # validacion de que sean solo letras y espacios
            if not all(palabra.isalpha() for palabra in busqueda.split()):
                raise ValueError("El nombre solo puede contener letras y espacios")
            
            busqueda = busqueda.replace(" ","").lower()  # le quito los espacios y lo pongo en minus al input para despues buscarlo en el csv
            break  # si esta todo bien salgo del while
        except ValueError as e:
            console.print(f"[red]Error: {e}")  

    with open("data/paises.csv", "r")as archivo:
        encabezado = archivo.readline().strip().split(",")
        table.add_column(encabezado[0].capitalize(), style="cyan")
        table.add_column(encabezado[1].capitalize(), style="magenta")
        table.add_column(encabezado[2].capitalize(), style="green")
        table.add_column(encabezado[3].capitalize(), style="blue")

        lineas = archivo.readlines()

        for i in lineas:
            if busqueda in i.strip().split(",")[0].replace(" ","").lower(): #al csv tambien le quito los espacios y lo pongo en minus para verificar si existe
                encontrado.append(i.strip().split(","))  #me llevo todo el pais con sus datos para despues mostrarlos       

    if len(encontrado) > 0:
        console.print("\n:white_check_mark: Se encontraron los siguientes paises: \n", style="bold underline green")

        for i in encontrado:
            table.add_row(*i)
                
        console.print(table)
    else:      
        console.print(":x: No se encontro ningun pais :x:", style="bold underline red")
             