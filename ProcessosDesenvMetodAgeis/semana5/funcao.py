#
# Exemplo de função em Python
#

def saudacao(nome):
    """Função que recebe um nome e retorna uma saudação personalizada."""
    return f"Olá, {nome}! Bem-vindo(a) ao curso de Desenvolvimento Ágil!"


def teste_funcao():
    """Função de teste para verificar o funcionamento da função saudacao."""
    nome_teste = "Maria"
    resultado = saudacao(nome_teste)
    print(f"\n{resultado}\n")


if __name__ == "__main__":
    """Função principal para executar o teste."""
    teste_funcao()