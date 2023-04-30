import random

hasCycle = False
done = False
counter = 0

def hamCycle(graph, multiple):
    global hasCycle
    global counter
    global done

    done = False
    counter = 0
    hasCycle = False  
    path = []
    path.append(random.randint(1, len(graph)))
 
    visited = [False]*(len(graph)) 
    visited[0] = True

    FindHamCycle(graph, 1, path, visited, multiple)
 
    if hasCycle:
        print("No Hamiltonian Cycle" + "possible ")
        return 0
    return counter

def FindHamCycle(graph, pos, path, visited, multiple):
  global done
  global counter
  
  if multiple:
      done = False
  if not done:
    if pos == len(graph):
        
        if path[-1] in graph[1]:
            counter += 1
            done = True
                        
            path.append(1)
            # for i in range(len(path)):
            #     print(path[i], end = " ")
            # print()                
            path.pop()
        
            hasCycle = True
        return

    for v in graph[path[pos-1]]:
        if not visited[v-1]:
            path.append(v)
            visited[v-1] = True

            FindHamCycle(graph, pos + 1, path, visited, multiple)

            visited[v-1] = False
            path.pop()
