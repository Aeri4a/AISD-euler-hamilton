import random


def createGraph(n, d):

    m = n * (n - 1) / 2 * d
    graph = {i + 1: {} for i in range(n)}

    # Make circle
    first = random.randint(1, n)
    save = [first]
    prev = first
    for i in range(n - 1):
        another = random.randint(1, n)
        while another in save:
            another = random.randint(1, n)
        save.append(another)
        graph[prev][another] = 0
        graph[another][prev] = 0
        prev = another

    graph[prev][first] = 0
    graph[first][prev] = 0

    e = n

    while e < m:
        v1 = random.choice(list(graph.keys()))
        v2 = random.choice([el for el in list(graph[v1].keys())])
        nb = [el for el in list(graph[v1].keys(
        ))] + [el for el in list(graph[v2].keys()) if el not in list(graph[v1].keys())]
        if len(nb) < n:
            v3 = random.choice(
                [el for el in list(graph.keys()) if el not in nb])
            del graph[v1][v2]
            del graph[v2][v1]

            graph[v3][v1] = 0
            graph[v3][v2] = 0
            graph[v1][v3] = 0
            graph[v2][v3] = 0
            e += 1

    return graph, (e / (n * (n - 1) * 0.5))
