# external imports
import argparse
import os

# third party imports
from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session
from sqlalchemy.engine import Connection

# internal imports
from create import create_db
from load_data import NDBEntry, load_example
from schema import NetworkEntry
from string_utils.string_converter import path_to_str


def init_connection() -> Connection:
    engine = create_engine("sqlite:///src/db/network.db")

    try:
        connection = engine.connect()
        print("Connection established")

    except:
        print("Connection failed")

    return connection


def terminate_connection(connection) -> None:
    # Close the connection when done
    connection.close()
    print("Connection closed")
    return


def test_connection(connection, table_name: str) -> bool:
    result = connection.execute(
        "SELECT * FROM {table_name};".format(table_name=table_name)
    )

    if result:
        print("Connection successful")
        return True
    else:
        print("Connection failed")
        return False


def insert_data(db_engine, data: list[NDBEntry]) -> None:
    """
    REF: https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_sql.html#r689dfd12abe5-1
    this function takes the connection endpoint and a list of lists of data to insert and inserts it into the database
    :param connection: the connection endpoint
    :param data: the data to insert
    :return: None
    """
    pass


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "path",
        help="path to the directory containing the example for the data generation",
        type=str,
        default="../../net2text_generator/examples/att_na_100",
    )
    parsed_args = parser.parse_args()

    main(parsed_args.path)
