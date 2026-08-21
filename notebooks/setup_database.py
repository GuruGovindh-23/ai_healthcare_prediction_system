import os
import pandas as pd
import mysql.connector

# Read your CSV
df = pd.read_csv("datasets/heart_disease_clean.csv")

# Connect to Railway MySQL
connection = mysql.connector.connect(
        host=os.environ["sakura.proxy.rlwy.net"],
        port=int(os.environ["58563"]),
        user=os.environ["root"],
        password=os.environ["eBPHVYOROlryVqBDabSNQMRYRPNJkwzj"],
        database=os.environ["railway"]
    )

cursor = connection.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS heart_disease (
    id INT AUTO_INCREMENT PRIMARY KEY,
    age FLOAT,
    sex INT,
    cp INT,
    trestbps FLOAT,
    chol FLOAT,
    fbs INT,
    restecg INT,
    thalach FLOAT,
    exang INT,
    oldpeak FLOAT,
    slope INT,
    ca INT,
    thal INT,
    target INT,
    disease_status VARCHAR(50)
)
""")

# Insert CSV data
for _, row in df.iterrows():
    cursor.execute("""
        INSERT INTO heart_disease
        (age, sex, cp, trestbps, chol, fbs, restecg,
         thalach, exang, oldpeak, slope, ca, thal,
         target, disease_status)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s,
                %s, %s, %s, %s, %s, %s)
    """, tuple(row))

connection.commit()

cursor.close()
connection.close()

print("Database setup completed successfully!")
