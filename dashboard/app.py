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

@import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@500;600;700&family=Inter:wght@300;400;500&display=swap');

.stApp{
    background-color:#F8F3F0;
    color:#2B2B2B;
}

section[data-testid="stSidebar"]{
    background-color:#F3ECE8;
    border-right:1px solid rgba(0,0,0,0.04);
}

h1,h2,h3{
    color:#6E4B4B;
    font-family:'Cormorant Garamond', serif;
    letter-spacing:0.5px;
}

p, label, div{
    font-family:'Inter', sans-serif;
}

.card{
    background:#FCF8F6;
    padding:35px;
    border-radius:28px;
    border:1px solid rgba(0,0,0,0.05);
    box-shadow:0 2px 12px rgba(0,0,0,0.03);
    text-align:center;
}

.number{
    font-size:58px;
    font-family:'Cormorant Garamond', serif;
    font-weight:600;
    color:#5E4A47;
}

.label{
    color:#8A7B75;
    margin-top:10px;
    font-size:15px;
    letter-spacing:0.5px;
}

.insight-box{
    background:#FCF8F6;
    padding:40px;
    border-radius:28px;
    border:1px solid rgba(0,0,0,0.05);
    color:#5E5552;
    line-height:1.9;
    font-size:17px;
}

div[data-testid="stMetric"]{
    background:transparent;
    box-shadow:none;
    border:none;
}

.stTextInput input{
    border-radius:18px !important;
    border:1px solid rgba(0,0,0,0.08) !important;
    background:#FCF8F6 !important;
    padding:14px !important;
}

.stSelectbox div[data-baseweb="select"]{
    border-radius:18px !important;
    background:#FCF8F6 !important;
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

st.sidebar.markdown("""
<h1 style="
font-family:'Cormorant Garamond', serif;
color:#4E3B38;
font-size:42px;
margin-bottom:0;
">
ELUNOR
</h1>
""", unsafe_allow_html=True)

st.sidebar.markdown("""
<p style="
color:#7D6B66;
font-size:15px;
margin-top:-10px;
">
Curated beauty intelligence,
powered by AI.
</p>
""", unsafe_allow_html=True)

st.sidebar.markdown("---")

st.sidebar.info("""
Luxury beauty analytics,
consumer insights,
and AI-driven recommendations.
""")

# ==================================================
# HERO SECTION
# ==================================================

st.markdown("""
<div style='padding-top:60px; padding-bottom:40px;'>

<h1 style='
text-align:center;
font-size:96px;
font-family:"Cormorant Garamond", serif;
font-weight:600;
color:#4E3B38;
letter-spacing:1px;
margin-bottom:0;
'>
ELUNOR
</h1>

<p style='
text-align:center;
font-size:20px;
font-family:Inter;
font-weight:300;
color:#7D6B66;
margin-top:-8px;
letter-spacing:1px;
'>
Beauty, personalized by AI.
</p>

</div>
""", unsafe_allow_html=True)

# ==================================================
# HERO IMAGE
# ==================================================

st.image(
    "https://www.mediainfoline.com/wp-content/uploads/2021/11/kaybeauty_2yrs.jpg",
    use_container_width=True
)

# ==================================================
# SPACING
# ==================================================

st.markdown("<div style='height:80px'></div>", unsafe_allow_html=True)

# ==================================================
# KPI CARDS
# ==================================================

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(f"""
    <div class="card">
        <div class="number">{len(df)}</div>
        <div class="label">Products</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div class="card">
        <div class="number">{df['BRAND NAME'].nunique()}</div>
        <div class="label">Brands</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown(f"""
    <div class="card">
        <div class="number">{round(df['RATING'].mean(),2)}</div>
        <div class="label">Average Rating</div>
    </div>
    """, unsafe_allow_html=True)

# ==================================================
# SPACING
# ==================================================

st.markdown("<div style='height:100px'></div>", unsafe_allow_html=True)

# ==================================================
# PRODUCT EXPLORER
# ==================================================

st.markdown("""
<h2 style="
font-size:52px;
margin-bottom:20px;
">
Product Explorer
</h2>
""", unsafe_allow_html=True)

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

    st.markdown(f"""
    <div style="
    padding:35px;
    background:#FCF8F6;
    border-radius:28px;
    margin-bottom:24px;
    border:1px solid rgba(0,0,0,0.05);
    ">

    <h3 style="
    font-family:'Cormorant Garamond', serif;
    font-size:38px;
    color:#4E3B38;
    margin-bottom:6px;
    ">
    {row["product_name"]}
    </h3>

    <p style="
    color:#8A7B75;
    font-family:Inter;
    font-size:15px;
    margin-top:0;
    letter-spacing:0.3px;
    ">
    {row["brand_name"]}
    </p>

    <div style="
    margin-top:18px;
    color:#5E5552;
    font-size:16px;
    line-height:1.8;
    ">
    Rating: {round(row["rating"],2)} ⭐
    <br>
    Price: ${row["price_usd"]}
    </div>

    </div>
    """, unsafe_allow_html=True)

# ==================================================
# SPACING
# ==================================================

st.markdown("<div style='height:100px'></div>", unsafe_allow_html=True)

# ==================================================
# BRAND PERFORMANCE
# ==================================================

st.markdown("""
<h2 style="
font-size:52px;
margin-bottom:30px;
">
Brand Performance
</h2>
""", unsafe_allow_html=True)

top_brands = (
    df["brand_name"]
    .value_counts()
    .head(10)
)

fig, ax = plt.subplots(figsize=(10,5))

top_brands.plot(
    kind="bar",
    color="#D8B7AE",
    ax=ax
)

ax.set_facecolor("#F8F3F0")
fig.patch.set_facecolor("#F8F3F0")

ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.spines["left"].set_visible(False)

ax.tick_params(colors="#7D6B66")

ax.set_title(
    "Top Brands",
    fontsize=22,
    color="#5E5552"
)

plt.xticks(rotation=20)

st.pyplot(fig)

# ==================================================
# SPACING
# ==================================================

st.markdown("<div style='height:100px'></div>", unsafe_allow_html=True)

# ==================================================
# AI INSIGHTS
# ==================================================

st.markdown("""
<h2 style="
font-size:52px;
margin-bottom:30px;
">
AI Insights
</h2>
""", unsafe_allow_html=True)

st.markdown("""
<div class="insight-box">

Skincare products continue to dominate consumer attention,
while premium beauty brands maintain stronger engagement
and higher average customer satisfaction.

Ingredient-focused positioning appears highly correlated
with purchasing behavior, especially within luxury skincare segments.

</div>
""", unsafe_allow_html=True)

# ==================================================
# FOOTER
# ==================================================

st.markdown("<div style='height:80px'></div>", unsafe_allow_html=True)

st.markdown("""
<p style="
text-align:center;
color:#8A7B75;
font-size:14px;
letter-spacing:0.5px;
">
Built using Machine Learning, NLP, and Beauty Intelligence.
</p>
""", unsafe_allow_html=True)