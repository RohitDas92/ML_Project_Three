import sys
from src.chicken_disease_CNN.exception import CustomExeption
from src.chicken_disease_CNN.config.configuration import ConfigurationManager
from src.chicken_disease_CNN.components.prepare_base_model import PrepareBaseModel
from src.chicken_disease_CNN.logging import logger

STAGE_NAME = 'Prepare Base Model Stage'

class PrepareBaseModelPipeline:
    def __init__(self):
        pass

    def main(self):

        try:
            config = ConfigurationManager()
            prepare_base_model_config = config.get_prepare_base_model_cofig()
            prepare_base_model = PrepareBaseModel(config=prepare_base_model_config)
            prepare_base_model.get_base_model()
            prepare_base_model.update_base_model()

        except Exception as e:
            raise CustomExeption(e,sys)
        


if __name__ == '__main__':
    try:
        logger.info(f'{STAGE_NAME} Started')
        obj = PrepareBaseModelPipeline()
        obj.main()
        logger.info(f'{STAGE_NAME} Completed')
        
    except Exception as e:
        raise CustomExeption(e,sys)