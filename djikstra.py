from numpy import inf

data = []
with open("list.txt", "r") as a_file:
    for line in a_file:
        start, end, wage = line.split()
        data.append([start, end, wage])

graph = {}
costs = {}
parents = {}
path = []
for row in data:
    if row[0] not in graph.keys():
        graph[row[0]] = {}
    if row[1] not in graph.keys():
        graph[row[1]] = {}
    graph[row[0]][row[1]] = int(row[2])


# print(graph)


def djikstra(graph, start, end):
    for key in graph.keys():
        costs[key] = inf
    costs[start] = 0
    Q = graph
    while Q:
        minNode = None

        for node in Q:
            if minNode == None:
                minNode = node
            elif costs[node] < costs[minNode]:
                minNode = node

        for childNode, weight in graph[minNode].items():
            if weight + costs[minNode] < costs[childNode]:
                costs[childNode] = weight + costs[minNode]
                parents[childNode] = minNode
        Q.pop(minNode)
    if end=='':
        print("Najmnieszy koszt dotarcia : "+ str(costs))
        return
    currentNode = end
    while currentNode != start:
        try:
            path.insert(0, currentNode)
            currentNode = parents[currentNode]
        except KeyError:
            print("Nie można wyznaczyć ścieżki")
            break
    path.insert(0, start)
    if costs[end] != inf:
        print(" Koszt dotarcia do węzła {}: ".format(end) + str(costs[end]))
        print("Ścieżka: " + str(path))


print("Wprowadź węzeł początkowy i końcowy, jeśli chcesz uzyskać koszt dotarcia do każdego węzła nie podawaj węzła docelowego:")
djikstra(graph, str(input()), str(input()))
