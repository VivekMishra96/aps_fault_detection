from Sensor.logger import logging
from Sensor.exception import SensorException
from Sensor.utils import get_collection_as_dataframe
import sys,os
from Sensor.entity import config_entity
from Sensor.components.data_ingestion import DataIngestion




def start_training_pipeline():
    try:
        training_pipeline_config = config_entity.TrainingPipelineConfig()

        #data ingestion
        data_ingestion_config  = config_entity.DataIngestionConfig(training_pipeline_config=training_pipeline_config)
        print(data_ingestion_config.to_dict())
        data_ingestion = DataIngestion(data_ingestion_config=data_ingestion_config)
        data_ingestion_artifact = data_ingestion.initiate_data_ingestion()
        
    except Exception as e:
     raise SensorException(e, sys)