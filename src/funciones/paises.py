import requests

def get_paises():
    try:
        res = requests.get("https://restcountries.com/v3.1/all?fields=name,population,area,continents")
        res.raise_for_status()
        todo = res.json()
        csv = [
            "nombre,poblacion,superficie,continente\n"
    ]
        info = list(map(lambda e: f"{e['name']['common']},{e['population']},{round(e['area'])},{e['continents'][0]}\n",todo))
        csv += info

    except requests.exceptions.RequestException as error:
        print("Error", error)  

    with open("data/paises.csv", "w")as archivo:
        archivo.writelines(csv)


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
                
