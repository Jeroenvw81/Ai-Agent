import os
from google.genai import types


def get_files_info(working_directory, directory="."):
    abs_working_directory = os.path.abspath(working_directory)
    abs_target_directory = os.path.abspath(os.path.join(working_directory, directory))
    
    if not abs_target_directory.startswith(abs_working_directory):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    if not os.path.isdir(abs_target_directory):
        return f'Error: "{directory}" is not a directory'
    try:
        files_info = []
        for item in sorted(os.listdir(abs_target_directory)):
            abs_item_directory = os.path.join(abs_target_directory, item)
            item_size = os.path.getsize(abs_item_directory)
            item_type = os.path.isdir(abs_item_directory)
            files_info.append(
                f'- {item}: file_size={item_size}, is_dir={item_type}'
            )
        return "\n".join(files_info)
            
    except Exception as e:
        return f"Error listing files: {str(e)}"


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