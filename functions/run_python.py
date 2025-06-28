import os
import subprocess

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
        run = subprocess.run(["python3", full_file_path], capture_output=True, cwd=working_dir_path, timeout=30)
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