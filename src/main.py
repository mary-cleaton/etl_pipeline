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
    """ """
    df = pd.read_csv(
        INPUT_FILEPATH + INPUT_FILE_NAME,
        index_col=0,
        header=0,
    )

    soc_lookup = pd.read_csv(
        INPUT_FILEPATH + SOC_LOOKUP_FILE_NAME,
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
