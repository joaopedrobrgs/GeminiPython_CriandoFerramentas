import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

CHAVE_API_GOOGLE = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=CHAVE_API_GOOGLE)

#MODELOS

MODELO_FLASH_LITE = "gemini-2.5-flash-lite"
MODELO_FLASH = "gemini-2.5-flash"
MODELO_PRO = "gemini-2.5-pro"

#CUSTOS DE CADA MODELO

##CUSTOS FLASH LITE
CUSTO_ENTRADA_FLASH_LITE = 0.1
CUSTO_SAIDA_FLASH_LITE = 0.4

##CUSTOS FLASH
CUSTO_ENTRADA_FLASH = 0.3
CUSTO_SAIDA_FLASH = 2.5

##CUSTOS PRO
CUSTO_ENTRADA_PRO = 2.5
CUSTO_SAIDA_PRO = 15

#LIMITES DE CADA MODELO

model_flash_lite = genai.get_model(f"models/{MODELO_FLASH_LITE}")
limites_modelo_flash_lite = {
    "tokens_entrada": model_flash_lite.input_token_limit,
    "tokens_saida": model_flash_lite.output_token_limit
}
print(f"Limites do modelo flash lite são: {limites_modelo_flash_lite}")

model_flash = genai.get_model(f"models/{MODELO_FLASH}")
limites_modelo_flash = {
    "tokens_entrada": model_flash.input_token_limit,
    "tokens_saida": model_flash.output_token_limit
}
print(f"Limites do modelo flash são: {limites_modelo_flash}")

model_pro = genai.get_model(f"models/{MODELO_PRO}")
limites_modelo_pro = {
    "tokens_entrada": model_pro.input_token_limit,
    "tokens_saida": model_pro.output_token_limit
}
print(f"Limites do modelo pro são: {limites_modelo_pro}")

# Criando modelo flash lite:
llm_flash_lite = genai.GenerativeModel(f"models/{MODELO_FLASH_LITE}")
quantidade_tokens_flash_lite = llm_flash_lite.count_tokens("O que é uma calça de shopping?")
if(quantidade_tokens_flash_lite is not None):
  print(f"A quantidade de tokens é: {quantidade_tokens_flash_lite}")
  
# Criando modelo flash:
llm_flash = genai.GenerativeModel(f"models/{MODELO_FLASH}")
quantidade_tokens_flash = llm_flash.count_tokens("O que é uma calça de shopping?")
if(quantidade_tokens_flash is not None):
  print(f"A quantidade de tokens é: {quantidade_tokens_flash}")
  
resposta_flash = llm_flash.generate_content("O que é uma calça de shopping?")
tokens_prompt_flash = resposta_flash.usage_metadata.prompt_token_count
tokens_resposta_flash = resposta_flash.usage_metadata.candidates_token_count

custo_total_flash = (tokens_prompt_flash * CUSTO_ENTRADA_FLASH) / 1000000 + (tokens_resposta_flash * CUSTO_SAIDA_FLASH) / 1000000
print(f"Custo Total U$ Flash: ", custo_total_flash)
  
# Criando modelo pro:
llm_pro = genai.GenerativeModel(f"models/{MODELO_PRO}")
quantidade_tokens_pro = llm_pro.count_tokens("O que é uma calça de shopping?")
if(quantidade_tokens_pro is not None):
  print(f"A quantidade de tokens é: {quantidade_tokens_pro}")
  
resposta_pro = llm_flash.generate_content("O que é uma calça de shopping?")
tokens_prompt_pro = resposta_pro.usage_metadata.prompt_token_count
tokens_resposta_pro = resposta_pro.usage_metadata.candidates_token_count

custo_total_pro = (tokens_prompt_pro * CUSTO_ENTRADA_PRO) / 1000000 + (tokens_resposta_pro * CUSTO_SAIDA_PRO) / 1000000
print(f"Custo Total U$ Pro: ", custo_total_pro)