import os
from google.genai import types

def write_file(working_directory, file_path, content):
    try:
        working_dir_path = os.path.abspath(working_directory)
        full_file_path = os.path.abspath(os.path.join(working_directory, file_path))
        if not full_file_path.startswith(working_dir_path):
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
        if not os.path.exists(full_file_path):
            os.makedirs(os.path.dirname(full_file_path))
        with open(full_file_path, "w") as w:
            w.write(content)
    except Exception as e:
        return f"Error: {e}"
    return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'

schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Writes content in the specified file, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file to write the content in, relative to the working directory.",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="The content to write in the file.",
            ),
        },
    ),
)