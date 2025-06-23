import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)
try:
    prompt = sys.argv[1]
except Exception:
    print("Error: Prompt not inputed")
    sys.exit(1)

messages = [
    types.Content(role="user", parts=[types.Part(text=prompt)]),
]
generated_content = client.models.generate_content(model="gemini-2.0-flash-001", contents=messages)
response = generated_content.text
prompt_tokens = generated_content.usage_metadata.prompt_token_count
response_tokens = generated_content.usage_metadata.candidates_token_count
print(response)
if len(sys.argv) > 2 and sys.argv[2] == "--verbose":
    print(
        f"Prompt tokens: {prompt_tokens}\
        Response tokens: {response_tokens}"
    )
    print(f"User prompt: {prompt}")