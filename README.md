# AI Flood Prediction System

A Flask web application that predicts flood risk from environmental and infrastructure indicators using a trained machine-learning model.

## Run Locally

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python flood_api.py
```

Open http://127.0.0.1:9698 in a browser.

The file `flood_prediction_model.bin` must be present in the project root. It contains the trained feature transformer and prediction model used by the API.

## Cloud Deployment on Render

This project can be deployed as a Render Web Service.

1. Push the project to GitHub, including:
   - `flood_api.py`
   - `requirements.txt`
   - `flood_prediction_model.bin`
   - `templates/index.html`
2. In Render, choose **New > Web Service** and connect the GitHub repository.
3. Use these settings:

   ```text
   Environment: Python 3
   Build Command: pip install -r requirements.txt
   Start Command: gunicorn --bind 0.0.0.0:$PORT flood_api:app
   ```

4. Choose a plan and click **Deploy Web Service**.
5. Open the Render URL. The web interface is available at `/`, and predictions are sent to `/predict`.

Gunicorn uses Render's `$PORT` value, which allows the Flask service to receive public traffic from the cloud platform.

### Render Notes

- Do not remove `flood_prediction_model.bin`; the application loads it during startup.
- The repository must contain the `templates` directory because the home page is rendered from `templates/index.html`.
- After deployment, test the service by opening the public URL in a browser.

## Docker Deployment

Build and run the application locally with Docker:

```bash
docker build -t flood-prediction .
docker run --rm -p 9698:9698 flood-prediction
```

Open http://127.0.0.1:9698.

The included `Dockerfile` installs the Python dependencies and packages the model and web template with the application.

## API Example

Send a JSON request containing the 20 model input fields:

```bash
curl -X POST http://127.0.0.1:9698/predict \
  -H "Content-Type: application/json" \
  -d '{
    "MonsoonIntensity": 6,
    "TopographyDrainage": 7,
    "RiverManagement": 5,
    "Deforestation": 6,
    "Urbanization": 7,
    "ClimateChange": 8,
    "DamsQuality": 6,
    "Siltation": 7,
    "AgriculturalPractices": 5,
    "Encroachments": 6,
    "IneffectiveDisasterPreparedness": 5,
    "DrainageSystems": 4,
    "CoastalVulnerability": 3,
    "Landslides": 2,
    "Watersheds": 6,
    "DeterioratingInfrastructure": 5,
    "PopulationScore": 7,
    "WetlandLoss": 6,
    "InadequatePlanning": 7,
    "PoliticalFactors": 4
  }'
```

The response includes the predicted flood probability, risk level, recommendation, and whether emergency action is required.
# AI Flood Prediction System

A Flask web application that predicts flood risk from environmental and infrastructure indicators using a trained machine-learning model.

## Cloud Deployment on Render

This project can be deployed as a Render Web Service.

1. Push the project to GitHub, including `flood_api.py`, `requirements.txt`, `flood_prediction_model.bin`, and `templates/index.html`.
2. In Render, choose **New > Web Service** and connect the GitHub repository.
3. Use these settings:

  ```text
  Environment: Python 3
  Build Command: pip install -r requirements.txt
  Start Command: gunicorn --bind 0.0.0.0:$PORT flood_api:app
  ```

4. Choose a plan and click **Deploy Web Service**.
5. Open the Render URL. The web interface is available at `/`, and predictions are sent to `/predict`.

Gunicorn uses Render's `$PORT` value, allowing the Flask service to receive public cloud traffic.

The model file is required at startup. Do not remove `flood_prediction_model.bin` or the `templates` directory.

### Verify the deployment

The prediction endpoint accepts a JSON `POST` request:

```bash
curl -X POST https://your-service-name.onrender.com/predict \
  -H "Content-Type: application/json" \
  -d '{
    "MonsoonIntensity": 6,
    "TopographyDrainage": 7,
    "RiverManagement": 5,
    "Deforestation": 6,
    "Urbanization": 7,
    "ClimateChange": 8,
    "DamsQuality": 6,
    "Siltation": 7,
    "AgriculturalPractices": 5,
    "Encroachments": 6,
    "IneffectiveDisasterPreparedness": 5,
    "DrainageSystems": 4,
    "CoastalVulnerability": 3,
    "Landslides": 2,
    "Watersheds": 6,
    "DeterioratingInfrastructure": 5,
    "PopulationScore": 7,
    "WetlandLoss": 6,
    "InadequatePlanning": 7,
    "PoliticalFactors": 4
  }'
```

A successful response includes the flood probability, risk level, recommendation, and whether emergency action is required.

## Run Locally

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python flood_api.py
```

Open `http://localhost:9698` in a browser.

## Docker Deployment

```bash
docker build -t flood-prediction .
docker run --rm -p 9698:9698 flood-prediction
```

Then open `http://localhost:9698`.

The included `Dockerfile` installs the dependencies and packages the model and web template with the application.
