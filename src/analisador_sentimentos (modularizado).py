import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

CHAVE_API_GEMINI = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=CHAVE_API_GEMINI)
MODELO = "gemini-2.5-pro"

def carrega(nome_do_arquivo):
  try:
    with open(nome_do_arquivo, "r")as arquivo:
            dados = arquivo.read()
    return dados
  except IOError  as e:
        print(f"Erro: {e}")

def salva(nome_do_arquivo, conteudo):
  try:
    with open(nome_do_arquivo, "w", encoding="utf-8") as arquivo: 
      arquivo.write(conteudo)
  except IOError as e:
    print(f"Erro ao salvar arquivo: {e}")
    
def analisador_sentimentos(nome_produto):
  prompt_sistema = f"""
    Você é um analisador de sentimentos de avaliações de produtos.
    Escreva um parágrafo com até 50 palavras resumindo as avaliações e
    depois atribua qual o sentimento geral para o produto.
    Identifique também 3 pontos fortes e 3 pontos fracos identificados a partir das avaliações.

    # Formato de Saída

    Nome do Produto:
    Resumo das Avaliações:
    Sentimento Geral: [utilize aqui apenas Positivo, Negativo ou Neutro]
    Ponto fortes: lista com três bullets
    Pontos fracos: lista com três bullets
  """
  
  prompt_usuario = carrega(f"src/dados/avaliacoes/avaliacoes-{nome_produto}.txt")

  print(f"Iniciando a análise de sentimentos do produto: {nome_produto}")

  llm = genai.GenerativeModel(
    model_name=MODELO,
    system_instruction=prompt_sistema,
  )

  resposta = llm.generate_content(prompt_usuario)

  salva(f"src/dados/respostas/resposta-{nome_produto}.txt", resposta.text)
  
def main():
  lista_de_produtos = ["Camisetas de algodão orgânico", "Jeans feitos com materiais reciclados", "Maquiagem mineral"]
  
  for prod in lista_de_produtos:
    analisador_sentimentos(prod)
    
if __name__ == "__main__":
  main()