import os
import sys
import logging

logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

logs_dir = 'logs'
logfile_path = os.path.join(logs_dir,'running_logs.log')
os.makedirs(logs_dir,exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format=logging_str,
    handlers=[
        logging.FileHandler(logfile_path),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger('mlProjectLogger')