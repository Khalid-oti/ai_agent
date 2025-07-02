import os
import subprocess
from google.genai import types

def run_python_file(working_directory, file_path):
    working_dir_path = os.path.abspath(working_directory)
    full_file_path = os.path.abspath(os.path.join(working_directory, file_path))
    if not full_file_path.startswith(working_dir_path):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    if not os.path.exists(full_file_path):
        return f'Error: File "{file_path}" not found.'
    if not file_path.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file.'
    try:
        run = subprocess.run(["python3", full_file_path], capture_output=True, text=True, cwd=working_dir_path, timeout=30)
        output = []
        if run.stderr:
            output.append(f"STDERR: {run.stderr}")
        if run.stdout:
            output.append(f"STDOUT: {run.stdout}")
        if run.returncode > 0:
            output.append(f"Process exited with code {run.returncode}")
        if output == []:
            return "No output produced"
        return "\n".join(output)
    except Exception as e:
        return f"Error: executing Python file: {e}"
    
schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="runs a python file, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file to run, relative to the working directory.",
            ),
        },
    ),
)