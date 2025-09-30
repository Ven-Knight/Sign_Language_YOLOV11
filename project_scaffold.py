import os
import logging
from pathlib import Path

# ---------------------------------------------------------
# Logging setup: timestamped output for audit traceability
# ---------------------------------------------------------
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

# ---------------------------------------------------------
# Project name used to scaffold internal package structure
# ---------------------------------------------------------
project_name = "sign_lang"

# ---------------------------------------------------------
# File list to scaffold modular ML pipeline structure
# Each path reflects a specific responsibility in lifecycle
# ---------------------------------------------------------
list_of_files = [
                    # CI/CD and data placeholders
                    ".github/workflows/.gitkeep",                           # Ensures Git tracks empty workflows folder
                    "data/.gitkeep",                                        # Placeholder for raw data ingestion

                    # Core package initializer
                    f"{project_name}/__init__.py",

                    # Component logic: ingestion, validation, training
                    f"{project_name}/components/__init__.py",
                    f"{project_name}/components/data_ingestion.py",
                    f"{project_name}/components/data_validation.py",
                    f"{project_name}/components/model_trainer.py",

                    # Constants for pipeline config and application metadata
                    f"{project_name}/constant/__init__.py",
                    f"{project_name}/constant/training_pipeline/__init__.py",
                    f"{project_name}/constant/application.py",

                    # Entity definitions for config and artifact tracking
                    f"{project_name}/entity/config_entity.py",
                    f"{project_name}/entity/artifacts_entity.py",

                    # Custom exception and logging hooks
                    f"{project_name}/exception/__init__.py",
                    f"{project_name}/logger/__init__.py",

                    # Pipeline orchestration logic
                    f"{project_name}/pipeline/__init__.py",
                    f"{project_name}/pipeline/training_pipeline.py",

                    # Shared utility functions
                    f"{project_name}/utils/__init__.py",
                    f"{project_name}/utils/main_utils.py",

                    # Research and experimentation notebook
                    "reseach/trials.ipynb",

                    # Frontend template for web interface
                    "templates/index.html",

                    # Entry point for API or web app
                    "app.py",

                    # Containerization and dependency management
                    "Dockerfile",
                    "requirements.txt",
                    "setup.py",
                ]

# ---------------------------------------------------------
# Scaffold directories and files with reproducibility checks
# ---------------------------------------------------------
for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    # ---------------------------------------------------------
    # Create parent directory if it doesn't exist
    # ---------------------------------------------------------
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for the file {filename}")

    # ---------------------------------------------------------
    # Create empty file only if missing or zero-byte
    # ---------------------------------------------------------
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass  # Empty placeholder for future implementation
        logging.info(f"Creating empty file: {filename}")
    else:
        logging.info(f"{filename} is already created")