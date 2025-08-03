import os

def write_file(working_directory, file_path, content):
    abs_working_directory = os.path.abspath(working_directory)
    abs_target_file_path = os.path.abspath(os.path.join(working_directory, file_path))

    if not abs_target_file_path.startswith(abs_working_directory):
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    
    try:
        os.makedirs(os.path.dirname(abs_target_file_path), exist_ok=True)
    except Exception as e:
         return f"Error: creating directory: {e}"       #is this to catch potential permission issue in creating the directory?
    
    if os.path.exists(abs_target_file_path) and os.path.isdir(abs_target_file_path):
         return f"Error: {file_path} is a directory, not a file"
    
    try:
        with open(abs_target_file_path, "w") as f:
            f.write(content)
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'

    except Exception as e:
        return f"Error writing file: {e}"
    
    

        


