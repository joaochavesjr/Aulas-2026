from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# 1. Dados de treinamento (mensagens e rótulos)
mensagens_treino = [
    "ganhe dinheiro rapido e facil",
    "voce ganhou um premio em dinheiro",
    "reuniao de trabalho amanha as nove",
    "relatorio do projeto enviado em anexo",
    "oferta exclusiva compre dinheiro facil",
    "confirme sua presenca na reuniao"
]

# 1 = Spam, 0 = Não Spam
labels_treino = [1, 1, 0, 0, 1, 0]

# 2. Converte os textos em uma matriz de contagem de palavras (Bag of Words)
vectorizer = CountVectorizer()
X_treino = vectorizer.fit_transform(mensagens_treino)

# 3. Inicializa e treina o modelo Naive Bayes
modelo = MultinomialNB()
modelo.fit(X_treino, labels_treino)

# 4. Novas mensagens para teste
novas_mensagens = [
    "reuniao sobre o relatorio do projeto",
    "ganhe dinheiro com essa oferta exclusiva"
]

# Transforma os novos textos usando o mesmo vocabulario
X_teste = vectorizer.transform(novas_mensagens)

# 5. Previsão
previsoes = modelo.predict(X_teste)
probabilidades = modelo.predict_proba(X_teste)

# Exibe os resultados
classes = {0: "Não Spam", 1: "Spam"}


for msg, pred, prob in zip(novas_mensagens, previsoes, probabilidades):
    print(f"Mensagem: '{msg}'")
    print(f"Classificação: {classes[pred]}")
    print(f"Probabilidade (Não Spam / Spam): {prob.round(2)}\n")

