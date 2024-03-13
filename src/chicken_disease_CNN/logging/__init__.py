import logging
import os
from datetime import datetime

logging_str = '[%(asctime)s :  %(name)s : %(levelname)s : %(module)s : %(lineno)d : %(message)s]'

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
logs_path = os.path.join(os.getcwd(),"logs",LOG_FILE)
os.makedirs(logs_path,exist_ok=True)

LOG_FILE_PATH = os.path.join(logs_path,LOG_FILE)

logging.basicConfig(
    filename = LOG_FILE_PATH,
    format= logging_str,
    level = logging.INFO,

)

logger = logging.getLogger('chicken_disease_CNNLogger')