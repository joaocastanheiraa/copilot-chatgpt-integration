import openai 
# Configuracao da API do ChatGPT 
openai.api_key = "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"
# Testando a conexao com a API do ChatGPT
try:
    response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "system", "content": "Voc um assistente til e sempre responde em portugues."},{"role": "user", "content": "Teste de conexo com a API"}], max_tokens=50
)
    print(response["choices"][0]["message"]["content"].strip())
except Exception as e:
    print(f"Erro ao conectar com o ChatGPT: {e}")
