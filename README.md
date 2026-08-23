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

🔌 API

The trained model is exposed through a Flask REST API.

Endpoint
                                                                          
                                                                          POST /predict
Local URL
                                                                          
                                                                          http://localhost:9698/predict
Request

## 🔌 API

The trained model is exposed through a Flask REST API.

Endpoint
POST /predict
Local URL
http://localhost:9698/predict
Request

The API accepts JSON containing the flood-risk features.

Example:

                {
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
             
             }
### Response

The API returns:

                  {
                        "Flood_Probability": 0.317,
                        "risk_level": "Moderate Flood Risk",
                        "recommendation": "Monitor updates closely.",

### 🐳 CONTAINERIZATION

The application is containerized using Docker to provide a consistent runtime environment.

### Build the Docker image
                                                        
                                                        docker build -t flood-prediction:v1 .
###Run the container

                                                       docker run -d --name flood-api -p 9698:9698 flood-prediction:v1                       

 ## 🧪 Testing the API

A prediction request can be sent using curl:

                                             curl -X POST http://localhost:9698/predict \
                                               -H "Content-Type: application/json" \
                                               -d '{
                                                    "MonsoonIntensity": 5,
                                                    "TopographyDrainage": 4,
                                                     "Deforestation": 5,
                                                     "ClimateChange": 5,
                                                     "DamsQuality": 3,
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
## ☁️ CLOUD DEPLOYMENT

The Flood Prediction API was deployed to the cloud using **Render**. The application is packaged as a Docker container, allowing the same environment used during local development to be used in production.

### Deployment Platform

- **Cloud Platform:** Render
- **Application Framework:** Flask
- **Containerization:** Docker
- **Machine Learning Model:** XGBoost Regressor
- **API Endpoint:** `/predict`

### 🌐 Live Application

The deployed Flood Prediction application is publicly accessible through the following URL:

https://flood-prediction-3eui.onrender.com

The web interface allows users to enter the required flood-related features and submit them to the prediction API.

### 🔌 Production API

The same `/predict` endpoint used during local development is available through the deployed application.

Production endpoint:

https://flood-prediction-3eui.onrender.com/predict

The API receives the environmental, infrastructure, and socio-economic features as JSON and returns the predicted flood probability together with the corresponding risk level and recommended action.

### 🚀 Deployment Process

The application was first containerized using Docker:

    docker build -t flood-prediction:v1 .

The Docker image contains:

- Flask API
- Trained machine learning model
- DictVectorizer
- Python dependencies
- Application files

The containerized application was then deployed to Render as a web service.

Render builds the Docker image and runs the Flask application in the cloud, making the prediction service accessible through a public URL.

### 🔄 Deployment Architecture

    User
      │
      ▼
    Web Interface
      │
      ▼
    Render Cloud
      │
      ▼
    Docker Container
      │
      ▼
    Flask REST API
      │
      ▼
    DictVectorizer
      │
      ▼
    Trained XGBoost Model
      │
      ▼
    Flood Probability
      │
      ▼
    Risk Level & Recommendation

### 🧪 Cloud Testing

After deployment, the API was tested using the public Render URL to verify that the production environment could successfully load the trained model and process prediction requests.

A successful request returns information such as:

    {
        "Flood_Probability": 0.317,
        "risk_level": "Moderate Flood Risk",
        "recommendation": "Monitor updates closely.",
        "emergency_action_required": false,
        "color_code": "yellow"
    }

The cloud deployment makes the Flood Prediction System accessible without requiring users to install Python, the model, or the project dependencies locally.
