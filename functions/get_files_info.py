import os
from google.genai import types

def get_files_info(working_directory, directory=None):
    working_dir_path = os.path.abspath(working_directory)
    directory_path = working_dir_path
    if directory != None:
        directory_path = os.path.abspath(os.path.join(working_directory, directory))
    if not directory_path.startswith(working_dir_path):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    if not os.path.isdir(directory_path):
        return f'Error: "{directory}" is not a directory'
    
    try:
        files_info = ""
        dir_contents = os.listdir(directory_path)
        for content in dir_contents:
            content_path = os.path.join(directory_path, content)
            size = os.path.getsize(content_path)
            dir_or_not = os.path.isdir(content_path)
            files_info += f"- {content}: file_size={size}, is_dir={dir_or_not}\n"
    except Exception as e:
        return f"Error: {e}"

    return files_info

schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)