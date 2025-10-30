import csv
from rich.console import Console # type: ignore
from rich.table import Table # type: ignore
from rich.panel import Panel # type: ignore

# Crear una consola para usar Rich (como un print mejorado)
console = Console()

def estadistica_pais():
    console.clear()
    print()
    print()

    # 1. CARGAR DATOS
    try:
        with open("data/paises.csv", 'r', encoding='utf-8') as archivo:
            # csv.DictReader convierte cada fila en un diccionario
            # list() convierte todo en una lista de diccionarios
            paises = list(csv.DictReader(archivo))
            console.print(f"[green]✓ Se cargaron {len(paises)} países[/green]")  # Para debugging
    except FileNotFoundError:
        console.print(
            Panel(
                "[bold red]❌ Error: El archivo paises.csv no existe[/bold red]\n"
                "[yellow]💡 Verifica que el archivo esté en la carpeta data/[/yellow]",
                title="Error",
                border_style="red"
            )
        )
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
    
    # 3. MOSTRAR RESULTADOS CON RICH
    console.print(
        Panel.fit(
            "[bold cyan]🌍 CANTIDAD DE PAÍSES POR CONTINENTE[/bold cyan]",
            style="bold cyan"
        )
    )
    
    # Crear una tabla con Rich
    tabla = Table(
        title="📊 Estadísticas por Continente",
        show_header=True,
        header_style="bold magenta"
    )
    
    # Agregar columnas a la tabla
    tabla.add_column("Continente", style="bold cyan", width=15)
    tabla.add_column("Cantidad", style="bold yellow", justify="center")
    
    # Ordenamos los continentes alfabéticamente para mejor presentación
    continentes_ordenados = sorted(conteo_continentes.items())
    
    # Calcular el total de países
    total_paises = sum(conteo_continentes.values())
    
    # Agregar cada continente a la tabla
    for continente, cantidad in continentes_ordenados:
        # Calcular porcentaje
        porcentaje = (cantidad / total_paises) * 100
        
        # Agregar fila a la tabla
        tabla.add_row(
            f"📍 {continente}",
            f"{cantidad} países",
        )
    
    # Mostrar la tabla
    console.print(tabla)
    
    # Mostrar el total en un panel especial
    console.print(
        Panel(
            f"[bold green]📊 TOTAL: {total_paises} países[/bold green]",
            border_style="green"
        )
    )
    console.input("Presione Enter para continuar...")

# Si quieres probar la función directamente
if __name__ == "__main__":
    estadistica_pais()