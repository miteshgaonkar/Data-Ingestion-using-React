# Sales Dashboard: ETL Pipeline and Data Visualization

## Project Overview

This project demonstrates an ETL (Extract, Transform, Load) pipeline that processes sales data from a CSV file, stores it in a MySQL database, and serves it via a FastAPI backend. The processed data is then visualized using a React.js frontend with Recharts.

## Prerequisites

Ensure you have the following installed on your system:

- Python 3.x

- Node.js and npm

- MySQL database

- Git (optional, for version control)

## Project Setup

### 1. Clone the Repository
```yaml
 git clone <repository-url>
 cd sales-dashboard
```
### 2. Set Up the Python Environment

#### a. Create and Activate a Virtual Environment
```yaml
python -m venv data_env
```
For Windows:
```yaml
.\data_env\Scripts\activate
```
For macOS/Linux:
```yaml
source data_env/bin/activate
```

#### b. Upgrade pip and Install Dependencies

```yaml
python -m pip install --upgrade pip
pip install --upgrade sqlalchemy pymysql fastapi uvicorn pandas
```

## Database Setup

Ensure you have MySQL running and update db.py with your database credentials:

```yaml
DB_USER = "root"
DB_PASSWORD = "password"
DB_HOST = "localhost"
DB_PORT = "3306"
DB_NAME = "inventory"
```

## Running the Backend

### 1. Run the ETL Pipeline

This will extract, transform, and load data from sales_data.csv into the MySQL database.

```yaml
python data_ingestion.py
```

### 2. Start the FastAPI Server

```yaml
uvicorn api:app --reload
```

The API will be accessible at `http://localhost:8000/sales_data`

## Frontend Setup (React.js)

### 1. Create a React App (if not already created)

```yaml
npx create-react-app sales-dashboard
cd sales-dashboard
```
### 2. Install Required Packages

```yaml
npm install recharts
```

### 3. Run the React App

```yaml
npm start
```
Your frontend will be available at `http://localhost:3000/`

## How It Works

### ETL Process

- **Extract**: Reads sales data from a CSV file.

- **Transform**: Cleans the data, converts date formats, and calculates total sales.

- **Load**: Stores the processed data in a MySQL database.

## API Endpoint

**GET** `/sales_data`: Fetches aggregated sales revenue per region and formats the revenue for better readability.

## Data Visualization

The React frontend fetches sales data from the FastAPI backend and visualizes revenue per region using a bar chart.

## Project Structure
```yaml
📁 Data Ingestion using React
│── 📄 data_ingestion.py    # Extract, Transform, and Load (ETL) script
│── 📄 db.py                # Database connection setup
│── 📄 api.py               # FastAPI backend to serve processed data
│── 📂 sales-dashboard     # React.js frontend for data visualization
│── 📄 sales_data.csv       # Sample sales data file
│── 📄 README.md            # Project documentation
```
## Project Breakdown

### Python Code

`data_ingestion.py`

This script:

- Extracts data from a CSV file.

- Transforms it by handling missing values, converting date formats, and calculating total prices.

- Loads the transformed data into a MySQL database.

`db.py`

- Handles database connection using `SQLAlchemy`.

`api.py`

- Sets up a FastAPI server to serve data from the database.

- Implements an endpoint `/sales_data` to fetch sales revenue grouped by region.

- Applies scaling to format large revenue values (Thousands, Millions, Billions) for readability.

- Uses CORS middleware to enable cross-origin requests from the React frontend.

### React.js Code

`SalesDashboard.js`

- Fetches sales data from the FastAPI backend.

- Formats revenue values for better visualization.

- Uses `recharts` to display a bar chart showing revenue per region.


## Screenshots

### 1. Data after ETL 
This screenshot displays the data after being processed by the backend. Raw sales data is cleaned, transformed, and stored in a MySQL database for visualization.
![MySQL](https://github.com/user-attachments/assets/79bdfd4a-c6e9-45d4-83da-f8f6af3c67c5)
### 2. Bar Chart 
This visualization represents sales revenue by region. It allows for better insights into sales performance across different areas.
![Bar chart](https://github.com/user-attachments/assets/7e0324a6-0cb2-443c-bceb-15caf36bc4ed)
