#%% 
import sqlite3
import pandas as pd
import numpy as np
import pytest as pt 
import pyspark as pyspark
# %%
list = np.class
# %%
cursor = connection.cursor()

# %%
#%%
cursor.execute("CREATE TABLE IF NOT EXISTS example (id INTEGER, name TEXT, age INTEGER)")
#%%
cursor.execute("INSERT INTO example VALUES (1, 'alice', 20)")  # 'alice' should be in quotes
cursor.execute("INSERT INTO example VALUES (2, 'bob', 30)")
cursor.execute("INSERT INTO example VALUES (3, 'eve', 40)")
# %%
connection.commit()
# %%
#%%
cursor.execute("SELECT * FROM example")
rows = cursor.fetchall()
for row in rows:
    print(row)
# %%
