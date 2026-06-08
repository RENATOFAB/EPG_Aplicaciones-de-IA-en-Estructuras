# EPG_Aplicaciones-de-IA-en-Estructuras

# Predicción de la Resistencia del Concreto de Alto Desempeño usando Redes Neuronales
-

# Descripcion del proyecto
-
- El objetivo de la investigacion estudiada tuvo como objetivo predecir la resistencia a la compresion de concreto de alta resistencia (HPC) utilizando como herramieenta la Inteligencia artificial, especificamente las Redes Neuronales Artificiales (ANN).
- La finalidad de la investigacion es de reducir la dependdencia de la realizacion de ensayos experimentales en laboratorio y optimizar el tiempo y costo para determinar las resistencias.
  
# Objetivo
---------
- Desarrollar un modelo predictivo basado en redes neuronales que estime la resistencia del concreto en funcion a sus componentes.
  
# Objetivos especificos
-
- Aplicar e implmentar el machine learning
- Aplicacar los principios de Veridical Data Science (PCS framework) basados en el trabajo de Bin Yu. Deben justificar la predictibilidad, computabilidad y estabilidad esperada de sus datos.
- Analizar los datos, limpiarlos y realizar el analisis de correlacion.

# Dataset
------------------------------------
Descripción del Dataset

El conjunto de datos contiene registros experimentales de mezclas de concreto con sus respectivas resistencias a compresión.

Fuente
Dataset basado en el estudio:
Modeling of strength of high-performance concrete using artificial neural networks
  Original Owner and Donor : Prof. I-Cheng Yeh
  Department of Information Management 
  Chung-Hua University, 
  Hsin Chu, Taiwan 30067, R.O.C.
  e-mail:icyeh@chu.edu.tw
  TEL:886-3-5186511
  Date Donated: August 3, 2007
  
 Variables de Entrada
 -----------------------------------------
- Cemento (kg/m³)
- Escoria de alto horno (kg/m³)
- Ceniza volante (kg/m³)
- Agua (kg/m³)
- Superplastificante (kg/m³)
- Agregado grueso (kg/m³)
- Agregado fino (kg/m³)
- Edad del concreto (días)

Variable de Salida
---------------------------------------------
- Resistencia a compresión (MPa)

Tipo de Datos
---------------------------------
Variables numéricas continuas
Dataset supervisado (regresión)
Relación no lineal entre variables

Tamaño del Dataset
----------------------------------------
1030 muestras
8 variables de entrada
1 variable de salida

Marco de Veridical Data Science (PCS Framework)
-----------------------------------------------
Se aplican los principios de Veridical Data Science (VDS) propuestos por Yu & Barter (2024), basados en el marco PCS:

Predictibilidad
-

El problema presenta alta predictibilidad debido a que:

- Existe una relación directa entre la composición del concreto y su resistencia.
- Estudios previos han demostrado que modelos ANN logran buenos resultados.

Se espera que el modelo pueda capturar relaciones no lineales complejas entre las variables.

Computabilidad
-

El modelo es computacionalmente viable debido a que:

- El dataset es de tamaño moderado.
- Las redes neuronales pueden entrenarse en computadoras personales.
- Herramientas como Python, TensorFlow o Scikit-learn facilitan la implementación.

No se requieren recursos de alto rendimiento.

Estabilidad
-
La estabilidad del modelo se evaluará considerando:

- Sensibilidad a cambios en los datos de entrenamiento
- Validación cruzada
- Comparación con otros modelos (regresión lineal, árboles, etc.)

Se espera que el modelo ANN sea relativamente estable si se entrena adecuadamente.
