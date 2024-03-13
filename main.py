from src.chicken_disease_CNN.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from src.chicken_disease_CNN.logging import logger
from src.chicken_disease_CNN.exception import CustomExeption
import sys

STAGE_NAME = 'Data Ingestion Stage'

try:
        logger.info(f'{STAGE_NAME} Started')
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f'{STAGE_NAME} Completed')
        
except Exception as e:
        raise CustomExeption(e,sys)  

