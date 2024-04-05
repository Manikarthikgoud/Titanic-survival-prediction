
# Titanic Survival Prediction Web App

This is a web application built using Streamlit for predicting survival on the Titanic based on passenger information. It uses a [Machine Learning Model Type] model trained on the [Data Source].

## Prerequisites

Before running the application, make sure you have the following installed:

- Python (3.x recommended)
- Streamlit
- scikit-learn
- pandas
- numpy

You can install Streamlit and other dependencies using pip:


pip install streamlit scikit-learn pandas numpy

### Training the Model

To train the machine learning model used in the app:

1. Open and run the `titanic.ipynb` notebook.
2. The notebook performs data preprocessing, model training, and model evaluation.
3. The trained model (`model.pkl`) will be saved after training process is completed.

#### Running the Streamlit webApp

streamlit run streamlit.py  # This will open the app in your default web browser.
```bash

Usage
1.Select the passenger class, sex, age, number of siblings/spouses aboard, number of parents/children aboard, and port of embarkation using the dropdowns and input fields.
2.The app will predict the survival probability of the passenger based on the input data.

Example:
If you select:

Pclass:1
Sex: Male
Age: 30
Sibling/Spouses: 1
Parents/Children: 0
Port of Embarkation: S(Southampton)

The app might predict a high probability of survival for this passenger.