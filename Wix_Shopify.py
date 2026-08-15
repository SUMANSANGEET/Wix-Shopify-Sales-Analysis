import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(page_title="Shopify Sales Intelligence | P Suman", layout="wide",
                    page_icon="🏃", initial_sidebar_state="expanded")

STATE_ABBR = {
    'Alabama': 'AL', 'Alaska': 'AK', 'Arizona': 'AZ', 'Arkansas': 'AR', 'California': 'CA',
    'Colorado': 'CO', 'Connecticut': 'CT', 'Delaware': 'DE', 'District of Columbia': 'DC',
    'Florida': 'FL', 'Georgia': 'GA', 'Hawaii': 'HI', 'Idaho': 'ID', 'Illinois': 'IL',
    'Indiana': 'IN', 'Iowa': 'IA', 'Kansas': 'KS', 'Kentucky': 'KY', 'Louisiana': 'LA',
    'Maine': 'ME', 'Maryland': 'MD', 'Massachusetts': 'MA', 'Michigan': 'MI', 'Minnesota': 'MN',
    'Mississippi': 'MS', 'Missouri': 'MO', 'Montana': 'MT', 'Nebraska': 'NE', 'Nevada': 'NV',
    'New Hampshire': 'NH', 'New Jersey': 'NJ', 'New Mexico': 'NM', 'New York': 'NY',
    'North Carolina': 'NC', 'North Dakota': 'ND', 'Ohio': 'OH', 'Oklahoma': 'OK', 'Oregon': 'OR',
    'Pennsylvania': 'PA', 'Rhode Island': 'RI', 'South Carolina': 'SC', 'South Dakota': 'SD',
    'Tennessee': 'TN', 'Texas': 'TX', 'Utah': 'UT', 'Vermont': 'VT', 'Virginia': 'VA',
    'Washington': 'WA', 'West Virginia': 'WV', 'Wisconsin': 'WI', 'Wyoming': 'WY'
}

# ---------------------------------------------------------------------------
# Design system — "scoreboard" identity for a footwear/athletic-retail brand
# ---------------------------------------------------------------------------
INK = "#0B1220"
SURFACE = "#141B2E"
SURFACE_2 = "#1B2338"
TEXT = "#EDEFF5"
MUTED = "#8A93A8"
SIGNAL = "#17E3B0"
GOLD = "#F5B942"
LINE = "#232C44"

st.markdown(f"""
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@500;600;700&family=Inter:wght@400;500;600&family=JetBrains+Mono:wght@500;600;700&display=swap" rel="stylesheet">
<style>
    html, body, [class*="css"]  {{ font-family: 'Inter', sans-serif; }}
    .stApp {{ background-color: {INK}; color: {TEXT}; }}
    section[data-testid="stSidebar"] {{ background-color: {SURFACE}; border-right: 1px solid {LINE}; }}
    h1, h2, h3 {{ font-family: 'Space Grotesk', sans-serif !important; color: {TEXT} !important; }}
    p, span, label, div {{ color: {TEXT}; }}
    .hero {{
        padding: 28px 32px; margin-bottom: 22px; border-radius: 4px;
        background: linear-gradient(135deg, {SURFACE} 0%, {SURFACE_2} 100%);
        border-left: 3px solid {SIGNAL};
    }}
    .hero-eyebrow {{ font-family:'JetBrains Mono'; font-size:12px; letter-spacing:2px;
        color:{SIGNAL}; text-transform:uppercase; margin-bottom:6px; }}
    .hero-title {{ font-family:'Space Grotesk'; font-size:32px; font-weight:700; margin:0; }}
    .hero-sub {{ color:{MUTED}; font-size:14.5px; margin-top:8px; max-width:760px; line-height:1.5; }}
    .scorecard {{
        background:{SURFACE}; border:1px solid {LINE}; border-bottom:3px solid {SIGNAL};
        border-radius:3px; padding:14px 16px; text-align:left;
    }}
    .scorecard .label {{ font-family:'JetBrains Mono'; font-size:11px; letter-spacing:1px;
        color:{MUTED}; text-transform:uppercase; }}
    .scorecard .value {{ font-family:'JetBrains Mono'; font-size:26px; font-weight:700;
        color:{TEXT}; margin-top:4px; }}
    .insight-box {{
        background:{SURFACE}; border:1px solid {LINE}; border-left:3px solid {GOLD};
        border-radius:3px; padding:16px 18px; margin-bottom:10px;
    }}
    .insight-box b {{ color:{SIGNAL}; }}
    .section-label {{ font-family:'JetBrains Mono'; font-size:11.5px; letter-spacing:2px;
        color:{MUTED}; text-transform:uppercase; margin-bottom:2px; }}
    .stTabs [data-baseweb="tab-list"] {{ gap: 4px; border-bottom: 1px solid {LINE}; }}
    .stTabs [data-baseweb="tab"] {{ font-family:'Space Grotesk'; color:{MUTED}; }}
    .stTabs [aria-selected="true"] {{ color:{SIGNAL} !important; }}
    footer {{visibility:hidden;}}
    #MainMenu {{visibility:hidden;}}
</style>
""", unsafe_allow_html=True)


