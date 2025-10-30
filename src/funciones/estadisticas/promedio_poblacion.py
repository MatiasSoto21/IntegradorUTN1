import csv
from rich.table import Table # type: ignore
from rich.console import Console # type: ignore

def estadistica_poblacionContinente():
    console = Console()

    while True:
        try:
            continente = console.input("""
            [bold][underline] Seleccione el continente del cual desea saber el promedio de Poblacion [/bold][/underline]
            1)Promedio de Poblacion de África
            2)Promedio de Poblacion de América del Norte
            3)Promedio de Poblacion de América del Sur
            4)Promedio de Poblacion de Asia
            5)Promedio de Poblacion de Oceania
            6)Promedio de Poblacion de Europa  
            7)Promedio de Poblacion de Antartida     
            8)Promedio de poblacion de Todos los países           
            """)

            if continente not in ("1","2","3","4","5","6","7", "8"):
                raise ValueError("Porfavor seleccione algunas de las opciones (1,2,3,4,5,6,7 u 8)")
            break
        except ValueError as e:
            console.print(f"[red]{e}")    

    if continente == "1":
        continente = "Africa"  
    elif continente == "2":
        continente = "North America"
    elif continente == "3":
        continente = "South America"  
    elif continente == "4":
        continente = "Asia"    
    elif continente == "5":
        continente = "Oceania"      
    elif continente == "6":
        continente = "Europe"  
    elif continente == "7":
        continente = "Antarctica"
    elif continente == "8":
        continente = "todos"    
  
    with open("data/paises.csv", "r", newline="", encoding="utf-8")as archivo:
        datos = csv.DictReader(archivo)

        paises = list(datos)

        totalSuma = 0 
        cantidad = 0
        for i in paises:
            if continente == "todos" or i["continente"] == continente:
                totalSuma += int(i["poblacion"])
                cantidad += 1

        promedioTodos = totalSuma / cantidad

    return console.print(f"El promedio de poblacion de {'todos los paises' if continente == 'todos' else 'los paises de ' + continente} es: {promedioTodos:.2f}")             