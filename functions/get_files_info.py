import os

def get_files_info(working_directory, directory=None):
    files_info = ""
    try:
        dir = os.path.isdir(directory)
    except Exception as e:
        return f"Error: {e}"
    try:
        absolute_path = os.path.abspath(working_directory)
    except Exception as e:
        return f"Error: {e}"
    if directory not in absolute_path:
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    if not dir:
        return f'Error: "{directory}" is not a directory'
    for file in os.listdir(directory):
        try:
            size = os.path.getsize(file)
        except Exception as e:
            return f"Error: {e}"
        try:
            type = os.path.isdir(file)
        except Exception as e:
            return f"Error: {e}"
        files_info += f"- {file}: file_size={size}, is_dir={type}\n"