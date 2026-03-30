#
# Exemplo de função com parâmetros float em Python
#

def parametros(valor1=0.0, valor2=0.0):
    """Função que recebe dois valores e retorna a soma. O segundo valor é opcional."""    
    try:
        soma =  float(valor1) + float(valor2)
    except Exception as e:
        print("Erro: Certifique-se de que os valores passados são números decimais (float).")
        print(f"** Detalhes do erro: {e}")
        return

    return soma

def teste_parametros():
    """Função de teste para verificar o funcionamento da função parametros."""
    valor1 = '0,1'
    valor2 = '0,2'
    resultado = parametros(valor1, valor2)

    print(f"\nResultado com ambos os parâmetros: {resultado}")


if __name__ == "__main__":
    """Função principal para executar o teste."""
    teste_parametros()