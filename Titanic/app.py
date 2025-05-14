import streamlit as st
import pickle
import numpy as np

# Load your trained model
with open('titanic_model.pkl', 'rb') as file:
    model = pickle.load(file)

# Set up the app interface
st.title('Titanic Survival Prediction')

# Input fields for user data
pclass = st.number_input('Pclass', min_value=1, max_value=3, value=1)
sex = st.selectbox('Sex', ['male', 'female'])
age = st.number_input('Age', min_value=0, max_value=100, value=30)
fare = st.number_input('Fare', min_value=0.0, max_value=500.0, value=30.0)

# Convert 'Sex' to numeric (1 for female, 0 for male)
sex = 1 if sex == 'female' else 0

# Prepare input features for prediction
features = np.array([[pclass, sex, age, fare]])

# Predict the result when the button is pressed
if st.button('Predict'):
    prediction = model.predict(features)
    if prediction == 1:
        st.success('Survived')
    else:
        st.error('Did not survive')





# ## flask


# from flask import Flask, request, jsonify
# import pickle
# import numpy as np

# # Load the model
# with open('titanic_model.pkl', 'rb') as f:
#     model = pickle.load(f)

# # Initialize Flask app
# app = Flask(__name__)

# @app.route('/')
# def home():
#     return 'Titanic Prediction API is running! Send POST request to /predict.'

# @app.route('/predict', methods=['POST'])
# def predict():
#     try:
#         # Get JSON data
#         data = request.get_json(force=True)
        
#         # Example input: {'Pclass': 1, 'Sex': 1, 'Age': 25, 'Fare': 50}
#         features = np.array([[data['Pclass'], data['Sex'], data['Age'], data['Fare']]])
        
#         # Make prediction
#         prediction = model.predict(features)[0]
        
#         # Return response
#         return jsonify({'prediction': int(prediction)})
    
#     except Exception as e:
#         return jsonify({'error': str(e)})

# if __name__ == '__main__':
#     app.run(debug=True)
