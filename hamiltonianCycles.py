
stack = []
pos = 0
visited = []
done = False
counter = 0


def findHC(multiple, v, graph):
    global stack, pos, visited, done, counter

    if multiple:
        done = False

    if not done:
        stack.append(v)
        pos += 1
        if pos < len(graph):
            visited[v-1] = True
            # Search for a neighbour
            for nb in graph[v].keys():
                if not visited[nb-1]:
                    findHC(multiple, nb, graph)
            visited[v-1] = False
        else:
            test = False  # assume cycle not present
            # Check if it is a cycle
            for nb in graph[v].keys():
                if nb == 1:
                    test = True
                    break

            if test:
                counter += 1
                done = True
                # stack.append(1)
                # for i in range(pos+1):
                #     print(stack[i], end=" ")
                # print()
                # stack.pop()
        stack.pop()
        pos -= 1


def hamiltonianCycles(multiple, graph):
    global stack, pos, visited, done, counter
    counter = 0

    # Visited indexes - from 0 to lenght-1, call by vertex-1
    visited = [False]*len(graph)
    stack = []
    pos = 0
    done = False

    findHC(multiple, 1, graph)
    return counter
