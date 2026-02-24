import os

def get_files_info(working_directory, directory="."):
    try:
        # validate directory  is inside working_directory
        abs_path_wd = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(abs_path_wd, directory))
        valid_target_dir = os.path.commonpath([abs_path_wd, target_dir]) == abs_path_wd
        if not valid_target_dir:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        
        if not os.path.isdir(target_dir):
            return f'Error: "{directory}" is not a directory'
        
        dir_print = f"'{directory}'" if directory != '.' else 'current'
        output_string = f"Result for {dir_print} directory "
        for el in os.scandir(target_dir):
            #- README.md: file_size=1032 bytes, is_dir=False
            output_string+=f"- {el.name}: file_size={os.path.getsize(el.path)} bytes, is_dir={el.is_dir()} "
        return output_string
    except Exception as ex:
        f"Error: {ex}"


schema_get_files_info = {
    'type': 'function',
    'function': {
        'name': 'get_files_info',
        'description': 'Lists files in a specified directory relative to the working directory, providing file size and directory status',
        'parameters': {
            'type': 'object',
            'required': ['directory'],
            'properties': {
                'directory': {
                    'type': 'string',
                    'description': 'Directory path to list files from, relative to the working directory (default is the working directory itself)'
                },
            },
        },
    },
}