from fastapi import FastAPI
from pydantic import BaseModel
from joblib import load
import pandas as pd

# Load the saved pipeline and label encoder
model_pipeline = load("RandomForestClassifier_pipeline_final.pkl")
label_encoder = load("label_encoder.pkl")

# Initialize the FastAPI app
app = FastAPI()

# Define the input schema
class PlayerStats(BaseModel):
    PTS_per_game: float
    REB_per_game: float
    AST_per_game: float
    three_PA_per_game: float
    three_PM_per_game: float
    FG: float
    three_P: float

# Root endpoint
@app.get("/")
def read_root():
    return {"message": "NBA Player Type Classification API"}

from fastapi.responses import JSONResponse

@app.post("/predict")
def predict(player_stats: PlayerStats):
        print("Received Input:", player_stats)
        # Convert input to DataFrame
        input_data = pd.DataFrame([player_stats.dict()])
        input_data.rename(columns={
            'FG': 'FG%',
            'three_P': '3P%'}, inplace=True)
  
        prediction = model_pipeline.predict(input_data)
        decoded_prediction = label_encoder.inverse_transform(prediction)
  
        return {"player_type": decoded_prediction[0]}