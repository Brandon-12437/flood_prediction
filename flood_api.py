import pickle
from flask import Flask
from flask import request
from flask import jsonify

# Load the model and preprocessor
model_file = 'flood_prediction_model.bin'

with open(model_file, 'rb') as f_in:
    dv, model = pickle.load(f_in)

app = Flask('Flood_Prediction')

# NEW HOME ROUTE
@app.route('/', methods=['GET'])
def home():
    return jsonify({
        "message": "Flood Prediction API is running.",
        "usage": "Send POST request to /predict with flood data.",
        "features_required": [
            "MonsoonIntensity", "TopographyDrainage", "RiverManagement",
            "Deforestation", "Urbanization", "ClimateChange", "DamsQuality",
            "Siltation", "AgriculturalPractices", "Encroachments",
            "IneffectiveDisasterPreparedness", "DrainageSystems",
            "CoastalVulnerability", "Landslides", "Watersheds",
            "DeterioratingInfrastructure", "PopulationScore", "WetlandLoss",
            "InadequatePlanning", "PoliticalFactors"
        ]
    })

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get JSON data
        flood_data = request.get_json()
        
        # Transform the data
        X_new = dv.transform([flood_data])
        
        # Make prediction
        predicted_probability = model.predict(X_new)[0]
        
        # Determine risk level and measure
        if predicted_probability >= 0.75:
            risk_level = "Very High Flood Risk"
            measure = "Evacuate to higher ground immediately and follow official orders."
            color = "red"
            emergency = True
        elif predicted_probability >= 0.50:
            risk_level = "High Flood Risk"
            measure = "Prepare to evacuate — move valuables higher and charge devices."
            color = "orange"
            emergency = True
        elif predicted_probability >= 0.25:
            risk_level = "Moderate Flood Risk"
            measure = "Monitor updates closely and have your emergency kit ready."
            color = "yellow"
            emergency = False
        else:
            risk_level = "Low Flood Risk"
            measure = "Stay informed and review your household emergency plan."
            color = "green"
            emergency = False
        
        result = {
            'Flood_Probability': float(predicted_probability),
            'risk_level': risk_level,
            'recommendation': measure,
            'emergency_action_required': emergency,
            'color_code': color
        }
        
        return jsonify(result)
    
    except KeyError as e:
        return jsonify({
            'error': f'Missing required field: {str(e)}',
            'message': 'Please check your input data format'
        }), 400
    
    except Exception as e:
        return jsonify({
            'error': str(e),
            'message': 'Internal server error'
        }), 500

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=9698)