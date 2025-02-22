from flask import Flask, request, jsonify
from flask_cors import CORS
from PIL import Image
import io
import torch
import torch.nn as nn
import torch.nn.functional as F
import numpy as np

app = Flask(__name__)
CORS(app)


class SimpleCNN(nn.Module):
    def __init__(self):
        super(SimpleCNN, self).__init__()
        self.conv1 = nn.Conv2d(3, 16, kernel_size=3, padding=1)
        self.conv2 = nn.Conv2d(16, 32, kernel_size=3, padding=1)
        self.fc1 = nn.Linear(32 * 64 * 64, 128)
        self.fc2 = nn.Linear(128, 10)

    def forward(self, x):
        x = F.relu(self.conv1(x))
        x = F.max_pool2d(x, 2)
        x = F.relu(self.conv2(x))
        x = F.max_pool2d(x, 2)
        x = x.view(-1, 32 * 64 * 64)
        x = F.relu(self.fc1(x))
        x = self.fc2(x)
        return F.softmax(x, dim=1)


def load_model():
    model = SimpleCNN()
    model.load_state_dict(torch.load("simple_cnn_model.pth"))
    model.eval()
    return model


def tensor_to_float(num):
    return round(float(num), 3)


try:
    model = load_model()
except Exception as e:
    print(f"Error loading model: {e}")
    model = None


@app.route("/analyse", methods=["POST"])
def analyse_image():
    if model is None:
        return jsonify({"error": "Model not loaded"}), 500

    if "image" not in request.files:
        return jsonify({"error": "No image provided"}), 400

    file = request.files["image"]
    if not file.filename:
        return jsonify({"error": "Empty file provided"}), 400

    try:
        image_data = file.read()

        with Image.open(io.BytesIO(image_data)) as img:
            reshape_image = img.resize((256, 256))
            model_input = (
                torch.tensor(np.array(reshape_image))
                .permute(2, 0, 1)
                .unsqueeze(0)
                .float()
                / 255.0
            )
            model_output = model(model_input)[0]
            (
                aze_passport,
                est_id,
                esp_id,
                grc_passport,
                rus_internalpassport,
                srb_passport,
                svk_id,
                lva_passport,
                fin_id,
                alb_id,
            ) = model_output

        return jsonify(
            {
                "aze_passport": tensor_to_float(aze_passport),
                "est_id": tensor_to_float(est_id),
                "esp_id": tensor_to_float(esp_id),
                "grc_passport": tensor_to_float(grc_passport),
                "rus_internalpassport": tensor_to_float(rus_internalpassport),
                "srb_passport": tensor_to_float(srb_passport),
                "svk_id": tensor_to_float(svk_id),
                "lva_passport": tensor_to_float(lva_passport),
                "fin_id": tensor_to_float(fin_id),
                "alb_id": tensor_to_float(alb_id),
            }
        )
    except IOError:
        return jsonify({"error": "Unable to open image file"}), 400
    except Exception as e:
        return jsonify({"error": f"Unexpected error: {str(e)}"}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
