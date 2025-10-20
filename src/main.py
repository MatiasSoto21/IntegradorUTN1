from funciones.getpaises.paises import get_paises
from funciones.filtros.filtro_continente import filtrar_continente
from funciones.buscar.buscar import buscar_pais
from rich.console import Console # type: ignore

bandera: bool = True
console = Console()

while bandera:
    respuesta = console.input("""
        [bold][underline]Bienvenido a la app de Paises![/bold][/underline]
                              
        Elija la opcion deseada
        ---------------------------------------------------
        1) Buscar Pais
        2) Filtrar paises por continente
        3) Filtrar por rango de poblacion
        4) Filtrar por rango de superficie
        5) Ordenar paises por Nombre
        6) Ordenar paises por Poblacion                 
        7) Ordenar paises por Superficie                 
        8) Mostrar estadisticas                                                       
        9) SALIR
                          
""")
    get_paises()
    
    if respuesta == "1":
        buscar_pais()        
    elif respuesta == "2":
        filtrar_continente()
    elif respuesta == "3":
        pass
    elif respuesta == "4":
        pass
    elif respuesta == "5":
        pass
    elif respuesta == "6":
        pass
    elif respuesta == "7":
        pass
    elif respuesta == "8":
        pass
    elif respuesta == "9":
        bandera = False
        print("ADIOS")
    else: console.print("[red]ERROR, opcion no valida, intente de nuevo")