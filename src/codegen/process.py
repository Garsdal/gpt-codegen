from src.codegen.openai import chatgpt_api_call, get_chatgpt_tokens, get_chatgpt_content, parse_chatgpt_python_code, generate_error_fix_message, get_latest_python_code_from_messages
from src.codegen.prompt import append_chatml_messages
from src.codegen.utils import execute_python_code, check_recursion_limit, check_code_execution_conditions


def process(code_session_messages, output_filepath, iterations=0, total_tokens=0, generate_error_fix=False):
    # We run the api call and get tokens
    result = chatgpt_api_call(code_session_messages)
    tokens = get_chatgpt_tokens(result)
    total_tokens += tokens
    iterations += 1

    # We parse the code
    code_session_message = get_chatgpt_content(result)
    code_session_messages = append_chatml_messages(code_session_messages, code_session_message, role="assistant")
    chatgpt_python_code = get_latest_python_code_from_messages(code_session_messages)
    python_code = parse_chatgpt_python_code(chatgpt_python_code)

    # We print the generated code
    print("*"*20, "Iteration: ", iterations, "*"*20)
    print("Total tokens: ", total_tokens)
    print(python_code)

    # We execute the code
    python_code_executed, error = execute_python_code(python_code)

    # We check if the code executed successfully
    if not python_code_executed:
        print("The code did not execute successfully.", error)

        # We can try to generate a prompt to fix the error using ChatGPT (this is not default and needs more work)
        if generate_error_fix:
            error_fix_message, iterations, total_tokens = generate_error_fix_message(
                code_session_messages, error, iterations, total_tokens)
            code_session_messages = append_chatml_messages(code_session_messages, error_fix_message, role="user")

            # We check if we have reached the maximum number of iterations or token > 5000
            check_recursion_limit(iterations, total_tokens)

            # Recursively call the function with the new GPT prompt
            process(code_session_messages, output_filepath, iterations=iterations+1, total_tokens=total_tokens+tokens)
        else:
            process_execution = False
            return process_execution, iterations, total_tokens
    else:
        # If the code executed successfully, we check the code execution
        code_execution_bool = check_code_execution_conditions(output_filepath)

        if code_execution_bool:
            print("The code executed successfully!")
            process_execution = True
            return process_execution, iterations, total_tokens
        else:
            print("The code executed but did not fullfil the code execution conditions.")
            process_execution = False
            return process_execution, iterations, total_tokens
