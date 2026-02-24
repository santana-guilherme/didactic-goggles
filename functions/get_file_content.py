import os
from config import MAX_CHARS

def get_file_content(working_directory, file_path):
    try:
        # validate directory  is inside working_directory
        abs_path_wd = os.path.abspath(working_directory)
        target_file = os.path.normpath(os.path.join(abs_path_wd, file_path))
        valid_target_dir = os.path.commonpath([abs_path_wd, target_file]) == abs_path_wd
        if not valid_target_dir:
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        
        if not os.path.isfile(target_file):
            return f'Error: File not found or is not a regular file: "{file_path}"'
        
        with open(target_file) as f:
            content = f.read(MAX_CHARS)
            if f.read(1):
                content += f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'
            
            return content
    except Exception as ex:
        return f"Error: {ex}"
    

schema_get_file_content = {
    'type': 'function',
    'function': {
        'name': 'get_file_content',
        'description': 'Get content of a file in the specified path',
        'parameters': {
            'type': 'object',
            'required': ['file_path'],
            'properties': {
                'file_path': {
                    'type': 'string',
                    'description': 'Path of the file to get the content, relative to the working directory (default is the working directory itself)'
                },
            },
        },
    },
}