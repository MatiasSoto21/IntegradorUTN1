import requests



try:
    res = requests.get("https://www.apicountries.com/countries")
    res.raise_for_status()
    todo = res.json()
    nombres = list(map(lambda e: e["name"], todo))
    print ("names", nombres)


except requests.exceptions.RequestException as error:
    print("Error", error)  