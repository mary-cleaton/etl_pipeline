import os
from contextlib import nullcontext as does_not_raise

import pytest
import yaml

from src import utils


@pytest.mark.parametrize(
    "filepath, contents, expected_output, expected_context",
    [
        (
            "test_file.yaml",
            """value: 'a'""",
            {"value": "a"},
            does_not_raise(),
        ),
        # Test for error raising
    ],
)
def test_read_yaml(
    filepath,
    contents,
    expected_output,
    expected_context,
):
    with open(filepath, "w") as file:
        test = yaml.safe_load(contents)
        yaml.dump(test, file)

    with expected_context:
        assert utils.read_yaml(filepath) == expected_output

    os.remove(filepath)


@pytest.mark.parametrize(
    "params, test_input_fixture, expected_output_fixture, expected_context",
    [
        (
            {"df": None, "col": "forename"},
            "get_input_dataset",
            "get_output_dataset_2",
            does_not_raise(),
        ),
        (
            {"df": None, "col": "surname"},
            "get_input_dataset",
            "get_output_dataset_2",
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
def test_remove_symbols_in_string_col(
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
        assert utils.remove_symbols_in_string_col(**params)[
            params["col"]
        ].equals(expected_output[params["col"]])


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
