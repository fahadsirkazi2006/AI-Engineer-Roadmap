from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#finding the project folder and dataset
PROJECT_DIR = Path(__file__).resolve().parent.parent
DATA_PATH = PROJECT_DIR/ "data" /"online_retail.xlsx"

#loading the excel file
df=pd.read_excel(DATA_PATH)

#INSPECTING FIRST 5 ROWS
# print(df.head())
#DATASET DIMENSIONS
# print(f"dataset dimensions: {df.shape} ")
# print(f"total rows : {df.shape[0]} ")

#inspecting datatype and missing values
# print(df.info())

# print("------Missing values-------")
# print(f"total missing values: {df.isnull().sum()}")

# print("---------missing value report--------")
# missing_count = df.isnull().sum()
# missing_percentage = ((missing_count/len(df))*100)
# print(missing_percentage.round(2))

# print("-----QUANTITY STATISTICS--------")
# print(df["Quantity"].describe())

# print("------UnitPrice statistics-------")
# print(df["UnitPrice"].describe())

print("-------negative value count---------")
negative_quantity = (df["Quantity"]<0).sum()
negative_price = (df["UnitPrice"]<0).sum()
print(f"negative quantity= {negative_quantity}")
print(f"negative price = {negative_price}")

#INSPECTING -VE QUANTITY TRANSACTION
print("negative QUANTITY EXAMPLE")
negative_rows = df[df["Quantity"]<0]

print(negative_rows[["InvoiceNo","StockCode","Description","Quantity","UnitPrice"]].head(10))

print("invoice no. starting with c")
print(negative_rows["InvoiceNo"].astype(str)
      .str.startswith("C").sum()
      )

#creating REVENUE COLUMN
df["Revenue"]=df["Quantity"]*df["UnitPrice"]
print("REVENUE STATISTICS")
print(df["Revenue"].describe())

print("Total lines in the row")
print(df["Revenue"].sum())

#identify cancellation invoice
is_cancellation = df["InvoiceNo"].astype(str).str.startswith("C")


#raw revenue
raw_revenue = df["Revenue"].sum()

#revenue without cancelation invoice
revenue_without_cancellation =  df.loc[~is_cancellation,"Revenue"].sum()
print(f"Raw revenue: {raw_revenue:,.2f}")
print(f"cancellation invoice rows: {is_cancellation.sum()}")
print(f"revenue without cancellation invoice: {revenue_without_cancellation:,.2f}")
#verifying the metrics
cancellation_revenue = df.loc[is_cancellation,"Revenue"].sum()
print(f"revenue of cancellation invoice : {cancellation_revenue:,.2f}")
print(f"reconcillation : {round(revenue_without_cancellation+cancellation_revenue,2)}")
print("negative price record")
negative_price_rows = df[df["UnitPrice"]<0]

print(negative_price_rows[["InvoiceNo","StockCode","Description","Quantity","UnitPrice","Revenue"]])

#creating a sales only dataset
is_bad_debt = df["Description"].eq("Adjust bad debt")
sales_df = df.loc[~is_cancellation&~is_bad_debt].copy()
print(f"total no. of rows in raw dataset:{len(df)}")
print(f"total no. ofrows in sales df: {len(sales_df)}")
print(f"total revenue of sales_df : {sales_df["Revenue"].sum():,.2f}")
#checking for -ve quantity in sales  df
nonPositive_quantity = sales_df[sales_df["Quantity"]<0]
print(f"total no. of -ve quantity is :{len(nonPositive_quantity)}")

print("example")
print(
    nonPositive_quantity[["InvoiceNo","StockCode","Description","Quantity","UnitPrice","Revenue"]
].head(10))

#checking for zero or negative price in sales df
nonPositive_price= sales_df[sales_df["UnitPrice"]<=0]
print(f"total no. of rows with zero or negative price is :{len(nonPositive_price)}")
print("example")
print(
    nonPositive_price[["InvoiceNo","Description","Quantity","UnitPrice","Revenue"]
].head(10))
#catogarize unusual transaction
print("negative quantity by description")
print(
    sales_df.loc[sales_df["Quantity"]<0,"Description"]
    .fillna("MISSING DESCRIPTION")
    .value_counts()
    .head(10)
)

print("negative & 0 Price by invoice prefix")
print(
    sales_df.loc[sales_df["Quantity"]<0,"InvoiceNo"]
    .astype(str)
    .str[0]
    .value_counts()
)

print("unit price destribution")
print(f"zero price rows: {(sales_df["UnitPrice"]==0).sum()}")
print(f"negative price rows:{(sales_df["UnitPrice"]<0).sum()}")
print(f"positive price rows :{(sales_df["UnitPrice"]).sum()}")

#create negative quantitty df
negative_quantity_df= sales_df.loc[sales_df["Quantity"]<0].copy()

