# external imports
import argparse
import os
import sys

# third party imports
from sqlalchemy import create_engine, select

from sqlalchemy.orm import Session
from sqlalchemy.engine import Connection
from sqlalchemy.orm import sessionmaker

# internal imports
from create import create_db
from load_data import NDBEntry, load_example
from schema import NetworkEntry

sys.path.append("/Users/yan/git-repos/net2text-compnet/src/")
from string_utils.string_converter import path_to_str


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
    with Session(db_engine) as session:
        """
        network_entry = NetworkEntry(
            path=path_to_str([12, 35, 57, 46]),
            prefix="156.5.3",
            org="GOOGLE",
            ingress="SH",
            egress="NEWY",
            destination="NEWY",
            shortest_path=True,
            traffic_size=40,
        )
        """

        for row in data:
            network_entry = NetworkEntry(
                path=path_to_str(row.path),
                prefix=row.prefix,
                ingress=row.path[0],
                egress=row.path[-1],
                destination=row.destination,
                shortest_path=row.shortest_path,
                traffic_size=row.traffic_size,
            )
            # Add to db
            session.add(network_entry)
        # Commit when all the rows are added
        session.commit()

        # Run the query and return one result (out of potentially more)
        query = select(NetworkEntry).where(NetworkEntry.id.is_("1"))
        print("TEST CONNECTION", session.scalars(query).all())


def main(example_path):
    topo_file = "ndb_topo.out"
    data_file = "ndb_dump.out"

    topo_path = os.path.join(example_path, topo_file)
    data_path = os.path.join(example_path, data_file)

    (
        paths,
        topo,
        dest_to_prefix,
        prefix_to_dest,
        node_to_name,
        name_to_node,
    ) = load_example(topo_path, data_path)
    print(paths[:1])

    engine = create_db()
    insert_data(engine, paths)


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
