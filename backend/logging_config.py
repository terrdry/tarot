import logging
import logging.config

def setup_logging(default_level=logging.WARN, filename="tarot.log"):
    logging.basicConfig(level=default_level,
                        filename=filename,
                        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    
    # Add more configuration if needed
    # logging.config.fileConfig('logging.conf')  # Optionally load from a config file
