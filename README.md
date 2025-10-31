# IntegradorUTN1

##  Descripción del programa
Este proyecto es una aplicación desarrollada en **Python 3** que permite **gestionar, analizar y obtener estadísticas de un conjunto de países** a partir de un archivo CSV.  
El sistema fue diseñado aplicando los principios de **programación modular**, utilizando **listas, diccionarios y funciones** para mantener el código claro, reutilizable y bien organizado.

A través de un menú interactivo en consola, el usuario puede realizar **búsquedas personalizadas**, **filtrar información por distintos criterios**, **ordenar** y **consultar estadísticas** clave como el país con mayor o menor población, promedios de población o superficie, y cantidad de países por continente.  
Todo esto se realiza procesando los datos del archivo CSV, aplicando validaciones para evitar errores y asegurando una interacción sencilla y fluida.

El objetivo principal de este trabajo es demostrar el dominio de los conceptos fundamentales de **estructuras de datos**, **condicionales**, **bucles**, **manejo de archivos** y **estadísticas básicas**.

---

## ⚙️ Instrucciones de uso
El proyecto puede ejecutarse tanto de forma local como dentro de un **entorno Docker**, lo que facilita su implementación en cualquier sistema sin necesidad de instalar dependencias manualmente.

### Ejecución local
1. Clonar o descargar el repositorio:
   ```bash
   git clone 
2. Asegurarse de tener instalado Python 3.x en el sistema.
3. Ejecutar el programa principal desde una terminal o entorno de desarrollo:
    python main.py   

### 🐳Ejecución con Docker 

1. Abrir una terminal en la carpeta raíz del proyecto.

2. Construir la imagen de Docker (el nombre puede ser cualquiera):
    ```bash
    docker build -t nombre_ejemplo .

3. Ejecutar el contenedor con el siguiente comando:
    ```bash
    docker run -it --rm -v ${PWD}:/app nombre_ejemplo

### Ejemplos de entradas y salidas
    ```bash
    Bienvenido a la app de Paises!

            Elija la opcion deseada
            ---------------------------------------------------
            1) Buscar Pais
            2) Filtrar paises por continente
            3) Filtrar por rango de poblacion
            4) Filtrar por rango de superficie
            5) Ordenar paises por Nombre
            6) Ordenar paises por Poblacion                 
            7) Ordenar paises por Superficie                 
            8) Mostrar estadisticas                                                       
            9) SALIR

Ingreso 1-Buscar Pais
      
        ───────────────────────────────────────────── Búsqueda de Paises 

    🔍 Ingrese el nombre del país a buscar o escriba 'exit' para volver al menu anterior
    #Escribo: "guay"

     ────────────────────────────╮
    │ ✅ Resultados encontrados: │
    ╰────────────────────────────╯
                          🌎 Países                      
    ┏━━━━━━━━━━┳━━━━━━━━━━━┳━━━━━━━━━━━━┳━━━━━━━━━━━━━━━┓
    ┃ Nombre   ┃ Poblacion ┃ Superficie ┃ Continente    ┃
    ┡━━━━━━━━━━╇━━━━━━━━━━━╇━━━━━━━━━━━━╇━━━━━━━━━━━━━━━┩
    │ Uruguay  │ 3473727   │ 181034 km2 │ South America │
    ├──────────┼───────────┼────────────┼───────────────┤
    │ Paraguay │ 7132530   │ 406752 km2 │ South America │
    └──────────┴───────────┴────────────┴───────────────┘
    Página (1/1)

    Escriba 's' para siguiente | 'a' para anterior | 'e' para salir


### LINKS

Video: https://www.youtube.com/watch?si=x0sVcb-ajBi_yWv5&v=uhh8eJi8P8c&feature=youtu.be
CarpetaDigital(GoogleDrive): https://drive.google.com/drive/folders/1wtY8J5zDjcjz2uo0UIJC96HrNafIiWKn?usp=sharing

### Integrantes
Soto Matías

Pereyra Agustín