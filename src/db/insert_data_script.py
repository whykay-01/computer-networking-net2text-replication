from sqlalchemy import create_engine
import pandas as pd
from load_data import load_example


def init_connection():
    engine = create_engine("sqlite:///src/db/network.db")

    try:
        connection = engine.connect()
        # cursor = connection.cursor()
        print("Connection established")

    except:
        # cursor = None
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


def insert_data(connection, data: list[list]):
    """
    REF: https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_sql.html#r689dfd12abe5-1
    this function takes the connection endpoint and a list of lists of data to insert and inserts it into the database
    :param connection: the connection endpoint
    :param data: the data to insert
    :return: None
    """
    pass


if __name__ == "__main__":
    connection = init_connection()

    # data = load_example(
    #     # TODO: figure out what args should I pass. What is the topo and data path?
    #     topo_path="net2text_generator/examples/att_na_10000",
    #     data_path="net2text_generator/examples/att_na_10000",
    # )

    test_connection(connection, "network")
    terminate_connection(connection)
