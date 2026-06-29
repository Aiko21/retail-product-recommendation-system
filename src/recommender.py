import pandas as pd


def get_recommendations(
    similarity_df,
    product_lookup,
    stock_code,
    top_n=5
):

    similar_items = (
        similarity_df.loc[stock_code]
        .sort_values(ascending=False)
        .drop(stock_code)
        .head(top_n)
        .reset_index()
    )

    similar_items.columns = [
        "StockCode",
        "SimilarityScore"
    ]

    recommendation_df = similar_items.merge(
        product_lookup,
        on="StockCode",
        how="left"
    )

    return recommendation_df