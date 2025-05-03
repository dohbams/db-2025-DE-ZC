import pandas as pd
from sqlalchemy import create_engine
from time import time
import argparse
import os

def main(params):
    # parameters needed for database connection and data ingestion 
    user = params.user
    password = params.password
    host = params.host
    port = params.port
    db = params.db
    table_name = params.table_name
    url = params.url
    parquet_name = 'output.parquet'

    # print statement to track start of ingestion
    print("Starting data ingestion...")

    # use the time package to record the start time
    start_time = time()  

    # download the PARQUET file using the wget function from os
    os.system(f"wget {url} -O {parquet_name}")
    
    # create a PostgreSQL connection to our existing database container
    engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{db}')

    # read the downloaded Parquet file
    df = pd.read_parquet(parquet_name)

    # upload the DataFrame to the database
    df.to_sql(name=table_name, con=engine, if_exists="replace", index=False)
    
    # record the end time
    end_time = time()  
    
    # calculate the total time taken
    elapsed_time = end_time - start_time

    # print statement to track if ingestion was successful and the time it took to ingest
    print(f"Data successfully ingested into {table_name}")
    print(f"Time taken: {elapsed_time:.2f} seconds")

# use python main block to parse command-line arguments and execute the script  (we use argparse for this)
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Ingest PARQUET into PostgreSQL database')
    
    parser.add_argument('--user', required=True, help='PostgreSQL username')
    parser.add_argument('--password', required=True, help='PostgreSQL password')
    parser.add_argument('--host', required=True, help='PostgreSQL host')
    parser.add_argument('--port', required=True, help='PostgreSQL port')
    parser.add_argument('--db', required=True, help='PostgreSQL database name')
    parser.add_argument('--table_name', required=True, help='Target table name')
    parser.add_argument('--url', required=True, help='URL of the PARQUET file')

    # parse arguments and execute the main function
    args = parser.parse_args()
    main(args)