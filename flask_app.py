from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

# Load trained model
with open("weather_model.pkl", "rb") as f:
    model = pickle.load(f)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        temp = float(request.form["temp"])
        hum = float(request.form["humidity"])
        press = float(request.form["pressure"])
        wind = float(request.form["wind"])

        # Predict weather
        prediction = model.predict([[temp, hum, press, wind]])[0]

        return render_template("prediction.html", ans=prediction)

    return render_template("whether.html")

if __name__ == "__main__":
    app.run(debug=True)