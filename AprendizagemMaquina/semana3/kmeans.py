# Instalar bibliotecas (se necessário)
!pip install scikit-learn matplotlib pandas --quiet

# Importar bibliotecas
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# Criar o DataFrame
dados = {
    "Nome": ["Lucas", "Letícia", "Oliver", "Paulo", "Márcia",
             "Alfredo", "Matheus", "Luísa", "Ludmilla"],
    "Disponibilidade": [4, 3.5, 2, 2, 4.5, 5, 3.5, 4, 4],
    "Idade": [19, 20, 27, 39, 36, 60, 18, 60, 21]
}

df = pd.DataFrame(dados)

# Selecionar apenas as variáveis numéricas
X = df[["Disponibilidade", "Idade"]]

# Normalizar os dados (importante para KMeans)
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Definir número de clusters (você pode alterar)
kmeans = KMeans(n_clusters=3, random_state=42)
df["Cluster"] = kmeans.fit_predict(X_scaled)

# Mostrar resultado
print(df)

# Visualização gráfica
plt.figure(figsize=(8,6))
plt.scatter(df["Disponibilidade"], df["Idade"], 
            c=df["Cluster"], cmap="viridis", s=100)

for i, nome in enumerate(df["Nome"]):
    plt.text(df["Disponibilidade"][i]+0.02,
             df["Idade"][i]+0.5,
             nome)

plt.xlabel("Disponibilidade (dias)")
plt.ylabel("Idade")
plt.title("Clusters - KMeans")
plt.colorbar(label="Cluster")
plt.show()
