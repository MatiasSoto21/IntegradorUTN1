import csv
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.prompt import Prompt
from rich.text import Text

console = Console()

def ordenar_poblacion():
    """Función que ordena países por población con interfaz Rich y paginación"""
    
    try:
        # Leer y procesar los datos
        with open("data/paises.csv", "r", encoding="utf-8") as archivo:
            lector = csv.reader(archivo)
            next(lector)  # Saltar encabezado
            
            datos = []
            paises_con_error = []
            
            for linea in lector:
                if not linea or len(linea) < 2:
                    continue
                    
                pais = linea[0].strip()
                poblacion_str = linea[1].strip()
                
                try:
                    poblacion_int = int(poblacion_str)
                    datos.append((pais, poblacion_int))
                except ValueError:
                    paises_con_error.append(pais)
                    continue
        
        # Mostrar advertencias si hay países con datos inválidos
        if paises_con_error:
            console.print(
                Panel(
                    f"[yellow]⚠️ Advertencia: No se pudo procesar la población de {len(paises_con_error)} países[/yellow]\n"
                    f"[dim]Países afectados: {', '.join(paises_con_error[:5])}{'...' if len(paises_con_error) > 5 else ''}[/dim]",
                    title="Advertencia de Datos",
                    border_style="yellow"
                )
            )
            console.input("\nPresione Enter para continuar...")
        
        if not datos:
            console.print(
                Panel(
                    "[red]❌ No se encontraron datos válidos de población[/red]",
                    title="Error de Datos",
                    border_style="red"
                )
            )
            console.input("\nPresione Enter para continuar...")
            return
        
        # Ordenar datos
        ascendente = sorted(datos, key=lambda x: x[1])
        descendente = sorted(datos, key=lambda x: x[1], reverse=True)

        # Menú principal
        while True:
            console.clear()
            console.print(
                Panel.fit(
                    "[bold cyan]🌎 ORDENAR POBLACIÓN DE PAÍSES[/bold cyan]",
                    border_style="cyan"
                )
            )
            
            console.print("\n[bold]Selecciona el tipo de orden:[/bold]")
            console.print("[cyan]1.[/cyan] Orden Ascendente (Menor → Mayor Población)")
            console.print("[cyan]2.[/cyan] Orden Descendente (Mayor → Menor Población)")  
            console.print("[cyan]3.[/cyan] Regresar al menú principal")
            
            # Validación manual en español
            while True:
                opcion = console.input("\nTu elección (1-3): ").strip()
                if opcion in ["1", "2", "3"]:
                    break
                else:
                    console.print("[red]❌ Error: Por favor seleccione 1, 2 o 3[/red]")
            
            if opcion == "3":
                break
            elif opcion == "1":
                mostrar_poblacion_paginada(ascendente, "📈 POBLACIÓN ASCENDENTE", "Menor a Mayor")
            elif opcion == "2":
                mostrar_poblacion_paginada(descendente, "📉 POBLACIÓN DESCENDENTE", "Mayor a Menor")
    
    except FileNotFoundError:
        console.print(
            Panel(
                "[bold red]❌ Error: No se encuentra el archivo data/paises.csv[/bold red]",
                title="Error de Archivo",
                border_style="red"
            )
        )
        console.input("\nPresione Enter para continuar...")
    except Exception as e:
        console.print(
            Panel(
                f"[bold red]❌ Error inesperado: {str(e)}[/bold red]",
                title="Error",
                border_style="red"
            )
        )
        console.input("\nPresione Enter para continuar...")

def mostrar_poblacion_paginada(datos, titulo, subtitulo):
    """Muestra la lista de países con población en formato paginado"""
    
    elementos_por_pagina = 15
    total_paginas = (len(datos) + elementos_por_pagina - 1) // elementos_por_pagina
    pagina_actual = 1
    
    while True:
        console.clear()
        
        # Crear tabla
        table = Table(
            title=f"{titulo} - {subtitulo}",
            show_header=True,
            header_style="bold magenta",
            title_style="bold green",
            caption=f"Página {pagina_actual} de {total_paginas}"
        )
        table.add_column("#", style="dim", width=6, justify="right")
        table.add_column("País", style="cyan", min_width=25)
        table.add_column("Población", style="bold green", width=15, justify="right")
        
        # Calcular índices para la página actual
        inicio = (pagina_actual - 1) * elementos_por_pagina
        fin = min(inicio + elementos_por_pagina, len(datos))
        
        # Agregar filas a la tabla
        for i in range(inicio, fin):
            pais, poblacion = datos[i]
            # Formatear población con separadores de miles
            poblacion_formateada = f"{poblacion:,}"
            table.add_row(str(i + 1), pais, poblacion_formateada)
        
        # Estadísticas
        total_poblacion = sum(p[1] for p in datos)
        promedio_poblacion = total_poblacion // len(datos)
        
        # Mostrar tabla
        console.print(table)
        
        # Panel de estadísticas
        console.print(
            Panel(
                f"[bold]Estadísticas:[/bold]\n"
                f"• Total de países: [cyan]{len(datos):,}[/cyan]\n"
                f"• Población total: [green]{total_poblacion:,}[/green]\n"
                f"• Población promedio: [yellow]{promedio_poblacion:,}[/yellow]",
                title="📊 Resumen",
                border_style="blue"
            )
        )
        
        console.print(f"\n[dim]Mostrando {inicio + 1}-{fin} de {len(datos)} países[/dim]")
        
        # Opciones de navegación - VALIDACIÓN MANUAL EN ESPAÑOL
        console.print("\n[bold]Opciones de navegación:[/bold]")
        
        opciones_texto = []
        opciones_validas = []
        
        if pagina_actual > 1:
            opciones_texto.append("[green]← Anterior (A)[/green]")
            opciones_validas.extend(['a', 'A'])
        
        if pagina_actual < total_paginas:
            opciones_texto.append("[green]Siguiente → (S)[/green]")
            opciones_validas.extend(['s', 'S'])
        
        opciones_texto.append("[yellow]Volver al menú (V)[/yellow]")
        opciones_validas.extend(['v', 'V'])
        
        # Mostrar opciones disponibles
        console.print(" • ".join(opciones_texto))
        
        # Validación manual de entrada
        while True:
            opcion = console.input("\nSelecciona una opción: ").strip().lower()
            
            if opcion in opciones_validas:
                break
            else:
                opciones_disponibles = "/".join(set([opt.upper() for opt in opciones_validas]))
                console.print(f"[red]❌ Error: Opción no válida. Use: {opciones_disponibles}[/red]")
        
        # Procesar opción
        if opcion == 'a' and pagina_actual > 1:
            pagina_actual -= 1
        elif opcion == 's' and pagina_actual < total_paginas:
            pagina_actual += 1
        elif opcion == 'v':
            break

if __name__ == "__main__":
    # Para testing independiente
    ordenar_poblacion()