import os
from config import CHAR_LIMIT


def get_file_content(working_directory, file_path):
    abs_working_directory = os.path.abspath(working_directory)
    abs_target_file_path = os.path.abspath(os.path.join(working_directory, file_path))

    if not abs_target_file_path.startswith(abs_working_directory):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    if not os.path.isfile(abs_target_file_path):
        return f'Error: File not found or is not a regular file: "{file_path}"'
    try:
        with open(abs_target_file_path, "r") as text:
            file_content_string = text.read(CHAR_LIMIT)
            if len(file_content_string) == CHAR_LIMIT:
                return file_content_string + f'[...File: "{file_path}" truncated at {CHAR_LIMIT} characters]'
            return file_content_string
    except Exception as e:
        return f"Error reading file: {str(e)}"
        
