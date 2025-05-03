# %%
import pandas as pd

# %%
df = pd.read_parquet("yellow_tripdata_2024-01.parquet")


# %%
df.head(10)

# %%
from sqlalchemy import create_engine

# %%
engine =  create_engine('postgresql://root:root@localhost:5432/ny_taxi_db')

# %%
engine.connect()

# %%
schema = pd.io.sql.get_schema(df, "yellow_taxi_data", con= engine)

# %%
print(schema)

# %%
# Upload the full DataFrame at once
df.to_sql("yellow_taxi_data", con=engine, if_exists="append", index=False)

# %%



