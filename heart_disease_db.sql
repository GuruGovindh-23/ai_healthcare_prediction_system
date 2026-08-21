CREATE DATABASE heart_disease_db;
USE heart_disease_db;
SHOW DATABASES;
SELECT DATABASE();

SHOW TABLES;
DESCRIBE heart_patients;
SELECT * FROM heart_patients
LIMIT 10;


-- 1. HIGH CHOLESTEROL
SELECT
    age,
    sex,
    chol,
    disease_status
FROM heart_patients
WHERE chol >= 240
ORDER BY chol DESC;


-- 2. HIGH BLOOD PRESSURE
SELECT
    age,
    trestbps,
    chol,
    disease_status
FROM heart_patients
WHERE trestbps >= 140
ORDER BY trestbps DESC;


-- 3. COMBINED RISK
SELECT
    age,
    chol,
    trestbps,
    disease_status
FROM heart_patients
WHERE chol >= 240
  AND trestbps >= 140
ORDER BY age DESC;


-- 4. ANGINA PATIENTS
SELECT
    age,
    sex,
    thalach,
    exang,
    disease_status
FROM heart_patients
WHERE target = 1
  AND exang = 1;


-- 5. LOW HEART RATE
SELECT
    age,
    thalach,
    disease_status
FROM heart_patients
WHERE thalach < 100
ORDER BY thalach;


-- 6. TOP CHOLESTEROL
SELECT
    age,
    sex,
    chol,
    trestbps,
    disease_status
FROM heart_patients
ORDER BY chol DESC
LIMIT 10;


-- 7. DISEASE CHOLESTEROL
SELECT
    age,
    sex,
    chol,
    trestbps,
    disease_status
FROM heart_patients
WHERE target = 1
  AND chol >= 240
ORDER BY chol DESC;


-- 8. ANGINA ANALYSIS
SELECT
    CASE
        WHEN exang = 0 THEN 'No Exercise Angina'
        WHEN exang = 1 THEN 'Exercise Angina'
    END AS exercise_angina,
    
    COUNT(*) AS total_patients,
    
    SUM(target) AS heart_disease_patients,
    
    ROUND(
        SUM(target) * 100.0 / COUNT(*),
        2
    ) AS disease_rate

FROM heart_patients
GROUP BY exang;


-- 9. CHEST PAIN ANALYSIS
SELECT
    cp AS chest_pain_type,
    COUNT(*) AS total_patients,
    SUM(target) AS heart_disease_patients
FROM heart_patients
GROUP BY cp
ORDER BY cp;


-- 10. PATIENT TARGET
SELECT
    age,
    sex,
    cp,
    chol,
    trestbps,
    target,
    disease_status
FROM heart_patients
WHERE target = 1
ORDER BY age DESC
LIMIT 10;