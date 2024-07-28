""" """

from src import logging_handler, utils

configs = utils.read_yaml("input/config.yaml")
print(configs["TABLE_NAME"])
print(type(configs["TABLE_NAME"]))


def run_pipeline(configs):
    table_name = configs["TABLE_NAME"]
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
    run_pipeline(configs)
