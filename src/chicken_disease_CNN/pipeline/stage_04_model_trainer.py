import sys
from src.chicken_disease_CNN.exception import CustomExeption
from src.chicken_disease_CNN.components.model_trainer import Training
from src.chicken_disease_CNN.components.prepare_callback import PrepareCallback
from src.chicken_disease_CNN.config.configuration import ConfigurationManager
from src.chicken_disease_CNN.logging import logger

STAGE_NAME = 'Prepare Callback and Model Training Stage'

class ModelTrainingPipeline:
    def __init__(self):
        pass

    def main(self):

        try:
            config = ConfigurationManager()
            prepare_callbacks_config = config.get_prepare_callbacks_config()
            prepare_callbacks = PrepareCallback(config=prepare_callbacks_config)
            callback_list = prepare_callbacks.get_tb_ckpt_callbacks()

            training_config = config.get_training_config()

            training = Training(config=training_config)
            training.get_base_model()
            training.train_valid_generator()
            training.train(callback_list=callback_list)

        except Exception as e:
            raise CustomExeption(e,sys)
        
if __name__ == '__main__':
    try:
        logger.info(f'{STAGE_NAME} Started')
        obj = ModelTrainingPipeline()
        obj.main()
        logger.info(f'{STAGE_NAME} Completed')
        
    except Exception as e:
        raise CustomExeption(e,sys)        