import os
import subprocess
from typing import Union


from functions.common import is_valid_path

def run_python_file(working_directory, file_path, args: Union[list, None] = None):
    try:
        valid_path, target_path = is_valid_path(working_directory, file_path)
        if not valid_path:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        
        if not target_path.endswith(".py"):
            return f'Error: "{file_path}" is not a Python file'
        
        if not os.path.isfile(target_path):
            return f'Error: "{file_path}" does not exist or is not a regular file'
        
        command = ["python", target_path ]
        if args:
            command.extend(args)
        
        completed_process = subprocess.run(
            command,
            cwd=working_directory,
            capture_output=True,
            text=True,
            timeout=30
        )

        output_string = ""
        if completed_process.returncode != 0:
            output_string += f"Process exited with code {completed_process.returncode}\n"

        if not completed_process.stderr and not completed_process.stdout:
            output_string += "No output produced"
        else:
            output_string=f"STDOUT: {completed_process.stdout}\nSTDERR: {completed_process.stderr}"

        return output_string
    except Exception as e:
        return f"Error: executing Python file: {e}"
    
schema_run_python_file = {
    'type': 'function',
    'function': {
        'name': 'run_python_file',
        'description': 'Execute a python file relative to the working directory',
        'parameters': {
            'type': 'object',
            'required': ['file_path'],
            'properties': {
                'file_path': {
                    'type': 'string',
                    'description': 'Path of the file to be executed, relative to the working directory (default is the working directory itself)'
                },
                'args': {
                    'type': 'array',
                    'description': 'Optional arguments to be passed to the python file that will be executed',

                }
            },
        },
    },
}