# ─────────────────────────────────────────────────────────────
# Model Trainer — YOLOv11 Training via Ultralytics API
# ─────────────────────────────────────────────────────────────

import os
import sys
from ultralytics                       import YOLO

from sign_lang.logger                  import logging
from sign_lang.exception               import AppException
from sign_lang.entity.config_entity    import ModelTrainerConfig
from sign_lang.entity.artifacts_entity import ModelTrainerArtifact

# ─────────────────────────────────────────────────────────────
# Trains YOLOv11 model using Ultralytics interface
# ─────────────────────────────────────────────────────────────
class ModelTrainer:
    def __init__(self, model_trainer_config: ModelTrainerConfig):
        self.model_trainer_config = model_trainer_config

    # ─────────────────────────────────────────────────────────
    # Entry point for training — returns model artifact
    # ─────────────────────────────────────────────────────────
    def initiate_model_trainer(self) -> ModelTrainerArtifact:
        logging.info("Starting YOLOv11 training")

        try:
            # Load pretrained model
            model = YOLO(self.model_trainer_config.weight_name)

            # Train using data.yaml and config params
            model.train(
                            data="data.yaml",
                            epochs=self.model_trainer_config.no_epochs,
                            batch=self.model_trainer_config.batch_size,
                            imgsz=416,
                            name="yolov11_sign_language",
                            cache=True
                        )

            # Locate best.pt from training output
            best_model_path  = os.path.join("runs", "detect", "yolov11_sign_language", "weights", "best.pt")

            # Save to model_trainer_dir
            os.makedirs(self.model_trainer_config.model_trainer_dir, exist_ok=True)
            
            final_model_path = os.path.join(self.model_trainer_config.model_trainer_dir, "best.pt")
            
            os.system(f"cp {best_model_path} {final_model_path}")

            # Return artifact
            artifact         = ModelTrainerArtifact(trained_model_file_path=final_model_path)
            logging.info(f"Model training completed: {artifact}")
            return artifact

        except Exception as e:
            raise AppException(e, sys)