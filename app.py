from flask import Flask, render_template, request
import pandas as pd
import joblib
import mysql.connector
import os

app = Flask(__name__)

final_model = joblib.load("heart_disease_naive_bayes_model.pkl")


def get_db_connection():
    connection = mysql.connector.connect(
        host=os.environ["MYSQLHOST"],
        port=int(os.environ["MYSQLPORT"]),
        user=os.environ["MYSQLUSER"],
        password=os.environ["MYSQLPASSWORD"],
        database=os.environ["MYSQL_DATABASE"]
    )
    return connection


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    try:
        age = float(request.form["age"])
        sex = int(request.form["sex"])
        cp = int(request.form["cp"])
        trestbps = float(request.form["trestbps"])
        chol = float(request.form["chol"])
        fbs = int(request.form["fbs"])
        restecg = int(request.form["restecg"])
        thalach = float(request.form["thalach"])
        exang = int(request.form["exang"])
        oldpeak = float(request.form["oldpeak"])
        slope = int(request.form["slope"])
        ca = int(request.form["ca"])
        thal = int(request.form["thal"])

        patient = pd.DataFrame(
            [[
                age, sex, cp, trestbps, chol, fbs, restecg,
                thalach, exang, oldpeak, slope, ca, thal
            ]],
            columns=[
                "age", "sex", "cp", "trestbps", "chol", "fbs",
                "restecg", "thalach", "exang", "oldpeak",
                "slope", "ca", "thal"
            ]
        )

        prediction = final_model.predict(patient)
        predicted_class = int(prediction[0])

        probability_values = final_model.predict_proba(patient)[0]
        model_classes = list(final_model.classes_)

        if 1 in model_classes:
            disease_class_index = model_classes.index(1)
            probability = float(
                probability_values[disease_class_index] * 100
            )
        else:
            probability = 0.0

        probability = max(0.0, min(100.0, probability))

        if probability <= 30:
            risk_level = "Low Risk"
        elif probability <= 70:
            risk_level = "Moderate Risk"
        else:
            risk_level = "High Risk"

        if predicted_class == 1:
            prediction_result = "Heart Disease"
        else:
            prediction_result = "No Heart Disease"

        insights = []

        if age >= 60:
            insights.append(
                "Patient belongs to an older age group."
            )

        if trestbps >= 140:
            insights.append(
                "Resting blood pressure is elevated."
            )

        if chol >= 240:
            insights.append(
                "Cholesterol level is elevated."
            )

        if thalach < 120:
            insights.append(
                "Maximum heart rate is relatively low."
            )

        if exang == 1:
            insights.append(
                "Exercise-induced angina is present."
            )

        if oldpeak > 2:
            insights.append(
                "ST depression (oldpeak) is elevated."
            )

        if cp >= 3:
            insights.append(
                "Chest pain category may be associated with increased model risk."
            )

        if ca >= 2:
            insights.append(
                "Major vessel involvement value is elevated."
            )

        if len(insights) == 0:
            insights.append(
                "No major feature-level indicators were identified using the project rules."
            )

        if risk_level == "High Risk":
            decision_support = [
                "The model indicates a high predicted risk.",
                "Further clinical evaluation is recommended."
            ]
        elif risk_level == "Moderate Risk":
            decision_support = [
                "The model indicates a moderate predicted risk.",
                "Further assessment may be appropriate."
            ]
        else:
            decision_support = [
                "The model indicates a low predicted risk.",
                "Continue appropriate health monitoring."
            ]

        connection = get_db_connection()
        cursor = connection.cursor()

        query = """
        INSERT INTO predictions
        (
            age, sex, cp, trestbps, chol, fbs, restecg,
            thalach, exang, oldpeak, slope, ca, thal,
            prediction, prediction_result,
            prediction_probability, risk_category
        )
        VALUES
        (
            %s, %s, %s, %s, %s, %s, %s,
            %s, %s, %s, %s, %s, %s,
            %s, %s, %s, %s
        )
        """

        values = (
            int(age),
            sex,
            cp,
            int(trestbps),
            int(chol),
            fbs,
            restecg,
            int(thalach),
            exang,
            oldpeak,
            slope,
            ca,
            thal,
            predicted_class,
            prediction_result,
            probability,
            risk_level
        )

        cursor.execute(query, values)
        connection.commit()

        cursor.close()
        connection.close()

        return render_template(
            "index.html",
            prediction=prediction_result,
            probability=f"{probability:.2f}",
            risk=risk_level,
            insights=insights,
            decision_support=decision_support
        )

    except Exception as e:
        return render_template(
            "index.html",
            error=str(e)
        )


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 5000))
    )
