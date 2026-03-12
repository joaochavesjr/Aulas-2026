# pip install google-generativeai
# pip install dotenv

import os
import sys
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv('.env')

GEMINI_API_KEY = os.environ.get('GEMINI_API_KEY')

genai.configure(api_key=GEMINI_API_KEY)

try:
    listar = sys.argv[1]
except:
    listar = None

if listar:
    for m in genai.list_models():
        print ('Nome modelo:', m.name)
    sys.exit(0)

# Inicializa o modelo e o chat
modelo = genai.GenerativeModel('gemini-3.1-flash-lite-preview')
chat = modelo.start_chat(history=[])

print("Assistente Gemini: Olá! Sou um assistente com IA generativa. Pergunte algo ou digite 'sair'.")

while True:
    pergunta = input("\nVocê: ")
    if pergunta.lower() in ['sair', 'exit', 'tchau']:
        print("Assistente Gemini: Até mais!")
        break

    try:
        # Aqui a mágica acontece!
        resposta = chat.send_message(pergunta)
        print(f"Assistente Gemini: {resposta.text}")
    except Exception as e:
        print(f"Erro: {e}. Verifique a chave API.")

# Opcional: exibe histórico
print("\nHistórico da conversa:")
for mensagem in chat.history:
    print(f"{mensagem.role.upper()}: {mensagem.parts[0].text}")
