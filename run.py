"""
LANGUAGE: Python
WHAT IT DOES:
* reads configs from yaml file
* reads .csv file
* applies standard cleaning
* writes outputs to .csv file

AUTHOR: Mary Cleaton
DATE: 28/07/2024
REF: UKHSA Data Engineer job application
"""

from src import logging_handler, main, utils

config_filepath = "input/config.yaml"
table_name = "test"


def run(config_filepath, table_name):
    configs = utils.read_yaml(config_filepath)

    logger = logging_handler.Logger(table_name).get_logger()
    logger.info(f"Commenced {table_name} processing")

    try:
        main.pipeline(**configs)
        logger.info(f"Successfully processed {table_name}")
    except Exception as e:
        logger.exception(e)


if __name__ == "__main__":
    run(config_filepath, table_name)
