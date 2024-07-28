# etl_pipeline

A basic ETL pipeline built for UKHSA Data Engineer application, July 2024.

----------

## Desk instructions

### Set up

1. Create and activate a virtual environment.
2. Run `pip install .` in the terminal to install dependencies.

## Run

1. Check the config file at `etl_pipeline/input/config.yaml` and update as
   necessary.
   As default, it is set up to run on the `mock_data.csv` in
   `etl_pipeline/input/`.
2. Run `python run.py` in the terminal.


----------

## Pipeline flowchart

----------

## Developer instructions

### Set up

1. Create and activate a virtual environment.
2. Run `pip install .[dev]` in the terminal to install dependencies, including developer dependencies.
3. Run `pre-commit install` in the terminal to install project pre-commits

----------

## Input data