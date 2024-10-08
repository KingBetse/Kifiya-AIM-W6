# app.py

from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

app = FastAPI()

# Load the trained model
model = joblib.load('./Random_Forest.pkl')  # Adjust the model path as needed

# Define the input data model
class InputData(BaseModel):
    country_code: int
    amount: float
    value: int
    pricing_strategy: int
    total_transaction_amount: float
    avg_transaction_amount: float
    transaction_count: int
    std_transaction_amount: float
    transaction_hour: int
    transaction_day: int
    transaction_month: int
    transaction_year: int
    product_category_data_bundles: bool
    product_category_financial_services: bool
    product_category_movies: bool
    product_category_other: bool
    product_category_ticket: bool
    product_category_transport: bool
    product_category_tv: bool
    product_category_utility_bill: bool
    provider_id_encoded: int
    amount_normalized: float
    amount_standardized: float
    recency: int
    frequency: int
    monetary: float
    seasonality: int
    credit_risk: str  # Adjust based on your encoding

@app.get("/")
def read_root():
    return {"message": "Welcome to the Fraud Detection API!"}

@app.post("/predict")
def predict(data: InputData):
    # Prepare the features array for model prediction
    features = np.array([[ 
        data.country_code,
        data.amount,
        data.value,
        data.pricing_strategy,
        data.total_transaction_amount,
        data.avg_transaction_amount,
        data.transaction_count,
        data.std_transaction_amount,
        data.transaction_hour,
        data.transaction_day,
        data.transaction_month,
        data.transaction_year,
        int(data.product_category_data_bundles),
        int(data.product_category_financial_services),
        int(data.product_category_movies),
        int(data.product_category_other),
        int(data.product_category_ticket),
        int(data.product_category_transport),
        int(data.product_category_tv),
        int(data.product_category_utility_bill),
        data.provider_id_encoded,
        data.amount_normalized,
        data.amount_standardized,
        data.recency,
        data.frequency,
        data.monetary,
        data.seasonality,
        # Convert credit risk to a suitable numerical representation if necessary
    ]])
    
    # Make a prediction
    prediction = model.predict(features)
    
    return {"prediction": int(prediction[0])}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)