@st.cache_data
def load_data():
    df = pd.read_csv("shopify_data.csv", parse_dates=["Invoice Date"])
    df["Order Date"] = df["Invoice Date"].dt.date
    df["State Abbr"] = df["Billing Address Province"].map(STATE_ABBR)
    return df


df = load_data()

PLOTLY_TEMPLATE = go.layout.Template(
    layout=go.Layout(
        paper_bgcolor=SURFACE, plot_bgcolor=SURFACE,
        font=dict(family="Inter", color=TEXT, size=12),
        colorway=[SIGNAL, GOLD, "#5B8DEF", "#E85D75", "#8A93A8", "#6FCF97"],
        xaxis=dict(gridcolor=LINE, zerolinecolor=LINE),
        yaxis=dict(gridcolor=LINE, zerolinecolor=LINE),
        legend=dict(bgcolor="rgba(0,0,0,0)"),
        margin=dict(t=40, l=10, r=10, b=10),
    )
)

# ---------------- Sidebar: control panel ----------------
st.sidebar.markdown("### 🎛️ Control Panel")
st.sidebar.caption("Filter the live dataset below")
date_min, date_max = df["Order Date"].min(), df["Order Date"].max()
date_range = st.sidebar.date_input("Date range", (date_min, date_max), min_value=date_min, max_value=date_max)
product_types = st.sidebar.multiselect("Product Type", sorted(df["Product Type"].dropna().unique()))
states = st.sidebar.multiselect("State", sorted(df["Billing Address Province"].dropna().unique()))

st.sidebar.divider()
st.sidebar.markdown("### 📎 About this project")
st.sidebar.markdown(
    "<span style='color:#8A93A8;font-size:13px'>Built by <b style='color:#EDEFF5'>P Suman Sangeet</b> — "
    "Data Analyst &amp; AI Intern, LABMENTIX, PGDM in Big Data Analytics . "
    "End-to-end Business Intelligence  • An Interactive Power BI Dashboard BI capstone: data cleaning, DAX modeling in Power BI, "
    "and this Python/Streamlit companion dashboard.</span>",unsafe_allow_html=True)
st.sidebar.markdown(
    "<span style='color:#8A93A8;font-size:12.5px'><b>Stack:</b> Python · pandas · Plotly · Streamlit · Power Query (ETL) · Data Modeling · "
    "Power BI · DAX</span>", unsafe_allow_html=True
)

f = df.copy()
if isinstance(date_range, tuple) and len(date_range) == 2:
    f = f[(f["Order Date"] >= date_range[0]) & (f["Order Date"] <= date_range[1])]
if product_types:
    f = f[f["Product Type"].isin(product_types)]
if states:
    f = f[f["Billing Address Province"].isin(states)]

# ---------------- Hero ----------------
st.markdown(f"""
<div class="hero">
    <div class="hero-eyebrow">BI Capstone · Shopify Sales Intelligence</div>
    <p class="hero-title">Shopify Sales Analytics Dashboard</p>
    <p class="hero-sub">An interactive read on revenue, purchasing behaviour, and customer retention
    for a footwear &amp; outdoor-apparel Shopify store — {f['Order Number'].nunique():,} orders across
    {f['Billing Address Province'].nunique()} states, built to surface the decisions stakeholders actually need to make.</p>
</div>
""", unsafe_allow_html=True)

