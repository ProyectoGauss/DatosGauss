# DatosGauss


url = https://github.com/ProyectoGauss/DatosGauss.git


Este código en Python genera un conjunto de datos aleatorios basados en ciertos rangos y luego compara la distribución de estos datos con una distribución normal. Aquí está el desglose:

1. Importa las bibliotecas necesarias: pandas para la manipulación de datos, numpy para operaciones matemáticas, scipy.stats para estadísticas y matplotlib.pyplot para la visualización de datos.

2. Define una lista `cabecera` que contiene los nombres de las columnas para el DataFrame que se creará más adelante.

3. Define un diccionario `rangos` que contiene los rangos de valores para cada columna. Para 'edad', 'altura', 'peso' y 'nota_final', los rangos son tuplas que representan el mínimo y el máximo. Para 'genero', el rango es una lista de opciones posibles.

4. Define una función `generacion_datos` que genera 1000 datos aleatorios para cada columna. Si la columna es 'genero', se elige aleatoriamente entre las opciones disponibles. Para las otras columnas, se genera un número aleatorio de una distribución normal con la media y la desviación estándar calculadas a partir del rango.

5. Define una función `comparar_datos` que toma un DataFrame y un nombre de columna (parámetro) como entrada. Calcula la media y la desviación estándar de los datos en esa columna, luego traza una distribución normal basada en esos valores. También traza un histograma de los datos reales. Ambas gráficas se muestran en la misma figura para facilitar la comparación.

6. Genera los datos llamando a `generacion_datos` y redondea los valores de 'edad', 'altura', 'peso' y 'nota_final' a dos decimales.

7. Guarda los datos en un archivo CSV llamado 'datosGauss.csv'.

8. Finalmente, para cada columna excepto 'genero', llama a `comparar_datos` para trazar la distribución de los datos y compararla con una distribución normal.
