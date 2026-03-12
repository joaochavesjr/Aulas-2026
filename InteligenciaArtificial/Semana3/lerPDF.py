#
# pip install google-generativeai PyPDF2
#

import os
import re
import google.generativeai as genai
import PyPDF2
from dotenv import load_dotenv

load_dotenv('.env')

GEMINI_API_KEY = os.environ.get('GEMINI_API_KEY')

genai.configure(api_key=GEMINI_API_KEY)

modelo = genai.GenerativeModel('gemini-3.1-flash-lite-preview')

def extrair_texto_pdf(caminho_pdf):
    """Extrai texto de um PDF e divide em chunks de ~2000 chars."""
    texto_completo = ""
    with open(caminho_pdf, 'rb') as arquivo:
        leitor = PyPDF2.PdfReader(arquivo)
        for pagina in leitor.pages:
            texto_completo += pagina.extract_text() + "\n"

    # Divide em chunks para caber no contexto do Gemini
    chunks = re.split(r'\n\n', texto_completo)
    chunks_filtrados = [chunk.strip() for chunk in chunks if len(chunk) > 50]
    return chunks_filtrados

def responder_pergunta(chunks, pergunta):
    """Envia pergunta com contexto relevante do PDF para o Gemini."""
    contexto = "\n\n".join(chunks[:10])  # Usa os primeiros 10 chunks como contexto inicial
    prompt = f"""Conteúdo do PDF (use apenas isso para responder):

{contexto}

Pergunta: {pergunta}
Responda de forma precisa e cite partes do texto se possível."""

    resposta = modelo.generate_content(prompt)
    return resposta.text

# Exemplo de uso
caminho_pdf = "CLT.pdf"  # Substitua pelo caminho do seu PDF
if os.path.exists(caminho_pdf):
    chunks = extrair_texto_pdf(caminho_pdf)
    print(f"PDF carregado com {len(chunks)} chunks de texto.")

    print("Pergunte sobre o PDF ou digite 'sair'.")
    while True:
        pergunta = input("\nSua pergunta: ")
        if pergunta.lower() in ['sair', 'exit']:
            break
        resposta = responder_pergunta(chunks, pergunta)
        print(f"\nConteudo PDF: {resposta}")
else:
    print("Arquivo PDF não encontrado!")
