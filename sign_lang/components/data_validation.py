# ─────────────────────────────────────────────────────────────
# Data Validation Component — Structure Check + Status Logging
# ─────────────────────────────────────────────────────────────

import os
import sys
import shutil

from sign_lang.logger                  import logging
from sign_lang.exception               import AppException
from sign_lang.entity.config_entity    import DataValidationConfig
from sign_lang.entity.artifacts_entity import (
                                                DataIngestionArtifact,
                                                DataValidationArtifact
                                              )

# ─────────────────────────────────────────────────────────────
# Validates expected files in feature store directory
# ─────────────────────────────────────────────────────────────
class DataValidation:
    def __init__(
                    self,
                    data_ingestion_artifact : DataIngestionArtifact,
                    data_validation_config  : DataValidationConfig,
                ):
        try:
            self.data_ingestion_artifact    = data_ingestion_artifact
            self.data_validation_config     = data_validation_config
        except Exception as e:
            raise AppException(e, sys)

    # ─────────────────────────────────────────────────────────
    # Check if all required files exist in extracted dataset
    # ─────────────────────────────────────────────────────────
    def validate_all_files_exist(self) -> bool:
        try:
            os.makedirs(self.data_validation_config.data_validation_dir, exist_ok=True)
            extracted_files   = os.listdir(self.data_ingestion_artifact.feature_store_path)

            # Ensure all required files are present
            missing_files     = [
                                    file for file in self.data_validation_config.required_file_list
                                    if file not in extracted_files
                                ]

            validation_status = len(missing_files) == 0

            # Log status to status.txt
            with open(self.data_validation_config.valid_status_file_dir, 'w') as f:
                f.write(f"Validation status: {validation_status}")

            return validation_status

        except Exception as e:
            raise AppException(e, sys)

    # ─────────────────────────────────────────────────────────
    # Orchestrates validation and returns artifact
    # ─────────────────────────────────────────────────────────
    def initiate_data_validation(self) -> DataValidationArtifact:
        logging.info("Starting data validation")

        try:
            status   = self.validate_all_files_exist()
            artifact = DataValidationArtifact(validation_status = status)

            logging.info(f"Validation completed: {artifact}")

            # Optionally copy zip file to working directory for traceability
            if status:
                shutil.copy(self.data_ingestion_artifact.data_zip_file_path, os.getcwd())

            return artifact

        except Exception as e:
            raise AppException(e, sys)