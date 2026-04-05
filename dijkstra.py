import heapq

def dijkstra(graph, start):
    pq = [(0, start)]
    dist = {node: float('inf') for node in graph.graph}
    dist[start] = 0
    parent = {node: None for node in graph.graph}

    while pq:
        curr_dist, node = heapq.heappop(pq)

        for neighbor, weight in graph.get_neighbors(node):
            new_dist = curr_dist + weight

            if new_dist < dist[neighbor]:
                dist[neighbor] = new_dist
                parent[neighbor] = node
                heapq.heappush(pq, (new_dist, neighbor))

    return dist, parent


def get_path(parent, start, end):
    path = []
    while end is not None:
        path.append(end)
        end = parent[end]
    return path[::-1]