# ─────────────────────────────────────────────────────────────
# Pipeline Constants — Directory Names, URLs, Training Params
# ─────────────────────────────────────────────────────────────

# Root directory for all pipeline artifacts
ARTIFACTS_DIR: str                        = "artifacts"

# ─────────────────────────────────────────────────────────────
# Data Ingestion
# ─────────────────────────────────────────────────────────────
DATA_INGESTION_DIR_NAME             : str = "data_ingestion"                 # ingestion stage folder
DATA_INGESTION_FEATURE_STORE_DIR    : str = "feature_store"                  # raw data storage
DATA_DOWNLOAD_URL                   : str = "https://drive.google.com/file/d/1VJ8fl31MvTpDvA8w9TScMCmuhiwr_ozq/view?usp=sharing"

# ─────────────────────────────────────────────────────────────
# Data Validation
# ─────────────────────────────────────────────────────────────
DATA_VALIDATION_DIR_NAME            : str = "data_validation"                # validation stage folder
DATA_VALIDATION_STATUS_FILE         : str = "status.txt"                     # file to log validation status
DATA_VALIDATION_ALL_REQUIRED_FILES        = ["train", "valid", "data.yaml"]  # expected structure

# ─────────────────────────────────────────────────────────────
# Model Trainer
# ─────────────────────────────────────────────────────────────
MODEL_TRAINER_DIR_NAME              : str = "model_trainer"                  # training stage folder
MODEL_TRAINER_PRETRAINED_WEIGHT_NAME: str = "yolov11.pt"                     # base weights
MODEL_TRAINER_NO_EPOCHS             : int = 1                                # training epochs
MODEL_TRAINER_BATCH_SIZE            : int = 16                               # batch size