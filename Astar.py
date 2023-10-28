import heapq
import math


def heuristic(node, goal):
    # Euclidean distance heuristic
    x1, y1 = node
    x2, y2 = goal
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


def astar(graph, start, goal):
    open_set = [(0, start)]  # Priority queue with (f_score, node)
    g_score = {node: float("inf") for node in graph}
    g_score[start] = 0
    came_from = {}

    while open_set:
        _, current = heapq.heappop(open_set)

        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            return path[::-1]

        for neighbor in graph[current]:
            x, y = neighbor
            tentative_g_score = g_score[current] + graph[current][neighbor]

            if tentative_g_score < g_score.get((x, y), float("inf")):
                came_from[(x, y)] = current
                g_score[(x, y)] = tentative_g_score
                f_score = tentative_g_score + heuristic((x, y), goal)
                heapq.heappush(open_set, (f_score, (x, y)))

    return None  # No path found


def create_graph():
    graph = {}
    while True:
        edge = input(
            "Enter an edge (format: 'x1 y1 x2 y2 cost', or type 'done' to finish): "
        ).strip()
        if edge.lower() == "done":
            break
        x1, y1, x2, y2, cost = map(int, edge.split())
        if (x1, y1) not in graph:
            graph[(x1, y1)] = {}
        if (x2, y2) not in graph:
            graph[(x2, y2)] = {}
        graph[(x1, y1)][(x2, y2)] = cost
        graph[(x2, y2)][(x1, y1)] = cost

    return graph


def main():
    graph = create_graph()
    start_x, start_y = map(int, input("Enter the starting node (x y): ").split())
    goal_x, goal_y = map(int, input("Enter the goal node (x y): ").split())
    start_node = (start_x, start_y)
    goal_node = (goal_x, goal_y)

    path = astar(graph, start_node, goal_node)

    if path:
        print("Path found:", path)
    else:
        print("No path found.")


if __name__ == "__main__":
    main()
