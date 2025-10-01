from pandas import DataFrame

NAME_MAP = {
    "Order_ID": "order_id",
    "Customer_Email": "customer_email",
    "Product_Name": "product_name",
    "Price ($)": "price_$",
    "Region": "region",
    "Status": "status",
    "Discount_Applied": "discount_applied",
    "Date": "date",
}


def rename_columns(df: DataFrame) -> DataFrame:
    df.columns = df.columns.str.strip()
    df.rename(columns=NAME_MAP, inplace=True)
    # print(df.columns)
