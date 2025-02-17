from datetime import datetime
import pandas as pd
import Utils.consultas_mysql as cst
from Utils.functions import config_logging

def run(fecha: datetime, df_load: pd.DataFrame, query: str):
    """
    Loads records into the database using a SQL query file.
    
    Args:
        fecha (datetime): Date of the execution, used for logging.
        df_load (pd.DataFrame): Data to be inserted.
        query (str): Name of the SQL file (without extension) containing the insert query.
    """
    try:
        dia = int(str(fecha).replace('-', '')[:8])
        logger = config_logging(dia)
        logger.info("Starting data load process...")
        sql_file_path = f'./SQL/INSERT/{query}.sql'

        try:
            with open(sql_file_path, encoding='utf-8') as file:
                query_insert = file.read()
            logger.info("Successfully read SQL query file: %s", sql_file_path)
        except FileNotFoundError:
            logger.error("SQL file not found: %s", sql_file_path, exc_info=True)
            raise
        except Exception as e:
            logger.error("Error reading SQL file: %s", e, exc_info=True)
            raise

        try:
            cst.truncate_table(query)
            cst.load_records(df_load, query_insert)
            logger.info("Data successfully loaded into the database.")
        except Exception as e:
            logger.error("Error loading data into the database: %s", e, exc_info=True)
            raise

    except Exception as e:
        logger.critical("Critical failure in data load process: %s", e, exc_info=True)
        raise
