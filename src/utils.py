import pandas as pd
import yaml


def read_yaml(filepath: str) -> dict:
    """
    Reads a yaml file from the specified filepath.

    Args:
        filepath (str): The filepath of the yaml file to be read.

    Returns:
        dict: The contents of the yaml file as a dictionary.

    Raises:
        yaml.YAMLError: if yaml file cannot be read.
    """
    with open(filepath, "r") as file:
        try:
            return yaml.safe_load(file)
        except yaml.YAMLError as error:
            raise error


def remove_symbols_in_string_col(df: pd.DataFrame, col: str) -> pd.DataFrame:
    """
    Converts the values of a string column in a Pandas dataframe to remove all
        characters except alphanumeric and spaces.

    Args:
        df (pd.DataFrame): The Pandas dataframe containing the string column.
        col (str): The name of the string column to be converted.

    Returns:
        df_updated (pd.DataFrame): The Pandas dataframe df with the values of
            the string column col converted to remove all characters except
            alphanumeric and spaces.

    Raises:
        ValueError: if col is not a column of df.
    """
    if col not in df.columns:
        raise ValueError("col must be a column of df")
    df_updated = df
    df_updated[col] = df_updated[col].str.replace(
        r"[^0-9a-zA-Z ]+",
        r" ",
        regex=True,
    )
    return df_updated


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
