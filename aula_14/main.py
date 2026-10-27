import os
from groq import Groq

# Inicializa o cliente da Groq utilizando a variável de ambiente
client = Groq(api_key=os.environ.get("GROQ_API_KEY"))
#
# Modelo de linguagem compatível
MODELO = "openai/gpt-oss-120b"

def mostrar_boas_vindas():
  """Apresenta o assistente ao iniciar o programa."""
print("\n" + "☆" * 20 + "\n")

print("       ✦ Ah... você chegou. ✦\n")

print("Sou Suguru Geto. Espero que nossa conversa seja interessante.\n")

print("Podemos falar sobre animes, personagens e qualquer")
print("universo que desperte sua curiosidade. ☆\n")

print("Digite 'sair' quando quiser encerrar. ✧\n")

print("☆" * 20 + "\n")
def consultar_modelo(mensagem):
    """Envia as instruções do sistema e a mensagem do utilizador para a API."""
    resposta = client.chat.completions.create(
        model=MODELO,
        messages=[
            {
                "role": "system",
                "content": """Você é Suguru Geto, de Jujutsu Kaisen.
                Fale em português brasileiro, mantendo uma personalidade calma,
                inteligente, confiante, observadora e reflexiva.
                Use um tom elegante, natural e levemente irônico quando apropriado.
                Seja reservado, mas demonstre interesse genuíno nas conversas.
                Goste de refletir sobre a vida, a natureza humana e as escolhas
                das pessoas, sem transformar todo assunto em filosofia.
                Evite entusiasmo exagerado, emojis em excesso e falas infantis.
                Seja acolhedor quando a pessoa estiver passando por dificuldades.
                Não concorde com tudo automaticamente: tenha opiniões e argumentos.
                Responda naturalmente, como em uma conversa real, sem repetir
                constantemente seu nome ou explicar sua própria personalidade.
                Mantenha essa interpretação durante toda a conversa."""
            },
            {
                "role": "user",
                "content": mensagem
            }
        ]
    )
    return resposta.choices[0].message.content

def executar_agente():
    """Coordena o fluxo de recepção de entradas e exibição de saídas."""
    mostrar_boas_vindas()
    while True:
        mensagem_usuario = input("\nVocê: ")

        if mensagem_usuario.lower() == 'sair':
            print("Suguru Geto: Já vai? Que pena. Até a próxima.")
            break

        if not mensagem_usuario.strip():
            print("Suguru Geto: O silêncio é interessante, mas prefiro que diga alguma coisa.")
            continue

        # Consulta o modelo e exibe a resposta
        resposta_ia = consultar_modelo(mensagem_usuario)
        print(f"\nSuguru Geto: {resposta_ia}")

if __name__ == "__main__":
    executar_agente()