from graph import Graph
from dijkstra import dijkstra, get_path
from ui import draw_graph

# create graph
g = Graph()

# add nodes
for node in ["A", "B", "C", "D", "E"]:
    g.add_node(node)

# add edges
g.add_edge("A", "B", 4)
g.add_edge("A", "C", 2)
g.add_edge("B", "D", 5)
g.add_edge("C", "D", 1)
g.add_edge("D", "E", 3)

# input
start = "A"
end = "E"

# run algorithm
dist, parent = dijkstra(g, start)
path = get_path(parent, start, end)

print("Shortest Distance:", dist[end])
print("Path:", path)

# visualize
draw_graph(g, path)