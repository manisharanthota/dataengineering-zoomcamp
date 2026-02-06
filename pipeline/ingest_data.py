#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


prefix = 'https://github.com/DataTalksClub/nyc-tlc-data/releases/download/yellow/'
url = f'{prefix}/yellow_tripdata_2021-01.csv.gz'
url


# In[3]:


df = pd.read_csv(url)


# In[4]:


df.dtypes


# In[5]:


df.shape


# In[6]:


dtype = {
    "VendorID": "Int64",
    "passenger_count": "Int64",
    "trip_distance": "float64",
    "RatecodeID": "Int64",
    "store_and_fwd_flag": "string",
    "PULocationID": "Int64",
    "DOLocationID": "Int64",
    "payment_type": "Int64",
    "fare_amount": "float64",
    "extra": "float64",
    "mta_tax": "float64",
    "tip_amount": "float64",
    "tolls_amount": "float64",
    "improvement_surcharge": "float64",
    "total_amount": "float64",
    "congestion_surcharge": "float64"
}

parse_dates = [
    "tpep_pickup_datetime",
    "tpep_dropoff_datetime"
]

df = pd.read_csv(
    url,
    dtype=dtype,
    parse_dates=parse_dates
)


# In[ ]:





# In[7]:


df['tpep_pickup_datetime']


# In[8]:


get_ipython().system('uv add sqlalchemy psycopg2-binary')


# In[9]:


from sqlalchemy import create_engine
engine = create_engine('postgresql://root:root@localhost:5432/ny_taxi')


# In[10]:


df.head(n=0).to_sql(name='yellow_taxi_data', con=engine, if_exists='replace')


# In[18]:


df_iter  = pd.read_csv(
    url,
    dtype=dtype,
    parse_dates=parse_dates,
    iterator = True,
    chunksize = 100000
)


# In[12]:


for df_chunk in df_iter:
    print(len(df_chunk))


# In[13]:


get_ipython().system('uv add tqdm')


# In[19]:


first = True

for df_chunk in df_iter:

    if first:
        # Create table schema (no data)
        df_chunk.head(0).to_sql(
            name="yellow_taxi_data",
            con=engine,
            if_exists="replace"
        )
        first = False
        print("Table created")

    # Insert chunk
    df_chunk.to_sql(
        name="yellow_taxi_data",
        con=engine,
        if_exists="append"
    )

    print("Inserted:", len(df_chunk))


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




