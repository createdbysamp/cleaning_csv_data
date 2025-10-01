from pandas import DataFrame


def missing_price(df: DataFrame) -> DataFrame:
    # missing_price = df["price_$"].isnull().sum()
    # print(missing_price
    df_missing_prices = df.dropna(subset=["price_$"])
    # print(df_missing_prices)
    return df_missing_prices
    # if df["price_$"].isnull():
    #     print(df["price_$"])
