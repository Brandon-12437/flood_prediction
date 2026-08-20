# FLOOD PREDICTION PROJECT
### Problem Description
This project develops a machine learning system for predicting flood risk using environmental, infrastructure, climate, and geographical factors. The system provides a flood probability and corresponding risk level to support early awareness and decision-making.
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
