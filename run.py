""" """

from src import logging_handler

table_name = "test_dataset"


def run_pipeline(table_name):
    logger = logging_handler.Logger(table_name).get_logger()
    logger.info(f"Commenced {table_name} processing")

    try:
        # Pipeline here
        x = "HELLO WORLD"
        print(5 / x)

        logger.info(f"Successfully processed {table_name}")
    except Exception as e:
        logger.exception(e)


if __name__ == "__main__":
    run_pipeline(table_name)