# ---------------- KPI scorecards ----------------
total_revenue = f["Total Price Usd"].sum()
total_orders = f["Order Number"].nunique()
aov = total_revenue / total_orders if total_orders else 0
unique_customers = f["Customer Id"].nunique()
orders_per_cust = f.groupby("Customer Id")["Order Number"].nunique()
repeat_customers = int((orders_per_cust > 1).sum())
repeat_rate = (repeat_customers / unique_customers * 100) if unique_customers else 0
purchase_freq = orders_per_cust.mean() if unique_customers else 0

cards = [
    ("Total Revenue", f"${total_revenue:,.0f}"),
    ("Total Orders", f"{total_orders:,}"),
    ("Avg Order Value", f"${aov:,.2f}"),
    ("Unique Customers", f"{unique_customers:,}"),
    ("Repeat Purchase Rate", f"{repeat_rate:.1f}%"),
    ("Purchase Frequency", f"{purchase_freq:.2f}"),
]
cols = st.columns(6)
for col, (label, value) in zip(cols, cards):
    col.markdown(f"""<div class="scorecard"><div class="label">{label}</div>
        <div class="value">{value}</div></div>""", unsafe_allow_html=True)

st.write("")

# ---------------- Key insights (recruiter-friendly narrative) ----------------
top_product = f.groupby("Product Type")["Total Price Usd"].sum().idxmax()
top_product_share = f.groupby("Product Type")["Total Price Usd"].sum().max() / total_revenue * 100
top_state = f.groupby("Billing Address Province")["Total Price Usd"].sum().idxmax()
top_city = f.groupby("CITY")["Total Price Usd"].sum().idxmax()

st.markdown(f"""
<div class="insight-box">
📌 <b>{top_product}</b> drives <b>{top_product_share:.0f}%</b> of total revenue —
<b>{repeat_rate:.0f}%</b> of customers are repeat buyers averaging <b>{purchase_freq:.1f} orders</b> each —
<b>{top_state}</b> leads by state, with <b>{top_city}</b> the single largest city market.
</div>
""", unsafe_allow_html=True)

# ---------------- Tabs ----------------
tab1, tab2, tab3, tab4 = st.tabs(["📈 Sales & Trends", "👥 Customers & Retention", "🗺️ Geography", "🔎 Data Explorer"])

with tab1:
    c1, c2 = st.columns([2, 1])
    with c1:
        st.markdown('<div class="section-label">Revenue Trend</div>', unsafe_allow_html=True)
        daily = f.groupby("Order Date")["Total Price Usd"].sum().reset_index()
        fig = px.line(daily, x="Order Date", y="Total Price Usd", markers=True, template=PLOTLY_TEMPLATE)
        fig.update_traces(line_color=SIGNAL, marker_color=SIGNAL)
        fig.update_layout(yaxis_title="Revenue ($)", xaxis_title="", height=340)
        st.plotly_chart(fig, use_container_width=True)
    with c2:
        st.markdown('<div class="section-label">Revenue by Product Type</div>', unsafe_allow_html=True)
        prod = f.groupby("Product Type")["Total Price Usd"].sum().reset_index()
        fig = px.treemap(prod, path=["Product Type"], values="Total Price Usd",
                          color="Total Price Usd", color_continuous_scale=[SURFACE_2, SIGNAL],
                          template=PLOTLY_TEMPLATE)
        fig.update_layout(height=340, margin=dict(t=10, l=0, r=0, b=0))
        st.plotly_chart(fig, use_container_width=True)

    c3, c4 = st.columns(2)
    with c3:
        st.markdown('<div class="section-label">Daily Revenue Bridge</div>', unsafe_allow_html=True)
        deltas = daily["Total Price Usd"].diff().fillna(daily["Total Price Usd"])
        fig = go.Figure(go.Waterfall(
            x=[str(d) for d in daily["Order Date"]], y=deltas,
            measure=["absolute"] + ["relative"] * (len(deltas) - 1),
            increasing=dict(marker_color=SIGNAL), decreasing=dict(marker_color="#E85D75"),
            totals=dict(marker_color=GOLD),
            connector={"line": {"color": LINE}}
        ))
        fig.update_layout(template=PLOTLY_TEMPLATE, height=320)
        st.plotly_chart(fig, use_container_width=True)
    with c4:
        st.markdown('<div class="section-label">Daily AOV vs Order Volume</div>', unsafe_allow_html=True)
        daily_stats = f.groupby("Order Date").agg(orders=("Order Number", "nunique"),
                                                    revenue=("Total Price Usd", "sum")).reset_index()
        daily_stats["aov"] = daily_stats["revenue"] / daily_stats["orders"]
        fig = px.scatter(daily_stats, x="orders", y="aov", size="revenue", color="revenue",
                          hover_data=["Order Date"], color_continuous_scale=[SURFACE_2, SIGNAL],
                          template=PLOTLY_TEMPLATE)
        fig.update_layout(xaxis_title="Orders per day", yaxis_title="AOV ($)", height=320)
        st.plotly_chart(fig, use_container_width=True)

