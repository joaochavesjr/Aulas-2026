import random

# Configuração inicial: Probabilidades das características
cores = ['vermelha', 'azul', 'amarela']
texturas = ['lisa', 'áspera']

# Probabilidades associadas
probabilidade_cor = {'vermelha': 0.6, 'azul': 0.2, 'amarela': 0.2}
probabilidade_textura = {'lisa': 0.8, 'áspera': 0.2}

# Função para gerar uma bola aleatória com base nas probabilidades
def gerar_bola():
    cor = random.choices(cores, weights=[probabilidade_cor[c] for c in cores], k=1)[0]
    textura = random.choices(texturas, weights=[probabilidade_textura[t] for t in texturas], k=1)[0]
    return {'cor': cor, 'textura': textura}

# Gerando uma simulação de 10 bolas
caixa = [gerar_bola() for _ in range(10)]

# Exibindo as bolas geradas
print("Bolas geradas na simulação:")
for i, bola in enumerate(caixa, 1):
    print(f"Bola {i}: Cor: {bola['cor']}, Textura: {bola['textura']}")

