import os
import argparse
from ollama import chat
from ollama import ChatResponse
from prompts import system_prompt
from functions.call_function import available_functions, call_function, function_map

# https://docs.ollama.com/
# https://ollama.com/blog/ollama-is-now-available-as-an-official-docker-image

# docker run -d -v ollama:/root/.ollama -p 11434:11434 --name ollama ollama/ollama
# docker exec -it ollama ollama run llama3.1

# https://medium.com/@laurentkubaski/ollama-tool-support-aka-function-calling-23a1c0189bee

parser = argparse.ArgumentParser(description="Chatbot")
parser.add_argument("user_prompt", type=str, help="User prompt")
parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
args = parser.parse_args()


def call_agent(args, messages):
    response: ChatResponse = chat(
        model="qwen3",
        messages=messages,
        tools=available_functions,
        think=True,
    )


    if args.verbose:
        print(f"User prompt: {args.user_prompt}\nPrompt tokens: {response.prompt_eval_count}\nResponse tokens: {response.eval_count}\n")
    return response


messages = [
    {
        'role': 'system',
        'content': system_prompt
    },
    {
        'role': 'user',
        'content': args.user_prompt
    }
]
for _ in range(30):
    if args.verbose:
        print(f"Using messages: {messages[-2:]}")

    response = call_agent(args, messages)

    print(f"Thinking: {response.message.thinking}")

    if response.message.tool_calls:
        function_results = []
        for tool in response.message.tool_calls:
            function_result = call_function(tool.function, args.verbose)
            # if not function_result.parts:
            #     raise Exception("No parts")
            # if not function_result.parts[0].function_response.response:
            #     raise Exception("No response in function response")
            # function_results.append(function_result.parts[0].function_response.response.get("result"))
            if args.verbose:
                a = {"result": function_result}
                print(f"-> {a}")
                # print(f"-> {function_result.parts[0].function_response.response}")
            messages.append({"role": "tool", "tool_name": tool.function.name, "content": function_result })
    else:
        print(response.message.content)
        break