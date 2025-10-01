# ─────────────────────────────────────────────────────────────
# Data Ingestion Component — Download + Extract Dataset
# ─────────────────────────────────────────────────────────────

import os
import sys
import zipfile
import gdown

from sign_lang.logger                  import logging
from sign_lang.exception               import AppException
from sign_lang.entity.config_entity    import DataIngestionConfig
from sign_lang.entity.artifacts_entity import DataIngestionArtifact

# ─────────────────────────────────────────────────────────────
# Handles dataset download and extraction from Roboflow/Drive
# ─────────────────────────────────────────────────────────────
class DataIngestion:
    def __init__(self, data_ingestion_config: DataIngestionConfig = DataIngestionConfig()):
        try:
            self.data_ingestion_config = data_ingestion_config
        except Exception as e:
            raise AppException(e, sys)

    # ─────────────────────────────────────────────────────────
    # Download dataset zip from Google Drive
    # ─────────────────────────────────────────────────────────
    def download_data(self) -> str:
        try:
            dataset_url      = self.data_ingestion_config.data_download_url
            zip_download_dir = self.data_ingestion_config.data_ingestion_dir
            
            os.makedirs(zip_download_dir, exist_ok=True)

            zip_file_path    = os.path.join(zip_download_dir, "data.zip")
            logging.info(f"Downloading data from {dataset_url} into {zip_file_path}")

            file_id          = dataset_url.split("/")[-2]
            gdown.download(f"https://drive.google.com/uc?/export=download&id={file_id}", zip_file_path)

            logging.info(f"Download complete: {zip_file_path}")
            return zip_file_path

        except Exception as e:
            raise AppException(e, sys)

    # ─────────────────────────────────────────────────────────
    # Extract zip file into feature store directory
    # ─────────────────────────────────────────────────────────
    def extract_zip_file(self, zip_file_path: str) -> str:
        try:
            feature_store_path = self.data_ingestion_config.feature_store_file_path
            
            os.makedirs(feature_store_path, exist_ok=True)

            with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
                zip_ref.extractall(feature_store_path)

            logging.info(f"Extracted {zip_file_path} into {feature_store_path}")
            return feature_store_path

        except Exception as e:
            raise AppException(e, sys)

    # ─────────────────────────────────────────────────────────
    # Orchestrates download + extraction and returns artifact
    # ─────────────────────────────────────────────────────────
    def initiate_data_ingestion(self) -> DataIngestionArtifact:
        logging.info("Starting data ingestion pipeline")

        try:
            zip_file_path      = self.download_data()
            feature_store_path = self.extract_zip_file(zip_file_path)

            artifact           = DataIngestionArtifact(
                                                        data_zip_file_path = zip_file_path,
                                                        feature_store_path = feature_store_path
                                                      )

            logging.info(f"Data ingestion completed: {artifact}")
            return artifact

        except Exception as e:
            raise AppException(e, sys)