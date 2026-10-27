import pandas as pd
import matplotlib.pyplot as plt
#reading dataset
df=pd.read_csv("data/customers.csv")
print(df)
# #inspection of dataframe
print(df.shape)
print(df.columns)
print(df.head())
print(df.tail())
print(df.dtypes)
df.info()
print("-----DATA QUALITY INSPECTION-----")
print(df.isnull())
print(df.isnull().sum())
print("-------INSPECTION OF UNIQUE VALUES------")
header=df.columns
for column in header:
   print(df[column].unique())
print("-------CONVERT NUMERIC COLUMNS-------")
df["age"]=pd.to_numeric(df["age"],errors="coerce")
df["experience"]=pd.to_numeric(df["experience"],errors="coerce")
print(df)

print("-----FIX PURCHASED------")
df["purchased"]=df["purchased"].map({"1":1,"0":0,"yes":1,"no":0})
df["purchased"]=pd.to_numeric(df["purchased"],errors="coerce")
print(df)
print(df.dtypes)
print(df.isnull().sum())
print("-------CLEAN THE MISSING VALUE-----------")

median_salary=df["salary"].median()
df=df.dropna(subset=["age","experience"])
df["salary"]=df["salary"].fillna(median_salary)
print(df[df.isnull().any(axis=1)])

print("------CLEANED DATASET--------")
print(df)
print("-------missing values------")
print(df.isnull().sum())
print("---------DATA SUMMARY------")
print(f"rows: {len(df)} \n columns : {len(df.columns)}")
print("--------validate values------")
invalid_age=df[df["age"]<=0]
invalid_salary=df[df["salary"]<=0]
invalid_experience=df[df["experience"]<=0]
invalid_purchased=df[~df["purchased"].isin([0,1])]
print(f"the inavlid age record : {invalid_age}")
print(f"the inavlid salary record : {invalid_salary}")
print(f"the inavlid experience record : {invalid_experience}")
print(f"the invalid purchase record : {invalid_purchased}")

print("----validation report-------")
validation_report={
    "inavalid age": len(invalid_age),
    "inavalid salary":len(invalid_salary),
    "invalid experience":len(invalid_experience),
    "invalid purchase":len(invalid_purchased)
}
total_rows=len(df)
for check,count in validation_report.items():
    percentage=(count/total_rows)*100
    print(f"{check}:{count} invalid records ({percentage:.2f}%)")

print("----- BASIC STATISTICS -----")

print(df["age"].describe())
print(df["salary"].describe())
print(df["experience"].describe())

print("----- PURCHASE ANALYSIS -----")

print(df["purchased"].value_counts())
print(df["purchased"].value_counts(normalize=True) * 100)


print("----- AVERAGE SALARY BY PURCHASE STATUS -----")

salary_by_purchase=df.groupby("purchased")["salary"].mean()
print(salary_by_purchase)
print(f"difference: {salary_by_purchase.loc[1]-salary_by_purchase.loc[0]}")

print("----- AVERAGE AGE BY PURCHASE STATUS -----")
print(df.groupby("purchased")["age"].mean())

print("----- AGE STATISTICS BY PURCHASE STATUS -----")
print(df.groupby("purchased")["age"].agg(["count","mean","median","min","max"]))

df.boxplot(column="age", by="purchased")
plt.title("age distribution by pruchase status")
plt.suptitle("")
plt.xlabel("purchased (0=no and 1=yes)")
plt.ylabel("age")
plt.show()

age_summary=df.groupby("purchased")["age"].agg(["min","median","max"])
print(age_summary)

age_quartile =df.groupby("purchased")["age"].agg(
    Q1=lambda x:x.quantile(0.25),
    Q3=lambda x:x.quantile(0.75)
)

age_quartile["IQR"]=age_quartile["Q3"]-age_quartile["Q1"]
print(age_quartile)


