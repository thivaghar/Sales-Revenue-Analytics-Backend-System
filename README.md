
# Sales-Revenue-Analytics-Backend-System



CSV Data
   ↓
Python (pandas) – Cleaning & Validation
   ↓
MySQL Staging Table
   ↓
MySQL Core Tables (Normalized Schema)
   ↓
SQL Analytics
   ↓
Flask REST APIs (JSON)



**Analytics Implemented**
Total Revenue |
Monthly Revenue Trend |
Month-over-Month (MoM) Growth (window functions) |
Revenue by Category |
Revenue by Region |
Average Order Value (AOV)


**REST API Endpoints**

| Endpoint                   | Description                 |
| -------------------------- | --------------------------- |
| `/api/total-revenue`       | Returns total revenue       |
| `/api/monthly-revenue`     | Monthly revenue trend       |
| `/api/mom-growth`          | Month-over-month growth     |
| `/api/revenue-by-category` | Revenue by product category |
| `/api/revenue-by-region`   | Revenue by region           |
| `/api/average-order-value` | Average order value         |

