import json
import pandas as pd
from sqlalchemy import text
from utils import get_db_engine

def run_extraction():
    engine = get_db_engine()

    with engine.connect() as conn:
        conn.execute(text("CREATE SCHEMA IF NOT EXISTS raw;"))
        conn.commit()

    print("Cargando suscripciones en Postgres...")
    with open("data/subscriptions_mock.json", "r") as f:
        subscriptions_data = json.load(f)
    
    df_subscriptions = pd.DataFrame(subscriptions_data)
    df_subscriptions.to_sql(
        name="raw_subscriptions",
        con=engine,
        schema="raw",
        if_exists="replace",
        index=False
    )

    print("Cargando eventos de clickstream en Postgres...")
    df_events = pd.read_csv("data/user_events_mock.csv")
    df_events.to_sql(
        name="raw_user_events",
        con=engine,
        schema="raw",
        if_exists="replace",
        index=False
    )

    print("¡Extracción y carga cruda completada con éxito!")

if __name__ == "__main__":
    run_extraction()
