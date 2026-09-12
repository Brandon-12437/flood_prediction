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
