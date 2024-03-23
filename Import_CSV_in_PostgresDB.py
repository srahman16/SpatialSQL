'''
Title: Import a CSV file to public schema of your postgres database
Author: Shahriar Rahman
Email: shahriar.env12@gmail.com
@Credit: please acknowledge/provide credits if this script is useful for you. Thanks!
'''

import pandas as pd
from sqlalchemy import create_engine
db_connection_url = "postgresql://username:password@localhost:5432/yourdatabase" #username, password and yourdatabase
engine = create_engine(db_connection_url)
df = pd.read_csv('C:/location/name.csv') # your csv file
# create a dataframe
for col in df.columns:
    if df[col].dtype == object:
        df[col] = df[col].astype(str)
df.to_sql('env_cons', engine, if_exists='replace', index=False) # use the created dataframe to create a table in the Postgres database
print("Data imported successfully.")
