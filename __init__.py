import os

def validate_directory(working_directory, path):
    try:
        abs_path_wd = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(abs_path_wd, directory))
        valid_target_dir = os.path.commonpath([abs_path_wd, target_dir]) == abs_path_wd
        return valid_target_dir
    except Exception:
        return False


def get_files_info(working_directory, directory="."):
    try:
        # validate directory  is inside working_directory
        
        if not os.path.isdir(target_dir):
            return print(f'Error: "{directory}" is not a directory')
        
        dir_print = f"'{directory}'" if directory != '.' else 'current'
        print(f"Result for {dir_print} directory")
        for el in os.scandir(target_dir):
            #- README.md: file_size=1032 bytes, is_dir=False
            print(f"\t- {el.name}: file_size={os.path.getsize(el.path)} bytes, is_dir={el.is_dir()}")
    except Exception as ex:
        print(f"Error: {ex}")
