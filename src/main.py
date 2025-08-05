import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

CHAVE_API_GOOGLE = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=CHAVE_API_GOOGLE)
MODELO_ESCOLHIDO = "gemini-2.5-pro"

# Definindo prompt/instruções para o modelo:
prompt_sistema = f"""
Liste apenas os nomes dos produto e ofereça uma breve descrição.
"""

# Passando parâmetros para o modelo:
configuracao_modelo = {
  "temperature": 0.1,
  "top_p": 1.0,
  "top_k": 2,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain"
}

# Criando modelo de fato:
llm = genai.GenerativeModel(
  model_name=MODELO_ESCOLHIDO,
  system_instruction=prompt_sistema,
  generation_config=configuracao_modelo
)

pergunta = "Liste 3 produtos de moda sustentável para ir ao shopping"

resposta = llm.generate_content(pergunta)

if(resposta.text is not None):
  print(f"A resposta gerada para pergunta é: {resposta.text}")