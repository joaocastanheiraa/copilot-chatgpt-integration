import openai import sys # Configurao da API do ChatGPT CHATGPT_API_KEY = 
"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" def ask_chatgpt(prompt):
    openai.api_key = CHATGPT_API_KEY response = openai.Completion.create(
        engine="text-davinci-003", prompt=prompt, max_tokens=500
    ) return response.choices[0].text.strip() # Receber entrada do terminal if len(sys.argv) > 1: user_prompt = " ".join(sys.argv[1:]) else: user_prompt = "Explique esta consulta SQL." # Processar com o 
ChatGPT try:
    result = ask_chatgpt(user_prompt) print(f"\nResposta do ChatGPT:\n{result}\n") except Exception as e: print(f"Erro ao acessar o ChatGPT: {str(e)}")

