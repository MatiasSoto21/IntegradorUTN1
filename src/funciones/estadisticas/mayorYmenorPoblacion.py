import csv
from rich.table import Table # type: ignore
from rich.console import Console # type: ignore

def estadistica_poblacion():
    console = Console()
    table = Table(title="Países con Mayor y Menor Poblacion")
    estilos = ["cyan", "magenta", "green", "blue"]

    with open("data/paises.csv", "r", newline="", encoding="utf-8")as archivo:
        datos = csv.DictReader(archivo)

        for campo, estilo in zip(datos.fieldnames, estilos):
            table.add_column(campo.capitalize(), style=estilo)

        paises = list(datos)

        pais_mayor = max(paises, key=lambda x: x["poblacion"])
        pais_menor = min(paises, key=lambda x: x["poblacion"])
    
        table.add_row(*pais_mayor.values())
        table.add_row(*pais_menor.values())

    console.print(table)         