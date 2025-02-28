from fastapi import FastAPI
import pandas as pd 
from sqlalchemy import create_engine
import db 
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/sales_data")
def get_sale_data():
    query = "select region, SUM(total_price) as revenue FROM sales GROUP BY region"
    df = pd.read_sql(query, db.engine)

    min_value = df['revenue'].min()

    scale_factor, scale_label = get_scale_value(min_value)

    df['revenue'] = df['revenue'] / scale_factor
    df['revenue'] = df['revenue'].apply(lambda x: f"{x:.2f} {scale_label}" if scale_label else f"{x:.2f}")
    return df.to_dict(orient="records")


def get_scale_value(max_value):
    if max_value >= 1_000_000_000:  
        scale_factor = 1_000_000_000
        scale_label = "Billions"  
    elif max_value >= 1_000_000:  
        scale_factor = 1_000_000
        scale_label = "Millions"  
    elif max_value >= 10_000:  
        scale_factor = 10_000
        scale_label = "Thousands"  
    else:
        scale_factor = 1  
        scale_label = ""

    return scale_factor, scale_label