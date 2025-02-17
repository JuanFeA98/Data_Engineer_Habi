"Module for MYSQL connection"
import os

import pandas as pd
import mysql.connector
from dotenv import load_dotenv

load_dotenv()

# Variables globales
config = {
    "user": os.getenv('user'),
    "password": os.getenv('password'),
    "host": os.getenv('host'),  
    "database": os.getenv('database'),
    "port": os.getenv('port')
}

# Realizamos la conexión
conn = mysql.connector.connect(**config)
cursor = conn.cursor()

def load_records(df, query_insert):
    """Function to load records on database"""
    data = [tuple(row) for row in df.itertuples(index=False, name=None)]
    cursor.executemany(query_insert, data)
    conn.commit()

def get_data(query_get: str):
    """Function to read records from database"""
    cursor.execute(query_get)
    columns = [col[0] for col in cursor.description]  # Obtener nombres de columnas
    results = cursor.fetchall()
    return pd.DataFrame(results, columns=columns)

def truncate_table(table_name: str):
    """Function to truncate tables on database"""
    query_truncate = f"TRUNCATE TABLE {table_name}"
    cursor.execute(query_truncate)
