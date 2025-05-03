import pandas as pd
from sqlalchemy import create_engine
from time import time
import argparse
import os
import requests

def main(params):

    # define parameters
    user = params.user
    password = params.password
    host = params.host
    port = params.port
    db = params.db
    table_name = params.table_name
    url = params.url

    parquet_name = 'output.parquet'

    # download the PARQUET
    os.system(f"wget {url} -O {parquet_name}")

    #  create a postgres connection
    engine =  create_engine('postgresql://{user}:{password}@{host}:{port}/{db}')

    #  load the data
    df = pd.read_parquet({parquet_name})

    # Upload the full DataFrame at once to the db
    df.to_sql(name={table_name}, con=engine, if_exists="append", index=False)
    

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Ingest PARQUET into pg database')
    
    parser.add_argument('--user', help='username for postgres database')
    parser.add_argument('--password', help='password for postgres database')
    parser.add_argument('--host', help='host for postgres database')
    parser.add_argument('--port', help='port for postgres database')
    parser.add_argument('--db', help='database name for postgres database')
    parser.add_argument('--table_name', help='table name where we will ingest data in postgres')      
    parser.add_argument('--url', help='url of the PARQUET file')

    args = parser.parse_args()
    main(args)