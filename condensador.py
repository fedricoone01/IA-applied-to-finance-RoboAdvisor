# -*- coding: utf-8 -*-
"""
Created on Sun Apr 10 16:28:22 2022

@author: Fede
"""

import pandas as pd
import joblib
from Markowitz import obtencion_de_cartera

#Cuestionario
resultado_imputs = [[]]

pregunta_1 = input("¿Ha invertido alguna vez?\n(a) No\n(b) Si\n\nRespuesta:")
if pregunta_1 == "a":
    resultado_imputs[0].append(0)
else:
    resultado_imputs[0].append(1)

pregunta_2 = input("¿Cual es su edad aproximada?\n(a) 20 años\n(b) 40 años\n(C) 60 años\n\nRespuesta:")
if pregunta_2 == "a":
    resultado_imputs[0].append(0)
elif pregunta_2 == "b":
    resultado_imputs[0].append(1)
else:
    resultado_imputs[0].append(2)

pregunta_3 = input("¿Cual considera que es su nivel de conocimientos?\n(a) Nulo\n(b) Intermedio\n(c) Avanzado\n\nRespuesta:")
if pregunta_3 == "a":
    resultado_imputs[0].append(0)
elif pregunta_3 =="b":
    resultado_imputs[0].append(1)
else:
    resultado_imputs[0].append(2)

pregunta_4 = input("¿Cual es el % aproximado de su patrimonio que quiere invertir?\n(a) 10%\n(b) 25%\n(c) 50% o más\n\nRespuesta:")
if pregunta_4 == "a":
    resultado_imputs[0].append(10)
elif pregunta_4 =="b":
    resultado_imputs[0].append(25)
else:
    resultado_imputs[0].append(50)

pregunta_5 = input("Objetivo de la inversión\n(a) Preservar el capital\n(b) Equilibrio entre rentabilidad y riesgo\n(c) Rentabilidad alta aunque exija mayor riesgo\n\nRespuesta:")
if pregunta_5 == "a":
    resultado_imputs[0].append(0)
elif pregunta_5 =="b":
    resultado_imputs[0].append(1)
else:
    resultado_imputs[0].append(2)
print("\n","="*70,"\n")


#Armamos el dataframe
df = pd.DataFrame(resultado_imputs, columns=["Ha invertido alguna vez","Edad","Nivel de conocimientos","% de Patrimonio a invertir","Rentabilidad buscada"])

#Cargamos el modelo ya entrenado
arbol_decision = joblib.load("arbol_roboAdvisor.pkl")

#Usamos el modelo para obtener el perfi del inversor
y_pred = arbol_decision.predict(df)

#Otenemos la cartera sugerida segun el perfil
obtencion_de_cartera((y_pred))



