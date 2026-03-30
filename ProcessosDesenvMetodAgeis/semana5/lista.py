#
# Exemplo de função com parâmetros float em Python
#

class NovoObjeto:
    def __init__(self, valor):
        self.valor = valor

    def __str__(self):
        return self.valor


def parametros(lista=None):
    """Função que recebe uma lista e retorna o valor impresso."""    
    resultado = ""
    if lista:
        for item in lista:
            resultado += f"{item}\n"

    return resultado

def teste_parametros():
    """Função de teste para verificar o funcionamento da função parametros."""
    objeto = NovoObjeto("Valor do objeto")

    lista = ["Item 1", "Valor 2", 11, "Outro item", objeto]
    
    resultado = parametros(lista)

    print(f"\nResultado com ambos os parâmetros:\n {resultado}")


if __name__ == "__main__":
    """Função principal para executar o teste."""
    teste_parametros()