def filtrar_continente(continente):
    with open("data/paises.csv", "r")as archivo:
        encabezado = archivo.readline()
        lineas = archivo.readlines()
        filtrados = []
        for i in lineas:
            fila = i.strip().split(",")
            if continente in fila:
                filtrados.append(fila)

    return print(filtrados)