import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# ==================================================
# PAGE CONFIG
# ==================================================

st.set_page_config(
    page_title="Elunor",
    layout="wide",
    page_icon="✨"
)

# ==================================================
# CUSTOM CSS
# ==================================================

st.markdown("""
<style>

.stApp{
    background-color:#FFF8FB;
    color:#2B2B2B;
}

section[data-testid="stSidebar"]{
    background-color:#FFF1F5;
    border-right:1px solid rgba(0,0,0,0.05);
}

h1,h2,h3{
    color:#B76E79;
}

.hero-text{
    color:#777777;
    font-size:18px;
    margin-bottom:30px;
}

.card{
    background:white;
    padding:30px;
    border-radius:24px;
    box-shadow:0 4px 20px rgba(0,0,0,0.05);
    text-align:center;
}

.number{
    font-size:42px;
    font-weight:bold;
    color:#B76E79;
}

.label{
    color:#777777;
    margin-top:10px;
}

.insight-box{
    background:linear-gradient(
        135deg,
        #FFE4EC,
        #FFF7FA
    );

    padding:25px;
    border-radius:24px;

    box-shadow:0 4px 20px rgba(0,0,0,0.04);

    color:#555555;
    line-height:1.7;
}

div[data-testid="stMetric"]{
    background:white;
    padding:15px;
    border-radius:18px;
    box-shadow:0 4px 15px rgba(0,0,0,0.04);
}

</style>
""", unsafe_allow_html=True)

# ==================================================
# LOAD DATA
# ==================================================

df = pd.read_csv(
    "../data/processed/clean_products.csv"
)

# ==================================================
# SIDEBAR
# ==================================================

st.sidebar.title("Elunor")

st.sidebar.markdown(
    "Beauty Intelligence Platform"
)

st.sidebar.markdown("---")

st.sidebar.info("""
Explore beauty product trends,
consumer behavior,
pricing intelligence,
and product performance.
""")

# ==================================================
# HERO SECTION
# ==================================================

st.markdown("""
<h1 style='
text-align: center;
color: #B03060;
font-size: 72px;
margin-bottom: 0px;
font-weight: 700;
font-family: Arial;
'>
Elunor
</h1>
""", unsafe_allow_html=True)

st.markdown("""
<p style='
text-align: center;
color: #C06C84;
font-size: 20px;
margin-top: -10px;
font-family: Arial;
'>
Beauty Intelligence, Reimagined
</p>
""", unsafe_allow_html=True)


# ==================================================
# KPI CARDS
# ==================================================

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(f"""
    <div class="card">
        <div class="number">{len(df)}</div>
        <div class="label">Total Products</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div class="card">
        <div class="number">{df['brand_name'].nunique()}</div>
        <div class="label">Brands</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown(f"""
    <div class="card">
        <div class="number">{round(df['rating'].mean(),2)}</div>
        <div class="label">Average Rating</div>
    </div>
    """, unsafe_allow_html=True)

# ==================================================
# SPACING
# ==================================================

st.markdown("<br>", unsafe_allow_html=True)

# ==================================================
# SEARCH SECTION
# ==================================================

st.markdown("## Product Explorer")

search = st.text_input(
    "Search Product"
)

filtered_df = df[
    df["product_name"]
    .astype(str)
    .str.contains(
        search,
        case=False,
        na=False
    )
]

# ==================================================
# CATEGORY FILTER
# ==================================================

category = st.selectbox(
    "Select Category",
    sorted(
        df["primary_category"]
        .dropna()
        .unique()
    )
)

filtered_df = filtered_df[
    filtered_df["primary_category"] == category
]

# ==================================================
# PRODUCT DISPLAY
# ==================================================

for index, row in filtered_df.head(8).iterrows():

    st.markdown("### " + str(row["product_name"]))

    st.caption(str(row["brand_name"]))

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "Rating",
            round(row["rating"], 2)
        )

    with col2:
        st.metric(
            "Price",
            f"${row['price_usd']}"
        )

    st.markdown("---")

# ==================================================
# BRAND CHART
# ==================================================

st.markdown("## Brand Performance")

top_brands = (
    df["brand_name"]
    .value_counts()
    .head(10)
)

fig, ax = plt.subplots(figsize=(10,5))

top_brands.plot(
    kind="bar",
    color="#E6A4B4",
    ax=ax
)

ax.set_title("Top Brands")

ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

plt.xticks(rotation=25)

st.pyplot(fig)

# ==================================================
# AI INSIGHTS
# ==================================================

st.markdown("## AI Insights")

st.markdown("""
<div class="insight-box">

Skincare products dominate platform inventory
while premium-priced products maintain stronger
average customer ratings and engagement.

Ingredient-focused positioning appears strongly
correlated with consumer attention and purchasing behavior.

</div>
""", unsafe_allow_html=True)

# ==================================================
# FOOTER
# ==================================================

st.markdown("<br><br>", unsafe_allow_html=True)

st.caption(
    "Built using Machine Learning, NLP, and Data Intelligence."
)