import os
from sqlalchemy import create_engine
from dotenv import load_dotenv

load_dotenv()

def get_db_engine():
    user = os.getenv("POSTGRES_USER", "data_engineer")
    password = os.getenv("POSTGRES_PASSWORD", "secure_password123")
    host = os.getenv("POSTGRES_HOST", "localhost")
    port = os.getenv("POSTGRES_PORT", "5432")
    db = os.getenv("POSTGRES_DB", "saas_analytics")

    # Especificamos explícitamente postgresql+psycopg2
    connection_string = f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{db}"
    return create_engine(connection_string)

    