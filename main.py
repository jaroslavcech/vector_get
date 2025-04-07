import argparse
from arguments import parse_args, get_env
from get_from_db import get_chunks

if __name__ == '__main__':
    args = parse_args()
    env_dict = get_env()
    chunks = get_chunks(args.embedding_model, env_dict, args)
    print(chunks)
