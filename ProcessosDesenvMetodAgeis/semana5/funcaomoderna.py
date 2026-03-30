#
# Exemplo de função com parâmetros hibridos em Python
#

def parametros(indice: int, texto: str = "") -> str:
    """Função que recebe dois valores e retorna o valor impresso."""    
    result = f"Índice: {indice}, Texto: '{texto}'"

    return result

def teste_parametros():
    """Função de teste para verificar o funcionamento da função parametros."""
    indice = 193
    texto = "Exemplo de texto"
    resultado = parametros(indice, texto)

    print(f"\nResultado com ambos os parâmetros: {resultado}")


if __name__ == "__main__":
    """Função principal para executar o teste."""
    teste_parametros()