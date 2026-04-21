import heapq

def dijkstra(graph, start):
    pq = [(0, start)]
    dist = {node: float('inf') for node in graph}
    dist[start] = 0
    parent = {start: None}

    while pq:
        curr_dist, node = heapq.heappop(pq)

        for neighbor, weight in graph[node]:
            new_dist = curr_dist + weight

            if new_dist < dist[neighbor]:
                dist[neighbor] = new_dist
                parent[neighbor] = node
                heapq.heappush(pq, (new_dist, neighbor))

    return parent


def get_path(parent, start, end):
    path = []
    curr = end

    while curr is not None:
        path.append(curr)
        curr = parent.get(curr)

    return path[::-1]
























#A* (A-Star) Algorithm
#Breadth-First Search (BFS)
#Bellman-Ford Algorithm
#Floyd-Warshall Algorithm