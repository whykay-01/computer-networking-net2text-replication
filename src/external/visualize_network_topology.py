import networkx as nx
import matplotlib.pyplot as plt
import os

root_path = os.getcwd()
graph_path = os.path.join(
    root_path, "net2text_generator", "examples", "att_na", "AttMpls.graphml"
)
# Load the GraphML file
graph = nx.read_graphml(graph_path)

# Draw the graph
nx.draw(graph, with_labels=True, font_weight="bold")
plt.show()
