import requests

url = "https://flood-prediction-3eui.onrender.com/predict"

flood_data = {
    "MonsoonIntensity": 16,
    "TopographyDrainage": 17,
    "RiverManagement": 15,
    "Deforestation": 16,
    "Urbanization": 7,
    "ClimateChange": 18,
    "DamsQuality": 16,
    "Siltation": 7,
    "AgriculturalPractices": 15,
    "Encroachments": 16,
    "IneffectiveDisasterPreparedness": 5,
    "DrainageSystems": 14,
    "CoastalVulnerability": 13,
    "Landslides": 12,
    "Watersheds": 6,
    "DeterioratingInfrastructure": 5,
    "PopulationScore": 7,
    "WetlandLoss": 6,
    "InadequatePlanning": 7,
    "PoliticalFactors": 17
}

response = requests.post(url, json=flood_data).json()
print(" Prediction Results:")
print("=" * 50)
print(f"Flood Probability: {response.get('Flood_Probability', 'N/A'):.3f}")
print(f"Risk Level: {response.get('risk_level', 'N/A')}")
print(f"Recommendation: {response.get('recommendation', 'N/A')}")
print(f"Emergency Required: {response.get('emergency_action_required', 'N/A')}")
print("=" * 50)

# Action based on risk
if response.get('emergency_action_required'):
    print("\n EMERGENCY ACTION REQUIRED!")
    print("Please take immediate precautions.")
else:
    print("\n No emergency action required at this time.")
    print("Stay informed and prepared.")