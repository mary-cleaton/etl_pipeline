import pandas as pd


def set_string_col_to_upper(df: pd.DataFrame, col: str) -> pd.DataFrame:
    """
    Converts the values of a string column in a Pandas dataframe to uppercase.

    Args:
        df (pd.DataFrame): The Pandas dataframe containing the string column.
        col (str): The name of the string column to be converted.

    Returns:
        df_updated (pd.DataFrame): The Pandas dataframe df with the values of
            the string column col converted to uppercase.

    Raises:
        ValueError: if col is not a column of df.
    """
    if col not in df.columns:
        raise ValueError("col must be a column of df")
    df_updated = df
    df_updated[col] = df_updated[col].str.upper()
    return df_updated
