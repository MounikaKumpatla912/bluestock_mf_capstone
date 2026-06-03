# Data Dictionary

## 01_fund_master.csv

| Column | Type | Description |
|----------|----------|----------|
| amfi_code | Integer | Unique AMFI scheme code |
| fund_house | Text | Fund house name |
| scheme_name | Text | Scheme name |
| category | Text | Equity / Debt |
| sub_category | Text | Fund sub category |
| benchmark | Text | Benchmark index |
| risk_category | Text | Risk level |

---

## 02_nav_history.csv

| Column | Type | Description |
|----------|----------|----------|
| amfi_code | Integer | Scheme code |
| date | Date | NAV date |
| nav | Float | Net Asset Value |

---

## 03_aum_by_fund_house.csv

| Column | Type | Description |
|----------|----------|----------|
| date | Date | Quarter end |
| fund_house | Text | AMC Name |
| aum_crore | Float | Assets under management |

---

## 07_scheme_performance.csv

| Column | Type | Description |
|----------|----------|----------|
| return_1yr_pct | Float | 1 Year Return |
| return_3yr_pct | Float | 3 Year Return |
| return_5yr_pct | Float | 5 Year Return |
| sharpe_ratio | Float | Sharpe Ratio |
| sortino_ratio | Float | Sortino Ratio |
| alpha | Float | Alpha |
| beta | Float | Beta |
| max_drawdown_pct | Float | Maximum Drawdown |

---

## 08_investor_transactions.csv

| Column | Type | Description |
|----------|----------|----------|
| investor_id | Text | Investor ID |
| transaction_date | Date | Transaction Date |
| transaction_type | Text | SIP/Lumpsum/Redemption |
| amount_inr | Float | Transaction Amount |
| state | Text | Investor State |
| city | Text | Investor City |
| city_tier | Text | Tier Classification |
| annual_income_lakh | Float | Annual Income |
| kyc_status | Text | Verified/Pending |

Source:
- AMFI India
- mfapi.in
- Bluestock Capstone Dataset