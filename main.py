from src.chicken_disease_CNN.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from src.chicken_disease_CNN.pipeline.stage_02_prepare_base_model import PrepareBaseModelPipeline
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

STAGE_NAME = 'Prepare Base Model Stage'

try:
        logger.info(f'{STAGE_NAME} Started')
        obj = PrepareBaseModelPipeline()
        obj.main()
        logger.info(f'{STAGE_NAME} Completed')
        
except Exception as e:
        raise CustomExeption(e,sys)
