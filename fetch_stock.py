import requests
import time
import json
import os

os.makedirs("../data", exist_ok=True)

headers = {
    "User-Agent": "Mozilla/5.0"
}

stocks = ["AAPL", "MSFT", "GOOGL", "AMZN"]

while True:
    for stock in stocks:
        try:
            url = f"https://query1.finance.yahoo.com/v8/finance/chart/{stock}"
            response = requests.get(url, headers=headers)

            data_json = response.json()

            price = data_json["chart"]["result"][0]["meta"]["regularMarketPrice"]

            data = {
                "stock": stock,
                "price": price,
                "timestamp": time.time()
            }

            print(data)

            with open("../data/stock_data.json", "a") as f:
                f.write(json.dumps(data) + "\n")

        except Exception as e:
            print(f"Error in {stock}:", e)

    time.sleep(10)