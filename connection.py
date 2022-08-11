from sqlalchemy import create_engine


def get_connection():
    engine = create_engine("postgresql+psycopg2://saif:mohamed98@localhost:5432/data")
    connection = engine.connect()
    try:
        yield from (engine, connection)
    finally:
        connection.close()
