
#!/usr/bin/python3

from random import random

def get_rand(valor_max, inteiro=1):

    valor = random() * valor_max

    if inteiro:
        valor = int(valor)
    else:
        valor = round(valor, 2)
    return valor

def get_tipo():
    tipos = ['RPG', 'Estratégia', 'Aventura', 'Simulação']
    idx = int(random() * 3)
    return tipos[idx]

dados = """
Horas_Jogadas,Avaliacao_Usuarios,Jogadores_Online,Popularidade,Genero_Jogo,Preco_Jogo,Avaliacao_Critica,Vendas_Totais
38.08,4.36,36769,49.74,RPG,73.89,6.68,78008
95.12,4.00,10041,42.72,Estratégia,21.01,5.31,56371
73.47,2.59,17985,42.98,RPG,25.84,8.00,46140
60.27,6.47,33500,55.54,Aventura,94.69,10.00,58061
16.45,5.29,24622,31.86,Aventura,32.80,6.76,31434
"""

for _ in range(5, 95):
    linha = f"{get_rand(100,0)},{get_rand(10,0)},{get_rand(50000)},{get_rand(100,0)},{get_tipo()},{get_rand(100,0)},{get_rand(10,0)},{get_rand(100000)}\n"
    dados += linha

dados2 = """49.89,4.45,29270,46.83,Ação,83.69,7.22,64428
52.75,6.30,21656,40.42,RPG,47.28,8.22,28262
43.33,7.49,30263,47.40,Aventura,38.90,8.52,61902
3.52,3.17,47415,50.05,RPG,84.30,5.70,33858
11.68,2.51,10451,16.03,Simulação,71.83,7.60,45520
"""

dados += dados2

fd = open('data.csv', 'w')
fd.write(dados)
fd.close()