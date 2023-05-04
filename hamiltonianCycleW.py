def hasEdge(end, start, graph):
    for nb in graph[end].keys():
        if nb == start:
            return True

    return False


def hamiltonianCycle(graph, v, visited, path):
    if len(path) == len(graph):
        return hasEdge(path[-1], path[0], graph)

    for nb in graph[v].keys():
        if not visited[nb-1]:
            visited[nb-1] = True
            path.append(nb)
            if hamiltonianCycle(graph, nb, visited, path):
                return True
            visited[nb-1] = False
            path.pop()

    return False


def findHamiltonianCycle(graph):
    visited = [False]*len(graph)
    visited[0] = True
    path = [1]
    if hamiltonianCycle(graph, 1, visited, path):
        path.append(1)
        return path
    return False
