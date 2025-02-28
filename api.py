from fastapi import FastAPI
import pandas as pd 
from sqlalchemy import create_engine
import db 
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins (use specific domains in production)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/sales_data")
def get_sale_data():
    query = "select region, SUM(total_price) as revenue FROM sales GROUP BY region"
    df = pd.read_sql(query, db.engine)
    return df.to_dict(orient="records")
