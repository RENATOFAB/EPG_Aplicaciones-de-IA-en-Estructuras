# EPG_Aplicaciones-de-IA-en-Estructuras
# Predicción de la Resistencia del Concreto de Alto Desempeño usando Redes Neuronales
## Descripcion del proyecto
- El objetivo principal de la investigacion estudiada fue desarrollar un modelo capaz de predecir la resistencia a la compresion de concreto de alto desempeño (High-Performance Concrete, HPC) utilizando como herramienta la Inteligencia artificial, especificamente las Redes Neuronales Artificiales (Artificial Neural Networks, ANN).
- La finalidad de la investigacion es de reducir la dependencia de la realizacion de ensayos experimentales en laboratorio y optimizar el tiempo y costo para determinar las resistencias.
## Objetivo
- Desarrollar un modelo predictivo basado en redes neuronales artificiales (ANN) que estime la resistencia del concreto de alto desempeño (HPC) en funcion de sus componentes.
  ## Objetivos especificos
- Aplicar e implementar el machine learning
- Aplicar los principios de Veridical Data Science (PCS framework) basados en el trabajo de Bin Yu. Deben justificar la predictibilidad, computabilidad y estabilidad esperada de sus datos.
- Analizar los datos, limpiarlos y realizar el analisis de correlacion.
- Alimentar el modelo con distintos datos experimentales.
- Enseñarle al modelo las relaciones entre componentes del HPC y su resistencia.
- Permitir que el modelo prediga nuevas resistencias sin hacer ensayos físicos.
## Requisitos
- Sistema operativo: Linux, macOS o Windows con Python 3.10+.
- Python 3.10 o superior.
- Requiere `sqlite3` para consultar la base de datos SQLite.
- Paquetes de Python:
  - `pandas>=2.0.0`
  - `xlrd==2.0.1`
  - `sqlalchemy>=2.0.0`

Instalar dependencias desde `requirements.txt`:

```bash
python3 -m pip install -r requirements.txt
```

## Instalación rápida
1. Clonar el repositorio:

```bash
git clone https://github.com/RENATOFAB/EPG_Aplicaciones-de-IA-en-Estructuras.git
cd EPG_Aplicaciones-de-IA-en-Estructuras
```

2. Crear y activar un entorno virtual (recomendado):

```bash
python3 -m venv .venv
source .venv/bin/activate  # Linux/macOS
.venv\Scripts\activate    # Windows PowerShell
```

3. Instalar dependencias:

```bash
python3 -m pip install --upgrade pip
python3 -m pip install -r requirements.txt
```

4. Generar la base de datos SQLite a partir del Excel:

```bash
python3 scripts/import_concrete.py
```

5. Verificar la tabla y el número de registros:

```bash
sqlite3 data/concrete_data.db "SELECT name FROM sqlite_master WHERE type='table';"
sqlite3 data/concrete_data.db "SELECT COUNT(*) FROM concrete;"
```

## Dataset
**El conjunto de datos contiene registros experimentales de mezclas de concreto con sus respectivas resistencias a compresión.**

## Acceso a la base de datos

- Archivo original (Excel): [Concrete_Data.xls](Concrete_Data.xls#L1)
- Base de datos local (SQLite): [data/concrete_data.db](data/concrete_data.db#L1)
- Script de importación: [scripts/import_concrete.py](scripts/import_concrete.py#L1)

Usar el script para crear/actualizar la base de datos SQLite:

```bash
python3 scripts/import_concrete.py
# o especificar el archivo si hace falta:
python3 scripts/import_concrete.py Concrete_Data.xls
```

Comandos rápidos para verificar la DB con `sqlite3`:

```bash
sqlite3 data/concrete_data.db "SELECT COUNT(*) FROM concrete;"
sqlite3 data/concrete_data.db "SELECT * FROM concrete LIMIT 5;"
```

Ejemplo mínimo en Python para leer la tabla:

```python
import sqlite3
conn = sqlite3.connect('data/concrete_data.db')
cur = conn.cursor()
cur.execute('SELECT * FROM concrete LIMIT 5')
print(cur.fetchall())
conn.close()
```

### Fuente
**Dataset basado en el estudio: Modeling of strength of high-performance concrete using artificial neural networks** 
- **Original Owner and Donor:** Prof. I-Cheng Yeh
- **Department:** Information Management 
- **Institucion:**  Chung-Hua University, Hsin Chu, Taiwan 30067, R.O.C.
- **e-mail:** icyeh@chu.edu.tw
- **TEL:** 886-3-5186511
- **Date Donated:** August 3, 2007
### Variables de Entrada
- Cemento (kg/m³)
- Escoria de alto horno (kg/m³)
- Ceniza volante (kg/m³)
- Agua (kg/m³)
- Superplastificante (kg/m³)
- Agregado grueso (kg/m³)
- Agregado fino (kg/m³)
- Edad del concreto (días)
### Variable de Salida
- Resistencia a compresión (MPa)
### Tipo de Datos
Variables numéricas continuas
Dataset supervisado (regresión)
Relación no lineal entre variables
### Tamaño del Dataset
1030 muestras
8 variables de entrada
1 variable de salida
# Marco de Veridical Data Science (PCS Framework)
Se aplican los principios de Veridical Data Science (VDS) propuestos por Yu & Barter (2024), basados en el marco PCS:
## Predictibilidad
El problema presenta alta predictibilidad debido a que:
- Existe una relación directa entre la composición del concreto y su resistencia.
- Estudios previos han demostrado que modelos ANN logran buenos resultados.
- La fuente señala que el modelo obtuvo resultados favorables en la predicción de nuevos diseños de concreto cuando los valores de entrada se encuentran dentro del rango de datos con los que fue entrenado el modelo.
Se espera que el modelo pueda capturar relaciones no lineales complejas entre las variables de manera precisa.
## Computabilidad
El modelo es computacionalmente viable debido a que:
- El dataset es de tamaño moderado.
- Las redes neuronales pueden entrenarse en computadoras personales.
- Herramientas como Python, TensorFlow o Scikit-learn facilitan la implementación.
Se espera que el modelo no requiera recursos de alto rendimiento, que sea ejecutable y eficiente.
## Estabilidad
La estabilidad del modelo se evaluará considerando:
- Sensibilidad a cambios en los datos de entrenamiento
- Validación cruzada
- Comparación con otros modelos (regresión lineal, árboles, etc.)

No solo buscamos que el modelo prediga bien, sino que sea confiable y reproducible, siguiendo el enfoque PCS de Yu, que es el estándar moderno en ciencia de datos.
