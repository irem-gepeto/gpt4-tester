import openai
import os  

api_key = os.environ.get("OPENAI_API_KEY")

openai.api_key = api_key

message = [{"role":"user", "content":"tell me a joke about turkey"}] 

response = openai.ChatCompletion.create(
    model = "gpt-4",
    messages = message, 
    max_tokens = 300
)

print(response["choices"][0]["message"]["content"])