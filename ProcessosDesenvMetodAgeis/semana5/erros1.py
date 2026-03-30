#
# Exemplo de função com parâmetros em Python
#

def parametros(valor1, valor2):
    """Função que recebe dois valores e retorna a soma. O segundo valor é opcional."""
    soma =  valor1 + valor2
    
    #try:
    #    soma =  int(valor1) + int(valor2)
    #except ValueError:
    #    print("Erro: Certifique-se de que os valores passados são números.")
    #    return

    return soma

def teste_parametros():
    """Função de teste para verificar o funcionamento da função parametros."""
    valor1 = 'a'
    valor2 = 'b'
    resultado = parametros(valor1, valor2)

    print(f"\nResultado com ambos os parâmetros: {resultado}")


if __name__ == "__main__":
    """Função principal para executar o teste."""
    teste_parametros()