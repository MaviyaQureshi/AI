def dfs(graph, node, visited):
    if node not in visited:
        visited.append(node)
        for k in graph[node]:
            dfs(graph, k, visited)
    return visited


def main():
    graph = {}

    while True:
        edge = input(
            "Enter an edge (format: 'Node1 Node2', or type 'done' to finish): "
        ).strip()
        if edge.lower() == "done":
            break
        node1, node2 = edge.split()
        if node1 not in graph:
            graph[node1] = []
        if node2 not in graph:
            graph[node2] = []
        graph[node1].append(node2)
        graph[node2].append(node1)

    starting_node = input("Enter the starting node for DFS: ").strip().upper()

    if starting_node not in graph:
        print("Invalid starting node. Please choose a valid node.")
        return

    print("Graph:")
    print(graph)

    visited_nodes = dfs(graph, starting_node, [])
    print("DFS traversal starting from node", starting_node, "is:", visited_nodes)


if __name__ == "__main__":
    main()
