from Smart_TextCrunch_Engine.pipeline.data_ingestion import DataIngestionTrainingPipeline
from Smart_TextCrunch_Engine.pipeline.data_validation import DataValidationTrainingPipeline
from Smart_TextCrunch_Engine.pipeline.data_transformation import DataTransformationTrainingPipeline
from Smart_TextCrunch_Engine.logging import logger

STAGE_NAME = "Data Ingestion Stage"
try:
    logger.info(f">>>>> stage {STAGE_NAME} started <<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>> stage {STAGE_NAME} completed <<<<< \n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Data Validation Stage"
try:
    logger.info(f">>>>> stage {STAGE_NAME} started <<<<<")
    data_validation = DataValidationTrainingPipeline()
    data_validation.main()
    logger.info(f">>>>> stage {STAGE_NAME} completed <<<<< \n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Data Transformation Stage"
try:
    logger.info(f">>>>> stage {STAGE_NAME} started <<<<<")
    data_transformation = DataTransformationTrainingPipeline()
    data_transformation.main()
    logger.info(f">>>>> stage {STAGE_NAME} completed <<<<< \n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e

