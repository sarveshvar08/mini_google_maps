import networkx as nx
import matplotlib.pyplot as plt

def draw_graph(graph, path=None):
    G = nx.Graph()

    for node in graph.graph:
        for neighbor, weight in graph.graph[node]:
            G.add_edge(node, neighbor, weight=weight)

    pos = nx.spring_layout(G)

    # draw normal graph
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=2000)

    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

    # highlight path
    if path:
        edges = list(zip(path, path[1:]))
        nx.draw_networkx_edges(G, pos, edgelist=edges, edge_color='red', width=3)

    plt.show()