import openai
from src.codegen.prompt import create_chatml_messages, append_chatml_messages, get_system_prompt


def chatgpt_api_call(messages: list) -> dict:
    result = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    return result


def get_chatgpt_tokens(result: dict) -> int:
    """
    We get the total tokens cost from the result
    """
    return result["usage"]["total_tokens"]


def get_chatgpt_content(result: dict) -> str:
    """
    We return the output of the completion
    """
    return result['choices'][0]['message']['content']


def parse_chatgpt_python_code(chatgpt_python_code: str) -> str:
    """Parse the python code from the chatgpt output.
    We get each substring between "```python\n" and "```" from chatgpt_python_code
    We save all of these substrings in a list
    """
    python_code = ""
    parser_substrings = ["```python", "``` python\n", "```", " python", "python"]
    for parser_substring in parser_substrings:
        if parser_substring in chatgpt_python_code:
            for i in range(chatgpt_python_code.count(parser_substring)):
                python_code += chatgpt_python_code.split(parser_substring)[i+1].split("```")[0]
            return python_code
        else:
            python_code = chatgpt_python_code

    return python_code


def get_latest_python_code_from_messages(messages: list) -> str:
    """
    We iterate backwards through the messages in message list where the role is 'assistant' and the content is not empty.
    We return the first python code we find. We check if it is valid python code by checking if the content contains any of the parser substrings
    """
    parser_substrings = ["```", "```python", "``` python\n", "``` python", " python", "python", "import"]
    for message in reversed(messages):
        if message["role"] == "assistant" and message["content"] != "":
            for parser_substring in parser_substrings:
                if parser_substring in message["content"]:
                    return message["content"]
    return ""


def generate_error_fix_message(messages: list, error: str, iterations: int, total_tokens: int) -> tuple:
    chatgpt_python_code = get_latest_python_code_from_messages(messages)
    python_code = parse_chatgpt_python_code(chatgpt_python_code)

    # We get the system prompt
    system_prompt = get_system_prompt()
    user_prompt = f"""You have the following python code: {python_code}. 
    This code has the following error: {error}. 
    Please give me a short and brief prompt to fix the error.
    """

    # We create the error fix prompt
    error_fix_messages = create_chatml_messages(system_prompt, user_prompt)

    # We create the API_call
    result = chatgpt_api_call(error_fix_messages)
    tokens = get_chatgpt_tokens(result)
    total_tokens += tokens
    iterations += 1
    error_fix_message = get_chatgpt_content(result)

    # We update the message a bit
    error_fix_message = f"""Please update the previous python code based on the following update to fix the error: {error_fix_message}"""

    # We print the generated code
    print("*"*20, "Iteration: ", iterations, "*"*20)
    print("Total tokens: ", total_tokens)
    print(error_fix_message)

    return error_fix_message, iterations, total_tokens
