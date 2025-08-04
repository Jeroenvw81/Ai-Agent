import os
import subprocess

def run_python_file(working_directory, file_path, args=None):
    abs_working_directory = os.path.abspath(working_directory)
    abs_target_file_path = os.path.abspath(os.path.join(working_directory, file_path))
    
    if not os.path.isfile(abs_target_file_path):
        return f'Error: File "{file_path}" not found.'
    
    if not abs_target_file_path.endswith('.py'):
        return f'Error: File "{file_path}" is not a Python file'
    
    if os.path.commonpath([abs_working_directory, abs_target_file_path]) != abs_working_directory:
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    
    try:
        commands = ["python", abs_target_file_path]
        if args:
            commands.extend(args)
        result = subprocess.run(
            commands,
            capture_output=True,
            text=True,
            timeout=30,
            cwd=abs_working_directory,
            )
        output = []
        if result.stdout:
            output.append(f"STDOUT:\n{result.stdout}")
        if result.stderr:
            output.append(f"STDERR:\n{result.stderr}")

        if result.returncode != 0:
            output.append(f"Process exited with code {result.returncode}")

        return "\n".join(output) if output else "No output produced."
    except Exception as e:
        return f'Error: exececuting Python file: {e}'