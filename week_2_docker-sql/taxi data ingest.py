import pandas as pd
from sqlalchemy import create_engine
from time import time
import argparse

def main(params):

    user = params.user
    password = params.password
    host = params.host
    port = params.port
    db_name = params.db_name
    table_name = params.table_name

    parquet_name = 'output.parquet'

    # download the PARQUET


    #  create a postgres connection
    engine =  create_engine('postgresql://{user}:{password}@{host}:{port}/{db_name}')

    #  load the data
    df = pd.read_parquet({parquet_name})

    # check conneection
    # engine.connect()

    #  use pandas to extract schema from loaded data
    # schema = pd.io.sql.get_schema(df, "yellow_taxi_data", con= engine)

    # Upload the full DataFrame at once
    df.to_sql(name={table_name}, con=engine, if_exists="append", index=False)

    

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
                        prog='ingester',
                        description='Ingest PARQUET into pg database',
                        epilog='Welp')
    
    parser.add_argument('user', help='username for postgres database')
    parser.add_argument('password', help='password for postgres database')
    parser.add_argument('host', help='host for postgres database')
    parser.add_argument('port', help='port for postgres database')
    parser.add_argument('db_name', help='database name for postgres database')
    parser.add_argument('table_name', help='table name where we will ingest data in postgres')      
    parser.add_argument('url', help='url of the PARQUET file')

    args = parser.parse_args()
    main(args)


# #  load the data
# df = pd.read_parquet("yellow_tripdata_2024-01.parquet")

# #  create a postgres connection
# engine =  create_engine('postgresql://root:root@localhost:5432/ny_taxi_db')

# # check conneection
# engine.connect()

# #  use pandas to extract schema from loaded data
# schema = pd.io.sql.get_schema(df, "yellow_taxi_data", con= engine)

# # Upload the full DataFrame at once
# df.to_sql("yellow_taxi_data", con=engine, if_exists="append", index=False)
