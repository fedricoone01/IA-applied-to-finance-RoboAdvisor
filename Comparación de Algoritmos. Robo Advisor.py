# -*- coding: utf-8 -*-
"""
Created on Mon Apr 11 12:06:40 2022

@author: Fede
"""

from sklearn import tree, metrics, svm
from sklearn.metrics import accuracy_score, precision_score, confusion_matrix
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA
from sklearn.model_selection import train_test_split
from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sn

#Cargo los datos
df = pd.read_excel(r"C:\Users\fede_\OneDrive\Escritorio\clientes robo advisor2.xlsx")
df_datos = df.drop(["Resultado del perfil"], axis=1)
df_target = df["Resultado del perfil"]

# Separo el dataset
X_train, X_test, Y_train, Y_test = train_test_split(df_datos, df_target,test_size=0.3, random_state=0)

#=======================================================================
# Algoritmo: Arbol de decision
clf = tree.DecisionTreeClassifier(max_depth=9, random_state=42)
# Procedo a entrenarlo
clf.fit(X_train, Y_train)
# Obtengo las predicciones
y_pred = clf.predict(X_test)

print('\n\nMatriz de Confusión para "Arbol de decisión":')
matriz_arbol = confusion_matrix(Y_test, y_pred)
a = sn.heatmap(matriz_arbol, annot=True)
plt.show()
print("acuracy:", accuracy_score(Y_test, y_pred))
print("precision:", precision_score(Y_test, y_pred,average='weighted'))
print("recall" , metrics.recall_score(Y_test,y_pred,average='weighted'))

#=======================================================================
# Algoritmo: Maquina de soporte vectorial
svm = svm.SVC(kernel="linear")
# Procedo a entrenarlo
svm.fit(X_train,Y_train)
# Obtengo las predicciones
y_pred2 = svm.predict(X_test)

print('\n\nMatriz de Confusión para "Maquina de soporte vectorial":')
matriz_svm = confusion_matrix(Y_test, y_pred2)
sn.heatmap(matriz_svm, annot=True)
plt.show()
print("acuracy:", accuracy_score(Y_test, y_pred2))
print("precision:", precision_score(Y_test, y_pred2,average='weighted'))
print("recall" , metrics.recall_score(Y_test,y_pred2,average='weighted'))

#=======================================================================
# Algoritmo: Análisis de Discriminante Lineal
lda = LDA(n_components=2)
# Ajusto las escalas
X_train = lda.fit_transform(X_train, Y_train)
X_test = lda.transform(X_test)
# Hago la predicción con LDA
classifier = LDA()
# Procedo a entrenarlo
classifier.fit(X_train, Y_train)
# Obtengo las predicciones
y_pred3 = classifier.predict(X_test)

print('\n\nMatriz de Confusión para "Análisis de Discriminante Lineal":')
matriz_lda = confusion_matrix(Y_test, y_pred3)
sn.heatmap(matriz_lda, annot=True)
plt.show()
print("acuracy:", accuracy_score(Y_test, y_pred3))
print("precision:", precision_score(Y_test, y_pred3,average='weighted'))
print("recall" , metrics.recall_score(Y_test,y_pred3,average='weighted'))










