# agents_ollama_native.py

import ollama  # cliente oficial do Ollama

MODEL_NAME = "qwen3.5:4b"
MODEL_NAME = "qwen3:8b"


def call_ollama(messages, model=MODEL_NAME, temperature=0.2):
    """
    Chamada simples ao Ollama usando o módulo nativo.
    messages: lista no formato [{"role": "user"|"system"|"assistant", "content": "..."}]
    Retorna apenas o texto da resposta do modelo.
    """
    response = ollama.chat(
        model=model,
        messages=messages,
        options={
            "temperature": temperature
        }
    )

    # Formato típico: {"message": {"role": "assistant", "content": "..."}, ...}
    return response["message"]["content"].strip()


class ResearchAgent:
    """
    Agente que 'pesquisa' usando o LLM.
    Ele recebe um tópico e pede ao modelo para listar alguns fatos.
    """
    def __init__(self, name="ResearchAgent"):
        self.name = name

    def run(self, topic: str):
        prompt = (
            f"Liste 5 fatos objetivos, curtos, sobre o tópico: {topic}.\n"
            "Responda em uma lista numerada simples."
        )

        print(f"[{self.name}] Consultando LLM sobre: {topic!r}...")
        answer = call_ollama([
            {"role": "user", "content": prompt}
        ])
        print(f"[{self.name}] Fatos encontrados:\n{answer}\n")
        return answer


class AnalysisAgent:
    """
    Agente que analisa/condensa o texto vindo do ResearchAgent.
    """
    def __init__(self, name="AnalysisAgent"):
        self.name = name

    def run(self, raw_facts: str):
        prompt = (
            "Você receberá uma lista de fatos.\n"
            "1) Resuma em um parágrafo curto.\n"
            "2) Extraia 3 insights importantes.\n\n"
            f"Fatos:\n{raw_facts}"
        )

        print(f"[{self.name}] Pedindo ao LLM para resumir e analisar...")
        answer = call_ollama([
            {"role": "user", "content": prompt}
        ])
        print(f"[{self.name}] Análise produzida:\n{answer}\n")
        return answer


class SupervisorAgent:
    """
    Agente coordenador:
    - Escolhe um tópico
    - Pede ao ResearchAgent para coletar fatos
    - Pede ao AnalysisAgent para analisar
    - Pede ao LLM uma decisão final baseada na análise
    """
    def __init__(self, researcher: ResearchAgent, analyst: AnalysisAgent, name="SupervisorAgent"):
        self.name = name
        self.researcher = researcher
        self.analyst = analyst

    def decide_action(self, topic: str, analysis: str):
        """
        Usa o LLM para decidir uma ação recomendada baseada na análise.
        """
        prompt = (
            "Você é um agente supervisor que precisa tomar uma decisão prática.\n"
            f"Tópico: {topic}\n\n"
            "Aqui está uma análise anterior:\n"
            f"{analysis}\n\n"
            "Com base nisso, dê UMA recomendação de ação concreta em 2 ou 3 frases."
        )

        print(f"[{self.name}] Pedindo ao LLM uma decisão final...")
        decision = call_ollama([
            {"role": "user", "content": prompt}
        ])
        print(f"[{self.name}] Decisão final:\n{decision}\n")
        return decision

    def run_cycle(self, topic: str):
        print(f"\n[{self.name}] Iniciando ciclo para o tópico: {topic!r}\n")
        facts = self.researcher.run(topic)
        analysis = self.analyst.run(facts)
        decision = self.decide_action(topic, analysis)
        return decision


if __name__ == "__main__":
    topic = "adoção de IA em pequenas empresas"

    researcher = ResearchAgent()
    analyst = AnalysisAgent()
    supervisor = SupervisorAgent(researcher, analyst)

    supervisor.run_cycle(topic)
