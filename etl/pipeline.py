import pandas as pd
from pathlib import Path

def load_data(path):
    print("Loading data from {path}")
    df = pd.read_csv(path, parse_dates=["order_datetime"])
    return df

def clean_data(df):
    print("Cleaning data")
    df = df.dropna(subset=["item_name", "price", "quantity"])
    df["total_price"] = df["price"] * df["quantity"]
    return df

def aggregate_sales(df):
    print("Aggregating daily sales")
    daily = df.groupby(["restaurant_name", df["order_datetime"].dt.date]).agg({
        "total_price": "sum"
    }).reset_index().rename(columns={"order_datetime": "date"})
    return daily

if __name__ == "__main__":
    orders_path = Path("data/orders.csv").resolve()
    df = load_data(orders_path)
    df = clean_data(df)
    daily_sales = aggregate_sales(df)
    output_path = Path("data/daily_sales.csv").resolve()
    daily_sales.to_csv(output_path, index=False)
    print("ETL complete! Saved aggregated data to {output_path}")
