import pandas as pd
import io


def get_system_prompt() -> str:
    system_prompt = """I want you to act as a Python code expert. You will not output any text other than Python code. You must not comment the Python code. You are not allowed to put in filler text such as “sure, here is your answer:”."""
    return system_prompt


def get_user_prompt(input_filepath: str, output_filepath: str) -> str:
    user_prompt = f"""
    Later in this prompt I will provide you with the head() of a dataframe as csv inside [].

    You must write code to convert a dataframe to a standard format that must fulfill the conditions:
    1. The index must datetimeindex with format “%Y-%mm-%dd %HH:%MM”
    2. The index name must be "TimeUTC"
    3. There must only be one column
    3. The only column must contain Power signal as a float value with unit kW
    4. The column name must be “Power_kW“

    The Python code should fullfill the following conditions:
    1. The code must not contain any comments. Never.
    2. The code should set the index before any other operation.
    3. The code must be dynamic and work for a dataframe of any size but with the structure inside []
    4. The code must load the dataframe at the beginning from “{input_filepath}” without any formatting
    5. The code must save the dataframe to “{output_filepath}”
    6. The code must save the dataframe with sep=";" and index=True. Always.
    """

    # We get the head of the dataframe as string
    df = pd.read_csv(input_filepath)
    df_head_str = df.head(5).to_csv()

    # We get the info of the dataframe as string
    string_buffer = io.StringIO()
    df.info(verbose=True, buf=string_buffer)
    df_info_str = string_buffer.getvalue()

    # We add it to the end of the user prompt
    user_prompt += "\n" + f"[{df_head_str}]"

    return user_prompt


def create_chatml_messages(system_prompt: str, user_prompt: str) -> list:
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt}
    ]
    return messages


def append_chatml_messages(messages: list, prompt: str, role: str) -> list:
    messages.append({"role": role, "content": prompt})
    return messages
