import pandas as pd
import db

def extract_data(file_path):
    df = pd.read_csv(file_path)
    print(df.columns)
    return df

def transform_data(df):
    df.dropna(inplace = True)
    df['Sale_Date'] = pd.to_datetime(df['Sale_Date'])
    df['Total_Price'] = df['Quantity_Sold'] * df['Unit_Price']
    df['Total_Price'] = df['Total_Price'].round(3)
    return df

def load_data(df):
    df.to_sql("sales", db.engine, if_exists = 'replace', index = False)
    print("Data loaded successfully !")

def run_etl():
    file_path = "sales_data.csv"
    raw_data = extract_data(file_path)
    transform_data1 = transform_data(raw_data)
    load_data(transform_data1)
    print("ETL Pipeline completed!")

if __name__ == "__main__":
    run_etl()
