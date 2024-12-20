import streamlit as st
import requests
import json

# Set up the Streamlit app
st.title("NBA Player Type Classifier")
st.write("Enter the player statistics below to predict the player type.")

# Input fields
PTS_per_game = st.number_input("Points Per Game (PTS_per_game)", min_value=0.0, step=0.1)
REB_per_game = st.number_input("Rebounds Per Game (REB_per_game)", min_value=0.0, step=0.1)
AST_per_game = st.number_input("Assists Per Game (AST_per_game)", min_value=0.0, step=0.1)
three_PA_per_game = st.number_input("3-Point Attempts Per Game (three_PA_per_game)", min_value=0.0, step=0.1)
three_PM_per_game = st.number_input("3-Point Made Per Game (three_PM_per_game)", min_value=0.0, step=0.1)
FG = st.number_input("Field Goal Percentage (FG)", min_value=0.0, step=0.1)
three_P = st.number_input("3-Point Percentage (3P%)", min_value=0.0, step=0.1)

# Define the API endpoint
api_url = "https://nba-player-type-latest.onrender.com/predict"  # Replace with your deployed API URL

# Prediction button
if st.button("Predict Player Type"):
    # Prepare the input data
    input_data = {
        "PTS_per_game": PTS_per_game,
        "REB_per_game": REB_per_game,
        "AST_per_game": AST_per_game,
        "three_PA_per_game": three_PA_per_game,
        "three_PM_per_game": three_PM_per_game,
        "FG": FG,
        "three_P": three_P,
    }

    # Make a POST request to the API
    try:
        response = requests.post(api_url, headers={"Content-Type": "application/json"}, data=json.dumps(input_data))
        if response.status_code == 200:
            prediction = response.json().get("player_type", "Unknown")
            st.success(f"Predicted Player Type: {prediction}")
        else:
            st.error(f"API Error: {response.status_code} - {response.text}")
    except Exception as e:
        st.error(f"Error: {str(e)}")