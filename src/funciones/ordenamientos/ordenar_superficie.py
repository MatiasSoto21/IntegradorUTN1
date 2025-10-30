def ordenar_superficie():
    print("="*50)
    print("      🌍 ORDENAR PAÍSES POR SUPERFICIE")
    print("=" * 50)
    
    while True:
        print("\n¿Cómo quieres ordenar los países?")
        print("1. 📈 Ascendente (de pequeño a grande)")
        print("2. 📉 Descendente (de grande a pequeño)")
        print("3. 🚪 Salir")
        
        opcion = input("\nElige una opción (1, 2 o 3): ")
        
        if opcion == "3":
            print("¡Adiós! 👋")
            break
        
        if opcion not in ["1","2"]:
            print("❌ Opción no válida. Elige 1, 2 o 3.")
            continue

        try: 
            with open("data/paises.csv", "r", encoding="utf-8") as archivo:
                lineas = archivo.readlines()
                
            paises = []
            for i in range(1, len(lineas)):
                linea_limpia = lineas[i].strip()
                if linea_limpia:
                    datos = linea_limpia.split(",")
                    pais = {
                        'nombre': datos[0],
                        'superficie': int(datos[2]),
                        'continente': datos[3]
                    }
                    paises.append(pais)
                    
            if opcion == "1":
                paises_ordenados = sorted(paises, key=lambda x: x['superficie'])
                titulo = "ASCENDENTE (Menor a Mayor) 📈"
            elif opcion == "2":
                paises_ordenados = sorted(paises, key=lambda x: x['superficie'], reverse=True)
                titulo = "DESCENDENTE (Mayor a Menor) 📉"
            
            print(f"\n{'='*50}")
            print(f"{titulo}")
            print(f"{'='*50}")
            print(f"{'#':<2} {'PAÍS':<15} {'SUPERFICIE':<15} {'CONTINENTE':<12}")
            print("-" * 50)
            
            for i, pais in enumerate(paises_ordenados, 1):
                # Formatear número con puntos 
                superficie_bonita = f"{pais['superficie']:,.0f} km²".replace(",", ".")
                print(f"{i:<2} {pais['nombre']:<15} {superficie_bonita:<15} {pais['continente']:<12}")
                
            print(f"\n💡 Total de países mostrados: {len(paises_ordenados)}")
                
        except FileNotFoundError:
            print("❌ Error: No encuentro el archivo 'data/paises.csv'")
            print("   Asegúrate de que el archivo esté en la carpeta 'data/'")
        except Exception as e:
            print(f"❌ Error: {e}")