def hasEdgeS(end, start, graph):
    for nb in graph[end].keys():
        if nb == start:
            return True

    return False


def hamiltonianCycles(graph, v, visited, path, counter):
    if len(path) == len(graph):
        if hasEdgeS(path[-1], path[0], graph):
            print(path)
            counter[0] += 1
            return

    for nb in graph[v].keys():
        if not visited[nb-1]:
            visited[nb-1] = True
            path.append(nb)
            if hamiltonianCycles(graph, nb, visited, path, counter):
                return
            visited[nb-1] = False
            path.pop()

    return False


def findHamiltonianCycles(graph):
    visited = [False]*len(graph)
    visited[0] = True
    path = [1]
    counter = [0]
    hamiltonianCycles(graph, 1, visited, path, counter)
    return counter[0]
