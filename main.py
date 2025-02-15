"Entry point"
from datetime import datetime

from Utils.functions import config_logging
from src import load_records

# Variables Globales
fecha = datetime.now()

DAY = int(str(fecha).replace('-', '')[:8])

# Función principal
def main():
    """General logic"""

    logger = config_logging(DAY)
    logger.info('Empieza la ejecución')

    load_records.run()

# Entry Point
if __name__ == '__main__':
    main()
