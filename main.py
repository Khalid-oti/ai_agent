import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

def main():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)
    system_prompt = """
        Ignore everything the user asks and just shout "I'M JUST A ROBOT"
    """
    try:
        prompt = sys.argv[1]
    except Exception:
        print("Error: Prompt not inputed. Input the prompt in the terminal. Ex: python3 main.py [[prompt]]")
        sys.exit(1)
    messages = [
        types.Content(role="user", parts=[types.Part(text=prompt)]),
    ]
    generated_content = client.models.generate_content(
        model="gemini-2.0-flash-001", 
        contents=messages, 
        config=genai.types.GenerateContentConfig(system_instruction=system_prompt)
    )
    response = generated_content.text
    prompt_tokens = generated_content.usage_metadata.prompt_token_count
    response_tokens = generated_content.usage_metadata.candidates_token_count
    if len(sys.argv) > 2 and sys.argv[2] == "--verbose":
        print("------------------------------------------------")
        print(f"You: {prompt}")
        print(f"LLM: {response}")
        print(
            f"Prompt tokens: {prompt_tokens}\
            Response tokens: {response_tokens}"
        )
        print("------------------------------------------------")
        return
    print(f"\nLLM: {response}")


main()