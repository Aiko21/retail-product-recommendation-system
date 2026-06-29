import pandas as pd
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]


def load_product_lookup():

    path = (
        PROJECT_ROOT /
        "models" /
        "deployment" /
        "product_lookup.csv"
    )

    return pd.read_csv(
        path,
        dtype={"StockCode": str}
    )


def load_similarity_matrix():

    path = (
        PROJECT_ROOT /
        "models" /
        "advanced" /
        "item_similarity_matrix.csv"
    )

    similarity_df = pd.read_csv(
        path,
        index_col=0,
        low_memory=False
    )

    similarity_df.index = similarity_df.index.astype(str)
    similarity_df.columns = similarity_df.columns.astype(str)

    return similarity_df