print("negative QUANTITY:  price BREAKDOWN")
print(f"negative quantity prices : {negative_quantity_df["UnitPrice"].value_counts(dropna=False) }")
print("Negative Quantity Revenue")
print(f"Negative Quantity revenue : {(negative_quantity_df["Revenue"]).sum()}")
print("negative quantity by description catogary ")
print(negative_quantity_df["Description"].fillna("MISSING DESCRIPTION").str.strip().str.lower().value_counts().head(20))
#create the product sales dataset
is_positive_quantity = sales_df["Quantity"]>0
is_positive_price = sales_df["UnitPrice"]>0
product_sales_df = sales_df.loc[is_positive_quantity & is_positive_price].copy()
print(f"Row before filtering : {len(sales_df)}")
print(f"rows after filtering : {len(product_sales_df)}")
print(f"no. of rows excluded : {len(sales_df) - len(product_sales_df)}")
print(f"product sales revenue : {(product_sales_df["Revenue"].sum()):,.2f}")
print("========validation check====")
print(f"Non positive Quantity remaining:{(product_sales_df["Quantity"]<=0).sum()}")
print(f"non positive Price:{(product_sales_df["UnitPrice"]<=0).sum()}")
print(f"original number of rows:{len(sales_df)}")
#calculate monthly revenue
#create a monthly datase
monthly_df= product_sales_df.copy()
monthly_df["Month"]=(
    monthly_df["InvoiceDate"].dt.to_period("M")
)
monthly_revenue = (monthly_df.groupby("Month")["Revenue"].sum().sort_index())
print(f"========Monthly revenue=======")
print(monthly_revenue)
print(f"Highest revenue month")
print(monthly_revenue.idxmax(), monthly_revenue.max())
print(f"lowest revenue month")
print(monthly_revenue.idxmin(),monthly_revenue.min())
#plot monmthly revenue
monthly_revenue.index=monthly_revenue.index.astype(str)
monthly_revenue.plot(kind="line",marker="o")
plt.title("Montly Product Sales Revenue (2010-2011)")
plt.xlabel("Months")
plt.ylabel("Revenue(£)")
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.savefig("reports/monthly_revenue.png",dpi=150)
plt.show()
#investigating monthly invoice activity
monthly_metrics = (
    product_sales_df.assign(
        Month = product_sales_df["InvoiceDate"].dt.to_period("M")
    ).groupby("Month")
    .agg(
        Total_revenue=("Revenue","sum"),
        Unique_Invoices=("InvoiceNo","nunique"),
        Total_Quantity=("Quantity","sum")

    )
)
monthly_metrics["Average_invoice_value"]=(
    monthly_metrics["Total_revenue"]/monthly_metrics["Unique_Invoices"]
)

print("Monthly Business Metrics")
print(monthly_metrics.round(2))
#month over month change
monthly_metrics["Revenue_change%"]=(
    monthly_metrics["Total_revenue"].pct_change()*100
)
monthly_metrics["Invoices_change%"]=(
    monthly_metrics["Unique_Invoices"].pct_change()*100

)
print("======MONTH OVER MONTH CHANGES========")
print(
    monthly_metrics[
        ["Total_revenue","Unique_Invoices","Revenue_change%","Invoices_change%"]
    ].round(2).tail(5)
)
#monthly invoice activity
monthly_invoice = monthly_metrics["Unique_Invoices"]
plt.figure(figsize=(10,5))
monthly_invoice.plot(kind="line",marker="o")
plt.title("MONTHLY INVOICE ACTIVITY (2010-2011)")
plt.xlabel("Month")
plt.ylabel("number of invoice")
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.savefig("reports/monthly_invoice.png", dpi=150)
plt.show()
#CUSTOMER ANALYSIS
print(
    f"ROWS with missing customer ID:{product_sales_df["CustomerID"].isna().sum()}"
)
print(
    f"rows with known customer Id : {product_sales_df["CustomerID"].notna().sum()}"
)
print(
    f"rows with unique customer ID :{product_sales_df["CustomerID"].nunique()}"
)
print(
    f"percentage of missing customer ID:{(product_sales_df["CustomerID"].isna().mean()*100):,.2f}"
)
#customer revenue analysis
identified_sales=(
    product_sales_df.loc[product_sales_df["CustomerID"].notna()].copy()
)

customer_revenue=(
    identified_sales.groupby("CustomerID").agg(
        
            Total_revenue=("Revenue","sum"),
            Total_quantity=("Quantity","sum"),
            Unique_invoices=("InvoiceNo","nunique")
        
    ).sort_values("Total_revenue",ascending=False)
)

print("TOP 10 CUSTOMERS BY  REVENUE")
print(customer_revenue.head(10).round(2))
print("CUSTOMER REVENUE SUMMARY")
print(customer_revenue["Total_revenue"].describe().round(2))
#customer revenue concentration
Total_identified_revenue= customer_revenue["Total_revenue"].sum()
top_10_revenue=customer_revenue["Total_revenue"].head(10).sum()
top_50_revenue=customer_revenue["Total_revenue"].head(50).sum()
top_10_share = (
    top_10_revenue/Total_identified_revenue
)*100

