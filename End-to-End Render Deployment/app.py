from flask import Flask, render_template, request
import pandas as pd

from src.predict_pipeline import PredictPipeline

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/predict", methods=["GET", "POST"])
def predict():

    if request.method == "GET":
        return render_template("index.html")

    data = pd.DataFrame({

        "gender":[request.form["gender"]],

        "race/ethnicity":[request.form["race"]],

        "parental level of education":[request.form["education"]],

        "lunch":[request.form["lunch"]],

        "test preparation course":[request.form["prep"]],

        "reading score":[float(request.form["reading"])],

        "writing score":[float(request.form["writing"])]

    })

    predictor = PredictPipeline()

    prediction = predictor.predict(data)

    return render_template(
        "index.html",
        prediction_text=f"Predicted Math Score : {prediction[0]:.2f}"
    )


if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)