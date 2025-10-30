import csv
from rich.console import Console
from rich.table import Table
from rich.panel import Panel

console = Console()

def ordenar_nombre():
    """Función que ordena países por nombre (A-Z o Z-A) con interfaz Rich"""
    
    # Verificar que el archivo existe
    try:
        with open('data/paises.csv', 'r', encoding='utf-8') as archivo:
            pass
    except FileNotFoundError:
        console.print(
            Panel(
                "[bold red]❌ Error: No se encontró el archivo paises.csv[/bold red]",
                title="Error de Archivo",
                border_style="red"
            )
        )
        input("\nPresiona Enter para continuar...")
        return
    
    while True:
        console.clear()
        console.print(
            Panel.fit(
                "[bold cyan]📊 ORDENAR PAÍSES POR NOMBRE[/bold cyan]",
                border_style="cyan"
            )
        )
        
        console.print("\n[bold]Selecciona el tipo de orden:[/bold]")
        console.print("[cyan]1.[/cyan] Orden Ascendente (A-Z)")
        console.print("[cyan]2.[/cyan] Orden Descendente (Z-A)")
        console.print("[cyan]3.[/cyan] Volver al Menú Principal")
        
        opcion = input("\n👉 Tu elección (1-3): ").strip()
        
        if opcion == "3":
            return
        
        if opcion not in ["1", "2"]:
            console.print("\n[bold red]❌ Opción no válida. Por favor elige 1, 2 o 3.[/bold red]")
            input("\nPresiona Enter para continuar...")
            continue
        
        # Leer y ordenar los países
        paises = []
        try:
            with open('data/paises.csv', 'r', encoding='utf-8') as archivo:
                lector = csv.reader(archivo)
                next(lector)  # Saltar encabezado
                
                for linea in lector:
                    if linea and linea[0].strip():
                        paises.append(linea[0].strip())
            
            if not paises:
                console.print(
                    Panel(
                        "[yellow]⚠️ No se encontraron países en el archivo[/yellow]",
                        border_style="yellow"
                    )
                )
                input("\nPresiona Enter para continuar...")
                continue
            
            # Aplicar ordenamiento
            if opcion == "1":
                paises.sort()  # A-Z
                titulo = "🌍 Países Ordenados A-Z"
                orden_texto = "ascendente"
            else:
                paises.sort(reverse=True)  # Z-A
                titulo = "🌍 Países Ordenados Z-A"
                orden_texto = "descendente"
            
            # Mostrar resultados con paginación simple
            mostrar_paises_paginados(paises, titulo, orden_texto)
            
        except Exception as e:
            console.print(
                Panel(
                    f"[bold red]❌ Error al procesar el archivo: {e}[/bold red]",
                    title="Error",
                    border_style="red"
                )
            )
            input("\nPresiona Enter para continuar...")

def mostrar_paises_paginados(paises, titulo, orden_texto):
    """Muestra la lista de países con paginación simple"""
    
    if not paises:
        console.print(
            Panel(
                "[yellow]⚠️ No hay países para mostrar[/yellow]",
                border_style="yellow"
            )
        )
        input("\nPresiona Enter para continuar...")
        return
    
    elementos_por_pagina = 20
    total_paginas = (len(paises) + elementos_por_pagina - 1) // elementos_por_pagina
    pagina_actual = 1
    
    while True:
        console.clear()
        print()
        print()

        
        # Crear tabla
        table = Table(
            title=f"{titulo} - Página {pagina_actual} de {total_paginas}",
            show_header=True,
            header_style="bold magenta",
            title_style="bold green"
        )
        table.add_column("#", style="dim", width=6)
        table.add_column("País", style="cyan", min_width=25)
        
        # Calcular índices para la página actual
        inicio = (pagina_actual - 1) * elementos_por_pagina
        fin = min(inicio + elementos_por_pagina, len(paises))
        
        # Agregar filas a la tabla
        for i in range(inicio, fin):
            table.add_row(str(i + 1), paises[i])
        
        # Mostrar tabla
        console.print(table)
        console.print(f"\n[dim]Mostrando {inicio + 1}-{fin} de {len(paises)} países (Orden {orden_texto})[/dim]")
        
        # Navegación simple
        if total_paginas > 1:
            if pagina_actual < total_paginas:
                console.print(f"\n[bold green]Presiona Enter[/bold green] para ver la siguiente página")
            else:
                console.print(f"\n[bold yellow]✓ Fin de la lista[/bold yellow]")
            
            console.print(f"[bold red]Escribe 'M'[/bold red] para volver al menú")
            
            opcion = input("\n👉 ¿Qué deseas hacer? ").strip().upper()
            
            if opcion == "M":
                break
            elif pagina_actual < total_paginas:
                pagina_actual += 1
            else:
                # Si está en la última página y presiona Enter, volver
                break
        else:
            # Solo hay una página
            console.print(f"\n[bold yellow]✓ Fin de la lista[/bold yellow]")
            input("\nPresiona Enter para volver al menú...")
            break

if __name__ == "__main__":
    # Para testing independiente
    ordenar_nombre()