# FLOOD PREDICTION
## Problem Description

Flooding is a major environmental challenge that can cause loss of
lives, destruction of property, displacement of communities, and
damage to infrastructure.

## The Solution

FloodGuard AI addresses this challenge by using machine learning to
estimate flood probability from 20 flood-related factors.

The system uses an XGBoost regression model trained on historical
flood-related data. The trained model is exposed through a Flask REST
API, allowing applications to send flood-risk data and receive a
prediction.

## Exploratory Data Analysis

Exploratory Data Analysis (EDA) was performed to understand the
structure of the dataset, identify the characteristics of the
variables, and examine relationships between the flood-related
factors and the target variable.

The dataset contains **50,000 records and 21 columns**, consisting of
20 input features and the target variable `FloodProbability`.

### EDA Steps

The analysis included:

- Inspecting the shape and structure of the dataset.
- Checking for missing values.
- Checking for duplicate records.
- Examining data types and feature distributions.
- Calculating descriptive statistics.
- Analyzing the distribution of `FloodProbability`.
- Examining relationships between the input features and flood
  probability.
- Identifying potential patterns and trends in the data.

### Key Observations

The analysis showed that flood probability is influenced by a
combination of environmental, infrastructure, climate, and
community-related factors.

Features such as monsoon intensity, drainage conditions, river
management, deforestation, urbanization, and disaster preparedness
provide useful information for estimating flood risk.

The EDA findings were used to guide the preparation of the data for
machine learning model development.

## DATA VISUALIZATION

   <img width="700" alt="FloodGuard AI Screenshot" src="screenshots/Screenshot%20from%202026-09-14%2009-23-20.png" />

 ## MODEL TRAINING & REPRODUCIBILITY

The flood prediction model was developed using the `flood_data.csv`
dataset containing 50,000 records and 20 input features.

### Model Training

The target variable is `FloodProbability`.

An **XGBoost Regressor** was used to learn the relationship between
the flood-related factors and the target flood probability.

The model was trained using:

- Learning rate: `0.3`
- Maximum depth: `6`
- Minimum child weight: `1`
- Number of estimators: `200`
- Objective: `reg:squarederror`
- Random state: `42`

The dataset was divided into training, validation and testing sets before model
training.

### Model Evaluation

The trained model was evaluated using:

- **R² Score:** `0.99995`
- **MAE:** `0.0000129`
- **RMSE:** `0.000349`

These metrics measure how closely the model's predictions match the
target flood probability values.

### Model Serialization

After training, the `DictVectorizer` and trained XGBoost model were
serialized together using Python's `pickle` module.

                   with open("flood_prediction_model.bin", "wb") as f_out:
                       pickle.dump((dv, xgb_model), f_out, protocol=pickle.HIGHEST_PROTOCOL)
## CONTAINERIZATION

Docker was used to containerize the FloodGuard AI Flask API and its
machine learning dependencies.

The application is packaged into a Docker image so that it can run
consistently across different environments.

### Build the Docker Image

                            docker build -t flood-prediction:v3 .
### Run the container
                            docker run -d --name flood-api -p 9698:9698 flood-prediction:v3
                            
   <img width="700" alt="Docker Build" src="screenshots/Screenshot%20from%202026-09-15%2011-04-18.png" /> 

### Testing Locally with cURL

After starting the Docker container, the API can be tested locally
using cURL.

    ```bash      curl -X POST http://localhost:9698/predict \
                -H "Content-Type: application/json" \
                 -d '{
                "MonsoonIntensity":10,
                "TopographyDrainage":10,
                "RiverManagement":10,
                "Deforestation":10,
                "Urbanization":10,
                "ClimateChange":10,
                "DamsQuality":10,
                "Siltation":10,
                "AgriculturalPractices":10,
                "Encroachments":10,
                "IneffectiveDisasterPreparedness":10,
                "DrainageSystems":10,
                "CoastalVulnerability":10,
                "Landslides":10,
                "Watersheds":10,
                "DeterioratingInfrastructure":10,
                "PopulationScore":10,
                "WetlandLoss":10,
                "InadequatePlanning":10,
                "PoliticalFactors":10
                 }'
<img width="700" alt="Docker Container Running" src="screenshots/Screenshot%20from%202026-09-15%2011-05-57.png" />   

## CLOUD DEPLOYMENT

The FloodGuard AI application is deployed using two separate cloud
services.

### Backend API — Render

The Flask API and trained XGBoost model are deployed on Render.

The Dockerized API is hosted at:

                                            https://flood-prediction-3eui.onrender.com

The `/predict` endpoint receives the 20 flood-related input factors
and returns the predicted flood probability, risk level, and
<img width="700" alt="Cloud Deployment" src="screenshots/Screenshot%20from%202026-09-15%2011-22-46.png" />
recommended action.

### Frontend — GitHub Pages

The web interface is deployed separately using GitHub Pages.

Live application:

                                             https://brandon-12437.github.io/flood_prediction/

The frontend communicates with the deployed Flask API on Render to
generate predictions.

### Deployment Architecture
User
  │
  ▼
GitHub Pages
FloodGuard AI Frontend
  │
  │ HTTPS POST /predict
  ▼
Render
Flask REST API
  │
  ▼
XGBoost Model
  │
  ▼
Flood Prediction
  │
  ▼
Risk Level + Recommendation

