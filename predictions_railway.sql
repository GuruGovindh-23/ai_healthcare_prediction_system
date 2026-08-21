USE railway;

CREATE TABLE IF NOT EXISTS predictions (
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


SELECT*FROM predictions;