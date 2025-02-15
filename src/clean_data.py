"Module to clean data and transform it into structured datasets."
from datetime import datetime
import pandas as pd
from Utils.functions import config_logging, generate_numeric_id

def run(fecha: datetime, df_raw: pd.DataFrame):
    """
    Cleans raw data by generating unique property IDs, formatting user and property data,
    handling missing values, and adjusting data types.

    Args:
        fecha (datetime): Date of the execution, used for logging.
        df_raw (pd.DataFrame): Raw data containing property and user information.

    Returns:
        tuple: Cleaned dataframes (df_users, df_properties).
    """
    try:
        # Initialize logger
        dia = int(str(fecha).replace('-', '')[:8])
        logger = config_logging(dia)
        logger.info("Starting data cleaning process...")

        # Generate unique property IDs
        try:
            df_raw = generate_numeric_id(
                df_raw,
                ['STATE', 'CITY', 'COLONY', 'STREET', 'CODE', 'PRICE', 'PHONE_CONTACT'],
                'PROPERTIE_ID'
            )
            logger.info("Generated unique property IDs.")
        except Exception as e:
            logger.error("Error generating unique property IDs: %s", e, exc_info=True)
            raise

        # Convert types safely
        try:
            df_raw['USER_ID'] = pd.to_numeric(
                df_raw.get('CODE'),
                errors='coerce'
            ).fillna(0).astype(int)

            df_raw['USER_PHONE'] = pd.to_numeric(
                df_raw.get('PHONE_CONTACT'),
                errors='coerce'
            ).fillna(0).astype(int)

            df_raw['PRICE'] = pd.to_numeric(
                df_raw.get('PRICE'),
                errors='coerce'
            ).fillna(0).astype(int)

            logger.info("Converted data types successfully.")
        except Exception as e:
            logger.error("Error converting data types: %s", e, exc_info=True)
            raise

        # Process Users DataFrame
        try:
            df_users = df_raw[['USER_ID', 'MAIL_CONTACT', 'USER_PHONE']].copy()
            df_users.rename(columns={'MAIL_CONTACT': 'USER_MAIL'}, inplace=True)
            logger.info("Users data cleaned and formatted.")
        except KeyError as e:
            logger.error("Missing column in user data: %s", e, exc_info=True)
            raise
        except Exception as e:
            logger.error("Error processing user data: %s", e, exc_info=True)
            raise

        # Process Properties DataFrame
        try:
            df_properties = df_raw[[
                'PROPERTIE_ID', 'STATE', 'CITY', 'COLONY', 'STREET', 'EXTERNAL_NUM', 'USER_ID',
                'TYPE', 'PURPOSE', 'PRICE'
            ]].copy()

            df_properties.fillna({
                'COLONY': '<--->', 
                'STREET': '<--->', 
                'EXTERNAL_NUM': '<--->'
            }, inplace=True)
            logger.info("Properties data cleaned and formatted.")
        except KeyError as e:
            logger.error("Missing column in properties data: %s", e, exc_info=True)
            raise
        except Exception as e:
            logger.error("Error processing properties data: %s", e, exc_info=True)
            raise

        return df_users, df_properties

    except Exception as e:
        logger.critical("Critical failure in data cleaning: %s", e, exc_info=True)
        return None, None
