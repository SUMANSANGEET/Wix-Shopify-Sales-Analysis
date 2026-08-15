# 🏃 Shopify Sales Intelligence

**An interactive, cross-filtering Power BI dashboard that turns a raw Shopify transaction export into a decision-ready view of revenue, purchasing behaviour, and customer retention.**

[![Power BI](https://img.shields.io/badge/Power%20BI-F2C811?style=flat-square&logo=powerbi&logoColor=black)](#)
[![DAX](https://img.shields.io/badge/DAX-12%2B%20measures-0B1220?style=flat-square)](#)
[![Power Query](https://img.shields.io/badge/Power%20Query-ETL-217346?style=flat-square)](#)
[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=flat-square&logo=python&logoColor=white)](#)
[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=flat-square&logo=streamlit&logoColor=white)](#)
[![License](https://img.shields.io/badge/license-MIT-green?style=flat-square)](#license)

> **P Suman Sangeet** · Data Analyst & AI Intern, LabMentix · PGDM in Big Data Analytics

---

## 📌 Why this project

This isn't a single chart on a dataset — it's a **4-page, 35-visual Power BI report** built on a working data model (Power Query ETL → a modeled table set → 12+ DAX measures → cards, trend lines, a treemap, a ribbon chart, a scatter, a filled map, a waterfall, a funnel, a matrix, and a gauge), backed by a **Python/Streamlit companion app** so anyone reviewing this repo can explore the same KPIs in a browser without installing Power BI.

| | |
|---|---|
| **Dataset** | Shopify transactions export — 7,431 orders · 4,431 customers · 49 U.S. states |
| **Reporting window** | 18–24 March 2025 (7-day transaction snapshot) |
| **Deliverables** | `Shopify_Sales_Analytics_Dashboard.pbix` (Power BI) + `Wix_Shopify.py` (Streamlit) |
| **Stakeholders** | Store owner / GM, Marketing, Merchandising & Inventory planning |

---

## 🖥️ Live Dashboard (Streamlit companion)

Screenshots of the running Streamlit companion app — same KPIs and logic as the Power BI report — included here so the dashboard is reviewable straight from GitHub.

**Sales & Trends**
![Sales & Trends overview](screenshots/01-overview-sales-trends.png)

**Customers & Retention**
![Customers & Retention](screenshots/02-customers-retention.png)

**Geography**
![Geography](screenshots/03-geography.png)

```bash
pip install -r requirements.txt
streamlit run Wix_Shopify.py
```

---

## 🔢 Headline numbers

| Total Revenue | Total Orders | Avg. Order Value | Unique Customers | Repeat Purchase Rate | Purchase Frequency |
|:---:|:---:|:---:|:---:|:---:|:---:|
| **$4.60M** | **7,431** | **$618.89** | **4,431** | **46.0%** | **1.68 orders** |

---

## 🎯 Business questions the dashboard answers

- How much revenue are we generating, and how is it trending day over day?
- Which products and geographies drive the most (and least) revenue?
- When do customers actually shop — which days and hours should promotions target?
- What share of customers return, and how much more valuable are they than one-time buyers?
- Which customers should be prioritised for retention, and what is their long-term value?

---

## 💡 Key insights & recommendations

**1. Revenue is concentrated in footwear.**
Running Shoes alone drives **35.2% of total revenue** ($1.62M); the top three footwear categories (Running, Tennis, Walking Shoes) account for **71.3%** of sales combined. Accessories, Clogs, Boy's, and Water Shoes together generated just $30K (0.65% of revenue).
> **Recommendation:** Protect Running Shoes inventory availability, test bundled promotions to cross-sell adjacent categories, and review merchandising spend on the bottom four categories.

**2. Repeat customers are the profit engine.**
46% of customers are repeat buyers, yet they generate **67.8% of total revenue** — nearly double their share of the customer base. The top 10% of customers by spend account for only 21.9% of revenue, so retention isn't a small-VIP-tier problem.
> **Recommendation:** Build retention programs that reach the broad Loyal/At-Risk middle segment (62% of customers), not just top spenders.

**3. Demand is geographically concentrated.**
California, Texas, and Florida together contribute **31.9%** of revenue; at the city level, Washington D.C., Houston, and New York City are the top three markets.
> **Recommendation:** Prioritise regional marketing spend and fulfilment decisions around the top states/cities first.

**4. Shopping has a predictable rhythm.**
Monday ($752K) and Saturday ($708K) are the strongest revenue days, Tuesday ($578K) the weakest — roughly a 30% swing. Ordering activity concentrates in the **10 AM – 4 PM** window, peaking at 11 AM (568 orders, $349K).
> **Recommendation:** Shift ad spend, email sends, and flash-sale timing toward Monday/Saturday and the late-morning window rather than spreading it evenly.

**5. The model is built to scale.**
The export covers one week — every trend and growth claim is directionally sound but provisional pending more history. The `Revenue Growth %` measure (built on `DATEADD`) is wired up and will populate automatically once more months of data are loaded.

---

## 🧱 What's actually inside the `.pbix`

Rather than describe the file abstractly, here's what's really in it (verified directly from the report's Layout and data model diagram):

**Tables in the model**

| Table | Role |
|---|---|
| `shopify_sales` | The cleaned order-level export — the main fact table (Order Number, Customer Id, Invoice Date, Product Type, Quantity, City, State, Subtotal/Total/Tax) |
| `Date` | Dedicated calendar table, marked as the model's official Date table; hosts all the DAX measures used across the report |
| `Weekday Table` | Supports day-of-week slicing and analysis |
| `Funnel Stage` | Small lookup table driving the Customer Retention Funnel visual |
| `Table1` | Present in the model but not currently wired into any visual — worth removing or documenting before sharing |

**DAX measures used across the report's visuals:** `Total Revenue`, `Total Orders`, `AOV`, `Unique Customers`, `Repeat Customers`, `Repeat Purchase Rate`, `Purchase Frequency`, `Revenue Growth %`, `Revenue Per Customer`, `Customer Revenue`, `CLV`, `Revenue Target`.

```DAX
Total Revenue = SUM ( shopify_sales[Total Price Usd] )
Total Orders  = DISTINCTCOUNT ( shopify_sales[Order Number] )
AOV           = DIVIDE ( [Total Revenue], [Total Orders], 0 )

Revenue Growth % =
VAR PrevRevenue = CALCULATE ( [Total Revenue], DATEADD ( 'Date'[Date], -1, MONTH ) )
RETURN DIVIDE ( [Total Revenue] - PrevRevenue, PrevRevenue )
```

---

## 📊 Report structure — 4 pages, 35 visuals

**Page 1 — "Shopify Sales Analytics Dashboard"** (19 visuals: the overview page)

| Visual type | What's on it |
|---|---|
| KPI cards ×6 | Total Revenue, Total Orders, AOV, Unique Customers, Repeat Customers, Purchase Frequency |
| KPI visual | Revenue Growth % with target/status formatting |
| Column charts ×3 | Revenue per Customer, CLV, Repeat Purchase Rate |
| Line chart | **Revenue Trend** — Total Revenue by Month/Year |
| Clustered bar chart | **Revenue by Product** — Total Revenue by Product Type |
| Donut chart | **Customer Distribution by City** |
| Table | Customer Id, Total Orders, Customer Revenue |
| Slicers ×4 | Month/Year, Product Type, Customer Id, City — cross-filter every visual on the page |

**Page 2 — "Insights & Trends"** (8 visuals)

| Visual type | What's on it |
|---|---|
| Treemap | **Revenue by Product Type** — proportional revenue view |
| Ribbon chart | **Product Ranking by Revenue Over Time** |
| Scatter chart | **AOV vs Orders Analysis**, bubble-sized by revenue |
| Filled map | **Revenue by City** |

**Page 3 — "Insights & Trends"** (4 visuals)

| Visual type | What's on it |
|---|---|
| Waterfall chart | **Monthly Revenue Change Analysis** — period-over-period bridge |
| Funnel | **Customer Retention Funnel** — Unique → Repeat customers |

**Page 4 — "Insights & Trends"** (4 visuals)

| Visual type | What's on it |
|---|---|
| Pivot table (matrix) | **Product & City Performance** — cross-tab of the two key segment dimensions |
| Gauge | **Revenue Growth vs Target** |

Pages 2–4 each also carry a callout text box with a plain-language insight next to the visual it explains.

> **Before you publish:** the callout text boxes on pages 2–4 currently ship with generic placeholder wording (e.g. referencing "10,000 customers" and "Electronics") left over from the report template — they don't reflect this dataset's real numbers yet. Swap them for the verified figures in the [Key insights](#-key-insights--recommendations) section above before sharing the `.pbix` publicly. It's also worth renaming pages 2–4 (all currently labelled "Insights & Trends") to something more distinct, like *Product & Time*, *Revenue Trends*, and *Geography & Segments*, and removing the unused `Table1` from the model.

---

## 🛠️ Tools & skills demonstrated

- **Data cleaning & ETL** — Power Query: type correction, deduplication, text standardisation on a 7,431-row transactional export.
- **Data modeling** — a `shopify_sales` fact table joined to a dedicated `Date` table (marked as the official date table for correct time-intelligence behaviour), plus a `Weekday Table` and a `Funnel Stage` lookup table.
- **DAX** — 12+ measures spanning revenue, orders, AOV, retention, CLV, and a `DATEADD`-based growth measure.
- **Power BI visualization** — 35 visuals across 4 pages: cards, KPI, line, bar, donut, treemap, ribbon, scatter, map, waterfall, funnel, matrix, and gauge, each mapped to a specific business question.
- **Python** — `pandas` for analysis, `Plotly` for charting, and a custom-themed `Streamlit` app (custom CSS, multi-tab layout, cross-filtering) deployed as a standalone interactive product.
- **Applied analytics** — RFM-style customer segmentation and a documented-assumption CLV model.

---

## 📁 Repository structure

```
├── Shopify_Sales_Analytics_Dashboard.pbix   # Power BI report — 4 pages, 35 visuals, 12+ DAX measures
├── Wix_Shopify.py                           # Streamlit companion dashboard
├── shopify_data.csv                         # Cleaned transaction-level dataset (7,431 rows)
├── Shopify_Sales.xlsx                       # Source/working data in Excel
├── docs/
│   ├── Shopify_Sales_BI_Report.docx         # Full written BI report (stages, DAX, insights)
│   └── Shopify_Store_Owner_Briefing.pptx    # Stakeholder-facing summary deck
├── screenshots/                             # Dashboard screenshots used in this README
└── requirements.txt
```

## 🗂️ Data dictionary

`shopify_data.csv` — one row per order, 10 columns, zero nulls after cleaning:

| Column | Type | Description |
|---|---|---|
| `Order Number` | Whole number | Unique order identifier |
| `Customer Id` | Whole number | Unique customer identifier |
| `Invoice Date` | Date/Time | Timestamp of the order |
| `Product Type` | Text | Product category (14 distinct values, e.g. Running Shoes, Boots) |
| `Quantity` | Whole number | Units purchased on the order |
| `CITY` | Text | Customer's billing city |
| `Billing Address Province` | Text | Customer's billing U.S. state |
| `Subtotal Price` | Decimal | Pre-tax order value (USD) |
| `Total Price Usd` | Decimal | Post-tax order value (USD) |
| `Total Tax` | Decimal | Tax amount (USD) |

---

## ▶️ Getting started

```bash
# 1. Clone the repo
git clone https://github.com/<your-username>/shopify-sales-intelligence.git
cd shopify-sales-intelligence

# 2. Run the Streamlit companion dashboard
pip install -r requirements.txt
streamlit run Wix_Shopify.py

# 3. Explore the full Power BI report
# Open Shopify_Sales_Analytics_Dashboard.pbix in Power BI Desktop
```

**`requirements.txt`**
```
streamlit
pandas
plotly
```

---

## ⚠️ Data scope & limitations

The source export covers **18–24 March 2025** — one week of transactions. Every trend and growth claim is directionally sound but **provisional** pending a full month or more of history. The `Date` table and `Revenue Growth %` measure are already wired up to populate automatically as more data lands — no redesign needed.

---

## 👤 About the author

**P Suman Sangeet** — Data Analyst & AI Intern, LabMentix. PGDM in Big Data Analytics.

- 💼 LinkedIn: `<add your LinkedIn URL>`
- 📧 Email: `<add your email>`
- 🌐 Portfolio: `<add your portfolio URL>`

If you're a recruiter reviewing this project, the fastest path in is: **screenshots above → headline numbers → 5 key insights**. Everything else in this README is supporting detail.

## 📄 License

This project is available under the [MIT License](LICENSE). The underlying transaction data is a synthetic/sample Shopify export used for portfolio purposes only.
