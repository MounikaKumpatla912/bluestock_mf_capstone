-- 1. Top 5 Funds by AUM
SELECT scheme_name, aum_crore
FROM fact_performance
ORDER BY aum_crore DESC
LIMIT 5;

-- 2. Average NAV by Fund
SELECT amfi_code,
AVG(nav) AS avg_nav
FROM fact_nav
GROUP BY amfi_code;

-- 3. Total Transactions by State
SELECT state,
COUNT(*) AS total_transactions
FROM fact_transactions
GROUP BY state
ORDER BY total_transactions DESC;

-- 4. SIP Transactions Count
SELECT COUNT(*) AS sip_count
FROM fact_transactions
WHERE transaction_type='SIP';

-- 5. Funds with Expense Ratio < 1%
SELECT scheme_name,
expense_ratio_pct
FROM fact_performance
WHERE expense_ratio_pct < 1;

-- 6. Average Amount by Transaction Type
SELECT transaction_type,
AVG(amount_inr) AS avg_amount
FROM fact_transactions
GROUP BY transaction_type;

-- 7. Top 10 Investors by Investment Amount
SELECT investor_id,
SUM(amount_inr) AS total_amount
FROM fact_transactions
GROUP BY investor_id
ORDER BY total_amount DESC
LIMIT 10;

-- 8. Funds with Highest Sharpe Ratio
SELECT scheme_name,
sharpe_ratio
FROM fact_performance
ORDER BY sharpe_ratio DESC
LIMIT 10;

-- 9. State-wise Investment Amount
SELECT state,
SUM(amount_inr) AS total_investment
FROM fact_transactions
GROUP BY state
ORDER BY total_investment DESC;

-- 10. Fund Count by Risk Category
SELECT risk_category,
COUNT(*) AS total_funds
FROM dim_fund
GROUP BY risk_category;