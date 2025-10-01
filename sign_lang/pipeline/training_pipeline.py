# ─────────────────────────────────────────────────────────────
# Training Pipeline — Orchestrates Ingestion, Validation, Training
# ─────────────────────────────────────────────────────────────

import sys
from sign_lang.logger                     import logging
from sign_lang.exception                  import AppException

from sign_lang.components.data_ingestion  import DataIngestion
from sign_lang.components.data_validation import DataValidation
from sign_lang.components.model_trainer   import ModelTrainer

from sign_lang.entity.config_entity       import (
                                                    DataIngestionConfig,
                                                    DataValidationConfig,
                                                    ModelTrainerConfig
                                                 )

from sign_lang.entity.artifacts_entity    import (
                                                    DataIngestionArtifact,
                                                    DataValidationArtifact,
                                                    ModelTrainerArtifact
                                                 )

# ─────────────────────────────────────────────────────────────
# Pipeline Class — Entry Point for All Stages
# ─────────────────────────────────────────────────────────────
class TrainPipeline:
    def __init__(self):
        self.data_ingestion_config  = DataIngestionConfig()
        self.data_validation_config = DataValidationConfig()
        self.model_trainer_config   = ModelTrainerConfig()

    # ─────────────────────────────────────────────────────────
    # Stage 1 — Data Ingestion
    # ─────────────────────────────────────────────────────────
    def start_data_ingestion(self) -> DataIngestionArtifact:
        try:
            logging.info("Starting data ingestion")
            ingestion   = DataIngestion(self.data_ingestion_config)
            artifact    = ingestion.initiate_data_ingestion()
            logging.info(f"Data ingestion completed: {artifact}")
            return artifact
        except Exception as e:
            raise AppException(e, sys)

    # ─────────────────────────────────────────────────────────
    # Stage 2 — Data Validation
    # ─────────────────────────────────────────────────────────
    def start_data_validation(self, artifact: DataIngestionArtifact) -> DataValidationArtifact:
        try:
            logging.info("Starting data validation")
            validation  = DataValidation(
                                            data_ingestion_artifact = artifact,
                                            data_validation_config  = self.data_validation_config
                                        )
            result      = validation.initiate_data_validation()
            logging.info(f"Validation result: {result}")
            return result
        except Exception as e:
            raise AppException(e, sys)

    # ─────────────────────────────────────────────────────────
    # Stage 3 — Model Training
    # ─────────────────────────────────────────────────────────
    def start_model_trainer(self) -> ModelTrainerArtifact:
        try:
            logging.info("Starting model training")
            trainer     = ModelTrainer(self.model_trainer_config)
            artifact    = trainer.initiate_model_trainer()
            logging.info(f"Model training completed: {artifact}")
            return artifact
        except Exception as e:
            raise AppException(e, sys)

    # ─────────────────────────────────────────────────────────
    # Pipeline Runner — Executes All Stages Sequentially
    # ─────────────────────────────────────────────────────────
    def run_pipeline(self) -> None:
        try:
            ingestion_artifact  = self.start_data_ingestion()
            validation_artifact = self.start_data_validation(ingestion_artifact)

            if validation_artifact.validation_status:
                self.start_model_trainer()
            else:
                raise Exception("Data validation failed: incorrect format")

        except Exception as e:
            raise AppException(e, sys)