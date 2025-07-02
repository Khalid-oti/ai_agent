import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types
from functions.get_files_info import schema_get_files_info
from functions.get_file_content import schema_get_file_content
from functions.run_python_file import schema_run_python_file
from functions.write_file import schema_write_file

def main():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)
    system_prompt = """
        You are a helpful AI coding agent.

        When a user asks a question or makes a request, make a function call plan. You can perform the following operations:

        - List files and directories
        - Read file contents
        - Execute Python files with optional arguments
        - Write or overwrite files

        All paths you provide should be relative to the working directory. You do not need to specify the working directory in your function calls as it is automatically injected for security reasons.
    """
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
    available_functions = types.Tool(
        function_declarations=[
            schema_get_files_info,
            schema_run_python_file,
            schema_write_file,
            schema_get_file_content
        ]
    )
    generated_content = client.models.generate_content(
        model="gemini-2.0-flash-001", 
        contents=messages, 
        config=genai.types.GenerateContentConfig(tools=[available_functions], system_instruction=system_prompt)
    )
    output = []
    if generated_content.function_calls:
        called_functions = []
        for function_call_part in generated_content.function_calls:
            called_functions.append(f"Calling function: {function_call_part.name}({function_call_part.args})")
        output.append("\n".join(called_functions))
    response = f"LLM: {generated_content.text}"
    prompt_tokens = generated_content.usage_metadata.prompt_token_count
    response_tokens = generated_content.usage_metadata.candidates_token_count
    output.append(response)
    if len(sys.argv) > 2 and sys.argv[2] == "--verbose":
        output.extend([
            f"You: {prompt}", 
            f"Prompt tokens: {prompt_tokens}",
            f"Response tokens: {response_tokens}"
            ])
    for part in output:
        print(part+"\n")


main()