import pandas as pd
from sqlalchemy import create_engine


def save_to_csv(dataframe, filename="products.csv"):
    try:
        dataframe.to_csv(filename, index=False)
        return True
    except Exception as error:
        print(f"Error saving CSV: {error}")
        return False

def save_to_postgresql(
    dataframe,
    table_name="products",
    db_url="postgresql://postgres:ABhi290805.@localhost:5432/products"
):
    try:
        engine = create_engine(db_url)
        dataframe.to_sql(table_name, engine, if_exists="replace", index=False)
        return True
    except Exception as error:
        print(f"Error saving to PostgreSQL: {error}")
        return False