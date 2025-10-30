import csv
def estadistica_pais():
    # 1. CARGAR DATOS
    try:
        with open("data/paises.csv", 'r', encoding='utf-8') as archivo:
            # csv.DictReader convierte cada fila en un diccionario
            # list() convierte todo en una lista de diccionarios
            paises = list(csv.DictReader(archivo))
            print(f"Se cargaron {len(paises)} países")  # Para debugging
    except FileNotFoundError:
        print("Error: El archivo paises.csv no existe")
        return
    
    # 2. CONTAR PAÍSES
    # Creamos un diccionario vacío para guardar los conteos
    conteo_continentes = {}
    
    # Recorremos cada país de la lista
    for pais in paises:
        # Obtenemos el nombre del continente del país actual
        continente = pais.get('continente')
        
        # Solo procesamos si el país tiene continente
        if continente:
            # Si el continente YA está en el diccionario
            if continente in conteo_continentes:
                # Incrementamos el contador en 1
                conteo_continentes[continente] += 1
            else:
                # Si es la primera vez que vemos este continente, lo inicializamos en 1
                conteo_continentes[continente] = 1
    
    # 3. MOSTRAR RESULTADOS
    print("\n--- CANTIDAD DE PAÍSES POR CONTINENTE ---")
    
    # Ordenamos los continentes alfabéticamente para mejor presentación
    continentes_ordenados = sorted(conteo_continentes.items())
    
    for continente, cantidad in continentes_ordenados:
        print(f"📍 {continente}: {cantidad} países")
    
    # Cálculo del total
    total = sum(conteo_continentes.values())
    print(f"\n📊 TOTAL: {total} países")