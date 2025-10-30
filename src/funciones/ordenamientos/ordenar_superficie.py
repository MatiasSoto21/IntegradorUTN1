from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.prompt import Prompt
import os

def ordenar_superficie():
    console = Console()
    
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        
        console.print(Panel.fit(
            "🌍 ORDENAR PAÍSES POR SUPERFICIE",
            style="bold cyan",
            padding=(1, 2)
        ))
        
        console.print("\n")
        
        opciones = {
            "1": "📈 Ascendente (de pequeño a grande)",
            "2": "📉 Descendente (de grande a pequeño)", 
            "3": "🚪 Salir"
        }
        
        for key, value in opciones.items():
            console.print(f"[bold yellow]{key}.[/bold yellow] {value}")
        
        console.print("\n")
        
        opcion = input("Elige una opción (1, 2 o 3): ").strip()
        
        if opcion == "3":
            console.print("\n[bold green]¡Adiós! 👋[/bold green]")
            break
        
        if opcion not in ["1", "2"]:
            console.print("\n[bold red]❌ Opción no válida. Por favor elige 1, 2 o 3.[/bold red]")
            console.print("\n")
            input("Presiona Enter para continuar...")
            continue
        
        try:
            if not os.path.exists("data/paises.csv"):
                raise FileNotFoundError("No se encuentra el archivo 'data/paises.csv'")
            
            with open("data/paises.csv", "r", encoding="utf-8") as archivo:
                lineas = archivo.readlines()
                
            if len(lineas) <= 1:
                raise ValueError("El archivo está vacío o no contiene datos")
                
            paises = []
            for i in range(1, len(lineas)):
                linea_limpia = lineas[i].strip()
                if linea_limpia:
                    datos = linea_limpia.split(",")
                    if len(datos) < 4:
                        continue
                    
                    try:
                        pais = {
                            'nombre': datos[0],
                            'superficie': int(datos[2]),
                            'continente': datos[3]
                        }
                        paises.append(pais)
                    except (ValueError, IndexError):
                        continue
            
            if not paises:
                raise ValueError("No se pudieron cargar datos válidos de países")
                    
            if opcion == "1":
                paises_ordenados = sorted(paises, key=lambda x: x['superficie'])
                titulo = "📈 ORDEN ASCENDENTE (Menor a Mayor)"
                estilo_titulo = "bold green"
            else:
                paises_ordenados = sorted(paises, key=lambda x: x['superficie'], reverse=True)
                titulo = "📉 ORDEN DESCENDENTE (Mayor a Menor)"
                estilo_titulo = "bold red"
            
            # Paginación simple
            mostrar_paginacion_simple(console, paises_ordenados, titulo, estilo_titulo)
                
        except FileNotFoundError as e:
            console.print(f"\n[bold red]❌ ERROR: Archivo no encontrado[/bold red]")
            console.print(f"[red]Detalles: {e}[/red]")
        except Exception as e:
            console.print(f"\n[bold red]❌ ERROR: {e}[/bold red]")
        
        console.print("\n")
        input("Presiona Enter para continuar...")

def mostrar_paginacion_simple(console, paises, titulo, estilo_titulo):
    """Paginación simple sin navegación compleja"""
    
    elementos_por_pagina = 20  # Más elementos por página
    total_paginas = (len(paises) + elementos_por_pagina - 1) // elementos_por_pagina
    
    for pagina in range(total_paginas):
        os.system('cls' if os.name == 'nt' else 'clear')
        
        inicio = pagina * elementos_por_pagina
        fin = inicio + elementos_por_pagina
        paises_pagina = paises[inicio:fin]
        
        # Crear tabla
        tabla = Table(
            title=f"{titulo} - Página {pagina + 1} de {total_paginas}",
            title_style=estilo_titulo,
            show_header=True,
            header_style="bold magenta"
        )
        
        tabla.add_column("#", style="dim", width=4)
        tabla.add_column("País", style="bold cyan", width=20)
        tabla.add_column("Superficie", style="bold yellow", width=15)
        tabla.add_column("Continente", style="bold green", width=12)
        
        for i, pais in enumerate(paises_pagina, start=inicio + 1):
            superficie_formateada = f"{pais['superficie']:,.0f} km²".replace(",", ".")
            tabla.add_row(
                str(i),
                pais['nombre'],
                superficie_formateada,
                pais['continente']
            )
        
        console.print(tabla)
        console.print(f"\n[dim]Mostrando {len(paises_pagina)} de {len(paises)} países[/dim]")
        
        # Navegación simple sin Rich Prompt
        if pagina < total_paginas - 1:
            console.print(f"\n[bold yellow]Presiona Enter[/bold yellow] para ver siguiente página")
            console.print(f"[bold red]Escribe 'M'[/bold red] para volver al menú principal")
            
            opcion = input("\n¿Qué deseas hacer? ").strip().upper()
            
            if opcion == "M":
                break
            # Si presiona Enter o cualquier otra cosa, continúa a la siguiente página
        else:
            # Última página
            console.print(f"\n[bold green]✓ Fin de la lista[/bold green]")
            input("Presiona Enter para volver al menú...")
            break

if __name__ == "__main__":
    ordenar_superficie()