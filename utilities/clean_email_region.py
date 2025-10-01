from pandas import DataFrame


def clean_email_region(df: DataFrame) -> DataFrame:
    df["customer_email"] = df["customer_email"].str.strip().str.lower()
    df["region"] = df["region"].str.strip().str.lower()
    # print(df["customer_email"])
    # print(df["region"])
    return df
