from sensor.logger import logging
from sensor.exception import SensorException
from sensor.utils import get_collection_as_dataframe
import sys,os


if __name__=="__main__":
    try:
        get_collection_as_dataframe(database_name="APS", collection_name = "sensor_training_dataset")
    except Exception as e:
        print(e)