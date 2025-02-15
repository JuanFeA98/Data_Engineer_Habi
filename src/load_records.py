""
import pandas as pd
import Utils.consultas_mysql as cst

def run():
    """Load records on databse"""

    # Users
    with open('./SQL/INSERT/TBL_DIM_USERS.sql', encoding='utf-8') as file:
        query_insert = file.read()

    df_users = pd.read_csv('./Data/Final/Users_df.csv', sep='|')

    cst.load_records(df_users, query_insert)

    # Properties
    with open('./SQL/INSERT/TBL_FCT_PROPERTIES.sql', encoding='utf-8') as file:
        query_insert = file.read()

    df_properties = pd.read_csv('./Data/Final/Properties_df.csv')

    cst.load_records(df_properties, query_insert)
