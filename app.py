# ─────────────────────────────────────────────────────────────
# Flask App — Sign Language Detection via YOLOv11
# ─────────────────────────────────────────────────────────────

import os
import sys
from flask                                import Flask, request, jsonify, render_template, Response
from flask_cors                           import CORS, cross_origin
from ultralytics                          import YOLO

from sign_lang.pipeline.training_pipeline import TrainPipeline
from sign_lang.utils.main_utils           import decodeImage, encodeImageIntoBase64
from sign_lang.constant.application       import APP_HOST, APP_PORT

app = Flask(__name__)
CORS(app)

# ─────────────────────────────────────────────────────────
# ClientApp — Holds input image filename
# ─────────────────────────────────────────────────────────
class ClientApp:
    def __init__(self):
        self.filename = "inputImage.jpg"

clApp = ClientApp()

# ─────────────────────────────────────────────────────────
# Route: Trigger Training Pipeline
# ─────────────────────────────────────────────────────────
@app.route("/train")
def trainRoute():
    pipeline = TrainPipeline()
    pipeline.run_pipeline()
    return "Training Successful!!"

# ─────────────────────────────────────────────────────────
# Route: Home Page — Serves Frontend UI
# ─────────────────────────────────────────────────────────
@app.route("/")
def home():
    return render_template("index.html")

# ─────────────────────────────────────────────────────────
# Route: Predict from Uploaded Image
# ─────────────────────────────────────────────────────────
@app.route("/predict", methods=['POST', 'GET'])
@cross_origin()
def predictRoute():
    try:
        image           = request.json['image']
        decodeImage(image, clApp.filename)

        # Load trained YOLOv11 model
        model           = YOLO("yolov11/my_model.pt")          # Update path if needed

        # Run inference on uploaded image
        results = model.predict(source=os.path.join("data", clApp.filename), save=True)

        # Encode prediction result
        output_path     = os.path.join("runs", "detect", "predict", clApp.filename)
        opencodedbase64 = encodeImageIntoBase64(output_path)
        result = {"image": opencodedbase64.decode('utf-8')}

        # Cleanup
        os.system("rm -rf runs")

    except ValueError as val:
        print(val)
        return Response("Value not found inside JSON data")
    except KeyError:
        return Response("Incorrect key passed in JSON")
    except Exception as e:
        print(e)
        return Response("Invalid input")

    return jsonify(result)

# ─────────────────────────────────────────────────────────
# Route: Live Camera Detection
# ─────────────────────────────────────────────────────────
@app.route("/live", methods=['GET'])
@cross_origin()
def predictLive():
    try:
        model = YOLO("yolov11/my_model.pt")  # Update path if needed
        model.predict(source=0, show=True)   # Live webcam feed
        os.system("rm -rf runs")
        return "Camera started!!"

    except ValueError as val:
        print(val)
        return Response("Value not found inside JSON data")
    except Exception as e:
        print(e)
        return Response("Camera error")

# ─────────────────────────────────────────────────────────
# App Entry Point
# ─────────────────────────────────────────────────────────
if __name__ == "__main__":
    app.run(host=APP_HOST, port=APP_PORT)