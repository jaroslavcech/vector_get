import argparse
import os
from dotenv import load_dotenv

def parse_args():
    parser = argparse.ArgumentParser(description='Retrieve similar chunk(s) from postgres vector table.')

    parser.add_argument('-q', '--query',  type=str, required=True,
                        help='Text to find similar chunks from.')

    parser.add_argument('-t', '--table', type=str, required=False,
                        default='embeddings',
                        help='Table name where embedding column exists.')

    parser.add_argument('-f', '--fields', type=str, required=False,
                        default='id, file, page, position, text_chunk',
                        help='Field names to retrieve.')

    parser.add_argument('-c', '--column', type=str, required=False,
                        default='embedding',
                        help='Column name where embeddings are stored.')

    parser.add_argument('-n', '--number_chunks', type=int, required=False,
                        default=1,
                        help='How many chunks to retrieve.')

    parser.add_argument('-m', '--embedding_model', required=True,
                        choices=['text-embedding-3-small', 'text-embedding-3-large','text-embedding-ada-002'],
                        help='Name of the embedding model to use for the vectorization of input string (e.g., text-embedding-ada-002).')

    args = parser.parse_args()

    print('Command line parameters:')
    for key, value in vars(args).items():
        print(f"{key}: {value}")
    return args

def get_env():
    load_dotenv()
    env_dict = {
        "DB_HOST" : os.getenv("DB_HOST"),
        "DB_PORT" : os.getenv("DB_PORT"),
        "DB_NAME" : os.getenv("DB_NAME"),
        "DB_USER" : os.getenv("DB_USER"),
        "DB_PASSWORD" : os.getenv("DB_PASSWORD"),
        "OPENAI_API_KEY" : os.getenv("OPENAI_API_KEY"),
    }

    truncate_keys = {"OPENAI_API_KEY", "db_password"}
    for key, value in env_dict.items():
        if key in truncate_keys:
            print(f"{key}: {value[:3]}...")
        else:
            print(f"{key}: {value}")

    return env_dict

def limited_int(arg, arg_min, arg_max, variable_name):
    value = int(arg)
    if not (arg_min <= value <= arg_max):
        raise argparse.ArgumentTypeError(f"Value of {variable_name} must be between {arg_min} and {arg_max}.")
    return value