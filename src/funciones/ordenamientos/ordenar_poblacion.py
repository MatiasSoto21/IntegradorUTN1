def ordenar_poblacion():
    try:
        with open("data/paises.csv","r",encoding="utf-8") as archivo:
            lineas = archivo.readlines()
        datos=[]
        for linea in lineas[1: ]: # ← Esto salta la primera línea
            linea = linea.strip()
            if not linea:
                continue
            partes = linea.split(",")
            if len(partes) >= 2 :
                pais = partes[0].strip()
                poblacion_str = partes[1].strip()
                try:
                    poblacion_int = int(poblacion_str)
                    datos.append((pais, poblacion_int))
                except ValueError:
                    print(f"Advertencia: No se pudo convertir '{poblacion_str}' a número")
                    continue
        ascendente = sorted(datos, key=lambda x: x[1])
        descendente = sorted(datos, key=lambda x: x[1], reverse=True)

        while True:
            print("\n" + "="*50)
            print("🌎 ORDENAR POBLACIÓN DE PAÍSES")
            print("="*50)
            print("1) Orden Ascendente (Menor → Mayor Población)")
            print("2) Orden Descendente (Mayor → Menor Población)")  
            print("3) Regresar al menú principal")
            print("="*50)
            opcion=input("Elija una opcion del 1 al 3: ")
            if opcion == "1":
                print("="*40)
                print("📈 Orden Ascendente")
                print("="*40)
                for pais, poblacion in ascendente:
                    print(f"{pais}: {poblacion:,}")
            elif opcion == "2":
                print("="*40)
                print("📉 Orden Descendente")
                print("="*40)
                for pais, poblacion in descendente:
                    print(f"{pais}: {poblacion:,}")
            elif opcion == "3":
                break
            else:
                print("Error, Intente Nuevamente con: 1, 2 ó 3")
    
    except FileNotFoundError:
        print("Error: No se encuentra el archivo data/paises.csv")
    except Exception as e:
        print(f"Error inesperado: {e}")