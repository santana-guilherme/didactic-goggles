import os
from functions.common import is_valid_path

def write_file(working_directory, file_path, content):
    try:
        valid_path, target_path = is_valid_path(working_directory, file_path)
        if not valid_path:
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
        
        if os.path.isdir(target_path):
            return f'Error: Cannot write to "{target_path}" as it is a directory'
        
        # make directories
        os.makedirs(target_path.rsplit("/")[-1], exist_ok=True)

        with open(target_path, 'w') as f:
            f.write(content)
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as ex:
        return f"Error: {ex}"
    

schema_write_file = {
    'type': 'function',
    'function': {
        'name': 'write_file',
        'description': 'Write contents to a new file. If the file already exists returns an error',
        'parameters': {
            'type': 'object',
            'required': ['file_path', 'content'],
            'properties': {
                'file_path': {
                    'type': 'string',
                    'description': 'Path of the file to be created with the given content, relative to the working directory (default is the working directory itself)'
                },
                'content': {
                    'type': 'string',
                    'description': 'Content to be written on the file',
                     
                }
            },
        },
    },
}