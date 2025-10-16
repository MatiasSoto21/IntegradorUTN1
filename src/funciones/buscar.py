def buscar_pais():

    encontrado = []

    while True:
        try:
            busqueda = input("Ingresa el nombre del país a buscar: \n").strip()
        
            if not busqueda:
                raise ValueError("El nombre no puede estar vacío")
        
             # validacion de que sean solo letras y espacios
            if not all(palabra.isalpha() for palabra in busqueda.split()):
                raise ValueError("El nombre solo puede contener letras y espacios")
            
            busqueda = busqueda.replace(" ","").lower()  # le quito los espacios y lo pongo en minus al input para despues buscarlo en el csv
            break  # si esta todo bien salgo del while
        except ValueError as e:
            print(f"Error: {e}")  

    with open("data/paises.csv", "r")as archivo:
        encabezado = archivo.readline().strip().split(",")
        lineas = archivo.readlines()

        for i in lineas:
            if busqueda in i.strip().split(",")[0].replace(" ","").lower(): #al csv tambien le quito los espacios y lo pongo en minus para verificar si existe
                encontrado.append(i.strip().split(","))  #me llevo todo el pais con sus datos para despues mostrarlos       

    if len(encontrado) > 0:
        print("\nSe encontraron los siguientes paises: \n")
        for i in encontrado:
            for c,v in zip(encabezado, i):
                print(f"{c.capitalize()}: {v}") # armo el print con la columna y el valor de la fila
            print("-----------------")
    else: print("No se encontro ningun pais")
             