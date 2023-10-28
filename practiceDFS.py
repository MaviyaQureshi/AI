def dfs(graph, node, visit):
    if node not in visit:
        visit.append(node)

        for k in graph[node]:
            dfs(graph, k, visit)

    return visit


def main():
    graph = {}

    while True:
        edge = input("Enter edges (format : 'Node1 Node2') : ").strip()

        if edge.lower == "done":
            break

        node1, node2 = edge.split()

        if node1 not in graph:
            graph[node1] = []

        if node2 not in graph:
            graph[node2] = []

        graph[node1].append(node2)
        graph[node2].append(node1)

    starting_node = input("Enter starting node for DFS : ")

    if starting_node not in graph:
        print("Enter a valid node")
        return

    print("Graph : ")
    print(graph)

    visited_nodes = dfs(graph, starting_node, [])

    print("DFS traversal starting from node", starting_node, "is :", visited_nodes)
    print(visited_nodes)
