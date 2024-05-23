# Project: Heart Disease Diagnosis System

## Description
This project implements a heart disease diagnosis system using a machine-learning model built with Python. It offers a user-friendly web interface for interactive prediction, leveraging the strengths of Streamlit for the frontend and FastAPI for the backend. Docker ensures seamless deployment and containerization.

## Key Technologies
* **Frontend:** Streamlit
* **Backend:** FastAPI
* **Deployment:** Docker

## User Interface
The Streamlit frontend provides an intuitive interface where users can input various heart-related features. The application then utilizes the trained neural network model to predict the likelihood of heart disease.

## Model Training
The details of the machine learning model training process, including the neural network architecture, hyperparameter tuning, and performance evaluation, are comprehensively documented in the heart_disease_model.ipynb notebook inside the model trining folder alongside the dataset.

## Deployment
Docker is employed to create a containerized application, simplifying deployment to various cloud platforms. The Dockerfile and accompanying instructions guide the deployment process.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/habash2125/heart-disease-diagnosis.git
    ```
    
## Usage

1. Run the application:
  - if you are running the code using docker
   ```bash
    docker-compose up 
   ```
  that will run the whole app and you can access it directly
  - if you are not using docker
    - you will have to run the frontend from using
    ```bash
    streamlit run app.py 
    ```
    - then you will have to run the backend using
    ```bash
    uvicorn --reload backend:app 
    ```

## Disclaimer
This system is for demonstration purposes only and should not be used for actual medical diagnoses. Please consult a qualified medical professional for heart-related concerns.
