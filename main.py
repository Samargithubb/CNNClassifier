from CNNClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from CNNClassifier import logger

STAGE_NAME = "DATA INGESTION STAGE"

try:
    logger.info(f">>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>>>> stage {STAGE_NAME} completed  <<<<<<<<<<<<<\n\nx=========x")

except Exception as e:
    logger.exception(e)
    raise e