from queue import PriorityQueue

v = int(input("Enter the total number of vertices: "))

graph = [[] for i in range(v)]

def best_first_search(actual_Src, target, n):
    visited = [False] * n
    pq = PriorityQueue()
    pq.put((0, actual_Src))
    visited[actual_Src] = True

    while pq.empty() == False:
        u = pq.get()[1]
        print(u, end=" ")
        if u == target:
            break

        for v, c in graph[u]:
            if visited[v] == False:
                visited[v] = True
                pq.put((c, v))
    print()

def add_edge(x, y, cost):
    graph[x].append((y, cost))
    graph[y].append((x, cost))

num_edges = int(input("Enter the number of edges: "))

for _ in range(num_edges):
    x, y, cost = map(int, input("Enter edge (x y cost): ").split())
    add_edge(x, y, cost)

source = int(input("Enter the source node: "))
target = int(input("Enter the target node: "))

best_first_search(source, target, v)
