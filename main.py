import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types
from functions.call_function import available_functions, call_function

system_prompt = """
    You are a helpful AI coding agent.

    When a user asks a question or makes a request, make a function call plan. You can perform the following operations:

    - List files and directories
    - Read file contents
    - Execute Python files with optional arguments
    - Write or overwrite files
    - Call the specified functions

    All paths you provide should be relative to the working directory. You do not need to specify the working directory in your function calls as it is automatically injected for security reasons.
"""

def main():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)
    try:
        prompt = sys.argv[1]
    except Exception:
        print("Error: Prompt not inputed. Input the prompt in the terminal. Ex: python3 main.py [[prompt]]")
        sys.exit(1)
    messages = [
        types.Content(
        role="user", 
        parts=[types.Part(text=prompt)]
        )
    ]
    try:
        for i in range(21):
            if i == 20:
                print("Error: maximum generate_content iterations reached")
                continue
            LLM_resposne = generate_content(client, prompt, messages)
            if LLM_resposne:
                print(f"LLM: {LLM_resposne}")
                break
    except Exception as e:
         print(f"Error: {e}")

def generate_content(client, prompt, messages):
    global system_prompt
    generated_content = client.models.generate_content(
        model="gemini-2.0-flash-001", 
        contents=messages,
        config=genai.types.GenerateContentConfig(tools=[available_functions], system_instruction=system_prompt)
    )
    for candidate in generated_content.candidates:
        messages.append(candidate.content)

    prompt_tokens = generated_content.usage_metadata.prompt_token_count
    response_tokens = generated_content.usage_metadata.candidates_token_count
    verbose = len(sys.argv) > 2 and sys.argv[2] == "--verbose"

    if verbose:
        print(f"You: {prompt}")
        print(f"Prompt tokens: {prompt_tokens}")
        print(f"Response tokens: {response_tokens}")

    if not generated_content.function_calls:
        return generated_content.text

    function_responses = []
    for function_call_part in generated_content.function_calls:
        function_call_result = call_function(function_call_part, verbose=verbose)
        if not function_call_result.parts or not function_call_result.parts[0].function_response:
            raise Exception("empty function call result")
        if verbose:
            print(f"-> {function_call_result.parts[0].function_response.response}")
        function_responses.append(function_call_result.parts[0])
        
    if not function_responses:
        raise Exception("Error: function response not found")
    messages.append(types.Content(role="tool", parts=function_responses))
    


if __name__ == "__main__":
    main()