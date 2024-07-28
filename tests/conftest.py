import pandas as pd
import pytest


@pytest.fixture(scope="function")
def get_input_dataset():
    return pd.DataFrame(
        {
            "forename": ["Peter", "Aisha", "Colin", "Lucy-Anne"],
            "surname": ["Gardiner", "Al-Fayed", "Quentin Jr.", "Griffiths"],
        }
    )


@pytest.fixture(scope="function")
def get_null():
    return None


@pytest.fixture(scope="function")
def get_output_dataset_1():
    return pd.DataFrame(
        {
            "forename": ["PETER", "AISHA", "COLIN", "LUCY-ANNE"],
            "surname": ["GARDINER", "AL-FAYED", "QUENTIN JR.", "GRIFFITHS"],
        }
    )


@pytest.fixture(scope="function")
def get_output_dataset_2():
    return pd.DataFrame(
        {
            "forename": ["Peter", "Aisha", "Colin", "Lucy Anne"],
            "surname": ["Gardiner", "Al Fayed", "Quentin Jr ", "Griffiths"],
        }
    )
