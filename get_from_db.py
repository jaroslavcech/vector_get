from openai import OpenAI
import numpy as np
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
import json
import re

def get_embedding2(client, text, model="text-embedding-3-small"):
    normalized_text = normalize_text(text)
    return client.embeddings.create(input=[normalized_text], model=model).data[0].embedding

def normalize_text(text):
    text = text.lower()
    text = re.sub(r"\s+", " ", text)
    return text

def get_chunks(model, env_dict, args):
    try:
        client = OpenAI(api_key=env_dict['OPENAI_API_KEY'])
        db_host = env_dict['DB_HOST']
        port = env_dict['DB_PORT']
        db_user = env_dict['DB_USER']
        password = env_dict['DB_PASSWORD']
        db_name = env_dict['DB_NAME']
        table_name = args.table
        column_name = args.column
        text = args.query
        chunks_nr = args.number_chunks
        # Connect to the default postgres database to check/create database
        print(f"Starting to embed to {db_name}, table {table_name}")
        conn = psycopg2.connect(dbname=db_name, user=db_user, password=password, host=db_host, port=port)
        conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        cursor = conn.cursor()

        emb = get_embedding2(client, text, model)
        embedding_str = np.array(emb).tolist()
        query_str = f"SELECT {args.fields}, ({column_name} <#> '{embedding_str}'::vector) as similarity_score  from {table_name} ORDER BY {args.column} <#> '{embedding_str}'::vector ASC LIMIT {chunks_nr}"
        cursor.execute(query_str)
        columns = [desc[0] for desc in cursor.description]
        top_docs = cursor.fetchall()
        rows = [dict(zip(columns, row)) for row in top_docs]
        cursor.close()
        conn.close()
        return json.dumps(rows, indent=4)
    except Exception as e:
        print(f"Exception {e}")

