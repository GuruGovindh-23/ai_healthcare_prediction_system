USE heart_disease_db;
CREATE TABLE predictions (
    prediction_id INT AUTO_INCREMENT PRIMARY KEY,

    age INT,
    sex INT,
    cp INT,
    trestbps INT,
    chol INT,
    fbs INT,
    restecg INT,
    thalach INT,
    exang INT,
    oldpeak FLOAT,
    slope INT,
    ca INT,
    thal INT,

    prediction INT,
    prediction_result VARCHAR(50),
    prediction_probability FLOAT,
    risk_category VARCHAR(30),

    prediction_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

SELECT *
FROM predictions
ORDER BY prediction_id DESC;

SELECT
    prediction_id,
    age,
    sex,
    chol,
    prediction_result,
    prediction_probability,
    risk_category,
    prediction_date
FROM predictions
ORDER BY prediction_id DESC;

TRUNCATE TABLE predictions;