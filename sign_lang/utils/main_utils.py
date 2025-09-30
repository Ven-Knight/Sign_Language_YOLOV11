# ─────────────────────────────────────────────────────────────
# Utility Functions — YAML I/O + Base64 Encoding/Decoding
# ─────────────────────────────────────────────────────────────

import os
import sys
import yaml
import base64

from sign_lang.exception import AppException
from sign_lang.logger    import logging

# ─────────────────────────────────────────────────────────────
# Read YAML file and return as dict
# ─────────────────────────────────────────────────────────────
def read_yaml_file(file_path: str) -> dict:
    try:
        with open(file_path, "rb") as yaml_file:
            logging.info("YAML file read successfully")
            return yaml.safe_load(yaml_file)
    except Exception as e:
        raise AppException(e, sys) from e

# ─────────────────────────────────────────────────────────────
# Write content to YAML file (optionally replace if exists)
# ─────────────────────────────────────────────────────────────
def write_yaml_file(file_path: str, content: object, replace: bool = False) -> None:
    try:
        if replace and os.path.exists(file_path):
            os.remove(file_path)

        os.makedirs(os.path.dirname(file_path), exist_ok=True)

        with open(file_path, "w") as file:
            yaml.dump(content, file)
            logging.info("YAML file written successfully")
    except Exception as e:
        raise AppException(e, sys)

# ─────────────────────────────────────────────────────────────
# Decode base64 string and save as image
# ─────────────────────────────────────────────────────────────
def decodeImage(imgstring: str, fileName: str) -> None:
    imgdata = base64.b64decode(imgstring)

    with open(os.path.join("data", fileName), 'wb') as f:
        f.write(imgdata)

# ─────────────────────────────────────────────────────────────
# Encode image file into base64 string
# ─────────────────────────────────────────────────────────────
def encodeImageIntoBase64(croppedImagePath: str) -> bytes:
    with open(croppedImagePath, "rb") as f:
        return base64.b64encode(f.read())