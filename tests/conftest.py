import pandas as pd
import pytest


@pytest.fixture(scope="function")
def get_input_dataset_1():
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


@pytest.fixture(scope="function")
def get_input_dataset_2():
    return pd.DataFrame(
        {
            "creatures": ["cat", "dog", "parrot", "cuttlefish", "guppy"],
        }
    )


@pytest.fixture(scope="function")
def get_input_dataset_3():
    return pd.DataFrame(
        {
            "common_name": ["cat", "dog", "parrot", "squid", "guppy"],
            "animal_type": [
                "mammal",
                "mammal",
                "bird",
                "invertebrate",
                "fish",
            ],
            "vertebrate": [True, True, True, False, True],
        }
    )


@pytest.fixture(scope="function")
def get_output_dataset_3():
    return pd.DataFrame(
        {
            "creatures": ["cat", "dog", "parrot", "cuttlefish", "guppy"],
            "animal_type": ["mammal", "mammal", "bird", None, "fish"],
            "vertebrate": [True, True, True, None, True],
        }
    )
