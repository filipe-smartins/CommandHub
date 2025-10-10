from os import environ, path
from pathlib import Path
from dotenv import load_dotenv

env_file = path.join(path.dirname(__file__), '.env')

if path.exists(env_file):
    load_dotenv(env_file)
else:
    raise FileNotFoundError(
        'File settings/.env was not found. Please implement and configure your .env file.'
    )

base_dir = Path(__file__).resolve().parent.parent

name = environ.get('NAME')

usuario = environ.get('username')
