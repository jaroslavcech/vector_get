# Text Embedding and Retrieval

This project allows you to retrieve similar text chunks from a PostgreSQL vector database using OpenAI's embedding models.

## Overview

The project performs the following:
- Parses input arguments to specify the query text, database details, and embedding model.
- Embeds query text using OpenAI's embedding API.
- Queries a PostgreSQL database using vector similarity to find matching text chunks.

## Requirements
- Python 3.8+
- PostgreSQL database with vector support
- OpenAI API key

## Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/yourproject.git
cd yourproject
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Create and fill `.env` file with your database and API credentials:

```
DB_HOST=your_db_host
DB_PORT=your_db_port
DB_NAME=your_db_name
DB_USER=your_db_user
DB_PASSWORD=your_db_password
OPENAI_API_KEY=your_openai_api_key
```

## Usage

Execute the script with necessary arguments:

```bash
python main.py -q "Your query text" -m "text-embedding-3-small"
```

### Command Line Arguments

- `-q, --query`: Text input to find similar chunks.
- `-t, --table` *(optional)*: Table name (default: `embeddings`).
- `-f, --fields` *(optional)*: Fields to retrieve (default: `id, file, page, position, text_chunk`).
- `-c, --column` *(optional)*: Column containing embeddings (default: `embedding`).
- `-n, --number_chunks` *(optional)*: Number of similar chunks to retrieve (default: `1`).
- `-m, --embedding_model`: Embedding model to use (choices: `text-embedding-3-small`, `text-embedding-3-large`, `text-embedding-ada-002`).

## Output

The script returns a JSON-formatted list of matching text chunks sorted by similarity.

## Example

```bash
python main.py -q "Explain vector databases" -n 3 -m "text-embedding-3-small"
```
## License
This project is provided as-is without warranty. You are free to modify and distribute under your own terms.

## Author
- Jaro Cech (jaro@nowapp.cz)


