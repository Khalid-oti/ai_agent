import os
from dotenv import load_dotenv
from google import genai

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

prompt = "Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum."
generated_content = client.models.generate_content(model="gemini-2.0-flash-001", contents=prompt)
response = generated_content.text
prompt_tokens = generated_content.usage_metadata.prompt_token_count
response_tokens = generated_content.usage_metadata.candidates_token_count
print(response)
print(
    f"Prompt tokens: {prompt_tokens}\
    Response tokens: {response_tokens}"
)
