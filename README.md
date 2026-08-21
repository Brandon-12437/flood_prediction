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
- 
## 📊 Exploratory Data Analysis (EDA)

The dataset used for this project is the flood_data.csv dataset, originally hosted on Kaggle. It contains multiple features relevant to flood prediction, including environmental, infrastructure, and socio-economic indicators.

Dataset: flood_data.csv
Rows: 50,000
Columns: 21
Data Type: Raw dataset
Target: Flood prediction/risk

The dataset contains several factors that can influence flood occurrence and severity, such as monsoon intensity, drainage conditions, deforestation, urbanization, climate change, river management, landslides, wetland loss, population score, and inadequate planning.

## Data Preparation

Before training the machine learning models, the raw dataset was inspected and prepared for modeling. This included:

Checking the dataset structure and data types.
Identifying missing or inconsistent values.
Examining the distribution of the target variable.
Separating the input features from the prediction target.
Splitting the dataset into training, validation, and test sets.
Preparing the features in a format suitable for machine learning algorithms.
Feature Analysis

The project analyzes how different environmental and socio-economic factors contribute to flood risk. Features such as MonsoonIntensity, TopographyDrainage, Deforestation, Urbanization, ClimateChange, DrainageSystems, Landslides, WetlandLoss, and InadequatePlanning are particularly relevant to understanding flood vulnerability.

The prepared dataset was then used to compare different machine learning algorithms and identify a suitable model for deployment through the prediction API.
### Data Visualization




## 🤖 Model Selection & Training

Several machine learning approaches were evaluated during the development of the Flood Prediction System to identify a model that could effectively capture the relationship between environmental, infrastructure, and socio-economic factors and flood risk.

### Models Evaluated

The model selection process included:

Decision Tree Classifier
Random Forest Classifier
XGBoost Classifier

Different hyperparameter configurations were tested during the development process to improve model performance and identify a suitable final model for deployment.

### 🧠 Final Model

After comparing the evaluated approaches, the selected model was trained using the prepared flood dataset and saved for use by the prediction API.

The trained model is serialized and stored as:

flood_prediction_model.bin

The file contains the trained model together with the required data transformation object, allowing the API to load the model and make predictions on new flood-related input data.

🚀 Model Deployment

The serialized model is loaded by flood_api.py, which exposes a Flask REST API through the /predict endpoint.

The API receives flood-related features, transforms the input using the saved data transformer, and generates a flood probability and corresponding risk classification:

Low Flood Risk
Moderate Flood Risk
High Flood Risk
Very High Flood Risk

The prediction service is containerized using Docker and runs on port 9698.




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
