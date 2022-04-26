DFS (Dynamic Input + Iterative + Iteration-wise o/p)
Rightmost hai cause leftmost karna major magaj tha

print("""Enter the graph as parent node and its children separated by spaces 
      (the first letter will be considered as the parent followed by the children)
      (children should be entered from the left-most to the rightmost order)
      (enter '-1' to terminate):""")

graph = {}

#Input Section Start
while(True):
    node = input().split()
    if node == ['-1']:
        break
    else:
        graph[node[0]] = node[1:]

print("Graph Structure: ")
print(graph)

#Creating required data structures
start = input("Enter start state: ")
goal = input("Enter goal state: ")

frontier = [start]     #Queue for BFS
visited = []      #empty set cannot be created with {} (it creates dictionaries)
j = 0

while(True):

    print(f"=====Iteration {j}=====")
    j+=1
    print(f"Current Frontier: {frontier}")
    print(f"Nodes Visited: {visited}")
    print()

    if len(frontier) == 0:
        print("No path exists from start to goal")
        break

    node = frontier.pop(-1)
    visited.append(node)

    if node == goal:
        print("Goal Reached")
        print(f"Path from start to goal: {visited}")
        break

    visset = set(visited)
    children = graph[node]
    if len(children) >= 1:
        for i in children:
            if i in visset:
                continue
            frontier.append(i) 
