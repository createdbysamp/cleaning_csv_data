import pandas as pd
from pandas import DataFrame
from utilities import (
    clean_email_region,
    rename_columns,
    duplicated_order_id,
    missing_price,
    fill_values,
)


# // STRUCTURALLY CLEAN THE DATA-----------------_____________-------____---------||
# // 1. read the rawsalesdata file into a df
# // 2. Rename all columns to clean snake_case (e.g., Order_ID order_id).
# // 3. Clean the customer_email and region columns by removing all leading/trailing whitespace and converting all values to lowercase.

# // DATA QUALITY--------------------------______--------______--------||
# // 1. identify and remove records that are complete duplicates based on the order_id
# // 2. check for missing values in the price_$ column (drop any row where price is missing (NaN))
# // 3. fill any missing values in the discount_appplied column with a fail_safe value of 0.0 if not any

# // ANALYSIS AND LOAD (boolean indexing and .to_csv())---------||
# // 1. Apply Boolean Indexing to filter the DataFrame based on the three conditions above.
# // 2. Sort the final filtered DataFrame by the price_usd column in descending order.
# // 3. Export the final, cleaned, and filtered DataFrame to a new file named east_region_report.csv (without the index column)


# JAM MASTERS -------------------------------------||
# 1. DATA AGGREGATION
# - calculate the total revenue (sum of price_usd) column for the final east_region_report.csv and print it to the console

# // 2. BASIC FUNCTIONALITY
# // - refactor your script so that the logic is contained within functions named

SALES_DATA = "data/raw_sales_data.csv"
NA_VALUES = [" ", "", "N/A", "NA", "n/a", "NULL", "null"]
OUTPUT_FILE = "data/east_region_report.csv"


def extract(filepath: str) -> DataFrame:
    df = pd.read_csv(filepath, na_values=NA_VALUES, skipinitialspace=True)
    # print(df.head())
    return df


def transform(df):

    rename_columns(df)
    clean_email_region(df)
    duplicated_order_id(df)
    missing_price(df)
    fill_values(df)
    # print(df)
    # df.fill_values()


def load(df: DataFrame) -> None:
    mask = (
        (df["region"] == "east")
        & (df["price_$"] > 100.0)
        & (df["status"] == "COMPLETED")
    )

    filtered_df = df[mask]
    df_sorted = filtered_df.sort_values(by="price_$", ascending=False)

    df_sorted.to_csv(OUTPUT_FILE, index=False, encoding="utf-8")
    print("data frame printed!")

    # // filter for rows where;
    # // status === "returned"
    # // branch == east
    # // fee_usd>0
    # // sort results by fee_usd descending
    # // export to report.csv

    # // mask = df [a bunch of variables that we called earlier]
    # // filtered_df = df[mask]
    # // filtered_df_to_csv = OUTPUT_FILE(parameter1, parameter2, encoding)


def main():
    df = extract(SALES_DATA)
    transform(df)
    load(df)


if __name__ == "__main__":
    main()
