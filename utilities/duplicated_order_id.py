from pandas import DataFrame


def duplicated_order_id(df: DataFrame) -> DataFrame:
    # print(df["order_id"])
    df.drop_duplicates(subset=["order_id"])
    # print(df["order_id"])

    return df
