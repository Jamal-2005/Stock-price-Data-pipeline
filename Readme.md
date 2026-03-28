# 📊 Real-Time Stock Market Data Pipeline

## 📌 Overview
This project demonstrates an end-to-end data engineering pipeline that ingests, processes, and analyzes near real-time stock market data. The system collects stock prices using a public API and performs time-series transformations using PySpark in Databricks to generate actionable insights.

---

## 🎯 Objectives
- Track stock price movements over time  
- Perform time-series analysis on financial data  
- Simulate real-world data engineering workflows  
- Generate trading insights using analytical transformations  

---

## 🏗️ Architecture
Yahoo Finance API → Python Script → JSON Storage → Databricks (PySpark) → Transformations → Insights


---

## ⚙️ Tech Stack

- **Python** – Data ingestion  
- **PySpark** – Data processing & transformations  
- **Databricks** – Distributed data analytics platform  
- **Yahoo Finance API** – Data source  
- **JSON** – Storage format  

---

## 🔄 Data Pipeline

### 1. Data Ingestion
- Fetches stock price data at regular intervals using Python  
- Supports multiple stocks (e.g., AAPL, MSFT, GOOGL, AMZN)  
- Stores data in JSON format  

---

### 2. Data Processing (PySpark)

Performed the following transformations:

- **Timestamp Conversion** → Human-readable time  
- **Percentage Change** → Tracks price movement  
- **Moving Averages**  
  - Short-term (5 records)  
  - Long-term (20 records)  
- **Volatility Calculation** → Measures price fluctuation  
- **Signal Generation**  
  - BUY → Short MA > Long MA  
  - SELL → Short MA < Long MA  
  - HOLD → Otherwise  

---

## 📊 Sample Output

| stock | price | time | percent_change | ma_short | ma_long | volatility | signal |
|------|------|------|----------------|----------|----------|------------|--------|

---

## 🧠 Key Concepts Used

- Window Functions in PySpark  
- Time-Series Data Analysis  
- Moving Average Crossover Strategy  
- Data Pipeline Design  
- Data Transformation and Cleaning  

---

## 🚀 How to Run

### 1. Clone Repository
```bash
git clone https://github.com/your-username/stock-data-pipeline.git
cd stock-data-pipeline
```


### 2. Install Dependencies
pip install requests pyspark

### 3. Run Data Ingestion Script
python scripts/fetch_stock.py

### 4. Run Transformations
--> Upload data to Databricks
--> Run the notebook in databricks/ folder

### 📈 Use Cases
* Financial data analysis
* Trend detection
* Algorithmic trading simulation
* Real-time analytics pipelines

### 🔮 Future Enhancements
* Integrate real-time streaming (Kafka / Kinesis)
* Add dashboard (Power BI / Streamlit)
* Implement alert system for price spikes
* Automate pipeline scheduling

### 👤 Author
Jamal
Aspiring Data Engineer | Python | PySpark | Data Analytics

### ⭐ Acknowledgements
* Yahoo Finance API for providing stock data
* Databricks Community Edition for analytics platform
