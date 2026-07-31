# End-to-End Student Performance Prediction

## Overview

This project demonstrates a complete end-to-end Machine Learning workflow for predicting a student's mathematics score based on demographic and academic information. It covers the entire pipeline from data preprocessing and model training to deployment through a Flask web application.

The objective is to showcase how a trained machine learning model can be integrated into a user-friendly web interface for real-time predictions.

---

## Features

- Data preprocessing using Scikit-learn Pipelines
- One-Hot Encoding for categorical features
- Feature scaling using StandardScaler
- Random Forest Regression model
- Model evaluation using MAE, RMSE, and R² Score
- Model serialization using Pickle
- Flask-based web application
- Interactive prediction interface

---

## Dataset

The project uses the **Students Performance in Exams** dataset.

The dataset contains the following attributes:

- Gender
- Race/Ethnicity
- Parental Level of Education
- Lunch Type
- Test Preparation Course
- Reading Score
- Writing Score
- Mathematics Score (Target Variable)

---

## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Flask
- Pickle
- HTML

---

## Project Structure

```
End-to-End Render Deployment/
│
├── app.py
├── requirements.txt
├── student_performance.csv
│
├── artifacts/
│   └── model.pkl
│
├── notebook/
│   └── model_training.ipynb
│
├── src/
│   └── predict_pipeline.py
│
└── templates/
    ├── home.html
    └── index.html
```

---

## Model Performance

Evaluation Metrics:

- Mean Absolute Error (MAE): **4.62**
- Root Mean Squared Error (RMSE): **5.98**
- R² Score: **0.853**

These results indicate that the model can explain approximately **85%** of the variance in students' mathematics scores.

---

## Installation

Clone the repository

```bash
git clone <repository-url>
```

Navigate to the project directory

```bash
cd End-to-End Render Deployment
```

Install the required dependencies

```bash
pip install -r requirements.txt
```

---

## Running the Application

Start the Flask application

```bash
python app.py
```

Open your browser and visit

```
http://127.0.0.1:5000
```

---

## How It Works

1. The user enters student information through the web interface.
2. The input data is converted into a Pandas DataFrame.
3. The trained preprocessing pipeline transforms the features.
4. The Random Forest model predicts the mathematics score.
5. The predicted score is displayed on the webpage.

---

## Sample Prediction

**Input**

- Gender: Female
- Race: Group A
- Education: Bachelor's Degree
- Lunch: Standard
- Test Preparation: Completed
- Reading Score: 70
- Writing Score: 75

**Output**

```
Predicted Math Score: 71.97
```

---

## Future Improvements

- Deploy the application on Render or Railway
- Add input validation
- Compare multiple regression algorithms
- Improve frontend design
- Containerize the application using Docker

---

## Author

**Tanishq Kumar Gupta**
