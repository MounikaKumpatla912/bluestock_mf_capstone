# Data Dictionary

## 01_fund_master.csv

| Column | Data Type | Description |
|----------|----------|-------------|
| amfi_code | Integer | Unique AMFI scheme code |
| fund_house | Text | Mutual fund company |
| scheme_name | Text | Name of scheme |
| category | Text | Equity or Debt |
| sub_category | Text | Large Cap, Small Cap etc |
| plan | Text | Direct or Regular |
| launch_date | Date | Scheme launch date |
| benchmark | Text | Benchmark index |
| expense_ratio_pct | Float | Expense ratio percentage |
| exit_load_pct | Float | Exit load percentage |
| min_sip_amount | Integer | Minimum SIP amount |
| min_lumpsum_amount | Integer | Minimum lump sum amount |
| fund_manager | Text | Fund manager name |
| risk_category | Text | Risk category |
| sebi_category_code | Text | SEBI category code |

## 02_nav_history.csv

| Column | Data Type | Description |
|----------|----------|-------------|
| amfi_code | Integer | AMFI scheme code |
| date | Date | NAV date |
| nav | Float | Net Asset Value |

## 03_aum_by_fund_house.csv

| Column | Data Type | Description |
|----------|----------|-------------|
| date | Date | Reporting date |
| fund_house | Text | Fund house |
| aum_lakh_crore | Float | AUM in lakh crore |
| aum_crore | Integer | AUM in crore |
| num_schemes | Integer | Number of schemes |

## 04_monthly_sip_inflows.csv

| Column | Data Type | Description |
|----------|----------|-------------|
| month | Text | Month |
| sip_inflow_crore | Integer | SIP inflow amount |
| active_sip_accounts_crore | Float | Active SIP accounts |
| new_sip_accounts_lakh | Float | New SIP accounts |
| sip_aum_lakh_crore | Float | SIP AUM |
| yoy_growth_pct | Float | Year-on-year growth |

## 05_category_inflows.csv

| Column | Data Type | Description |
|----------|----------|-------------|
| month | Text | Month |
| category | Text | Fund category |
| net_inflow_crore | Float | Net inflow amount |

## 06_industry_folio_count.csv

| Column | Data Type | Description |
|----------|----------|-------------|
| month | Text | Month |
| total_folios_crore | Float | Total folios |
| equity_folios_crore | Float | Equity folios |
| debt_folios_crore | Float | Debt folios |
| hybrid_folios_crore | Float | Hybrid folios |
| others_folios_crore | Float | Other folios |

## 07_scheme_performance.csv

| Column | Data Type | Description |
|----------|----------|-------------|
| amfi_code | Integer | AMFI code |
| return_1yr_pct | Float | 1 Year Return |
| return_3yr_pct | Float | 3 Year Return |
| return_5yr_pct | Float | 5 Year Return |
| alpha | Float | Alpha |
| beta | Float | Beta |
| sharpe_ratio | Float | Sharpe Ratio |
| sortino_ratio | Float | Sortino Ratio |
| std_dev_ann_pct | Float | Annual Std Dev |
| max_drawdown_pct | Float | Maximum Drawdown |

## 08_investor_transactions.csv

| Column | Data Type | Description |
|----------|----------|-------------|
| investor_id | Text | Investor ID |
| transaction_date | Date | Transaction date |
| transaction_type | Text | SIP/Lumpsum/Redemption |
| amount_inr | Integer | Transaction amount |
| state | Text | Investor state |
| city | Text | Investor city |
| age_group | Text | Investor age group |
| gender | Text | Investor gender |

## 09_portfolio_holdings.csv

| Column | Data Type | Description |
|----------|----------|-------------|
| amfi_code | Integer | AMFI code |
| stock_symbol | Text | Stock symbol |
| stock_name | Text | Company name |
| sector | Text | Sector |
| weight_pct | Float | Portfolio weight |

## 10_benchmark_indices.csv

| Column | Data Type | Description |
|----------|----------|-------------|
| date | Date | Index date |
| index_name | Text | Index name |
| close_value | Float | Closing value |