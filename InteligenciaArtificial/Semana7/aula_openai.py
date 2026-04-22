from openai import OpenAI

# Coloque sua chave aqui
client = OpenAI(api_key="SUA_CHAVE_AQUI")

print("🤖 Professor IA - Corretor Inteligente")
print("Matérias disponíveis: matemática, física, biologia, história\n")

materia = input("Escolha a matéria: ")

# 1️⃣ Gerar pergunta
pergunta_response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {
            "role": "system",
            "content": f"Você é um professor do ensino médio de {materia}. Gere uma pergunta dissertativa adequada ao nível."
        }
    ]
)

pergunta = pergunta_response.choices[0].message.content

print("\n📘 Pergunta:")
print(pergunta)

# 2️⃣ Receber resposta do aluno
resposta_aluno = input("\n✏️ Sua resposta: ")

# 3️⃣ Corrigir resposta
correcao = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {
            "role": "system",
            "content": f"""
Você é um professor rigoroso, mas justo, de {materia}.
Avalie a resposta do aluno.

Forneça:
1. Nota de 0 a 10
2. Pontos positivos
3. O que faltou melhorar
4. Resposta ideal resumida
"""
        },
        {
            "role": "user",
            "content": f"""
Pergunta: {pergunta}

Resposta do aluno:
{resposta_aluno}
"""
        }
    ]
)

print("\n📊 Correção do Professor IA:\n")
print(correcao.choices[0].message.content)

print("\n✅ Fim da atividade!")
