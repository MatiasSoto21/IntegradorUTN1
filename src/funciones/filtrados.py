from rich.console import Console # type: ignore
from rich.table import Table # type: ignore

def filtrar_continente():
    console = Console()
    while True:
        try:
            filtro = console.input("""
            [bold][underline] Seleccione el filtro a aplicar: [/bold][/underline]
            1)Mostrar países de África
            2)Mostrar países de América del Norte
            3)Mostrar países de América del Sur
            4)Mostrar países de Asia
            5)Mostrar países de Oceania
            6)Mostrar países de Europa  
            7)Mostrar países de Antartida                     
            """)

            if filtro not in ("1","2","3","4","5","6","7"):
                raise ValueError("Porfavor seleccione algunas de las opciones (1,2,3,4,5,6 o 7)")
            break
        except ValueError as e:
            console.print(f"[red]{e}")    

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
        
    table = Table(title= f"Países de {filtro} :earth_americas:", style="bold")

    with open("data/paises.csv", "r")as archivo:
        encabezado = archivo.readline().strip().split(",")
        table.add_column(encabezado[0].capitalize(), style="cyan")
        table.add_column(encabezado[1].capitalize(), style="magenta")
        table.add_column(encabezado[2].capitalize(), style="green")
        table.add_column(encabezado[3].capitalize(), style="blue")

        lineas = archivo.readlines()
        filtrados = []

        for i in lineas:
            fila = i.strip().split(",")

            if any(filtro in elemento for elemento in fila):
                filtrados.append(fila)

    if filtrados:
        for i in filtrados:
            table.add_row(*i)
        return console.print(table)
    else:
        return print("No se encontraron paises para el filtro")