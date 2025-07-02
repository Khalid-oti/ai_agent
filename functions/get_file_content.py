import os
from google.genai import types

def get_file_content(working_directory, file_path):
    char_limit = 10000
    try:
        working_dir_path = os.path.abspath(working_directory)
        full_file_path = os.path.abspath(os.path.join(working_directory, file_path))
        if not full_file_path.startswith(working_dir_path):
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        if not os.path.isfile(full_file_path):
            return f'Error: File not found or is not a regular file: "{file_path}"'
        with open(full_file_path, "r") as r:
            file_content = r.read()
        file_chars = list(file_content)
        if len(file_chars) > char_limit:
            truncated_file_content = file_content[:10000]
            return truncated_file_content + f'...File "{file_path}" truncated at 10000 characters'
        return file_content
    except Exception as e:
        return f"Error: {e}"
    
schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Print the contents of the specified file. Limited to the first 10,000 characters. Constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file to print contents of, relative to the working directory.",
            ),
        },
    ),
)