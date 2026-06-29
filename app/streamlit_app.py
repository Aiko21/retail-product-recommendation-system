# ==================================================
# IMPORT SYSTEM LIBRARIES
# ==================================================

from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[1]

sys.path.append(str(PROJECT_ROOT))


# ==================================================
# IMPORT CUSTOM MODULES
# ==================================================

from src.loader import (
    load_similarity_matrix,
    load_product_lookup
)

from src.recommender import (
    get_recommendations
)

from src.utils import (
    load_metadata
)


# ==================================================
# IMPORT LIBRARIES
# ==================================================

import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt


# ==================================================
# PAGE CONFIG
# ==================================================

st.set_page_config(
    page_title="Retail Recommendation System",
    page_icon="🛒",
    layout="wide"
)


# ==================================================
# PROJECT TITLE
# ==================================================

st.title(
    "🛒 Retail Product Recommendation System"
)

st.markdown(
    """
    Recommendation engine for cross-selling optimization.
    """
)


# ==================================================
# LOAD DATA
# ==================================================

similarity_df = load_similarity_matrix()

product_lookup = load_product_lookup()

metadata = load_metadata()


POPULAR_PATH = (
    PROJECT_ROOT /
    "models" /
    "deployment" /
    "top_popular_products.csv"
)

popular_df = pd.read_csv(
    POPULAR_PATH,
    dtype={"StockCode": str}
)


# ==================================================
# SIDEBAR
# ==================================================

st.sidebar.header(
    "⚙️ Recommendation Settings"
)

product_options = sorted(
    product_lookup["StockCode"].unique()
)

selected_product = st.sidebar.selectbox(
    "Select Product",
    product_options
)

top_n = st.sidebar.slider(
    "Top N Recommendations",
    min_value=3,
    max_value=10,
    value=5
)


# ==================================================
# DASHBOARD METRICS
# ==================================================

col1, col2, col3, col4 = st.columns(4)

with col1:

    st.metric(
        "🛍️ Total Products",
        f"{product_lookup.shape[0]:,}"
    )

with col2:

    st.metric(
        "👥 Total Customers",
        "4,338"
    )

with col3:

    st.metric(
        "💰 Revenue",
        "£8.89M"
    )

with col4:

    st.metric(
        "📈 ROI",
        "6121%"
    )


# ==================================================
# GENERATE RECOMMENDATIONS
# ==================================================

try:

    recommendation_df = get_recommendations(
        similarity_df=similarity_df,
        product_lookup=product_lookup,
        stock_code=selected_product,
        top_n=top_n
    )

except Exception:

    st.warning(
        "Product not found. Showing popular products."
    )

    recommendation_df = popular_df.head(top_n)


# ==================================================
# PRODUCT TITLE
# ==================================================

selected_desc = product_lookup.loc[
    product_lookup["StockCode"] == selected_product,
    "Description"
]

if len(selected_desc) > 0:

    selected_name = selected_desc.iloc[0]

else:

    selected_name = selected_product


st.subheader(
    f"Recommendations for: {selected_name}"
)


# ==================================================
# FORMAT SCORE
# ==================================================

if "SimilarityScore" in recommendation_df.columns:

    recommendation_df["SimilarityScore"] = (

        recommendation_df["SimilarityScore"]

        .astype(float)

        .round(3)

    )


# ==================================================
# SHOW TABLE
# ==================================================

st.dataframe(
    recommendation_df,
    width="stretch"
)


# ==================================================
# DOWNLOAD BUTTON
# ==================================================

csv = recommendation_df.to_csv(
    index=False
)

st.download_button(
    label="📥 Download Recommendations",
    data=csv,
    file_name="recommendations.csv",
    mime="text/csv"
)


# ==================================================
# VISUALIZATION
# ==================================================

if "SimilarityScore" in recommendation_df.columns:

    st.subheader(
        "📊 Recommendation Similarity Scores"
    )

    fig, ax = plt.subplots(
        figsize=(10, 5)
    )

    plot_df = recommendation_df.copy()

    plot_df["Description"] = (

        plot_df["Description"]

        .fillna("Unknown Product")

        .astype(str)

    )

    ax.barh(

        plot_df["Description"],

        plot_df["SimilarityScore"]

    )

    ax.set_xlabel(
        "Similarity Score"
    )

    ax.set_title(
        "Recommendation Similarity Scores"
    )

    st.pyplot(fig)


# ==================================================
# EXPLAINABILITY
# ==================================================

with st.expander(
    "📖 How This Recommendation Works"
):

    st.write(
        """
        This recommendation system uses
        **Item-Based Collaborative Filtering**.

        Products that are frequently purchased by
        similar customers are recommended.

        The recommendation engine supports:

        - Cross-selling optimization
        - Product discovery
        - Customer engagement improvement
        - Revenue growth
        - Personalized shopping experiences

        Product similarity is calculated from
        customer purchasing behavior patterns.
        """
    )


# ==================================================
# BUSINESS INSIGHT
# ==================================================

st.markdown("---")

st.subheader(
    "💡 Business Insight"
)

st.info(
    """
    Personalized recommendations help businesses
    increase cross-selling opportunities.

    Customers receive relevant product suggestions,
    improving customer experience and increasing
    Average Order Value (AOV).

    This strategy has the potential to generate
    significant additional revenue.
    """
)


# ==================================================
# FOOTER
# ==================================================

st.markdown("---")

st.markdown(
    """
    ### About This Project

    **Developed by:** Soko Diraharja

    **Dataset:** UCI Online Retail Dataset

    **Model:** Item-Based Collaborative Filtering

    **Purpose:** Cross-Selling Optimization using
    Recommendation Systems
    """
)