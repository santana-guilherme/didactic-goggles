import os
from dotenv import load_dotenv
from google import genai
import argparse

# https://docs.ollama.com/
# https://ollama.com/blog/ollama-is-now-available-as-an-official-docker-image

# docker run -d -v ollama:/root/.ollama -p 11434:11434 --name ollama ollama/ollama
# docker exec -it ollama ollama run llama2

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

parser = argparse.ArgumentParser(description="Chatbot")
parser.add_argument("user_prompt", type=str, help="User prompt")
args = parser.parse_args()

client = genai.Client(api_key=api_key)
response = client.models.generate_content(
    model="gemini-2.5-flash", contents=args.user_prompt
)
usage = response.usage_metadata

if usage:
    print(f"Prompt tokens: {usage.prompt_token_count}\nResponse tokens: {usage.candidates_token_count}\n")
print(response.text)
