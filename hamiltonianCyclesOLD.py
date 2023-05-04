
stack = []
visited = []
done = False
counter = 0
notSafe = []


def findHC(multiple, v, graph):
    global stack, visited, done, counter, notSafe

    if multiple:
        done = False

    if not done:
        if len(stack) == len(graph):
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
            else:
                notSafe.append(stack)
        else:
            # print(f'Graph len: {len(graph)}; Stack: {stack}')
            stack.append(v)
            visited[v-1] = True
            # Search for a neighbour
            for nb in graph[v].keys():
                if not visited[nb-1] and stack not in notSafe:
                    findHC(multiple, nb, graph)
            visited[v-1] = False

        stack.pop()


def hamiltonianCycles(multiple, graph):
    global stack, pos, visited, done, counter
    counter = 0

    # Visited indexes - from 0 to lenght-1, call by vertex-1
    visited = [False]*len(graph)
    stack = []
    done = False

    findHC(multiple, 1, graph)
    return counter
