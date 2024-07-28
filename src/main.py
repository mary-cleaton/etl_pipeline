from typing import Dict, List

import pandas as pd

from src import utils


def pipeline(
    INPUT_FILE_NAME: str,
    OUTPUT_FILE_NAME: str,
    SOC_LOOKUP_FILE_NAME: str,
    INPUT_FILEPATH: str,
    OUTPUT_FILEPATH: str,
    STRING_COLUMNS: List[str],
    COLUMN_RENAME_DICT: Dict[str, str],
    SOC_LOOKUP_COLUMNS: Dict[str, str],
):
    """
    Runs the pipeline as follows:
        - Reads input dataframe and SOC lookup .csv files to Pandas dataframes.
        - Performs basic string cleaning.
        - Joins the SOC lookup onto the dataframe.
        - Hashes specified columns.
        - Writes the transformed dataframe to the specified output filepath and
          filename.

    Args:
        INPUT_FILE_NAME (str): The name of the file containing the dataset to
            be processed.
        OUTPUT_FILE_NAME (str): The name of the file that the transformed
            dataset will be written to.
        SOC_LOOKUP_FILE_NAME (str): The name of the file containing the SOC
            lookup.
        INPUT_FILEPATH (str): The filepath of the input folder, containing the
            input file and the SOC lookup.
        OUTPUT_FILEPATH (str): The filepath of the output folder, where the
            output file will be written to.
        STRING_COLUMNS (List[str]): The names of the string columns
            that string column cleaning will be applied to.
        COLUMN_RENAME_DICT (Dict[str, str]): The columns that will be renamed
            where dictionary keys are the old names and values are the new
            names.
        SOC_LOOKUP_COLUMNS (Dict[str, str]): The columns to use for joining on
            the SOC lookup. The keys must be "df_col" and "lookup_col" and the
            values are the names that those columns hold.

    Returns:
       df (pd.DataFrame): The transformed dataframe.
    """
    df = pd.read_csv(
        INPUT_FILEPATH + INPUT_FILE_NAME,
        index_col=0,
        header=0,
    )

    soc_lookup = pd.read_csv(
        INPUT_FILEPATH + SOC_LOOKUP_FILE_NAME,
        index_col=0,
        header=0,
    )

    for i in STRING_COLUMNS:
        df = utils.remove_symbols_in_string_col(
            df=df,
            col=i,
        )
        df = utils.set_string_col_to_upper(
            df=df,
            col=i,
        )

    df = utils.join_lookup(
        df,
        soc_lookup,
        SOC_LOOKUP_COLUMNS["df_col"],
        SOC_LOOKUP_COLUMNS["lookup_col"],
    )

    df.to_csv(OUTPUT_FILEPATH + OUTPUT_FILE_NAME)
    return df
