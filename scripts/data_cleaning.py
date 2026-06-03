import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

RAW_DATA = BASE_DIR / "data" / "raw"
PROCESSED_DATA = BASE_DIR / "data" / "processed"

PROCESSED_DATA.mkdir(exist_ok=True)

print("====================================")
print("DAY 2 - DATA CLEANING STARTED")
print("====================================")
print("\nLoading NAV History Dataset...")

nav_df = pd.read_csv(RAW_DATA / "02_nav_history.csv")

print("Shape:", nav_df.shape)
print(nav_df.head())
print("\nConverting date column to datetime...")

nav_df["date"] = pd.to_datetime(nav_df["date"])

print(nav_df.dtypes)
print("\nSorting data...")

nav_df = nav_df.sort_values(
    by=["amfi_code", "date"]
)

print("Sorting completed.")
print("\nChecking duplicates...")

before = len(nav_df)

nav_df = nav_df.drop_duplicates()

after = len(nav_df)

print("Duplicates removed:", before - after)
print("\nChecking NAV values...")

invalid_nav = nav_df[nav_df["nav"] <= 0]

print("Invalid NAV rows:", len(invalid_nav))
print("\nForward filling missing NAV values...")

nav_df["nav"] = nav_df.groupby("amfi_code")["nav"].ffill()

print("Forward fill completed.")
print("\nSaving cleaned NAV dataset...")

nav_df.to_csv(
    PROCESSED_DATA / "02_nav_history_cleaned.csv",
    index=False
)

print("Cleaned NAV file saved.")
print("\nDATA QUALITY SUMMARY")

print(f"Total Rows: {len(nav_df)}")
print(f"Missing NAV Values: {nav_df['nav'].isnull().sum()}")
print(f"Duplicate Rows: {nav_df.duplicated().sum()}")
print(f"Invalid NAV Values: {(nav_df['nav'] <= 0).sum()}")
print("\n====================================")
print("CLEANING INVESTOR TRANSACTIONS")
print("====================================")

txn_df = pd.read_csv(
    RAW_DATA / "08_investor_transactions.csv"
)

print("Shape:", txn_df.shape)
print(txn_df.head())
print("\nConverting transaction date...")

txn_df["transaction_date"] = pd.to_datetime(
    txn_df["transaction_date"]
)

print(txn_df.dtypes)
print("\nUnique Transaction Types Before:")

print(txn_df["transaction_type"].unique())
print("\nChecking transaction amounts...")

invalid_amounts = txn_df[txn_df["amount_inr"] <= 0]

print("Invalid Amount Rows:", len(invalid_amounts))
print("\nUnique KYC Status Values:")

print(txn_df["kyc_status"].unique())
print("\nChecking transaction duplicates...")

before = len(txn_df)

txn_df = txn_df.drop_duplicates()

after = len(txn_df)

print("Duplicates removed:", before - after)
print("\nSaving cleaned transactions dataset...")

txn_df.to_csv(
    PROCESSED_DATA / "08_investor_transactions_cleaned.csv",
    index=False
)

print("Transactions file saved.")
print("\n====================================")
print("CLEANING SCHEME PERFORMANCE")
print("====================================")

perf_df = pd.read_csv(
    RAW_DATA / "07_scheme_performance.csv"
)

print("Shape:", perf_df.shape)
print(perf_df.head())
print("\nMissing Values:")

print(perf_df.isnull().sum())
print("\nChecking Return Columns...")

return_columns = [
    "return_1yr_pct",
    "return_3yr_pct",
    "return_5yr_pct"
]

for col in return_columns:
    print(f"{col} datatype:", perf_df[col].dtype)
print("\nChecking Expense Ratio Range...")

invalid_expense = perf_df[
    (perf_df["expense_ratio_pct"] < 0.1)
    |
    (perf_df["expense_ratio_pct"] > 2.5)
]

print("Invalid Expense Ratio Rows:", len(invalid_expense))
print("\nSaving cleaned performance dataset...")

perf_df.to_csv(
    PROCESSED_DATA / "07_scheme_performance_cleaned.csv",
    index=False
)

print("Performance file saved.")