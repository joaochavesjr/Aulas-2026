import requests
import json

OLLAMA_URL = "http://localhost:11434/api/generate"
MODELO = "llama3.1:latest"  # ou "mistral"

def perguntar_ia(prompt):
    response = requests.post(
        OLLAMA_URL,
        json={
            "model": MODELO,
            "prompt": prompt,
            "stream": False
        }
    )
    
    return response.json()["response"]


print("🤖 Professor IA (Modelo Local com Ollama)")
print("Matérias disponíveis: matemática, física, biologia, história\n")

materia = input("Escolha a matéria: ")

# 1️⃣ Gerar pergunta
prompt_pergunta = f"""
Você é um professor do ensino médio de {materia}.
Gere uma pergunta dissertativa adequada ao nível do ensino médio.
Não dê a resposta.
"""

pergunta = perguntar_ia(prompt_pergunta)

print("\n📘 Pergunta:")
print(pergunta)

# 2️⃣ Receber resposta do aluno
resposta_aluno = input("\n✏️ Sua resposta: ")

# 3️⃣ Corrigir resposta
prompt_correcao = f"""
Você é um professor rigoroso, mas justo, de {materia}.

Avalie a resposta abaixo.

Forneça:

1. Nota de 0 a 10
2. Pontos positivos
3. O que precisa melhorar
4. Resposta ideal resumida

Pergunta:
{pergunta}

Resposta do aluno:
{resposta_aluno}
"""

correcao = perguntar_ia(prompt_correcao)

print("\n📊 Correção do Professor IA:\n")
print(correcao)

print("\n✅ Atividade finalizada!")
