from sqlalchemy import create_engine
from schema import NetworkEntry



def create_db():
	# Connect to db
	db_engine = create_engine("sqlite:///network.db")
	# Create Network Entry table
	NetworkEntry.metadata.create_all(db_engine)
	""" Example creation of db row:
	from sqlalcehmy import select
	from sqlalchemy.orm import Session
	from utils.string import path_to_str

	with Session(db_engine) as session:
		network_entry = NetworkEntry(
			path=path_to_str([12, 35, 57, 46]),
			prefix="156.5.3",
			org="GOOGLE",
			ingress="SH",
			egress="NEWY",
			destination="NEWY",
			shortest_path=True,
			traffic_size=40
		)
		# Add to db
		session.add(network_entry)
		session.commit()

		# SELECT NetworkEntry (all columns) WHERE org=GOOGLE
		query = select(NetworkEntry).where(NetworkEntry.org.is_("GOOGLE"))
		# Run the query and return one result (out of potentially more)
		print(session.scalars(query).one())
	"""
	

if __name__ == "__main__":
	pass