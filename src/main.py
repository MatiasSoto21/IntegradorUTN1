from funciones.paises import get_paises
from funciones.filtrados import filtrar_continente
from funciones.buscar import buscar_pais
from rich.console import Console # type: ignore

bandera: bool = True
console = Console()

while bandera:
    respuesta = console.input("""
          [bold][underline]Bienvenido a la app de Paises![/bold][/underline]
                              
          Elija la opcion deseada
          ---------------------------------------------------
          1) Buscar Pais
          2) Filtrar paises
          3)
          4) SALIR
                          
""")
    get_paises()
    
    if respuesta == "1":
        buscar_pais()        
    elif respuesta == "2":
        filtrar_continente("Africa")
    elif respuesta == "3":
        pass
    elif respuesta == "4":
        bandera = False
        print("ADIOS")
    else: console.print("[red]ERROR, opcion no valida, intente de nuevo")