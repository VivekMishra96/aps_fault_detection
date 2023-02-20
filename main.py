from Sensor.pipeline.training_pipeline import start_training_pipeline

from Sensor.logger import logging


def main():
    try:
         start_training_pipeline()
        
    except Exception as e:
        logging.error(f"{e}")
        print(e)
        
        
        
if __name__ == "__main__":
    main()