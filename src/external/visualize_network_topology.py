import networkx as nx
import os
from pyvis.network import Network

root_path = os.getcwd()
graph_path = os.path.join(
    root_path, "net2text_generator", "examples", "att_na", "AttMpls.graphml"
)
# Load the GraphML file
graph = nx.read_graphml(graph_path)

# # Draw the graph
# nx.draw(graph, with_labels=True, font_weight="bold")
# plt.show()


# create a network
net = Network(notebook=False)
# load the networkx graph
net.from_nx(graph)
# show
net.show("nx.html")
