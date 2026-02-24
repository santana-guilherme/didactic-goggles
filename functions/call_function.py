from functions.get_files_info import schema_get_files_info, get_files_info
from functions.get_file_content import schema_get_file_content, get_file_content
from functions.run_python_file import schema_run_python_file, run_python_file
from functions.write_file import schema_write_file, write_file

from google.genai import types

available_functions = [
    schema_get_files_info,
    schema_get_file_content,
    schema_run_python_file,
    schema_write_file
]


function_map = {
    "get_file_content": get_file_content,
    "get_files_info": get_files_info,
    "run_python_file": run_python_file,
    "write_file": write_file
}

def call_function(function_call, verbose=False):

    if verbose:
        print(f"Calling function: {function_call.name}({function_call.arguments})")
    else:
        print(f" - Calling function: {function_call.name}")

    function_name = function_call.name or ""

    f = function_map.get(function_name)

    if not f:
        return f"Unknown function: {function_name}"
        # return types.Content(
        #     role="tool",
        #     parts=[
        #         types.Part.from_function_response(
        #             name=function_name,
        #             response={"error": f"Unknown function: {function_name}"},
        #         )
        #     ],
        # )

    args = dict(function_call.arguments) if function_call.arguments else {}
    args["working_directory"] = "./calculator"
    response = f(**args)
    return response
    # return types.Content(
    #     role="tool",
    #     parts=[
    #         types.Part.from_function_response(
    #             name=function_name,
    #             response={"result": response},
    #         )
    #     ],
    # )
