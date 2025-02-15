"""Entry point"""
from datetime import datetime

from Utils.functions import config_logging
from src import read_data, clean_data, load_records

# Variables Globales
fecha = datetime.now()
dia = int(str(fecha).replace('-', '')[:8])

# Función principal
def main():
    """General logic"""
    logger = config_logging(dia, append=False)
    logger.info('The execution begins')

    try:
        df_raw = read_data.run(fecha)
        if df_raw is None:
            logger.error("Error reading data. Terminating execution.")
            return
    except Exception as e:
        logger.critical("Data reading failed: %s", e, exc_info=True)
        return

    try:
        df_users, df_properties = clean_data.run(fecha, df_raw)
        if df_users is None or df_properties is None:
            logger.error("Error in data cleaning. Terminating execution.")
            return
    except Exception as e:
        logger.critical("Data cleansing failed: %s", e, exc_info=True)
        return

    try:
        load_records.run(fecha, df_users, 'TBL_DIM_USERS')
        load_records.run(fecha, df_properties, 'TBL_FCT_PROPERTIES')
        logger.info("Data upload completed successfully.")
    except Exception as e:
        logger.critical("Data loading failed: %s", e, exc_info=True)
        return

# Entry Point
if __name__ == '__main__':
    main()
