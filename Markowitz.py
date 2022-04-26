# -*- coding: utf-8 -*-
"""
Created on Fri Apr  8 11:33:41 2022

@author: Fede
"""
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from matplotlib.axes._axes import _log as matplotlib_axes_logger


#Cargo el dataset
df = pd.read_excel(r"C:\Users\fede_\OneDrive\Escritorio\roboAdvisor\los_datos.xlsx", index_col="Fecha")
df = df[::-1]
shape = df.shape
nombre_activos = df.columns.values


#Crecimiento de los activos
(df/df.iloc[0] * 100).plot(figsize=(12,10))
plt.title('Precio Histórico los activos', fontsize=20)
plt.show()


#Rendimientos medios de los activos
rendimientos = df.pct_change()
rendimientos_medios = rendimientos.mean()*252
print(f"\n\nRendimiento medio de los activos: \n{rendimientos_medios}")
rendimientos.plot(figsize=(13,8))
plt.title('\nRendimientos medio de los activos', fontsize=20, y=1.05)
matplotlib_axes_logger.setLevel('ERROR')
plt.show()


#Matriz de correlación
correlaciones = df.corr()
fig=plt.figure(figsize=(12,9))
plt.matshow(correlaciones, fignum=fig.number, cmap='RdYlGn')
plt.xticks(range(correlaciones.shape[1]), correlaciones.columns, rotation=90, fontsize=10,fontweight="bold")
plt.yticks(range(correlaciones.shape[1]), correlaciones.columns, fontsize=10,fontweight="bold")

cb=plt.colorbar(orientation="vertical", label="Factor Correlacion")
cb.ax.tick_params(labelsize=10)
plt.title("Matriz de correlaciones", fontsize=18, y=1.12)

ax = plt.gca()
ax.set_xticks(np.arange(-.5, len(correlaciones), 1), minor=True);
ax.set_yticks(np.arange(-.5, len(correlaciones), 1), minor=True);
ax.grid(which="minor", color="black", linestyle="-", linewidth=3)
ax.grid(which="major", color="none", linestyle="-", linewidth=3)

for i in range(correlaciones.shape[0]):
    for j in range(correlaciones.shape[1]):
        if correlaciones.iloc[i,j]>0.6:
            color = "white"
        else:
            color = "black"
        fig.gca().text(i,j, "{:.2f}".format(correlaciones.iloc[i,j]), ha="center", va="center", c=color, size="7")
plt.show()


#Genero carteras con ponderaciones aleatorias de los activos
numero_activos = shape[1]
pesos = np.random.random(numero_activos)
pesos /=np.sum(pesos)


#Calculo retorno de 10000 combinaciones
port_rendimiento = []
port_volat = []
port_sharpe = []
port_pesos = []

for i in range(10000):
    #Generar ponderaciones aleatorias de los activos en cartera
    pesos = np.random.random(numero_activos)
    pesos /=np.sum(pesos)
    
    #Calculo de rendimiento 
    rendimiento = np.sum(pesos * rendimientos_medios)
    port_rendimiento.append(rendimiento)
    
    #Calculo de volatilidad
    volatilidad = np.sqrt(np.dot(pesos.T, np.dot(rendimientos.cov()*252, pesos)))
    port_volat.append(volatilidad)
    
    #Calculo del ratio de Sharpe
    sharpe = (rendimiento) / volatilidad
    port_sharpe.append(sharpe)
    
    #Guardado de los pesos de cada cartera
    port_pesos.append(pesos)


#graficando las carteras posibles
carteras = pd.DataFrame({"Rendimiento": port_rendimiento, "Volatilidad": port_volat})
carteras.plot(x="Volatilidad", y="Rendimiento", kind="scatter", figsize=(12,8))
plt.title('Rendimientos y volatilidad de las carteras', fontsize=20)
plt.show()

#Creación de 3 carteras basados en el nivel de riesgo
def obtencion_de_cartera(perfil):
    i=0
    if perfil == 0:
        sharpe_mayor = np.argmax(port_sharpe)
        print("\nEl perfil del inversor es: Conservador", "\nLa cartera sugerida es la siguiente:\n")
        while i < numero_activos:
            print("Activo : %s : %2.2f" % (nombre_activos[i],port_pesos[sharpe_mayor][i] * 100 ))
            i += 1
        print("\nVolatilidad :", round(port_volat[sharpe_mayor],2),"\nRendimiento :", round(port_rendimiento[sharpe_mayor],2))
    
    elif perfil == 1:
        port_sharpe.sort()
        sharpe_intermedio = int(port_sharpe[500])
        print("\n\nEl perfil del inversor es: Moderado", "\nLa cartera sugerida es la siguiente:\n")
        while i < numero_activos:
            print("Activo : %s : %2.2f" % (nombre_activos[i],port_pesos[sharpe_intermedio][i] * 100 ))
            i += 1
        print("\nVolatilidad :", round(port_volat[sharpe_intermedio],2), "\nRendimiento :", round(port_rendimiento[sharpe_intermedio],2))
    
    else:
        sharpe_menor = np.argmin(port_sharpe)
        print("\n\nEl perfil del inversor es: Agresivo", "\nLa cartera sugerida es la siguiente:\n")
        while i < numero_activos:
            print("Activo : %s : %2.2f" % (nombre_activos[i],port_pesos[sharpe_menor][i] * 100 ))
            i += 1
        print("\nVolatilidad :", round(port_volat[sharpe_menor],2), "\nRendimiento :", round(port_rendimiento[sharpe_menor],2))
    

obtencion_de_cartera(0)
obtencion_de_cartera(1)
obtencion_de_cartera(2)






