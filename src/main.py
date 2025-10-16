from funciones.paises import get_paises
from funciones.filtrados import filtrar_continente
from funciones.buscar import buscar_pais

bandera: bool = True

while bandera:
    respuesta = input("""
          Bienvenido a la app de Paises!
          Elija la opcion deseada
          ---------------------------------------------------
          1)Buscar Pais
          2)Filtrar paises
          3)
          4)SALIR
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
    else: print("ERROR, opcion no valida, intente de nuevo")