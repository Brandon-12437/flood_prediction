import pickle
from flask import Flask, request, jsonify
from flask import render_template
model_file = "flood_prediction_model.bin"

with open(model_file, "rb") as f_in:
    dv, model = pickle.load(f_in)

app = Flask("Flood_Prediction")


@app.route("/")
def index():
    return render_template("index.html")
    

@app.route("/predict", methods=["POST"])
def predict():
    try:
        flood_data = request.get_json()

        X_new = dv.transform([flood_data])

        predicted_probability = model.predict(X_new)[0]

        if predicted_probability >= 0.75:
            risk_level = "Very High Flood Risk"
            measure = "Evacuate to higher ground immediately."
            color = "red"
            emergency = True
        elif predicted_probability >= 0.50:
            risk_level = "High Flood Risk"
            measure = "Prepare to evacuate."
            color = "orange"
            emergency = True
        elif predicted_probability >= 0.25:
            risk_level = "Moderate Flood Risk"
            measure = "Monitor updates closely."
            color = "yellow"
            emergency = False
        else:
            risk_level = "Low Flood Risk"
            measure = "Stay informed."
            color = "green"
            emergency = False

        return jsonify({
            "Flood_Probability": float(predicted_probability),
            "risk_level": risk_level,
            "recommendation": measure,
            "emergency_action_required": emergency,
            "color_code": color
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9698)