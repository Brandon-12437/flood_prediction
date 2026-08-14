#!/usr/bin/env python
# coding: utf-8

# **PROBLEM DESCRIPTION**
# 
# **Flooding is a recurring natural disaster in Karimganj (Sribhumi) District, Assam, India, particularly during the monsoon season. The district** **is ***traversed by major rivers such as the Kushiyara, Longai, and Singla, which frequently overflow due to prolonged heavy rainfall. These floods** **damagehomes, roads, schools, farmland, and public infrastructure, while also disrupting transportation and economic activities.**
# 
# **Current flood warning systems often rely on limited monitoring and may not provide sufficiently accurate or timely forecasts for local communities.** **As a result, emergency response and resource allocation become more difficult, increasing the risk to lives and property.**
# 
# **This project aims to develop an AI-powered flood prediction system that integrates historical flood records, rainfall data, river water levels, topographical information, and weather conditions to predict the probability of flooding. By providing early warnings and risk assessments, the system will help government agencies, disaster management authorities, and local communities prepare for flood events, reduce losses, and improve disaster response.**



import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib 
import seaborn as sns
import sklearn
from sklearn.metrics import mutual_info_score
from sklearn.ensemble  import RandomForestClassifier
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction import DictVectorizer 
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error


# **DATA PREPARATION AND  EXPLORATOTY DATA ANALYSIS**



df = pd.read_csv('flood_data.csv')
df.head()

numerical = list(df.dtypes[(df.dtypes=='int64') | (df.dtypes=='float64')].index)
numerical
# **VISUALIZATION OF PATTERNS**
import seaborn as sns
import matplotlib.pyplot as plt

plt.figure(figsize=(9,8))
sns.histplot(df['FloodProbability'], bins=20, kde=True)
plt.title('Distribution of Flood Probability')
plt.show()

plt.figure(figsize=(18, 15))

sns.heatmap(
    df[numerical].corr(),
    annot=True,
    cmap="coolwarm",
    fmt=".2f",
    linewidths=0.5
)

plt.title("Flood Prediction Correlation Heatmap", fontsize=18)
plt.tight_layout()
plt.show()

df[numerical].hist(figsize = (13, 13))

plt.figure(figsize=(8, 6))

sns.boxplot(
    x="MonsoonIntensity",
    y="FloodProbability",
    data=df
)

plt.title("Flood Probability by Monsoon Intensity")
plt.show()

cols = [
    "MonsoonIntensity",
    "RiverManagement",
    "DrainageSystems",
    "Deforestation",
    "FloodProbability"
]

sns.pairplot(df[cols], diag_kind="hist")
plt.show()


# **SPLITTING THE DATA INTO VALIDATION /TRAIN/ TEST_SPLIT**
from sklearn.model_selection import train_test_split


df_full_train, df_test = train_test_split(df, test_size=0.2, random_state=42)
df_train, df_val = train_test_split(df_full_train, test_size=0.25, random_state=42)

df_train.reset_index(drop=True)
df_val.reset_index(drop=True)
df_test.reset_index(drop=True)


X_train = df_train.drop("FloodProbability", axis=1)
X_val = df_val.drop("FloodProbability", axis=1)
X_test = df_test.drop("FloodProbability", axis=1)


y_train = df_train.FloodProbability.values
y_val = df_val.FloodProbability.values
y_test = df_test.FloodProbability.values


# **PERFOMING ONE HOT ENCODING**



train_dicts = df_train.to_dict(orient = 'records')
dv= DictVectorizer(sparse = False) 
X_train = dv.fit_transform(train_dicts)


model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)


val_dicts = df_val.to_dict(orient = 'records')
X_val = dv.transform(val_dicts)


test_dicts = df_test.to_dict(orient = 'records')
X_test = dv.transform(test_dicts)


# **TRAINING SEVERAL MODELS THEN FINE TUNING**

# RANDOM FOREST REGRESSOR
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score, mean_squared_error
import pandas as pd

scores = []

for d in [5, 10, 15]:
    for n in range(10, 201, 10):

        rf = RandomForestRegressor(
            n_estimators=n,
            max_depth=d,
            random_state=42
        )

        rf.fit(X_train, y_train)

        y_pred = rf.predict(X_val)

        r2 = r2_score(y_val, y_pred)
        rmse = mean_squared_error(y_val, y_pred) ** 0.5

        scores.append((d, n, r2, rmse))

df_scores = pd.DataFrame(
    scores,
    columns=["max_depth", "n_estimators", "R2", "RMSE"]
)

df_scores.head()
plt.figure(figsize=(8,5))

plt.plot(df_scores["n_estimators"], df_scores["R2"])

plt.xlabel("Number of Trees")
plt.ylabel("R² Score")
plt.title("Random Forest Performance")

plt.grid(True)

plt.show()




scores = []

for depth in [5, 10, 15, 20, None]:
    rf = RandomForestRegressor(
        n_estimators=100,
        max_depth=depth,
        random_state=42
    )

    rf.fit(X_train, y_train)

    y_pred = rf.predict(X_val)

    r2 = r2_score(y_val, y_pred)

    scores.append((depth, r2))

pd.DataFrame(scores, columns=["max_depth", "R2"])

df_scores.columns

for d in [5, 10, 15]:
    df_subset = df_scores[df_scores["max_depth"] == d]

    plt.plot(
        df_subset["n_estimators"],
        df_subset["R2"], 
            label=f"max_depth={d}"
    )

plt.xlabel("Number of Trees (n_estimators)")
plt.ylabel("R² Score")
plt.title("Random Forest Performance")
plt.legend()
plt.grid(True)
plt.show()

max_depth = 15

scores = []

