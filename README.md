# FLOOD PREDICTION PROJECT
### Problem Description
Flooding is one of the most destructive natural hazards, causing loss of life, damage to infrastructure, displacement of communities, and significant economic losses.

### The Challenge

Flood risk is influenced by multiple interacting factors, including rainfall intensity, drainage conditions, deforestation, urbanization, infrastructure quality, and environmental degradation.

Traditional flood-risk assessment can be difficult to perform quickly when many variables need to be considered simultaneously.

### The Solution

This project develops a machine learning system that analyzes multiple environmental and infrastructure factors and produces a **flood probability and risk classification**.

The API provides:

- Flood probability
- Risk level
- Recommended action
# 📊 Exploratory Data Analysis (EDA)



### HOW TO RUN THE PROJECT
Install Dependencies

                                                             pip install -r requirements.txt
 Run API Locally
                                                             
                                                              python flood_api.py
Run with Docker
                                                              
                                                              docker build -t flood-prediction:v1 .   
                                                              docker run -d --name flood-api -p 9698:9698 flood-prediction:v1

Sending prediction requests to API

Check if Docker is running
                                                               
                                                               docker ps
Send a prediction request

                                                        curl -X POST http://localhost:9698/predict \
                                                          -H "Content-Type: application/json" \
                                                          -d '{
                                                             "MonsoonIntensity": 5,
                                                             "TopographyDrainage": 4,
                                                             "RiverManagement": 3,
                                                             "Deforestation": 5,
                                                             "Urbanization": 4,
                                                             "ClimateChange": 5,
                                                             "DamsQuality": 3,
                                                             "Siltation": 4,
                                                             "AgriculturalPractices": 3,
                                                             "Encroachments": 2,
                                                             "DrainageSystems": 4,
                                                             "CoastalVulnerability": 3,
                                                             "Landslides": 2,
                                                             "Watersheds": 4,
                                                             "DeterioratingInfrastructure": 3,
                                                             "PopulationScore": 5,
                                                             "WetlandLoss": 3,
                                                             "InadequatePlanning": 4,
                                                             "PoliticalFactors": 2
                                                           }'
