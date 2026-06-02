import pandas as pd
from pathlib import Path

print("=" * 60)
print("MUTUAL FUND ANALYTICS PLATFORM")
print("DAY 1 - DATA INGESTION")
print("=" * 60)

DATA_DIR = Path("data/raw")

csv_files = list(DATA_DIR.glob("*.csv"))

for file in csv_files:

    print("\n" + "=" * 60)
    print(f"Dataset: {file.name}")
    print("=" * 60)

    try:
        df = pd.read_csv(file)

        print("\nShape:")
        print(df.shape)

        print("\nData Types:")
        print(df.dtypes)

        print("\nFirst 5 Rows:")
        print(df.head())

        print("\nMissing Values:")
        print(df.isnull().sum())

        print("\nDuplicate Rows:")
        print(df.duplicated().sum())

    except Exception as e:
        print(f"Error reading {file.name}: {e}")
print("\n" + "="*60)
print("FUND MASTER EXPLORATION")
print("="*60)

fund_master = pd.read_csv("data/raw/01_fund_master.csv")

print("\nColumns:")

print(fund_master.columns)
print("\n" + "=" * 60)
print("FUND MASTER EXPLORATION")
print("=" * 60)

fund_master = pd.read_csv("data/raw/01_fund_master.csv")

print("\nUnique Fund Houses:")
print(fund_master["fund_house"].unique())

print("\nUnique Categories:")
print(fund_master["category"].unique())

print("\nUnique Sub Categories:")
print(fund_master["sub_category"].unique())

print("\nUnique Risk Categories:")
print(fund_master["risk_category"].unique())
print("\n" + "=" * 60)
print("AMFI CODE VALIDATION")
print("=" * 60)

nav_history = pd.read_csv("data/raw/02_nav_history.csv")

print("\nNAV History Columns:")
print(nav_history.columns)
# AMFI CODE VALIDATION

fund_codes = set(fund_master["amfi_code"])
nav_codes = set(nav_history["amfi_code"])

missing_codes = fund_codes - nav_codes

print("\nTotal Fund Master Codes:", len(fund_codes))
print("Total NAV Codes:", len(nav_codes))

if len(missing_codes) == 0:
    print("\n✅ All AMFI codes from fund_master exist in nav_history.")
else:
    print("\n❌ Missing AMFI Codes:")
    print(missing_codes)
print("\n" + "=" * 60)
print("DATA QUALITY SUMMARY")
print("=" * 60)

print("""
1. Successfully loaded all 10 datasets.

2. No duplicate records found in any dataset.

3. No missing values found in most datasets.

4. Dataset 04_monthly_sip_inflows.csv contains 12 missing values
   in yoy_growth_pct column. This is expected because the first
   year does not have a previous year for comparison.

5. All 40 AMFI scheme codes from fund_master are present
   in nav_history.

6. Fund Master contains:
   - 10 Fund Houses
   - 2 Categories
   - 12 Sub Categories
   - 5 Risk Categories

7. Dataset is suitable for ETL, analytics, and dashboarding.
""")