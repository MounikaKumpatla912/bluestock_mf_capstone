import pandas as pd
from sqlalchemy import create_engine
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

RAW = BASE_DIR / "data" / "raw"
PROCESSED = BASE_DIR / "data" / "processed"
DB = BASE_DIR / "data" / "db"

DB.mkdir(exist_ok=True)

engine = create_engine(
    f"sqlite:///{DB/'bluestock_mf.db'}"
)

print("Loading datasets...")

fund_df = pd.read_csv(RAW / "01_fund_master.csv")
nav_df = pd.read_csv(PROCESSED / "02_nav_history_cleaned.csv")
txn_df = pd.read_csv(PROCESSED / "08_investor_transactions_cleaned.csv")
perf_df = pd.read_csv(PROCESSED / "07_scheme_performance_cleaned.csv")
aum_df = pd.read_csv(RAW / "03_aum_by_fund_house.csv")

fund_df.to_sql(
    "dim_fund",
    engine,
    if_exists="replace",
    index=False
)

nav_df.to_sql(
    "fact_nav",
    engine,
    if_exists="replace",
    index=False
)

txn_df.to_sql(
    "fact_transactions",
    engine,
    if_exists="replace",
    index=False
)

perf_df.to_sql(
    "fact_performance",
    engine,
    if_exists="replace",
    index=False
)

aum_df.to_sql(
    "fact_aum",
    engine,
    if_exists="replace",
    index=False
)

print("Database loaded successfully.")