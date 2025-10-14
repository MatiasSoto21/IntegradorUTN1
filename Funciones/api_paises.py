import requests

try:
    res = requests.get("https://restcountries.com/v3.1/all?fields=name,population,area,continents")
    res.raise_for_status()
    todo = res.json()
    csv = [
        "nombre,poblacion,superficie,continente\n"
    ]
    info = list(map(lambda e: f"{e['name']['common']},{e['population']},{round(e['area'])},{e['continents'][0]}\n",todo))
    csv += info
    print("names", info)
    print("ARCHIVO LISTO:", csv)

except requests.exceptions.RequestException as error:
    print("Error", error)  

with open("paises.csv", "w")as archivo:
    archivo.writelines(csv) 