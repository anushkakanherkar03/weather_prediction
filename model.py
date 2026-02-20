import pandas as pd
import pickle
from sklearn.tree import DecisionTreeClassifier

# Sample weather dataset
data = pd.read_csv("weather_prediction.csv")
data

X = df[["Temperature", "Humidity", "WindSpeed"]]
y = df["Result"]

model = DecisionTreeClassifier()
model.fit(X, y)

# Save model
with open("weather_model.pkl", "wb") as f:
    pickle.dump(model, f)

print("Model Saved Successfully!")