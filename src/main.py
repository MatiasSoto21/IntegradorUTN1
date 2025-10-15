from funciones.paises import get_paises
from funciones.filtrados import filtrar_continente


bandera: bool = True

while bandera:
    respuesta = input("""
          Bienvenido a la app de Paises!
          Elija la opcion deseada
          ---------------------------------------------------
          1)Filtrar paises
          2)
          3)
          4)SALIR
""")
    get_paises()
    
    if respuesta == "1":
        filtrar_continente("Africa")
    elif respuesta == "2":
        pass
    elif respuesta == "3":
        pass
    elif respuesta == "4":
        bandera = False
        print("ADIOS")
    else: print("ERROR, opcion no valida, intente de nuevo")