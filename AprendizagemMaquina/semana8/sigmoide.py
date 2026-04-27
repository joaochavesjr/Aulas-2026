import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
# Dados
horas_estudadas = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]).reshape(-1, 1)
resultado = np.array([0, 0, 0, 1, 1, 1, 1, 1, 1, 1])
# Criar e treinar o modelo de regressão logística 
modelo = LogisticRegression() 
modelo.fit(horas_estudadas, resultado)
# Gerar predições para uma gama de valores de horas 
horas_novas = np.linspace(0, 12, 300).reshape(-1, 1)
probabilidades = modelo.predict_proba(horas_novas)[:, 1]
# Criar gráfico plt.figure(figsize=(8, 6)) plt.scatter(horas_estudadas, resultado, color='red', label='Dados Reais')
plt.plot(horas_novas, probabilidades, color='blue', label='Curva da Regressão Logística')
plt.xlabel('Horas Estudadas')
plt.ylabel('Probabilidade de Passar')
plt.title('Regressão Logística: Horas Estudadas vs. Passar na Prova')
plt.legend()
plt.grid(True)
plt.show()

