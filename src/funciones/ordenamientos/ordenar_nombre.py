import csv  

def ordenar_nombre(paises_csv="data/paises.csv", orden='A-Z'):
    paises = []
    try:
        with open(paises_csv, "r", encoding='utf-8') as archivo:
            lector = csv.reader(archivo)
            primera_fila = next(lector)  # salta el encabezado 
            
            for linea in lector:
                if linea and linea[0].strip():  # Verifica que no esté vacío
                    paises.append(linea[0].strip())
        
        if orden.upper() == "A-Z":
            paises.sort()
        elif orden.upper() == "Z-A":
            paises.sort(reverse=True)
        else:
            print("Error: Orden debe ser 'A-Z' o 'Z-A'")
            return []
        
        return paises
        
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo {paises_csv}")
        return []
    except Exception as e:
        print(f"Error: {e}")
        return []

if __name__ == "__main__":
    print("=== Países A-Z ===")
    paises_az = ordenar_nombre('data/paises.csv', 'A-Z')  # ✅ Ruta correcta
    for pais in paises_az:
        print(pais)

    print("\n=== Países Z-A ===")
    paises_za = ordenar_nombre('data/paises.csv', 'Z-A')  # ✅ Ruta correcta
    for pais in paises_za:
        print(pais)