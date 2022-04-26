DLS (scam: works for symmetric keys)
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

def DLS(start,goal,path,level,maxD):
    print('\nCurrent level-->',level)
    print('Goal node testing for',start)
    path.append(start)
    if start == goal:
        print("Goal test successful")
        return path
    print('Goal node testing failed')
    if level==maxD:
        return False
    print('\nExpanding the current node',start)
    for child in graph[start]:
        if DLS(child,goal,path,level+1,maxD):
            return path
        path.pop()
    return False



start = 'A'
goal = input('Enter the goal node:-')
maxD = int(input("Enter the maximum depth limit:-"))
print()
path = list()
res = DLS(start,goal,path,0,maxD)
if(res):
    print("Path to goal node available")
    print("Path",path)
else:
    print("No path available for the goal node in given depth limit")
