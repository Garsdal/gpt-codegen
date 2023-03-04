import os
import json
import pandas as pd


def setup_folder(folder_path):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)


def load_config(config_path):
    with open(config_path) as f:
        config_api = json.load(f)
    return config_api


def check_code_execution_conditions(output_filepath: str):
    if not os.path.exists(output_filepath):
        return False

    if not output_filepath.endswith(".csv"):
        return False

    # We load the output file as a dataframe
    df = pd.read_csv(output_filepath, sep=";", index_col=0, parse_dates=True)

    if len(df.columns) != 1:
        return False

    if df.columns[0] != "Power":
        return False

    if df.index.name != "TimeUTC":
        return False

    if not isinstance(df.index, pd.DatetimeIndex):
        return False

    return True


def check_recursion_limit(iteration: int, total_tokens: int):
    if iteration >= 5 or total_tokens > 5000:
        raise ValueError("Reached maximum number of iterations or tokens")


def execute_python_code(python_code: str) -> tuple:
    error = None
    python_code_executed = False
    try:
        exec(python_code)
        python_code_executed = True
    except Exception as e:
        error = e
        return python_code_executed, error

    return python_code_executed, error