top_50_share=(
    top_50_revenue/Total_identified_revenue
)*100

print("CUSTOMER REVENUE CONCENTRATION")
print(f"Total identified customer revenue : {Total_identified_revenue :,.2f}")
print(f"Top 10 customer revenue: {top_10_revenue:,.2f}")
print(f"top 10 customer share: {top_10_share:,.2f}")
print(f"top 50 customer share:{top_50_share:,.2f}")
#plot top 10 customer by revenue
top_10_customer = (
    customer_revenue["Total_revenue"].head(10).sort_values()
)

plt.figure(figsize=(10,6))
top_10_customer.plot(kind="barh")
plt.title("TOP 10CUSTOMER BY REVENUE")
plt.xlabel("REVENUE (£)")
plt.ylabel("CustomerID")
plt.tight_layout()
plt.savefig("reports/top_10_customers.png",dpi=150)
plt.show()
#PREPARE DATA FOR RFM
reference_date= (
    product_sales_df["InvoiceDate"].max().normalize() + pd.Timedelta(days=1)
)

print("====RFM ANALYSIS SETUP=====")
print(f"latest transaction : {product_sales_df["InvoiceDate"].max()}")
print(f"Reference Date : {reference_date}")

#cCALCULATE RFM METRICS
rfm=(
    identified_sales.groupby("CustomerID").agg(
        Recency = (
            "InvoiceDate",
            lambda dates: (reference_date-dates.max().normalize()).days

        ),
        Frequency = ("InvoiceNo","nunique"),
        Monetary = ("Revenue","sum")
    )
)

print("====RFM OF FIRST 10 CUSTOMERS======")
print(rfm.head(10).round(2))
print("=====RFM SUMMARY====")
print(rfm.describe().round(2))

#CREATE RFM SCORES
rfm["Recency_Score"]=(
    pd.qcut(rfm["Recency"].rank(method="first"),q=5,labels=[5,4,3,2,1]).astype(int)
)
rfm["Frequency_Score"]=(
    pd.qcut(rfm["Frequency"].rank(method="first"),q=5,labels=[1,2,3,4,5]).astype(int)
)
rfm["Monetary_Score"]=(
    pd.qcut(rfm["Monetary"].rank(method="first"),q=5,labels=[1,2,3,4,5]).astype(int)
)
print("======THE FRM SCORE TABLE OF FIRST 10 CUSTOMERS====")
print(rfm[
    ["Recency","Frequency","Monetary","Recency_Score","Frequency_Score","Monetary_Score"]
].head(10))
print(rfm[["Recency_Score","Frequency_Score","Monetary_Score"]].describe())
print(rfm["Frequency_Score"].value_counts().sort_index())
#putting all score together
rfm["RFM_Score"]=(
    rfm["Recency_Score"].astype(str)+
    rfm["Frequency_Score"].astype(str)+
    rfm["Monetary_Score"].astype(str)
)
print("The combined rfm scores")
print(
    rfm[
        ["Recency_Score","Frequency_Score","Monetary_Score","RFM_Score"]
        
        ].head(10)
)

print("Most Common RFM Scores")
print(rfm["RFM_Score"].value_counts().head())
#CUSTOMER DEGMENTATION
conditions=[
    ((rfm["Recency_Score"]>=4) &
     (rfm["Frequency_Score"]>=4) &
     (rfm["Monetary_Score"]>=4)
     
     ),
     rfm["Frequency_Score"]>=4,
     ((rfm["Recency_Score"]<=2) &
      (rfm["Frequency_Score"]>=3)
      ),
      rfm["Recency_Score"]==3
]
segment_names=[
    "Champions",
    "Loyal_Customers",
    "At Risk",
    "Need_Attention"
]

rfm["Segments"]=np.select(conditions,segment_names,default="Other")

print("Customers segment Count")
print(rfm["Segments"].value_counts())
print("customer segment percentage")
print((rfm["Segments"].value_counts(normalize=True)*100).round(2))
#Join customer segments back to identifiedtransaction record
sales_with_segments = identified_sales.merge(
    rfm[["Segments"]],
    left_on="CustomerID",
    right_index=True,
    how="left"
)
#calculate bussiness metric for each segnent
segment_analysis=(
    sales_with_segments.groupby("Segments")
    .agg(
        Customers=("CustomerID","nunique"),
        revenue=("Revenue","sum"),
        Invoices=("InvoiceNo","nunique")

    )
)

segment_analysis["Revenue_per_Customer"]=segment_analysis["revenue"]/segment_analysis["Customers"]
segment_analysis["Revenue_share_percent"]=(segment_analysis["revenue"]/(segment_analysis["revenue"].sum()))*100
segment_analysis=segment_analysis.sort_values("revenue",ascending=False)
print("==========REVENUE BY CUSTOMER SEGMENT======")
print(segment_analysis.round(10))

rfm.to_csv("reports/customer_rfm_segments.csv")
segment_analysis.to_csv("reports/customer_rfm_summary.csv")
