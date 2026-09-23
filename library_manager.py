import pandas as pd

df = pd.read_excel(r"C:\Users\User\Desktop\تورم مواد غذایی ایران پروژه.xlsx")

print(df.head())

df.columns = df.columns.str.strip()

df.columns = df.columns.str.strip()

df["ماه"] = (
    df["ماه"]
    .astype(str)
    .str.strip()
    .str.replace(r"\s+", " ", regex=True)
)

df["ماه"] = df["ماه"].str.replace("خرداد1405", "خرداد 1405")

month_order = {
    "دی 1404": 1,
    "بهمن 1404": 2,
    "اسفند 1404": 3,
    "فروردین 1405": 4,
    "اردیبهشت 1405": 5,
    "خرداد 1405": 6
}

df["ترتیب زمانی"] = df["ماه"].map(month_order)

print(df[["ماه", "ترتیب زمانی"]].drop_duplicates())

print(df[["ماه", "ترتیب زمانی"]].drop_duplicates())