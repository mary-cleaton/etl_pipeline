from contextlib import nullcontext as does_not_raise

import pytest

from src import utils


@pytest.mark.parametrize(
    "params, test_input_fixture, expected_output_fixture, expected_context",
    [
        (
            {"df": None, "col": "forename"},
            "get_input_dataset",
            "get_output_dataset_1",
            does_not_raise(),
        ),
        (
            {"df": None, "col": "surname"},
            "get_input_dataset",
            "get_output_dataset_1",
            does_not_raise(),
        ),
        (
            {"df": None, "col": "not_a_df_col"},
            "get_input_dataset",
            "get_null",
            pytest.raises(ValueError),
        ),
    ],
)
def test_set_string_col_to_upper(
    request,
    params,
    test_input_fixture,
    expected_output_fixture,
    expected_context,
) -> None:
    test_input = request.getfixturevalue(test_input_fixture)
    expected_output = request.getfixturevalue(expected_output_fixture)
    params["df"] = test_input
    with expected_context:
        assert utils.set_string_col_to_upper(**params)[params["col"]].equals(
            expected_output[params["col"]]
        )
