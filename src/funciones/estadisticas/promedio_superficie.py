import csv
def estadistica_superficie():
    while True:
        try: 
            with open("data/paises.csv",'r',encoding='utf-8') as archivo:
                paises = list(csv.DictReader(archivo))
        except:
            print("Error: No se pudo cargar el archivo paises.csv")
            return
        continentes = sorted(set(p['continente'] for p in paises if p.get('continente')))
        print("\n--- CONTINENTES DISPONIBLES ---")
        for i, c in enumerate(continentes, 1):
            print(f"{i}. {c}")
        try:
            opcion = int(input("\nElige un Continente: ")) - 1
            continente = continentes[opcion]
            superficies = [int(p['superficie']) for p in paises if p.get('continente') == continente and p.get('superficie')]
            if superficies:
                promedio = sum(superficies) / len(superficies)
                print(f"\nPromedio de superficie en {continente}: {promedio:,.2f} km²".replace(',','.'))
            else:
                print("No hay datos disponibles.")
        except (ValueError, IndexError):
            print("Selección inválida")
        print("\nDesea continuar: ")
        op = input("si o no: ")
        continuar = input("\n¿Desea continuar? (si/no): ").lower()
        if continuar != "si":
            print("¡Hasta luego!")
            break