with tab2:
    c5, c6 = st.columns(2)
    with c5:
        st.markdown('<div class="section-label">Customer Retention Funnel</div>', unsafe_allow_html=True)
        fig = go.Figure(go.Funnel(
            y=["Unique Customers", "Repeat Customers"], x=[unique_customers, repeat_customers],
            textinfo="value+percent initial", marker=dict(color=[SIGNAL, GOLD])
        ))
        fig.update_layout(template=PLOTLY_TEMPLATE, height=340)
        st.plotly_chart(fig, use_container_width=True)
    with c6:
        st.markdown('<div class="section-label">Orders per Customer (distribution)</div>', unsafe_allow_html=True)
        dist = orders_per_cust.value_counts().sort_index().reset_index()
        dist.columns = ["Orders", "Customers"]
        fig = px.bar(dist, x="Orders", y="Customers", template=PLOTLY_TEMPLATE)
        fig.update_traces(marker_color=SIGNAL)
        fig.update_layout(height=340)
        st.plotly_chart(fig, use_container_width=True)

    st.markdown('<div class="section-label">State × Product Type Revenue</div>', unsafe_allow_html=True)
    top_states_list = f.groupby("Billing Address Province")["Total Price Usd"].sum().nlargest(10).index
    pivot = f[f["Billing Address Province"].isin(top_states_list)].pivot_table(
        index="Billing Address Province", columns="Product Type",
        values="Total Price Usd", aggfunc="sum", fill_value=0)
    fig = px.imshow(pivot, aspect="auto", color_continuous_scale=[SURFACE_2, SIGNAL], template=PLOTLY_TEMPLATE)
    fig.update_layout(height=360)
    st.plotly_chart(fig, use_container_width=True)

with tab3:
    c7, c8 = st.columns(2)
    with c7:
        st.markdown('<div class="section-label">Revenue by State</div>', unsafe_allow_html=True)
        state_rev = f.dropna(subset=["State Abbr"]).groupby("State Abbr")["Total Price Usd"].sum().reset_index()
        fig = px.choropleth(state_rev, locations="State Abbr", locationmode="USA-states",
                             color="Total Price Usd", scope="usa",
                             color_continuous_scale=[SURFACE_2, SIGNAL])
        fig.update_layout(template=PLOTLY_TEMPLATE, height=380,
                           geo=dict(bgcolor=SURFACE, lakecolor=SURFACE))
        st.plotly_chart(fig, use_container_width=True)
    with c8:
        st.markdown('<div class="section-label">Top 10 Cities by Revenue</div>', unsafe_allow_html=True)
        top_cities = f.groupby("CITY")["Total Price Usd"].sum().nlargest(10).reset_index()
        fig = px.bar(top_cities, x="Total Price Usd", y="CITY", orientation="h", template=PLOTLY_TEMPLATE)
        fig.update_traces(marker_color=SIGNAL)
        fig.update_layout(yaxis={"categoryorder": "total ascending"}, xaxis_title="Revenue ($)", height=380)
        st.plotly_chart(fig, use_container_width=True)

with tab4:
    st.markdown('<div class="section-label">Order-level Data</div>', unsafe_allow_html=True)
    st.dataframe(f.sort_values("Invoice Date", ascending=False), use_container_width=True, height=420)
    st.download_button("⬇ Download filtered data (CSV)", f.to_csv(index=False), "shopify_filtered.csv", "text/csv")

st.markdown(f"""<div style="text-align:center;color:{MUTED};font-size:12px;padding:24px 0 8px;">
Shopify Sales Intelligence — built by P Suman · Data Science &amp; AI Intern, Innovexis
</div>""", unsafe_allow_html=True)