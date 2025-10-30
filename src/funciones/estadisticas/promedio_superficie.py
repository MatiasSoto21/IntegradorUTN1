import csv
from rich.console import Console
from rich.table import Table
from rich.panel import Panel

# Crear una consola para usar Rich
console = Console()

def estadistica_superficie():
    while True:
        # Limpiar pantalla
        console.clear()
        
        # Título principal con Panel
        console.print(
            Panel.fit(
                "📊 ESTADÍSTICAS DE SUPERFICIE POR CONTINENTE",
                style="bold cyan"
            )
        )
        
        try: 
            # Leer el archivo CSV
            with open("data/paises.csv", 'r', encoding='utf-8') as archivo:
                paises = list(csv.DictReader(archivo))
                
        except FileNotFoundError:
            # Mensaje de error con color
            console.print(
                Panel(
                    "[bold red]❌ Error: No se encontró el archivo paises.csv[/bold red]\n"
                    "[yellow]💡 Asegúrate de que el archivo esté en la carpeta data/[/yellow]",
                    title="Error",
                    border_style="red"
                )
            )
            input("\nPresiona Enter para volver...")
            return
            
        except Exception as e:
            console.print(f"[bold red]❌ Error al leer el archivo: {e}[/bold red]")
            input("\nPresiona Enter para volver...")
            return

        # Obtener lista de continentes únicos
        continentes = []
        for pais in paises:
            if pais.get('continente'):
                continentes.append(pais['continente'])
        
        continentes = sorted(set(continentes))
        
        # Mostrar continentes disponibles en una tabla
        console.print("\n[bold green]🌍 CONTINENTES DISPONIBLES[/bold green]")
        tabla_continentes = Table(show_header=True, header_style="bold magenta")
        tabla_continentes.add_column("N°", style="dim", width=4)
        tabla_continentes.add_column("Continente", style="cyan")
        
        for i, continente in enumerate(continentes, 1):
            tabla_continentes.add_row(str(i), continente)
            
        console.print(tabla_continentes)

        try:
            # Pedir al usuario que elija un continente
            opcion = int(input("\n👉 Elige un continente (número): ")) - 1
            continente_elegido = continentes[opcion]
            
            # Calcular estadísticas
            superficies = []
            for pais in paises:
                if (pais.get('continente') == continente_elegido and 
                    pais.get('superficie')):
                    try:
                        superficies.append(int(pais['superficie']))
                    except ValueError:
                        continue  # Si hay error en el número, lo saltamos
            
            if superficies:
                total_paises = len(superficies)
                suma_superficies = sum(superficies)
                promedio = suma_superficies / total_paises
                
                # Formatear números con puntos en lugar de comas
                superficie_total_formateada = f"{suma_superficies:,.0f}".replace(",", ".")
                promedio_formateado = f"{promedio:,.2f}".replace(",", ".")
                
                # Mostrar resultados en un Panel bonito
                console.print(
                    Panel(
                        f"[bold cyan]Continente:[/bold cyan] {continente_elegido}\n"
                        f"[bold green]Total de países:[/bold green] {total_paises}\n"
                        f"[bold yellow]Superficie total:[/bold yellow] {superficie_total_formateada} km²\n"
                        f"[bold magenta]Promedio de superficie:[/bold magenta] {promedio_formateado} km²",
                        title="📈 RESULTADOS",
                        border_style="green"
                    )
                )
            else:
                console.print(
                    Panel(
                        f"[yellow]No hay datos de superficie disponibles para {continente_elegido}[/yellow]",
                        border_style="yellow"
                    )
                )
                
        except (ValueError, IndexError):
            console.print("[bold red]❌ Error: Número de continente inválido[/bold red]")
        
        # Preguntar si quiere continuar
        console.print("\n")
        continuar = input("¿Quieres ver otra estadística? (sí/no): ").lower()
        
        if continuar not in ['si', 'sí', 's']:
            console.print("[bold green]¡Hasta luego! 👋[/bold green]")
            break

# Si quieres probar la función directamente
if __name__ == "__main__":
    estadistica_superficie()