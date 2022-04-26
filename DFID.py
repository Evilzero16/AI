DFID

graph = {}

print("""Enter the graph as parent node and its children separated by spaces 
      (the first letter will be considered as the parent followed by the class):""")
while True:
    seq = input().split()
    if seq == ['-1']:
        break
    graph[seq[0]] = seq[1:]

print("\nGraph Struture: ")
print(graph)


max_depth = int(input("\nEnter the maximum depth to traverse: "))
start_node = input("Enter the starting node: ")
destn_node = input("Enter the destination node: ")

path = list()


def DFS(currentNode,destination,graph,maxDepth,curList):
    print("\n----- Next Iteration -----")
    print("Checking for destination",currentNode)
#     print("Open list: ", open_list)
#     print("Closed_list: ", closed_list)
#     print()
    curList.append(currentNode)
    print(f"Closed List: {curList}")
    print("Open List: [", end = '')
    for i in list(graph.keys()):
        if i not in curList:
            print("'" + i + "'", end = ',')
    print("]")
    if currentNode==destination:
        return True
    if maxDepth<=0:
        path.append(curList)
        return False
    for node in graph[currentNode]:
        if DFS(node,destination,graph,maxDepth-1,curList):
            return True
        else:
            curList.pop()
    return False

def iterativeDDFS(currentNode,destination,graph,maxDepth):
    open_list = list(graph.keys())
    closed_list = []
    for i in range(maxDepth):
        curList = list()
        if DFS(currentNode,destination,graph,i,curList):
            return True
    return False

if not iterativeDDFS(start_node, destn_node, graph, max_depth):
    print("\nPath is not available!")
else:
    print("\nA path exists!")
