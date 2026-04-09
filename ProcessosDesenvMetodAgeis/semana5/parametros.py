#
# Exemplo de função com parâmetros em Python
#

def parametros(valor1, valor2=0):
    """Função que recebe dois valores e retorna a soma. O segundo valor é opcional."""
    soma =  valor1 + valor2
    return soma

def teste_parametros():
    """Função de teste para verificar o funcionamento da função parametros."""
    valor1_teste = 5
    valor2_teste = 10
    resultado_com_parametros = parametros(valor1_teste, valor2_teste)
    resultado_com_parametro_unico = parametros(valor1_teste)
    
    print(f"\nResultado com ambos os parâmetros: {resultado_com_parametros}")
    print(f"Resultado com apenas um parâmetro (valor2 assume o valor padrão): {resultado_com_parametro_unico}\n")


if __name__ == "__main__":
    """Função principal para executar o teste."""
    entrada = input("Numero de alunos:")
    entrada = int(entrada)
    b = 0
    a = 0
    c = 0
    for i in range(entrada):
        voto = input("Entre com o voto: %s" % i)
        if voto == "A":
            a += 1
        elif voto == 'B':
            b += 1
        else:
            c += 1
    print("Votos a:",a, "Votos b:", b)  
    #teste_parametros()