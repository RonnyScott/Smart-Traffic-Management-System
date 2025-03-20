from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from models.car_detection import detect_cars
from traffic_logic import control_traffic_signal

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/detect", methods=["POST"])
def detect():
    image = request.files["image"]
    image_path = f"dataset/{image.filename}"
    image.save(image_path)

    detected_objects = detect_cars(image_path)
    car_count = len(detected_objects)

    return jsonify({"car_count": car_count})

@app.route("/traffic_signal", methods=["GET"])
def traffic_signal():
    car_count_lane1 = request.args.get("lane1", type=int)
    car_count_lane2 = request.args.get("lane2", type=int)

    signal_status = control_traffic_signal(car_count_lane1, car_count_lane2)
    return jsonify({"signal_status": signal_status})

if __name__ == "__main__":
    app.run(debug=True)
