import pandas as pd
from sqlalchemy import create_engine
from time import time
import argparse
import os

def main(params):
    user = params.user
    password = params.password
    host = params.host
    port = params.port
    db = params.db
    table_name = params.table_name
    url = params.url

    parquet_name = 'output.parquet'

    print("Starting data ingestion...")
    start_time = time()  # Start timer

    # Download the PARQUET file
    os.system(f"wget {url} -O {parquet_name}")
    
    # Create a PostgreSQL connection using f-string
    engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{db}')

    # Read the downloaded Parquet file
    df = pd.read_parquet(parquet_name)

    # Upload the DataFrame to the database
    df.to_sql(name=table_name, con=engine, if_exists="replace", index=False)
    
    end_time = time()  # End timer
    elapsed_time = end_time - start_time  # Calculate elapsed time

    print(f"Data successfully ingested into {table_name}")
    print(f"Time taken: {elapsed_time:.2f} seconds")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Ingest PARQUET into PostgreSQL database')
    
    parser.add_argument('--user', required=True, help='PostgreSQL username')
    parser.add_argument('--password', required=True, help='PostgreSQL password')
    parser.add_argument('--host', required=True, help='PostgreSQL host')
    parser.add_argument('--port', required=True, help='PostgreSQL port')
    parser.add_argument('--db', required=True, help='PostgreSQL database name')
    parser.add_argument('--table_name', required=True, help='Target table name')
    parser.add_argument('--url', required=True, help='URL of the PARQUET file')

    args = parser.parse_args()
    main(args)
