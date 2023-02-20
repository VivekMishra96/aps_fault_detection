from Sensor.logger import logging
from Sensor.exception import SensorException
from Sensor.utils import get_collection_as_dataframe
import sys,os
from Sensor.entity import config_entity
from Sensor.components.data_ingestion import DataIngestion
from Sensor.components.data_validation import DataValidation
#from Sensor.components.data_transformation import DataTransformation
#from Sensor.components.model_trainer import ModelTrainer
#from Sensor.components.model_evaluation import ModelEvaluation
#from Sensor.components.model_pusher import ModelPusher


def start_training_pipeline():
    try:
        training_pipeline_config = config_entity.TrainingPipelineConfig()

        #data ingestion
        data_ingestion_config  = config_entity.DataIngestionConfig(training_pipeline_config=training_pipeline_config)
        print(data_ingestion_config.to_dict())
        data_ingestion = DataIngestion(data_ingestion_config=data_ingestion_config)
        data_ingestion_artifact = data_ingestion.initiate_data_ingestion()
        
        #data validation
        data_validation_config = config_entity.DataValidationConfig(training_pipeline_config=training_pipeline_config)
        data_validation = DataValidation(data_validation_config=data_validation_config,
                        data_ingestion_artifact=data_ingestion_artifact)

        data_validation_artifact = data_validation.initiate_data_validation()

        

        
    except Exception as e:
        raise SensorException(e, sys)