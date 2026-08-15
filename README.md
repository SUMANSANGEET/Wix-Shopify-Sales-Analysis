# 🛍️ Shopify Sales Analytics Dashboard

**An end-to-end Power BI analytics solution turning raw Shopify e-commerce data into actionable revenue, customer, and product insights.**

[![Power BI](https://img.shields.io/badge/Power%20BI-F2C811?style=for-the-badge&logo=powerbi&logoColor=black)](https://powerbi.microsoft.com/)
[![DAX](https://img.shields.io/badge/DAX-217346?style=for-the-badge&logo=microsoftexcel&logoColor=white)](https://learn.microsoft.com/en-us/dax/)
[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io/)
[![Data Source](https://img.shields.io/badge/Data-Shopify-95BF47?style=for-the-badge&logo=shopify&logoColor=white)](#)

🔗 **[Live Interactive Demo →](https://wix-shopify-sales-analysis-tw8dnzyuqy46fzhhwtecrm.streamlit.app/)**

---

## 📌 Overview

This project is a multi-page **Power BI** dashboard built on top of Shopify order and customer data. It's designed to give e-commerce stakeholders (marketing, merchandising, and leadership teams) a single source of truth for **revenue performance, customer retention, and product/regional trends** — paired with a lightweight **Streamlit** app for interactive, web-based exploration.

The report goes beyond static charts: each analytical page includes **narrative "insight" call-outs** written alongside the visuals, translating chart patterns into business takeaways — a habit borrowed from real analyst-facing reporting.

**Why this project?**
This was built to demonstrate practical, job-ready BI skills: data modeling, DAX measure design, UX-driven dashboard layout, and the ability to communicate insight — not just display numbers.

---

## 🖼️ Dashboard Preview

### 1. Executive Overview
KPI summary, revenue trend, product and city breakdown, and a live drill-through customer table.

![Main Dashboard](screenshots/01-main-dashboard.png)

### 2. Insights & Trends — Product & Regional Performance
Revenue-by-product treemap, AOV vs. order volume scatter analysis, product ranking over time, and a revenue-by-city map — each with a written insight panel.

![Insights & Trends](screenshots/02-insights-trends.png)

### 3. Revenue Volatility & Customer Retention Funnel
Waterfall breakdown of monthly revenue swings and a funnel tracking customers from first purchase through repeat and high-value status.

![Revenue & Retention](screenshots/03-revenue-retention.png)

### 4. Product × City Performance Matrix
A cross-tab matrix of revenue by product category and city, plus a revenue-growth-vs-target gauge.

![Product & City Performance](screenshots/04-product-city-performance.png)

---

## 🧭 Report Structure

| Page | Purpose | Key Visuals |
|---|---|---|
| **Shopify Sales Analytics Dashboard** | Executive summary / landing page | KPI cards, revenue trend line, revenue-by-product bar, customer distribution donut, revenue growth KPI, drill-through customer table |
| **Insights & Trends (I)** | Product & regional deep-dive | Treemap, scatter (AOV vs. Orders), ribbon chart (product ranking over time), map (revenue by city) |
| **Insights & Trends (II)** | Revenue volatility & retention | Waterfall chart, customer retention funnel |
| **Insights & Trends (III)** | Cross-dimensional performance | Product × City matrix table, revenue growth vs. target gauge |

**36 visuals across 4 pages**, including KPI cards, slicers, a treemap, waterfall, funnel, ribbon chart, scatter plot, map, pivot/matrix table, and gauge — chosen deliberately to fit the analytical purpose of each page rather than repeating one chart type throughout.

---

## 📊 Data Model

| Table | Role |
|---|---|
| `shopify_sales` | Core fact table — order-level transactions (Customer ID, City, Product Type, revenue) |
| `Date` | Date dimension table hosting the primary DAX measures |
| `Funnel Stage` | Lookup table driving the customer retention funnel stages |
| `Table1` / `Weekday Table` | Supporting dimension tables |

**Key measures (DAX):**
`Total Revenue` · `Total Orders` · `Unique Customers` · `AOV (Average Order Value)` · `Revenue Growth %` · `Revenue Target` · `Revenue Per Customer` · `Customer Revenue` · `CLV (Customer Lifetime Value)` · `Purchase Frequency` · `Repeat Customers` · `Repeat Purchase Rate`

---

## 🔍 Sample Insights Surfaced

- A small subset of product categories (Running, Walking, and Cycling Shoes) generate the majority of total revenue — informing inventory and promotional prioritization.
- Months with both high order volume **and** high AOV were identified as the strongest revenue contributors, flagged for campaign replication.
- Of ~10,000 customers, only a fraction convert to repeat buyers and an even smaller group become high-value customers — pinpointing where loyalty/retention programs would have the most leverage.
- City-level and product-level cross analysis highlights regional demand differences to support localized marketing and stocking decisions.

---

## 🛠️ Tech Stack

- **Power BI Desktop** — data modeling, DAX, report design
- **Power Query** — data shaping/transformation
- **DAX** — custom measures for revenue, retention, and customer-value KPIs
- **Streamlit** — companion interactive web app for lightweight access without Power BI Desktop
- **Shopify export data** — order, customer, and product-level source data

---

## 🚀 Getting Started

1. Clone this repository
2. Open `Shopify_Sales_Analytics_Dashboard.pbix` in **Power BI Desktop**
3. Refresh the data source connection under **Transform Data → Data Source Settings**
4. Explore all four report pages via the tabs at the bottom of the canvas

Or skip the install — explore the **[live Streamlit version](https://wix-shopify-sales-analysis-tw8dnzyuqy46fzhhwtecrm.streamlit.app/)** directly in your browser.

---

## 📈 Roadmap / Next Iteration

- [ ] Resolve blank/placeholder values on the Revenue Growth KPI and gauge visual
- [ ] Add RLS (row-level security) for regional stakeholder access
- [ ] Incorporate a cohort-based retention analysis
- [ ] Automate refresh via Power BI Service scheduled refresh / dataflow

---

## 👤 Author

**[Your Name]**
📧 [your.email@example.com](mailto:your.email@example.com) · 🔗 [LinkedIn](https://linkedin.com/in/yourprofile) · 💼 [Portfolio](https://yourportfolio.com)

*Open to Data Analyst / BI Analyst opportunities — feel free to reach out.*

---

⭐ If you found this project useful or interesting, consider giving it a star!
