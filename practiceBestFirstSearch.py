from queue import PriorityQueue


def bfs(source, destination, v):
    visited = [False] * v

    pq = PriorityQueue()
    pq.put((0, source))
    visited[source] = True

    while pq.empty() == False:
        u = pq.get()[1]
        print(u, end=" ")

        if u == destination:
            break

        for v, c in graph[u]:
            if visited[v] == False:
                visited[v] = True
                pq.put((c, v))


def add_edge(x, y, cost):
    graph[x].append((y, cost))
    graph[y].append((x, cost))


v = int(input("Enter the number of vertices : "))

graph = [[] for i in range(v)]

edges = int(input("Enter the number of edges : "))

for _ in range(edges):
    x, y, cost = map(int, input("Enter edge (x , y, cost) : ").split())
    add_edge(x, y, cost)

source = int(input("Enter the source node : "))
destination = int(input("Enter the destination node : "))

bfs(source, destination, v)
