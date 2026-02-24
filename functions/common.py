import os
from typing import Tuple

def is_valid_path(working_directory, target_path) -> Tuple[bool, str] :
    try:
        # validate directory  is inside working_directory
        abs_path_wd = os.path.abspath(working_directory)
        target_path = os.path.normpath(os.path.join(abs_path_wd, target_path))
        valid_target_dir = os.path.commonpath([abs_path_wd, target_path]) == abs_path_wd
        return valid_target_dir, target_path
    except Exception:
        return (False, "")