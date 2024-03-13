import sys
from src.chicken_disease_CNN.exception import CustomExeption
from src.chicken_disease_CNN.config.configuration import ConfigurationManager
from src.chicken_disease_CNN.components.data_ingestion import DataIngestion
from src.chicken_disease_CNN.logging import logger


STAGE_NAME = 'Data Ingestion Stage'

class DataIngestionTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            config = ConfigurationManager()
            data_ingestion_config = config.get_data_ingestion_config()
            data_ingestion = DataIngestion(config=data_ingestion_config)
            data_ingestion.download_file()
            data_ingestion.extract_zip_file()
            
        except Exception as e:
            raise CustomExeption(e,sys)
        

if __name__ == '__main__':
    try:
        logger.info(f'{STAGE_NAME} Started')
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f'{STAGE_NAME} Completed')
        
    except Exception as e:
        raise CustomExeption(e,sys)        