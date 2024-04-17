# TLP 3 - Python para Ciencia de datos
## Trabajo Práctico N° 3


El programa realiza lo siguiente:

**Agrupación y Exportación por Provincia:**

Posee una función llamada “analisis_estadistico” que acepta como parámetro una lista de valores numéricos extraídos de un csv y transformado a DataFrame de pandas. 

**Se implementó el cálculo de las siguientes columnas:**
- fi: Frecuencia absoluta de cada valor en la lista. 
- Fi: Frecuencia acumulada, es decir, la suma acumulada de las frecuencias absolutas.
- ri: Frecuencia relativa, que se calcula dividiendo la frecuencia absoluta de cada valor entre el tamaño total de la muestra.
- Ri: Frecuencia relativa acumulada, la suma acumulada de las frecuencias relativas.
- pi: Probabilidad, que se obtiene dividiendo la frecuencia absoluta de cada valor entre el tamaño total de la muestra.
- Pi: Probabilidad acumulada, la suma acumulada de las probabilidades. 

Devolviendo un DataFrame que contiene estas columnas como claves y las listas
correspondientes como valores asociados.

## Sobre el proyecto

Realizado con `python` y utilizando la librería `pandas`, el cual genera un análisis estadístico básico, calculando la frecuencia absoluta (fi), la frecuencia acumulada (Fi), la frecuencia relativa (ri), la frecuencia relativa acumulada (Ri), la probabilidad (pi) y la probabilidad acumulada (Pi).

### Bibliotecas utilizadas 
- pandas


### Requerimientos

- Archivo `edades-30Alumnos.csv` el cual se debe estar en la carpeta assets.

- Instalación de virtual env

```bash
py -m venv nombre_venv
```
- Ejecutar el virtual env desde 

- Instalación de la librería pandas

```bash
pip install pandas
```