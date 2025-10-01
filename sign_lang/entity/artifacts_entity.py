# ─────────────────────────────────────────────────────────────
# Artifact Entities — Outputs from Each Pipeline Stage
# ─────────────────────────────────────────────────────────────

from dataclasses import dataclass

# ─────────────────────────────────────────────────────────────
# Data Ingestion Artifact — Stores raw + extracted paths
# ─────────────────────────────────────────────────────────────
@dataclass
class DataIngestionArtifact:
    data_zip_file_path: str         # downloaded zip from Gdrive
    feature_store_path: str         # extracted dataset directory

# ─────────────────────────────────────────────────────────────
# Data Validation Artifact — Status flag for downstream gating
# ─────────────────────────────────────────────────────────────
@dataclass
class DataValidationArtifact:
    validation_status: bool         # True if structure is valid

# ─────────────────────────────────────────────────────────────
# Model Trainer Artifact — Path to trained YOLOv11 weights
# ─────────────────────────────────────────────────────────────
@dataclass
class ModelTrainerArtifact:
    trained_model_file_path: str    # final .pt file after training
