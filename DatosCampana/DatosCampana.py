import pandas as pd
import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt

cabecera = ['id', 'edad', 'altura', 'peso', 'nota_final', 'genero']

rangos = {
    'edad': (20, 25),
    'altura': (160, 180),
    'peso': (60, 70),
    'nota_final': (7, 9),
    'genero': ['Masculino', 'Femenino']
}

def generacion_datos():
    datos = {}

    datos['id'] = np.arange(1, 1001)
    for parametro in cabecera:
        if parametro == 'id':
            continue
        if parametro == 'genero':
            datos[parametro] = np.random.choice(rangos[parametro], 1000)
        else:
            datos[parametro] = np.random.normal(rangos[parametro][0], (rangos[parametro][1] - rangos[parametro][0]) / 4, 1000)
    return pd.DataFrame(datos)

def comparar(df, parametro):
    mu, sigma = df[parametro].mean(), df[parametro].std()
    x = np.linspace(mu - 3*sigma, mu + 3*sigma, 100)
    fp = norm.pdf(x, mu, sigma)
    plt.plot(x, fp, color='r')
    df[parametro].plot.hist(bins=20, density=True, alpha=0.6, color='g')
    plt.title('Distribución Normal')
    plt.xlabel('Valores')
    plt.ylabel('Probabilidad')
    plt.show()

df = generacion_datos()
df[['edad', 'altura', 'peso', 'nota_final']] = df[['edad', 'altura', 'peso', 'nota_final']].round(2)
df.to_csv('datosGauss.csv', index=False)
for parametro in cabecera[:-1]:
    comparar(df, parametro)