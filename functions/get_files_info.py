import os

def get_files_info(working_directory, directory=None):
    files_info = ""
    absolute_path = os.path.abspath(working_directory)
    print(working_directory)
    print(directory)

    if directory not in absolute_path:
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    
    if not os.path.isdir(directory):
        return f'Error: "{directory}" is not a directory'
    
    for file in os.listdir(directory):
        size = os.path.getsize(file)
        dir_or_not = os.path.isdir(file)
        files_info += f"- {file}: file_size={size}, is_dir={dir_or_not}\n"

    return files_info