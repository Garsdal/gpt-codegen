import openai
import json
import os
from src import _SRC_DIR
from codegen.process import process
from codegen.prompt import create_chatml_messages, get_system_prompt, get_user_prompt
from codegen.utils import check_recursion_limit

if __name__ == "__main__":
    input_filepath = "data/data_input/test1.csv"
    output_filepath = "data/data_output/test1.csv"

    # We load the config and set the api key
    config_file = os.path.join(_SRC_DIR.parent, "config", "config_api.json")
    with open('config/config_api.json', 'r') as f:
        config_api = json.load(f)
    openai.api_key = config_api['API_KEY']

    # We get the initial hardcoded prompts for this problem
    system_prompt = get_system_prompt()
    user_prompt = get_user_prompt(input_filepath, output_filepath)
    code_session_messages = create_chatml_messages(system_prompt, user_prompt)

    # We run the process in a while loop until the code executes successfully. We also check if we have reached the maximum number of iterations or token > 5000
    process_execution = False
    iterations = 0
    total_tokens = 0
    while not process_execution:
        code_session_messages = create_chatml_messages(system_prompt, user_prompt)

        process_execution, iterations, total_tokens = process(
            code_session_messages, output_filepath, iterations, total_tokens, generate_error_fix=False)
        check_recursion_limit(iterations, total_tokens)
