from pandas import DataFrame

NA_VALUES = (" ", "", "na", "null", "NaN", "n/a")


def fill_values(df: DataFrame) -> DataFrame:
    df["discount_applied"] = df["discount_applied"].fillna(0.0)

    # print(df)
    return df
