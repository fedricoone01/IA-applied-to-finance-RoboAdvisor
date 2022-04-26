# -*- coding: utf-8 -*-
"""
Created on Wed Apr  6 11:42:29 2022

@author: Fede
"""
from sklearn import tree, metrics
from sklearn.metrics import accuracy_score, precision_score, confusion_matrix
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sn
import joblib

# Cargo datos
df = pd.read_excel(r"C:\Users\fede_\OneDrive\Escritorio\clientes robo advisor2.xlsx")
df_datos = df.drop(["Resultado del perfil"], axis=1)
df_target = df["Resultado del perfil"]

# Invoco a la librería train_test_split para partir el dataset
X_train, X_test, Y_train, Y_test = train_test_split(df_datos, df_target,test_size=0.3, random_state=0)
print(X_train)

# Selecciono el algoritmo para clasificar los datos
clf = tree.DecisionTreeClassifier(max_depth=9, random_state=42)

# Procedo a entrenarlo
clf.fit(X_train, Y_train)

# Obtengo las predicciones
y_pred = clf.predict(X_test)

# Grafico
plt.figure(figsize=(15,10))
tree.plot_tree(clf)
plt.title("Arbol de decisión")
plt.savefig("Arbol de decisión.png")
plt.show()

# Matriz de confusion
matriz = confusion_matrix(Y_test, y_pred)
print('\n- Matriz de Confusión -')
sn.heatmap(matriz, annot=True)

# Metricas
print("Acuracy:", accuracy_score(Y_test, y_pred))
print("Precision:", precision_score(Y_test, y_pred,average='weighted'))
print("Recall" , metrics.recall_score(Y_test,y_pred,average='weighted'))
print(metrics.classification_report(Y_test, y_pred))
plt.show()

#Guardo el modelo
joblib.dump(clf, "arbol_roboAdvisor.pkl")

