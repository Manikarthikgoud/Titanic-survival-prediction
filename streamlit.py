
import streamlit as st
import pickle
import pandas as pd

# Load the pickled model
with open('model.pkl', 'rb') as file:
    model = pickle.load(file)

# Define the input variables
Pclass = st.selectbox('Select Passenger Class', ['1', '2', '3'])
Sex = st.selectbox('Select Sex', ['male', 'female'])
Age = st.number_input('Enter Age')
SibSp = st.number_input('Enter Number of Siblings/Spouses Aboard', min_value=0, max_value=10, value=0)
Parch = st.number_input('Enter Number of Parents/Children Aboard', min_value=0, max_value=10, value=0)
fare = st.number_input('Enter fare')
Embarked = st.selectbox('Select Port of Embarkation', ['C', 'Q', 'S'])

# Create a dataframe with the input variables
input_data = {'Pclass': [int(Pclass)], 'Sex': [Sex], 'Age': [Age], 'SibSp': [int(SibSp)], 'Parch': [int(Parch)],'fare': [int(fare)], 'Embarked': [Embarked]}
input_df = pd.DataFrame(input_data)

# Preprocess the input data to match the training data
input_df['Sex'] = input_df['Sex'].map({'male': 0, 'female': 1})
input_df['Embarked'] = input_df['Embarked'].map({'C': 0, 'Q': 1, 'S': 2})

# Define the Streamlit form
form = st.form(key='predict_form')

# Add form inputs
with form:
    submitted = form.form_submit_button(label='Predict Survival Probability')
    if submitted:
        # Make a prediction using the model
        prediction = model.predict(input_df)
        print(prediction)
        # Display the prediction
        st.write('The predicted survival probability is:', prediction)