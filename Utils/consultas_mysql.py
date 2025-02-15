"Module for MYSQL connection"
import os

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
