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
