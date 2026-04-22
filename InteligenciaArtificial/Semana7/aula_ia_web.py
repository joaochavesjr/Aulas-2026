from flask import Flask, render_template, request, jsonify
import requests
import re

app = Flask(__name__)

OLLAMA_URL = "http://localhost:11434/api/generate"
MODELO = "llama3"

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

def extrair_nota(texto):
    match = re.search(r'(\d+)', texto)
    if match:
        return min(int(match.group(1)), 10)
    return 0

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/gerar_pergunta", methods=["POST"])
def gerar_pergunta():
    materia = request.json["materia"]
    nivel = int(request.json["nivel"])

    dificuldades = {
        1: "fácil",
        2: "intermediária",
        3: "difícil",
        4: "muito difícil"
    }

    prompt = f"""
Você é um professor de {materia}.
Gere uma pergunta dissertativa de nível {dificuldades.get(nivel)} para ensino médio.
Não forneça a resposta.
"""

    pergunta = perguntar_ia(prompt)
    return jsonify({"pergunta": pergunta})

@app.route("/corrigir", methods=["POST"])
def corrigir():
    data = request.json
    materia = data["materia"]
    pergunta = data["pergunta"]
    resposta = data["resposta"]

    prompt = f"""
Você é um professor justo de {materia}.

Avalie a resposta.

Forneça:
Nota (0 a 10)
Breve explicação
Resposta ideal resumida

Pergunta:
{pergunta}

Resposta do aluno:
{resposta}
"""

    avaliacao = perguntar_ia(prompt)
    nota = extrair_nota(avaliacao)

    return jsonify({
        "avaliacao": avaliacao,
        "nota": nota
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