for s in [1, 3, 5, 10, 50]:
    for n in range(10, 201, 10):

        rf = RandomForestRegressor(
            n_estimators=n,
            max_depth=15, 
            min_samples_leaf=s,
            random_state=1
        )

        rf.fit(X_train, y_train)

        y_pred = rf.predict(X_val)

        r2 = r2_score(y_val, y_pred)

        scores.append((s, n, r2))

columns = ['min_samples_leaf', 'n_estimators', 'R2']
df_scores = pd.DataFrame(scores, columns=columns)




colors = ['black', 'blue', 'orange', 'red', 'green']
values = [1, 3, 5, 10, 50]

plt.figure(figsize=(8,6))

for s, col in zip(values, colors):
    df_subset = df_scores[df_scores.min_samples_leaf == s]

    plt.plot(
        df_subset.n_estimators,
        df_subset.R2,
        color=col,
        label=f"min_samples_leaf={s}"
    )

plt.xlabel("Number of Trees")
plt.ylabel("R² Score")
plt.title("Random Forest: Tuning min_samples_leaf")
plt.legend()
plt.grid(True)
plt.show()

min_samples_leaf = 1

max_depth = 15
min_samples_leaf = 1

rf = RandomForestRegressor(
    n_estimators=200,
    max_depth=max_depth,
    min_samples_leaf=min_samples_leaf,
    random_state=42
)

rf.fit(X_train, y_train)


# XG BOOST REGRESSOR
import xgboost as xgb
print(xgb.__version__)
dtrain = xgb.DMatrix(X_train, label=y_train)
dval = xgb.DMatrix(X_val, label=y_val)

watchlist = [(dtrain, "train"), (dval, "eval")]

from xgboost import XGBRegressor
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error

xgb_model = XGBRegressor(
    n_estimators=200,
    learning_rate=0.3,
    max_depth=6,
    min_child_weight=1,
    objective="reg:squarederror",
    random_state=42
)

xgb_model.fit(X_train, y_train)

y_pred = xgb_model.predict(X_val)

print("R²:", r2_score(y_val, y_pred))
print("MAE:", mean_absolute_error(y_val, y_pred))
print("RMSE:", mean_squared_error(y_val, y_pred) ** 0.5)


# DECISION TREE REGRESSOR
depths = [1, 2, 3, 4, 5, 6, 10, 15, 20, None]

for depth in depths:
    dt = DecisionTreeRegressor(
        max_depth=depth,
        random_state=42
    )

    dt.fit(X_train, y_train)

    y_pred = dt.predict(X_val)

    r2 = r2_score(y_val, y_pred)
    mae = mean_absolute_error(y_val, y_pred)
    rmse = np.sqrt(mean_squared_error(y_val, y_pred))

    print(f"Depth={depth}, R²={r2:.4f}, MAE={mae:.4f}, RMSE={rmse:.4f}")


results = []

for d in [4, 5, 6]:
    for leaf in [1, 2, 5, 10, 20, 50]:
        dt = DecisionTreeRegressor(
            max_depth=d,
            min_samples_leaf=leaf,
            random_state=42
        )

        dt.fit(X_train, y_train)
        y_pred = dt.predict(X_val)

        results.append({
            "max_depth": d,
            "min_samples_leaf": leaf,
            "R²": r2_score(y_val, y_pred),
            "MAE": mean_absolute_error(y_val, y_pred),
            "RMSE": np.sqrt(mean_squared_error(y_val, y_pred))
        })

results = pd.DataFrame(results)
print(results)

df_scores_pivot = results.pivot(
    index="min_samples_leaf",
    columns="max_depth",
    values="RMSE" 
)

plt.figure(figsize=(8, 6))
sns.heatmap(df_scores_pivot, annot=True, fmt=".5f", cmap="viridis")
plt.title("Decision Tree Hyperparameter Tuning (RMSE)")
plt.xlabel("Max Depth")
plt.ylabel("Min Samples Leaf")
plt.show()


# CHOOSING THE BEST MODEL

# We will pick xg boost regressor   because it has a coefficient of determination of  0.999951

# SAVING THE MODEL



import pickle




output_file = "flood_prediction_model.bin"
output_file

with open(output_file, "wb") as f_out:
    pickle.dump(xgb_model, f_out)

print("Model saved successfully!")


import pickle

with open("flood_prediction_model.bin", "rb") as f_in:
    xgb_model = pickle.load(f_in)

print(xgb_model)

import pickle

output_file = "flood_prediction_model.bin"
with open(output_file, "wb") as f_out:
    pickle.dump((dv, xgb_model), f_out, protocol=pickle.HIGHEST_PROTOCOL)

with open(output_file, "rb") as f_in:
    dv, model = pickle.load(f_in)

print(type(model), model.__class__.__module__, model.__class__.__name__)

# SAMPLE INPUT (use real values)
flood_data = {
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
    "PoliticalFactors": 4,
}

X_new = dv.transform([flood_data])
predicted_probability = model.predict(X_new)[0]
print(f"Predicted Flood Probability: {predicted_probability:.3f}")

def print_risk_and_measure(p):
    if p >= 0.75:
        print("🚨 Very High Flood Risk")
        print("Measure: Evacuate to higher ground immediately and follow official orders.")
    elif p >= 0.50:
        print("⚠️ High Flood Risk")
        print("Measure: Prepare to evacuate — move valuables higher and charge devices.")
    elif p >= 0.25:
        print("🟡 Moderate Flood Risk")
        print("Measure: Monitor updates closely and have your emergency kit ready.")
    else:
        print("🟢 Low Flood Risk")
        print("Measure: Stay informed and review your household emergency plan.")

print_risk_and_measure(predicted_probability)

