def eulerianCycle(graph):
    stack = [list(graph.keys())[0]]
    path = []

    # Main algorithm
    while stack:
        v = stack[-1]
        if graph[v]:
            u = list(graph[v])[0]
            stack.append(u)
            # Deleting edge u-v
            del graph[u][v]
            del graph[v][u]
        else:
            path.append(stack.pop())

    return path
