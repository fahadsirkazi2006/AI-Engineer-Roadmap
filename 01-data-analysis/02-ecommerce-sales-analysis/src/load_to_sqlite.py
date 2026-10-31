from pathlib import Path
import sqlite3
import pandas as pd 
#rootpath
ROOT = Path(__file__).resolve().parent.parent
DATA_PATH = ROOT/"data"/"online_retail.xlsx"
DB_PATH = ROOT / "data"/"retail_analysis.db"
def main():
    print("Loading excel dataset...")
    df=pd.read_excel(DATA_PATH)
    is_cancellation = df["InvoiceNo"].astype(str).str.startswith("C")
    is_bad_debt = df["Description"].eq("Adjust bad debt")
    df=df.loc[~is_cancellation & ~is_bad_debt].copy()
    df=df.loc[
        (df["Quantity"]>0)&
        (df["UnitPrice"]>0)
    ].copy()
    df["Revenue"] = df["Quantity"]*df["UnitPrice"]
    with sqlite3.connect(DB_PATH) as conn:
        df.to_sql(
            "product_sales",
            conn,
            if_exists="replace",
            index=False
        )
        row_count = pd.read_sql_query(
            "SELECT COUNT(*) AS total_rows FROM product_sales",
            conn
        ).iloc[0]["total_rows"]

        print(f"DATABASE CREATED : {DB_PATH}")
        print(f"ROWS LOADED: {row_count}")
if __name__ == "__main__":
    main()